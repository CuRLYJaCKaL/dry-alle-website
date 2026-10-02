// Google API erisimi — servis hesabi ile, HARICI PAKET YOK.
// Node 22'de crypto ve fetch yerlesik; googleapis paketi (~50 MB) eklemeye gerek
// kalmadan JWT imzalayip access token aliyoruz.
import { createSign } from 'node:crypto';

const GA4_PROPERTY = process.env.GA4_PROPERTY_ID || '548056288';
const GSC_SITE = process.env.GSC_SITE_URL || 'https://dryallekurutemizleme.com/';

let tokenCache = null;

async function accessToken() {
  if (tokenCache && tokenCache.exp > Date.now() + 60_000) return tokenCache.token;
  const raw = process.env.GOOGLE_SERVICE_ACCOUNT_JSON;
  if (!raw) throw new Error('GOOGLE_SERVICE_ACCOUNT_JSON tanimli degil');
  const sa = JSON.parse(raw);
  const scope = [
    'https://www.googleapis.com/auth/analytics.readonly',
    'https://www.googleapis.com/auth/webmasters.readonly',
  ].join(' ');
  const now = Math.floor(Date.now() / 1000);
  const b64 = (o) => Buffer.from(JSON.stringify(o)).toString('base64url');
  const head = b64({ alg: 'RS256', typ: 'JWT' });
  const body = b64({ iss: sa.client_email, scope, aud: 'https://oauth2.googleapis.com/token', exp: now + 3600, iat: now });
  const sig = createSign('RSA-SHA256').update(`${head}.${body}`).sign(sa.private_key, 'base64url');
  const res = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${head}.${body}.${sig}` }),
  });
  if (!res.ok) throw new Error(`Google token alinamadi: ${res.status} ${await res.text()}`);
  const j = await res.json();
  tokenCache = { token: j.access_token, exp: Date.now() + j.expires_in * 1000 };
  return tokenCache.token;
}

async function ga4(body) {
  const res = await fetch(`https://analyticsdata.googleapis.com/v1beta/properties/${GA4_PROPERTY}:runReport`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${await accessToken()}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`GA4 hatasi: ${res.status} ${await res.text()}`);
  return res.json();
}

const TEMAS = ['whatsapp_click', 'call_click', 'order_submit'];
const temasFiltresi = { filter: { fieldName: 'eventName', inListFilter: { values: TEMAS } } };

/** Bir donemin ozeti: oturum, kullanici, goruntuleme, temas kirilimi. */
export async function donemOzeti(baslangic, bitis) {
  const [genel, olaylar] = await Promise.all([
    ga4({ dateRanges: [{ startDate: baslangic, endDate: bitis }],
          metrics: [{ name: 'sessions' }, { name: 'activeUsers' }, { name: 'screenPageViews' }] }),
    ga4({ dateRanges: [{ startDate: baslangic, endDate: bitis }],
          dimensions: [{ name: 'eventName' }], metrics: [{ name: 'eventCount' }],
          dimensionFilter: temasFiltresi }),
  ]);
  const g = genel.rows?.[0]?.metricValues?.map((m) => Number(m.value)) ?? [0, 0, 0];
  const kirilim = Object.fromEntries(TEMAS.map((t) => [t, 0]));
  for (const r of olaylar.rows ?? []) kirilim[r.dimensionValues[0].value] = Number(r.metricValues[0].value);
  const temas = Object.values(kirilim).reduce((a, b) => a + b, 0);
  return {
    baslangic, bitis,
    oturum: g[0], kullanici: g[1], goruntuleme: g[2],
    temas, ...kirilim,
    temasOrani: g[0] ? (temas / g[0]) * 100 : 0,
  };
}

/** Gun gun temas sayisi — e-postadaki cubuk grafik icin. */
export async function gunlukTemas(baslangic, bitis) {
  const r = await ga4({ dateRanges: [{ startDate: baslangic, endDate: bitis }],
    dimensions: [{ name: 'date' }], metrics: [{ name: 'eventCount' }],
    dimensionFilter: temasFiltresi, orderBys: [{ dimension: { dimensionName: 'date' } }] });
  return (r.rows ?? []).map((x) => ({ tarih: x.dimensionValues[0].value, adet: Number(x.metricValues[0].value) }));
}

/** En cok temas getiren sayfalar. */
export async function enIyiSayfalar(baslangic, bitis, limit = 5) {
  const r = await ga4({ dateRanges: [{ startDate: baslangic, endDate: bitis }],
    dimensions: [{ name: 'pagePath' }], metrics: [{ name: 'eventCount' }],
    dimensionFilter: temasFiltresi,
    orderBys: [{ metric: { metricName: 'eventCount' }, desc: true }], limit });
  return (r.rows ?? []).map((x) => ({ yol: x.dimensionValues[0].value, temas: Number(x.metricValues[0].value) }));
}

/** Search Console: toplamlar ve en cok tiklanan sorgular. */
export async function aramaOzeti(baslangic, bitis, sorguLimit = 5) {
  const url = `https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(GSC_SITE)}/searchAnalytics/query`;
  const cek = async (govde) => {
    const res = await fetch(url, { method: 'POST',
      headers: { Authorization: `Bearer ${await accessToken()}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ startDate: baslangic, endDate: bitis, ...govde }) });
    if (!res.ok) throw new Error(`GSC hatasi: ${res.status} ${await res.text()}`);
    return res.json();
  };
  const [toplam, sorgular] = await Promise.all([
    cek({}),
    cek({ dimensions: ['query'], rowLimit: sorguLimit }),
  ]);
  const t = toplam.rows?.[0];
  return {
    tiklama: t?.clicks ?? 0, gosterim: t?.impressions ?? 0,
    to: (t?.ctr ?? 0) * 100, konum: t?.position ?? 0,
    sorgular: (sorgular.rows ?? []).map((r) => ({
      sorgu: r.keys[0], tiklama: r.clicks, gosterim: r.impressions, konum: r.position })),
  };
}
