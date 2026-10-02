// Haftalik rapor — veriyi ceker, e-postayi uretir, Resend ile gonderir.
//   npm run rapor          -> gercek veriyi ceker, gonderir
//   npm run rapor -- --dry -> gonderMEZ, HTML'i dist-report/ icine yazar (onizleme)
// Pazartesi sabahi calisir; onceki TAM hafta (Pzt-Paz) raporlanir.
// Ayin ilk 7 gunune denk gelen calismada biten ayin tamami onceki ayla
// karsilastirilir — kullanicinin istedigi "4. hafta aylik degerlendirme".
import { writeFileSync, mkdirSync } from 'node:fs';
import { donemOzeti, gunlukTemas, enIyiSayfalar, aramaOzeti } from './google.mjs';
import { raporHtml } from './render.mjs';

const kuru = process.argv.includes('--dry');
const iso = (d) => d.toISOString().slice(0, 10);

function donemler(bugun = new Date()) {
  const d = new Date(Date.UTC(bugun.getUTCFullYear(), bugun.getUTCMonth(), bugun.getUTCDate()));
  // En son TAMAMLANMIS pazartesi-pazar haftasi
  const gunIndex = (d.getUTCDay() + 6) % 7;            // Pzt=0
  const buPazartesi = new Date(d); buPazartesi.setUTCDate(d.getUTCDate() - gunIndex);
  const bit = new Date(buPazartesi); bit.setUTCDate(buPazartesi.getUTCDate() - 1);   // gecen pazar
  const bas = new Date(bit); bas.setUTCDate(bit.getUTCDate() - 6);                   // gecen pazartesi
  const oncekiBit = new Date(bas); oncekiBit.setUTCDate(bas.getUTCDate() - 1);
  const oncekiBas = new Date(oncekiBit); oncekiBas.setUTCDate(oncekiBit.getUTCDate() - 6);
  // "Gecen ayin ayni haftasi" = tam 28 gun oncesi. Takvim ayi degil 4 hafta geri
  // gidilir; boylece Pzt-Paz hizasi birebir korunur. Takvim ayi kullanilsaydi
  // ornegin cumartesi-pazara denk gelen bir pencereyle kiyaslanir, hafta sonu
  // etkisi farki kirletirdi.
  const gecenAyBas = new Date(bas); gecenAyBas.setUTCDate(bas.getUTCDate() - 28);
  const gecenAyBit = new Date(bit); gecenAyBit.setUTCDate(bit.getUTCDate() - 28);
  const ayBasi = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), 1));
  const aylikZamani = d.getUTCDate() <= 7;
  const ayTamBas = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() - 1, 1));
  const ayTamBit = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), 0));
  const oncekiAyBas = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() - 2, 1));
  const oncekiAyBit = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() - 1, 0));
  return { bas, bit, oncekiBas, oncekiBit, ayBasi, bugun: d, aylikZamani,
           gecenAyBas, gecenAyBit, ayTamBas, ayTamBit, oncekiAyBas, oncekiAyBit };
}

const p = donemler();
const sonuc = {
  donem: { bas: p.bas, bit: p.bit },
  gecenAyDonem: { bas: p.gecenAyBas, bit: p.gecenAyBit },
  onizleme: kuru,
  ayAdi: p.ayTamBas.toLocaleDateString('tr-TR', { month: 'long', year: 'numeric' }),
};

try {
  [sonuc.bu, sonuc.gecen, sonuc.gecenAy, sonuc.ayBasi, sonuc.gunler, sonuc.sayfalar] = await Promise.all([
    donemOzeti(iso(p.bas), iso(p.bit)),
    donemOzeti(iso(p.oncekiBas), iso(p.oncekiBit)),
    donemOzeti(iso(p.gecenAyBas), iso(p.gecenAyBit)),
    donemOzeti(iso(p.ayBasi), iso(p.bugun)),
    gunlukTemas(iso(p.bas), iso(p.bit)),
    enIyiSayfalar(iso(p.bas), iso(p.bit)),
  ]);
  // Search Console verisi ~2 gun gecikmeli gelir; alinamazsa rapor yine gonderilir.
  try {
    [sonuc.arama, sonuc.oncekiArama, sonuc.gecenAyArama] = await Promise.all([
      aramaOzeti(iso(p.bas), iso(p.bit)),
      aramaOzeti(iso(p.oncekiBas), iso(p.oncekiBit)),
      aramaOzeti(iso(p.gecenAyBas), iso(p.gecenAyBit)),
    ]);
  } catch (e) { console.error('[rapor] Search Console alinamadi, atlandi:', e.message); }

  if (p.aylikZamani) {
    [sonuc.ay, sonuc.oncekiAy] = await Promise.all([
      donemOzeti(iso(p.ayTamBas), iso(p.ayTamBit)),
      donemOzeti(iso(p.oncekiAyBas), iso(p.oncekiAyBit)),
    ]);
  }
} catch (e) {
  console.error('[rapor] Veri cekilemedi:', e.message);
  process.exit(1);
}

const html = raporHtml(sonuc);
const konu = `DryAlle haftalık rapor — ${sonuc.bu.temas} temas · ${sonuc.bu.oturum} oturum`;

if (kuru) {
  mkdirSync('dist-report', { recursive: true });
  writeFileSync('dist-report/rapor.html', html);
  console.log(`[rapor] ONIZLEME yazildi: dist-report/rapor.html`);
  console.log(`[rapor] konu: ${konu}`);
  console.log(`[rapor] bu hafta ${sonuc.bu.temas} temas / ${sonuc.bu.oturum} oturum · gecen hafta ${sonuc.gecen?.temas ?? '-'}`);
  process.exit(0);
}

const anahtar = process.env.RESEND_API_KEY;
const alici = (process.env.REPORT_TO || '').split(',').map((s) => s.trim()).filter(Boolean);
const gonderen = process.env.REPORT_FROM || 'DryAlle Rapor <rapor@dryallekurutemizleme.com>';
if (!anahtar || alici.length === 0) { console.error('[rapor] RESEND_API_KEY veya REPORT_TO eksik'); process.exit(1); }

const res = await fetch('https://api.resend.com/emails', {
  method: 'POST',
  headers: { Authorization: `Bearer ${anahtar}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ from: gonderen, to: alici, subject: konu, html }),
});
if (!res.ok) { console.error(`[rapor] Gonderilemedi: ${res.status} ${await res.text()}`); process.exit(1); }
console.log(`[rapor] Gonderildi -> ${alici.join(', ')} · ${konu}`);
