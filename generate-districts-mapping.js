// Intelligent District Cards Distribution Algorithm
// Bu script her sayfa için benzersiz kart kombinasyonları oluşturur

const districts = [
    // Kuru Temizleme Sayfaları
    { name: "acibadem-kuru-temizleme", title: "Acıbadem Kuru Temizleme", desc: "Sağlık merkezi çevresinde kaliteli hizmet", type: "kuru-temizleme", area: "kadikoy" },
    { name: "camlica-kuru-temizleme", title: "Çamlıca Kuru Temizleme", desc: "Elite bölgede premium kıyafet bakımı", type: "kuru-temizleme", area: "uskudar" },
    { name: "fenerbahce-kuru-temizleme", title: "Fenerbahçe Kuru Temizleme", desc: "Sahil kesiminde özel kıyafet temizleme", type: "kuru-temizleme", area: "kadikoy" },
    { name: "kadikoy-kuru-temizleme", title: "Kadıköy Kuru Temizleme", desc: "Merkezi konumda profesyonel hizmet", type: "kuru-temizleme", area: "kadikoy" },
    { name: "kozyatagi-kuru-temizleme", title: "Kozyatağı Kuru Temizleme", desc: "Modern semtte güvenilir temizlik", type: "kuru-temizleme", area: "kadikoy" },
    
    // Luxury/Premium Sayfaları  
    { name: "atasehir-premium-temizlik", title: "Ataşehir Premium Temizlik", desc: "İş merkezinde hızlı ve güvenilir hizmet", type: "premium", area: "atasehir" },
    { name: "bagdat-caddesi-haute-couture", title: "Bağdat Caddesi Haute Couture", desc: "Haute couture ve lüks giyim temizleme hizmeti", type: "luxury", area: "kadikoy" },
    { name: "kadikoy-luxury-kiyafet", title: "Kadıköy Luxury Kıyafet", desc: "Merkezi konumda premium kıyafet bakımı", type: "luxury", area: "kadikoy" },
    { name: "uskudar-luxury-kiyafet", title: "Üsküdar Luxury Kıyafet", desc: "Tarihi yarımadada profesyonel tekstil bakımı", type: "luxury", area: "uskudar" },
    { name: "altunizade-premium-temizlik", title: "Altunizade Premium Temizlik", desc: "Lüks semtte VIP temizlik hizmeti", type: "premium", area: "uskudar" },
    { name: "maltepe-luxury-hizmet", title: "Maltepe Luxury Hizmet", desc: "Sahil kesimi luxury kıyafet bakımı", type: "luxury", area: "maltepe" },
    { name: "sahrayicedit-premium-bakim", title: "Sahrayıcedit Premium Bakım", desc: "Elite konut bölgesinde özel hizmet", type: "premium", area: "kadikoy" },
    { name: "umraniye-vip-temizlik", title: "Ümraniye VIP Temizlik", desc: "Modern yaşam alanında VIP hizmet", type: "premium", area: "umraniye" },
    
    // Halı Yıkama Sayfaları
    { name: "altunizade-hali-yikama", title: "Altunizade Halı Yıkama", desc: "Designer halı yıkama ve bakım hizmeti", type: "hali-yikama", area: "uskudar" },
    { name: "atasehir-hali-yikama", title: "Ataşehir Halı Yıkama", desc: "Business center halı temizleme", type: "hali-yikama", area: "atasehir" },
    { name: "caddebostan-hali-yikama", title: "Caddebostan Halı Yıkama", desc: "Premium konutlarda halı temizleme hizmeti", type: "hali-yikama", area: "kadikoy" },
    { name: "erenkoy-hali-yikama", title: "Erenköy Halı Yıkama", desc: "Sakin semtte halı bakım hizmeti", type: "hali-yikama", area: "kadikoy" },
    { name: "goztepe-hali-yikama", title: "Göztepe Halı Yıkama", desc: "Merkezi lokasyonda halı temizleme", type: "hali-yikama", area: "kadikoy" },
    { name: "icerenkoy-hali-yikama", title: "İçerenköy Halı Yıkama", desc: "Modern semtte halı yıkama hizmeti", type: "hali-yikama", area: "atasehir" },
    { name: "kucukbakkalkoy-hali-yikama", title: "Küçükbakkalköy Halı Yıkama", desc: "Sakin bölgede kaliteli halı bakımı", type: "hali-yikama", area: "atasehir" },
    { name: "maltepe-hali-yikama", title: "Maltepe Halı Yıkama", desc: "Sahil kesiminde halı temizleme", type: "hali-yikama", area: "maltepe" },
    { name: "suadiye-hali-yikama", title: "Suadiye Halı Yıkama", desc: "Lüks semtte profesyonel halı temizleme", type: "hali-yikama", area: "kadikoy" },
    { name: "umraniye-hali-yikama", title: "Ümraniye Halı Yıkama", desc: "Modern yaşam alanında halı bakımı", type: "hali-yikama", area: "umraniye" },
    { name: "uskudar-hali-yikama", title: "Üsküdar Halı Yıkama", desc: "Tarihi yarımadada halı temizleme", type: "hali-yikama", area: "uskudar" },
    
    // Koltuk Yıkama Sayfaları
    { name: "bagdat-caddesi-koltuk-yikama", title: "Bağdat Caddesi Koltuk Yıkama", desc: "Luxury mobilya temizleme hizmeti", type: "koltuk-yikama", area: "kadikoy" },
    { name: "barbaros-koltuk-yikama", title: "Barbaros Koltuk Yıkama", desc: "VIP mobilya bakım hizmeti", type: "koltuk-yikama", area: "kadikoy" },
    { name: "bostanci-koltuk-yikama", title: "Bostancı Koltuk Yıkama", desc: "Sahil kesimi mobilya temizleme", type: "koltuk-yikama", area: "kadikoy" },
    { name: "fikirtepe-koltuk-yikama", title: "Fikirtepe Koltuk Yıkama", desc: "Modern semtte mobilya bakımı", type: "koltuk-yikama", area: "kadikoy" },
    { name: "kadikoy-koltuk-yikama", title: "Kadıköy Koltuk Yıkama", desc: "Sanat mobilya temizleme hizmeti", type: "koltuk-yikama", area: "kadikoy" },
    { name: "kalamis-koltuk-yikama", title: "Kalamış Koltuk Yıkama", desc: "Sahil kesimi koltuk temizleme", type: "koltuk-yikama", area: "kadikoy" },
    { name: "kartal-koltuk-yikama", title: "Kartal Koltuk Yıkama", desc: "Geniş alanda mobilya bakım hizmeti", type: "koltuk-yikama", area: "kartal" },
    { name: "kucukbakkalkoy-koltuk-yikama", title: "Küçükbakkalköy Koltuk Yıkama", desc: "Sakin bölgede koltuk bakımı", type: "koltuk-yikama", area: "atasehir" },
    { name: "moda-koltuk-yikama", title: "Moda Koltuk Yıkama", desc: "Trendy semtte mobilya temizleme", type: "koltuk-yikama", area: "kadikoy" },
    { name: "pendik-koltuk-yikama", title: "Pendik Koltuk Yıkama", desc: "Genişleyen bölgede koltuk bakımı", type: "koltuk-yikama", area: "pendik" },
    { name: "uskudar-koltuk-yikama", title: "Üsküdar Koltuk Yıkama", desc: "Tarihi semtte mobilya temizleme", type: "koltuk-yikama", area: "uskudar" },
    
    // Özel Hizmetler
    { name: "uskudar-gelinlik-temizleme", title: "Üsküdar Gelinlik Temizleme", desc: "Özel günler için gelinlik bakımı", type: "ozel", area: "uskudar" }
];

// Her sayfa için 8 unique kart seç
function generateDistrictCards(currentPage) {
    const current = districts.find(d => d.name === currentPage);
    if (!current) return [];
    
    let recommendations = [];
    
    // 1. Aynı tip hizmetler (2-3 kart)
    const sameType = districts.filter(d => 
        d.name !== currentPage && 
        d.type === current.type
    ).slice(0, 3);
    
    // 2. Aynı bölge, farklı hizmetler (2 kart)  
    const sameArea = districts.filter(d =>
        d.name !== currentPage &&
        d.area === current.area &&
        d.type !== current.type
    ).slice(0, 2);
    
    // 3. Popüler/Premium hizmetler (3 kart)
    const premium = districts.filter(d =>
        d.name !== currentPage &&
        !sameType.includes(d) &&
        !sameArea.includes(d) &&
        (d.type === 'luxury' || d.type === 'premium' || d.name.includes('bagdat-caddesi'))
    ).slice(0, 3);
    
    recommendations = [...sameType, ...sameArea, ...premium];
    
    // Eğer 8'den az varsa, rastgele tamamla
    while (recommendations.length < 8) {
        const remaining = districts.filter(d => 
            d.name !== currentPage && 
            !recommendations.includes(d)
        );
        
        if (remaining.length === 0) break;
        recommendations.push(remaining[Math.floor(Math.random() * remaining.length)]);
    }
    
    return recommendations.slice(0, 8);
}

// Her sayfa için kart setleri oluştur
console.log('// DYNAMIC DISTRICT CARDS MAPPING\n');

districts.forEach(district => {
    const cards = generateDistrictCards(district.name);
    console.log(`// ${district.title} için öneriler:`);
    console.log(`const ${district.name.replace(/-/g, '_')}_cards = [`);
    
    cards.forEach(card => {
        console.log(`    { name: "${card.name}", title: "${card.title}", desc: "${card.desc}" },`);
    });
    
    console.log('];\n');
});