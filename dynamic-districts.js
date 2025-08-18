// TÜM 36 BÖLGE SAYFASI VERİTABANI
const allDistricts = [
    // Kuru Temizleme (5 sayfa)
    { name: "acibadem-kuru-temizleme", title: "Acıbadem Kuru Temizleme", desc: "Sağlık merkezi çevresinde kaliteli hizmet", category: "kuru-temizleme" },
    { name: "camlica-kuru-temizleme", title: "Çamlıca Kuru Temizleme", desc: "Elite bölgede premium kıyafet bakımı", category: "kuru-temizleme" },
    { name: "fenerbahce-kuru-temizleme", title: "Fenerbahçe Kuru Temizleme", desc: "Sahil kesiminde özel kıyafet temizleme", category: "kuru-temizleme" },
    { name: "kadikoy-kuru-temizleme", title: "Kadıköy Kuru Temizleme", desc: "Merkezi konumda profesyonel hizmet", category: "kuru-temizleme" },
    { name: "kozyatagi-kuru-temizleme", title: "Kozyatağı Kuru Temizleme", desc: "Modern semtte güvenilir temizlik", category: "kuru-temizleme" },
    
    // Luxury/Premium (7 sayfa)
    { name: "atasehir-premium-temizlik", title: "Ataşehir Premium Temizlik", desc: "İş merkezinde hızlı ve güvenilir hizmet", category: "premium" },
    { name: "bagdat-caddesi-haute-couture", title: "Bağdat Caddesi Haute Couture", desc: "Haute couture ve lüks giyim temizleme hizmeti", category: "luxury" },
    { name: "kadikoy-luxury-kiyafet", title: "Kadıköy Luxury Kıyafet", desc: "Merkezi konumda premium kıyafet bakımı", category: "luxury" },
    { name: "uskudar-luxury-kiyafet", title: "Üsküdar Luxury Kıyafet", desc: "Tarihi yarımadada profesyonel tekstil bakımı", category: "luxury" },
    { name: "altunizade-premium-temizlik", title: "Altunizade Premium Temizlik", desc: "Lüks semtte VIP temizlik hizmeti", category: "premium" },
    { name: "maltepe-luxury-hizmet", title: "Maltepe Luxury Hizmet", desc: "Sahil kesimi luxury kıyafet bakımı", category: "luxury" },
    { name: "sahrayicedit-premium-bakim", title: "Sahrayıcedit Premium Bakım", desc: "Elite konut bölgesinde özel hizmet", category: "premium" },
    { name: "umraniye-vip-temizlik", title: "Ümraniye VIP Temizlik", desc: "Modern yaşam alanında VIP hizmet", category: "premium" },
    
    // Halı Yıkama (12 sayfa)
    { name: "altunizade-hali-yikama", title: "Altunizade Halı Yıkama", desc: "Designer halı yıkama ve bakım hizmeti", category: "hali-yikama" },
    { name: "atasehir-hali-yikama", title: "Ataşehir Halı Yıkama", desc: "Business center halı temizleme", category: "hali-yikama" },
    { name: "caddebostan-hali-yikama", title: "Caddebostan Halı Yıkama", desc: "Premium konutlarda halı temizleme hizmeti", category: "hali-yikama" },
    { name: "erenkoy-hali-yikama", title: "Erenköy Halı Yıkama", desc: "Sakin semtte halı bakım hizmeti", category: "hali-yikama" },
    { name: "goztepe-hali-yikama", title: "Göztepe Halı Yıkama", desc: "Merkezi lokasyonda halı temizleme", category: "hali-yikama" },
    { name: "icerenkoy-hali-yikama", title: "İçerenköy Halı Yıkama", desc: "Modern semtte halı yıkama hizmeti", category: "hali-yikama" },
    { name: "kucukbakkalkoy-hali-yikama", title: "Küçükbakkalköy Halı Yıkama", desc: "Sakin bölgede kaliteli halı bakımı", category: "hali-yikama" },
    { name: "maltepe-hali-yikama", title: "Maltepe Halı Yıkama", desc: "Sahil kesiminde halı temizleme", category: "hali-yikama" },
    { name: "suadiye-hali-yikama", title: "Suadiye Halı Yıkama", desc: "Lüks semtte profesyonel halı temizleme", category: "hali-yikama" },
    { name: "umraniye-hali-yikama", title: "Ümraniye Halı Yıkama", desc: "Modern yaşam alanında halı bakımı", category: "hali-yikama" },
    { name: "uskudar-hali-yikama", title: "Üsküdar Halı Yıkama", desc: "Tarihi yarımadada halı temizleme", category: "hali-yikama" },
    
    // Koltuk Yıkama (11 sayfa)
    { name: "bagdat-caddesi-koltuk-yikama", title: "Bağdat Caddesi Koltuk Yıkama", desc: "Luxury mobilya temizleme hizmeti", category: "koltuk-yikama" },
    { name: "barbaros-koltuk-yikama", title: "Barbaros Koltuk Yıkama", desc: "VIP mobilya bakım hizmeti", category: "koltuk-yikama" },
    { name: "bostanci-koltuk-yikama", title: "Bostancı Koltuk Yıkama", desc: "Sahil kesimi mobilya temizleme", category: "koltuk-yikama" },
    { name: "fikirtepe-koltuk-yikama", title: "Fikirtepe Koltuk Yıkama", desc: "Modern semtte mobilya bakımı", category: "koltuk-yikama" },
    { name: "kadikoy-koltuk-yikama", title: "Kadıköy Koltuk Yıkama", desc: "Sanat mobilya temizleme hizmeti", category: "koltuk-yikama" },
    { name: "kalamis-koltuk-yikama", title: "Kalamış Koltuk Yıkama", desc: "Sahil kesimi koltuk temizleme", category: "koltuk-yikama" },
    { name: "kartal-koltuk-yikama", title: "Kartal Koltuk Yıkama", desc: "Geniş alanda mobilya bakım hizmeti", category: "koltuk-yikama" },
    { name: "kucukbakkalkoy-koltuk-yikama", title: "Küçükbakkalköy Koltuk Yıkama", desc: "Sakin bölgede koltuk bakımı", category: "koltuk-yikama" },
    { name: "moda-koltuk-yikama", title: "Moda Koltuk Yıkama", desc: "Trendy semtte mobilya temizleme", category: "koltuk-yikama" },
    { name: "pendik-koltuk-yikama", title: "Pendik Koltuk Yıkama", desc: "Genişleyen bölgede koltuk bakımı", category: "koltuk-yikama" },
    { name: "uskudar-koltuk-yikama", title: "Üsküdar Koltuk Yıkama", desc: "Tarihi semtte mobilya temizleme", category: "koltuk-yikama" },
    
    // Özel Hizmet (1 sayfa)
    { name: "uskudar-gelinlik-temizleme", title: "Üsküdar Gelinlik Temizleme", desc: "Özel günler için gelinlik bakımı", category: "ozel-hizmet" }
];

// AKILLI KAR SEÇİM ALGORİTMASI
function generateUniqueCards(currentPageName) {
    const currentPage = allDistricts.find(d => d.name === currentPageName);
    if (!currentPage) return [];
    
    let selectedCards = [];
    let remainingDistricts = allDistricts.filter(d => d.name !== currentPageName);
    
    // 1. Aynı kategoriden 2-3 kart (benzer hizmetler)
    const sameCategory = remainingDistricts.filter(d => d.category === currentPage.category);
    selectedCards.push(...sameCategory.slice(0, 3));
    
    // 2. Premium/Luxury öncelik (popüler sayfalar)
    const premiumPages = remainingDistricts.filter(d => 
        !selectedCards.includes(d) && 
        (d.category === 'luxury' || d.category === 'premium')
    );
    selectedCards.push(...premiumPages.slice(0, 2));
    
    // 3. Kalan kategorilerden karışık seçim
    remainingDistricts = remainingDistricts.filter(d => !selectedCards.includes(d));
    
    // Hash-based selection (sayfa adına göre deterministic ama farklı)
    const pageHash = currentPageName.split('').reduce((hash, char) => hash + char.charCodeAt(0), 0);
    
    while (selectedCards.length < 8 && remainingDistricts.length > 0) {
        const index = (pageHash + selectedCards.length) % remainingDistricts.length;
        selectedCards.push(remainingDistricts[index]);
        remainingDistricts.splice(index, 1);
    }
    
    return selectedCards.slice(0, 8);
}

// HER SAYFA İÇİN BENZERSİZ KART KOMBİNASYONLARI OLUŞTUR
console.log("// DYNAMIC DISTRICT CARDS - HER SAYFA FARKLI 8 KART\\n");

allDistricts.forEach(district => {
    const uniqueCards = generateUniqueCards(district.name);
    
    console.log(`\\n// ${district.title} sayfası için özel kartlar:`);
    console.log(`const ${district.name.replace(/-/g, '_')}_districts = [`);
    
    uniqueCards.forEach(card => {
        console.log(`    {`);
        console.log(`        title: "${card.title}",`);
        console.log(`        desc: "${card.desc}",`);
        console.log(`        link: "${card.name}.html"`);
        console.log(`    },`);
    });
    
    console.log(`];\\n`);
});

console.log("\\n// Toplam", allDistricts.length, "sayfa, her birinde 8 benzersiz kart = %100 internal linking coverage!");