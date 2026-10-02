// Haftalik rapor e-postasi — tablo tabanli, satir ici stil.
// Posta istemcileri (ozellikle Outlook) flexbox/grid ve harici CSS desteklemez;
// bu yuzden duzen <table> ile kurulur, her stil inline yazilir.

import { sayfaAdi } from './etiket.mjs';

const YESIL = '#006A44', KOYU = '#16241E', GRI = '#5E6F67', CIZGI = '#DCE6DF';
const ZEMIN = '#F1F6F2', KART = '#FFFFFF', KIRMIZI = '#B4451F', ALTIN = '#E3A008';

const sayi = (n) => new Intl.NumberFormat('tr-TR').format(Math.round(n));
const yuzde = (n) => `%${n.toFixed(1).replace('.', ',')}`;
const gun = (d) => new Date(d).toLocaleDateString('tr-TR', { day: 'numeric', month: 'long' });
const aralik = (a, b) => `${gun(a)} – ${gun(b)}`;

function fark(simdi, once) {
  if (!once) return { metin: 'önceki dönem verisi yok', renk: GRI, ok: '' };
  const d = ((simdi - once) / once) * 100;
  if (Math.abs(d) < 0.5) return { metin: 'değişim yok', renk: GRI, ok: '→' };
  return { metin: `%${Math.abs(d).toFixed(0)} ${d > 0 ? 'artış' : 'azalış'}`, renk: d > 0 ? YESIL : KIRMIZI, ok: d > 0 ? '▲' : '▼' };
}

const kart = (ic) =>
  `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:${KART};border:1px solid ${CIZGI};border-radius:14px;margin:0 0 16px"><tr><td style="padding:22px 24px">${ic}</td></tr></table>`;

const baslik = (t, alt) =>
  `<div style="font:600 17px/1.3 -apple-system,Segoe UI,Roboto,sans-serif;color:${KOYU}">${t}</div>` +
  (alt ? `<div style="font:400 13px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:${GRI};margin-top:4px">${alt}</div>` : '');

function ozetTablo(satirlar) {
  const th = `font:600 11px/1.3 -apple-system,sans-serif;color:${GRI};text-transform:uppercase;letter-spacing:.05em;padding:8px 10px;text-align:right;border-bottom:1px solid ${CIZGI}`;
  const td = `font:400 14px/1.4 -apple-system,sans-serif;color:${KOYU};padding:10px;text-align:right;border-bottom:1px solid ${CIZGI}`;
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;margin-top:14px">
    <tr><th style="${th};text-align:left">Dönem</th><th style="${th}">Oturum</th><th style="${th}">Temas</th><th style="${th}">Oran</th></tr>
    ${satirlar.map((s) => `<tr${s.vurgu ? ` style="background:#F4F8F5"` : ''}>
      <td style="${td};text-align:left;font-weight:${s.vurgu ? 600 : 400}${s.soluk ? `;color:${GRI}` : ''}">${s.ad}</td>
      <td style="${td}">${sayi(s.d.oturum)}</td>
      <td style="${td};font-weight:600">${sayi(s.d.temas)}</td>
      <td style="${td}">${yuzde(s.d.temasOrani)}</td></tr>`).join('')}
  </table>`;
}

function kahraman(bu, gecen, gecenAy, gecenAyDonem) {
  const h = fark(bu.temas, gecen?.temas);
  const fa = fark(bu.temas, gecenAy?.temas);
  return kart(
    `<div style="font:400 13px/1.4 -apple-system,sans-serif;color:${GRI}">Bu hafta gelen temas</div>
     <div style="font:700 44px/1.1 -apple-system,sans-serif;color:${YESIL};margin:6px 0 4px">${sayi(bu.temas)}</div>
     <div style="font:400 14px/1.5 -apple-system,sans-serif;color:${KOYU}">
       ${sayi(bu.whatsapp_click)} WhatsApp · ${sayi(bu.call_click)} arama · ${sayi(bu.order_submit)} sipariş
     </div>
     <div style="font:600 13px/1.5 -apple-system,sans-serif;color:${h.renk};margin-top:8px">${h.ok} ${h.metin}${gecen ? ` (geçen hafta ${sayi(gecen.temas)})` : ''}</div>
     ${gecenAy ? `<div style="font:400 12px/1.5 -apple-system,sans-serif;color:${GRI};margin-top:3px">${fa.ok} geçen ayın aynı haftasına göre ${fa.metin} (${sayi(gecenAy.temas)} temas · ${aralik(gecenAyDonem.bas, gecenAyDonem.bit)})</div>` : ''}`);
}

function kutular(d) {
  const h = `font:400 12px/1.3 -apple-system,sans-serif;color:${GRI}`;
  const v = `font:700 22px/1.2 -apple-system,sans-serif;color:${KOYU};padding-top:4px`;
  const hucre = (b, s) => `<td width="25%" style="padding:14px 10px;border-right:1px solid ${CIZGI}"><div style="${h}">${b}</div><div style="${v}">${s}</div></td>`;
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:${KART};border:1px solid ${CIZGI};border-radius:14px;margin:0 0 16px;border-collapse:separate"><tr>
    ${hucre('Oturum', sayi(d.oturum))}${hucre('Ziyaretçi', sayi(d.kullanici))}
    ${hucre('Temas oranı', yuzde(d.temasOrani))}<td width="25%" style="padding:14px 10px"><div style="${h}">Sayfa görüntüleme</div><div style="${v}">${sayi(d.goruntuleme)}</div></td></tr></table>`;
}

function cubuklar(gunler) {
  if (!gunler.length) return '';
  const max = Math.max(...gunler.map((g) => g.adet), 1);
  const satir = (g) => {
    const w = Math.round((g.adet / max) * 100);
    const t = new Date(`${g.tarih.slice(0, 4)}-${g.tarih.slice(4, 6)}-${g.tarih.slice(6, 8)}`);
    const ad = t.toLocaleDateString('tr-TR', { weekday: 'short', day: 'numeric' });
    return `<tr>
      <td width="92" style="font:400 13px/1.6 -apple-system,sans-serif;color:${GRI};padding:3px 0">${ad}</td>
      <td style="padding:3px 0"><table role="presentation" cellpadding="0" cellspacing="0" width="100%"><tr>
        <td width="${w}%" style="background:${YESIL};height:16px;border-radius:4px;font-size:0">&nbsp;</td>
        <td style="font-size:0">&nbsp;</td></tr></table></td>
      <td width="34" style="font:600 13px/1.6 -apple-system,sans-serif;color:${KOYU};text-align:right;padding:3px 0">${g.adet}</td></tr>`;
  };
  return kart(baslik('Günlük temas', 'Haftanın hangi günü yoğun?') +
    `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:12px">${gunler.map(satir).join('')}</table>`);
}

function sayfaTablosu(sayfalar) {
  if (!sayfalar.length) return '';
  // Yol tek basina okunmuyordu ("/" satirinin ana sayfa oldugu anlasilmiyordu):
  // ustte insan adi, altinda kucuk ve soluk yol.
  const td = `padding:9px 0;border-bottom:1px solid ${CIZGI};vertical-align:top`;
  const ad = `font:600 14px/1.4 -apple-system,sans-serif;color:${KOYU}`;
  const yol = `font:400 12px/1.4 -apple-system,sans-serif;color:${GRI};margin-top:2px`;
  return kart(baslik('En çok müşteri getiren sayfalar') +
    `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:10px;border-collapse:collapse">
      ${sayfalar.map((s) => `<tr>
        <td style="${td}"><div style="${ad}">${sayfaAdi(s.yol)}</div><div style="${yol}">${s.yol}</div></td>
        <td style="${td};text-align:right;font:700 15px/1.4 -apple-system,sans-serif;color:${KOYU};width:56px">${s.temas}</td></tr>`).join('')}
    </table>`);
}

function aramaBolumu(a, oncekiA, gecenAyA, gecenAyDonem) {
  if (!a) return '';
  const f = fark(a.tiklama, oncekiA?.tiklama);
  const fa = fark(a.tiklama, gecenAyA?.tiklama);
  // Konumda KUCUK olan iyidir; fark() buyugu iyi sayar, bu yuzden isaret cevrilir.
  const kf = gecenAyA?.konum
    ? (() => { const d = gecenAyA.konum - a.konum;
        if (Math.abs(d) < 0.05) return 'konum aynı';
        return `konum ${Math.abs(d).toFixed(1).replace('.', ',')} sıra ${d > 0 ? 'yukarıda' : 'aşağıda'}`; })()
    : null;
  const td = `font:400 13px/1.5 -apple-system,sans-serif;color:${KOYU};padding:7px 0;border-bottom:1px solid ${CIZGI}`;
  return kart(baslik('Google aramasından gelen', `${sayi(a.tiklama)} tıklama · ${sayi(a.gosterim)} gösterim · ortalama konum ${a.konum.toFixed(1).replace('.', ',')}`) +
    `<div style="font:600 13px/1.5 -apple-system,sans-serif;color:${f.renk};margin-top:6px">${f.ok} ${f.metin}</div>` +
    (gecenAyA ? `<div style="font:400 12px/1.5 -apple-system,sans-serif;color:${GRI};margin-top:3px">${fa.ok} geçen ayın aynı haftasına göre ${fa.metin}${kf ? ` · ${kf}` : ''} (${sayi(gecenAyA.tiklama)} tıklama · ${aralik(gecenAyDonem.bas, gecenAyDonem.bit)})</div>` : '') +
    (a.sorgular.length ? `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:12px;border-collapse:collapse">
      <tr><td style="${td};color:${GRI};font-size:11px;text-transform:uppercase">Arama</td><td style="${td};color:${GRI};font-size:11px;text-align:right">Tıklama</td></tr>
      ${a.sorgular.map((q) => `<tr><td style="${td}">${q.sorgu}</td><td style="${td};text-align:right;font-weight:600">${q.tiklama}</td></tr>`).join('')}
    </table>` : ''));
}

function aylikBolum(ay, oncekiAy, ayAdi) {
  if (!ay) return '';
  const f = fark(ay.temas, oncekiAy?.temas);
  return kart(baslik(`Aylık değerlendirme · ${ayAdi}`, 'Dört haftada bir, biten ayın tamamı önceki ayla karşılaştırılır.') +
    ozetTablo([
      { ad: ayAdi, d: ay, vurgu: true },
      ...(oncekiAy ? [{ ad: 'Bir önceki ay', d: oncekiAy }] : []),
    ]) +
    `<div style="font:600 14px/1.6 -apple-system,sans-serif;color:${f.renk};margin-top:12px">${f.ok} Temas ${f.metin}</div>`);
}

export function raporHtml(v) {
  const { bu, gecen, gecenAy, gecenAyDonem, ayBasi, gunler, sayfalar,
          arama, oncekiArama, gecenAyArama, ay, oncekiAy, ayAdi, donem, onizleme } = v;
  const satirlar = [
    { ad: `Bu hafta · ${aralik(donem.bas, donem.bit)}`, d: bu, vurgu: true },
    ...(gecen ? [{ ad: 'Geçen hafta', d: gecen }] : []),
    ...(gecenAy ? [{ ad: `Geçen ay aynı hafta · ${aralik(gecenAyDonem.bas, gecenAyDonem.bit)}`, d: gecenAy, soluk: true }] : []),
    ...(ayBasi ? [{ ad: 'Ay başından bugüne', d: ayBasi }] : []),
  ];
  return `<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DryAlle haftalık rapor</title></head>
<body style="margin:0;padding:0;background:${ZEMIN}">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:${ZEMIN};padding:24px 12px">
<tr><td align="center">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px">
  <tr><td style="padding:0 2px 18px">
    ${onizleme ? `<div style="background:${ALTIN};color:#1a1205;font:600 12px/1.4 -apple-system,sans-serif;padding:8px 12px;border-radius:8px;margin-bottom:12px">ÖNİZLEME — bu bir test gönderimidir</div>` : ''}
    <div style="font:600 13px/1.3 -apple-system,sans-serif;color:${YESIL}">Dry Alle Kuru Temizleme</div>
    <div style="font:700 26px/1.25 -apple-system,sans-serif;color:${KOYU};margin-top:6px">Haftalık performans raporu</div>
    <div style="font:400 13px/1.5 -apple-system,sans-serif;color:${GRI};margin-top:6px">${gun(donem.bas)} – ${gun(donem.bit)} · temas = WhatsApp + arama + online sipariş</div>
  </td></tr>
  <tr><td>
    ${kahraman(bu, gecen, gecenAy, gecenAyDonem)}
    ${kutular(bu)}
    ${kart(baslik('Özet tablo', 'Temas oranı = temas ÷ oturum') + ozetTablo(satirlar))}
    ${cubuklar(gunler)}
    ${sayfaTablosu(sayfalar)}
    ${aramaBolumu(arama, oncekiArama, gecenAyArama, gecenAyDonem)}
    ${aylikBolum(ay, oncekiAy, ayAdi)}
    <div style="font:400 12px/1.6 -apple-system,sans-serif;color:${GRI};text-align:center;padding:8px 10px 0">
      Kaynak: Google Analytics 4 ve Search Console · her pazartesi 08:00'de otomatik gönderilir.<br>
      Veriler doğrudan Google'dan okunur; tahmin içermez.
    </div>
  </td></tr>
</table></td></tr></table></body></html>`;
}
