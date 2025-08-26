/* 
 * DryAlle Design System - Pricing Data Module
 * Multi-Service Data Structure
 * MIT-Level Architecture Implementation
 */

// Multi-Service Pricing Data
const multiServicePricingData = [
    {
        id: "esofman-takim",
        name: "EŞOFMAN TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "yikama", price: 120, popular: false },
            { type: "utuleme", price: 75, popular: false }
        ]
    },
    {
        id: "takim-elbise",
        name: "TAKIM ELBİSE (2 PARÇA)",
        category: "erkek-giyim", 
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 280, popular: true },
            { type: "utuleme", price: 140, popular: false },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "gomlek-erkek",
        name: "GÖMLEK ERKEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim", 
        services: [
            { type: "kuru-temizleme", price: 95, popular: true },
            { type: "yikama", price: 75, popular: false },
            { type: "utuleme", price: 45, popular: true }
        ]
    },
    {
        id: "ceket-erkek",
        name: "CEKET ERKEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 190, popular: true },
            { type: "utuleme", price: 95, popular: false }
        ]
    },
    {
        id: "elbise-kadin",
        name: "ELBİSE KADIN (NORMAL)",
        category: "kadin-giyim",
        subcategory: "kadin-elbise-takim",
        services: [
            { type: "kuru-temizleme", price: 165, popular: true },
            { type: "yikama", price: 135, popular: false },
            { type: "utuleme", price: 85, popular: false }
        ]
    },
    {
        id: "bluz-kadin",
        name: "BLUZ KADIN",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 95, popular: true },
            { type: "yikama", price: 75, popular: false },
            { type: "utuleme", price: 45, popular: true }
        ]
    },
    {
        id: "gelinlik",
        name: "GELİNLİK",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        services: [
            { type: "kuru-temizleme", price: 950, popular: true },
            { type: "leke-cikarma", price: 285, popular: false },
            { type: "utuleme", price: 190, popular: false }
        ]
    },
    {
        id: "cocuk-elbise",
        name: "ÇOCUK ELBİSESİ",
        category: "cocuk-giyim",
        subcategory: "cocuk-ozel-gunler",
        services: [
            { type: "kuru-temizleme", price: 135, popular: true },
            { type: "yikama", price: 95, popular: false },
            { type: "utuleme", price: 65, popular: false }
        ]
    },
    {
        id: "hali-m2",
        name: "HALI (m² Başına)",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-1572123979839-3749e9973aba?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 45, popular: true },
            { type: "hali-tamiri", price: 85, popular: false },
            { type: "sacak-tamiri", price: 25, popular: false },
            { type: "hali-boyama", price: 120, popular: false }
        ]
    },
    {
        id: "koltuk-temizlik",
        name: "KOLTUK TEMİZLİĞİ (Yerinde)",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        image: "https://images.unsplash.com/photo-1686178827149-6d55c72d81df?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 285, popular: true },
            { type: "leke-cikarma", price: 125, popular: false },
            { type: "antibakteriyel", price: 85, popular: false }
        ]
    },
    {
        id: "perde-m2",
        name: "PERDE (m² Başına)",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "https://plus.unsplash.com/premium_photo-1673152979215-69b97746b05e?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 35, popular: true },
            { type: "yikama", price: 28, popular: false },
            { type: "utuleme", price: 18, popular: false }
        ]
    },
    {
        id: "deri-ceket",
        name: "DERİ CEKET",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 385, popular: true },
            { type: "deri-boyama", price: 575, popular: false },
            { type: "leke-cikarma", price: 195, popular: false }
        ]
    },
    {
        id: "kilim-m2",
        name: "KİLİM (m² Başına)",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-1531162805941-58330188d75c?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yikama", price: 35, popular: true },
            { type: "kuru-temizleme", price: 45, popular: false },
            { type: "sacak-tamiri", price: 20, popular: false }
        ]
    },
    {
        id: "yatak-ortusu",
        name: "YATAK ÖRTÜSÜ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "https://images.unsplash.com/photo-1606855637183-ea2a00b6f15f?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 185, popular: true },
            { type: "yikama", price: 145, popular: false },
            { type: "utuleme", price: 85, popular: false }
        ]
    },
    {
        id: "carsaf-takimi",
        name: "ÇARŞAF TAKIMI",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "yikama", price: 95, popular: true },
            { type: "utuleme", price: 65, popular: false },
            { type: "kuru-temizleme", price: 125, popular: false }
        ]
    },
    {
        id: "kanepe-3lu",
        name: "KANEPE TEMİZLİĞİ (3lü)",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "yerinde-temizleme", price: 385, popular: true },
            { type: "antibakteriyel", price: 125, popular: false },
            { type: "leke-cikarma", price: 165, popular: false }
        ]
    },
    {
        id: "berjer-temizlik",
        name: "BERJER TEMİZLİĞİ",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "yerinde-temizleme", price: 185, popular: true },
            { type: "leke-cikarma", price: 95, popular: false },
            { type: "antibakteriyel", price: 65, popular: false }
        ]
    },
    {
        id: "silte-cift",
        name: "ŞİLTE (Çift Kişilik)",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "yerinde-temizleme", price: 285, popular: true },
            { type: "antibakteriyel", price: 95, popular: false },
            { type: "leke-cikarma", price: 125, popular: false }
        ]
    },
    // Batch 2: Excel entries 101-200 (48 items)
    {
        id: "mi-nder-tadi-lat-elyaflama-batch2",
        name: "MİNDER TADİLAT ELYAFLAMA",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "yerinde-temizleme", price: 1000, popular: false }
        ]
    },
    {
        id: "mi-nder-tadi-lat-d-meleme-batch2",
        name: "MİNDER TADİLAT/DÜĞMELEME",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "yikama", price: 357, popular: true },
            { type: "yerinde-temizleme", price: 1000, popular: false }
        ]
    },
    {
        id: "mont-kap-onlu-batch2",
        name: "MONT KAPŞONLU",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "motorcu-montu-batch2",
        name: "MOTORCU MONTU",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 850, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "muhteli-f-temi-zleme-batch2",
        name: "MUHTELİF TEMİZLEME",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "nevresi-m-i-ft-ki-i-li-k-batch2",
        name: "NEVRESİM ÇİFT KİŞİLİK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 300, popular: true }
        ]
    },
    {
        id: "nevresi-m-tek-ki-i-li-k-batch2",
        name: "NEVRESİM TEK KİŞİLİK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 450, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 300, popular: true }
        ]
    },
    {
        id: "overlok-normal-batch2",
        name: "OVERLOK NORMAL",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "hali-yikama", price: 150, popular: false }
        ]
    },
    {
        id: "overlok-y-n-batch2",
        name: "OVERLOK YÜN",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "hali-yikama", price: 200, popular: false }
        ]
    },
    {
        id: "pantolon-boyama-batch2",
        name: "PANTOLON BOYAMA",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "pantolon-grubu-batch2",
        name: "PANTOLON GRUBU",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "pelu-mont-batch2",
        name: "PELUŞ MONT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 595, popular: true }
        ]
    },
    {
        id: "perde-fon-i-ft-kat-batch2",
        name: "PERDE FON ÇİFT KAT",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 125, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 95, popular: true }
        ]
    },
    {
        id: "perde-fon-tek-kat-batch2",
        name: "PERDE FON TEK KAT",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 100, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 83, popular: true }
        ]
    },
    {
        id: "pi-ke-batch2",
        name: "PİKE",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 400, popular: false },
            { type: "yikama", price: 595, popular: true }
        ]
    },
    {
        id: "puf-batch2",
        name: "PUF",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "yerinde-temizleme", price: 450, popular: true }
        ]
    },
    {
        id: "robte-ambir-batch2",
        name: "ROBTEŞAMBIR",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 250, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "sandalye-temi-zleme-tam-batch2",
        name: "SANDALYE TEMİZLEME TAM",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "yerinde-temizleme", price: 300, popular: true }
        ]
    },
    {
        id: "sandalye-temi-zleme-yarim-batch2",
        name: "SANDALYE TEMİZLEME YARIM",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "yerinde-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "apka-boyama-batch2",
        name: "ŞAPKA BOYAMA",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "boyama", price: 200, popular: false }
        ]
    },
    {
        id: "stor-batch2",
        name: "STOR",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "yikama", price: 153, popular: true }
        ]
    },
    {
        id: "tadi-lat-batch2",
        name: "TADİLAT",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true }
        ]
    },
    {
        id: "takim-elbi-se-batch2",
        name: "TAKIM ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "terzi-tadi-lat-batch2",
        name: "TERZİ TADİLAT",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true }
        ]
    },
    {
        id: "tuhafi-ye-i-p-d-me-vs-demesi-batch2",
        name: "TUHAFİYE İP/ DÜĞME VS. ÖDEMESİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "yikama", price: 119, popular: true },
            { type: "yerinde-temizleme", price: 500, popular: false }
        ]
    },
    {
        id: "t-l-batch2",
        name: "TÜL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 50, popular: true },
            { type: "utuleme", price: 40, popular: false },
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "t-l-store-st-dahi-l-batch2",
        name: "TÜL STORE ST DAHİL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "tulum-elbi-se-batch2",
        name: "TULUM ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-elbise-takim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "vi-scon-hali-batch2",
        name: "VİSCON HALI",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "hali-yikama", price: 350, popular: true }
        ]
    },
    {
        id: "vi-skon-yastik-batch2",
        name: "VİSKON YASTIK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 500, popular: true }
        ]
    },
    {
        id: "yatak-ba-li-i-i-ft-batch2",
        name: "YATAK BAŞLIĞI ÇİFT",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "yerinde-temizleme", price: 1000, popular: true }
        ]
    },
    {
        id: "yatak-ba-li-i-tek-batch2",
        name: "YATAK BAŞLIĞI TEK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "yerinde-temizleme", price: 750, popular: true }
        ]
    },
    {
        id: "yatak-pedi-batch2",
        name: "YATAK PEDİ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 600, popular: true },
            { type: "yerinde-temizleme", price: 2000, popular: false }
        ]
    },
    {
        id: "yatak-yikama-i-ft-batch2",
        name: "YATAK YIKAMA ÇİFT",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "yerinde-temizleme", price: 2500, popular: true }
        ]
    },
    {
        id: "yatak-yikama-tek-batch2",
        name: "YATAK YIKAMA TEK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "yerinde-temizleme", price: 2000, popular: true }
        ]
    },
    {
        id: "yeri-nde-hali-yikama-batch2",
        name: "YERİNDE HALI YIKAMA",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "yerinde-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "yorgan-tek-ki-i-li-k-y-n-pamuk-batch2",
        name: "YORGAN TEK KİŞİLİK YÜN /PAMUK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 700, popular: true },
            { type: "yikama", price: 700, popular: true }
        ]
    },
    {
        id: "y-n-omuz-ali-batch2",
        name: "YÜN OMUZ ŞALI",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 450, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 350, popular: true }
        ]
    },
    {
        id: "zebra-perde-batch2",
        name: "ZEBRA PERDE",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "zebra-t-l-batch2",
        name: "ZEBRA TÜL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "ceket-batch2",
        name: "CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "pantolon-batch2",
        name: "PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 142, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "g-mlek-batch2",
        name: "GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "t-shi-rt-batch2",
        name: "T-SHİRT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 150, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "kazak-batch2",
        name: "KAZAK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "kravat-batch2",
        name: "KRAVAT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 150, popular: true }
        ]
    },
    {
        id: "mont-batch2",
        name: "MONT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 600, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "kaban-batch2",
        name: "KABAN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    // Batch 3: Excel entries 201-300 (36 items)
    {
        id: "kaban-batch3",
        name: "KABAN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "pardes-batch3",
        name: "PARDESÜ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 750, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "manto-palto-batch3",
        name: "MANTO - PALTO",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "yelek-batch3",
        name: "YELEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 200, popular: true }
        ]
    },
    {
        id: "bluz-batch3",
        name: "BLUZ",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "etek-batch3",
        name: "ETEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 250, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "bayan-elbi-se-batch3",
        name: "BAYAN ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-elbise-takim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 400, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "d-pi-yes-batch3",
        name: "DÖPİYES",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "mont-kaz-t-y-batch3",
        name: "MONT KAZ TÜYÜ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "utuleme", price: 250, popular: false },
            { type: "yikama", price: 800, popular: true }
        ]
    },
    {
        id: "kaban-kaz-t-y-batch3",
        name: "KABAN KAZ TÜYÜ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "utuleme", price: 119, popular: false },
            { type: "yikama", price: 800, popular: true }
        ]
    },
    {
        id: "al-batch3",
        name: "ŞAL",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 200, popular: true }
        ]
    },
    {
        id: "atki-batch3",
        name: "ATKI",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "yikama", price: 150, popular: true }
        ]
    },
    {
        id: "e-arp-batch3",
        name: "EŞARP",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 150, popular: true }
        ]
    },
    {
        id: "g-mlek-i-pek-batch3",
        name: "GÖMLEK İPEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "zel-elbi-se-batch3",
        name: "ÖZEL ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        services: [
            { type: "kuru-temizleme", price: 850, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "deri-elbi-se-batch3",
        name: "DERİ ELBİSE",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 500, popular: false },
            { type: "yikama", price: 714, popular: true },
            { type: "boyama", price: 1500, popular: false }
        ]
    },
    {
        id: "abi-ye-elbi-se-batch3",
        name: "ABİYE ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        services: [
            { type: "kuru-temizleme", price: 900, popular: true },
            { type: "utuleme", price: 350, popular: false },
            { type: "yikama", price: 900, popular: true }
        ]
    },
    {
        id: "geli-nli-k-batch3",
        name: "GELİNLİK",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true },
            { type: "utuleme", price: 750, popular: false },
            { type: "yikama", price: 1547, popular: true }
        ]
    },
    {
        id: "mont-deri-batch3",
        name: "MONT DERİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 500, popular: false },
            { type: "yikama", price: 1500, popular: true }
        ]
    },
    {
        id: "ceket-deri-batch3",
        name: "CEKET DERİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 500, popular: false },
            { type: "yikama", price: 952, popular: true }
        ]
    },
    {
        id: "ceket-s-et-batch3",
        name: "CEKET SÜET",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 500, popular: false },
            { type: "yikama", price: 1500, popular: true },
            { type: "boyama", price: 1500, popular: false }
        ]
    },
    {
        id: "ceket-nubuk-batch3",
        name: "CEKET NUBUK",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 500, popular: false },
            { type: "yikama", price: 1500, popular: true },
            { type: "boyama", price: 1500, popular: false }
        ]
    },
    {
        id: "mont-nubuk-batch3",
        name: "MONT NUBUK",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true },
            { type: "utuleme", price: 500, popular: false },
            { type: "yikama", price: 952, popular: true }
        ]
    },
    {
        id: "hali-maki-ne-batch3",
        name: "HALI MAKİNE",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "hali-yikama", price: 200, popular: true }
        ]
    },
    {
        id: "hali-nepal-batch3",
        name: "HALI NEPAL",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "hali-yikama", price: 300, popular: true }
        ]
    },
    {
        id: "hali-shagy-batch3",
        name: "HALI SHAGY",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "hali-yikama", price: 250, popular: true }
        ]
    },
    {
        id: "hali-step-batch3",
        name: "HALI STEP",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "hali-yikama", price: 350, popular: true }
        ]
    },
    {
        id: "hali-maki-ne-y-n-batch3",
        name: "HALI MAKİNE YÜNÜ",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "hali-yikama", price: 250, popular: true }
        ]
    },
    {
        id: "battani-ye-batch3",
        name: "BATTANİYE",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "bornoz-batch3",
        name: "BORNOZ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "boxer-batch3",
        name: "BOXER",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 100, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 85, popular: true }
        ]
    },
    {
        id: "ar-af-batch3",
        name: "ÇARŞAF",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "yikama", price: 190, popular: true }
        ]
    },
    {
        id: "ocuk-elbi-se-batch3",
        name: "ÇOCUK ELBİSE",
        category: "cocuk-giyim",
        subcategory: "cocuk-ozel-gunler",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 255, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "orap-batch3",
        name: "ÇORAP",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 50, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 35, popular: true }
        ]
    },
    {
        id: "c-bbe-kep-batch3",
        name: "CÜBBE - KEP",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "havlu-b-y-k-batch3",
        name: "HAVLU BÜYÜK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true }
        ]
    },
    // Batch 4: Excel entries 301-400 (40 items)
    {
        id: "havlu-b-y-k-batch4",
        name: "HAVLU BÜYÜK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 100, popular: true }
        ]
    },
    {
        id: "havlu-k-k-batch4",
        name: "HAVLU KÜÇÜK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 47, popular: true }
        ]
    },
    {
        id: "kaz-t-y-yastik-batch4",
        name: "KAZ TÜYÜ YASTIK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 700, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "nevresi-m-takimi-batch4",
        name: "NEVRESİM TAKIMI",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 400, popular: false },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "perde-kadi-fe-batch4",
        name: "PERDE KADİFE",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 95, popular: true }
        ]
    },
    {
        id: "perde-stor-st-dahi-l-batch4",
        name: "PERDE STOR ST DAHİL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "perde-stor-st-hari-batch4",
        name: "PERDE STOR ST HARİÇ",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "yikama", price: 200, popular: true }
        ]
    },
    {
        id: "perde-katlmali-st-dahi-l-batch4",
        name: "PERDE KATLMALI ST DAHİL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 107, popular: true }
        ]
    },
    {
        id: "perde-katlmali-st-hari-batch4",
        name: "PERDE KATLMALI ST HARİÇ",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 83, popular: true }
        ]
    },
    {
        id: "perde-t-l-b-y-k-batch4",
        name: "PERDE TÜL BÜYÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 400, popular: false },
            { type: "yikama", price: 595, popular: true }
        ]
    },
    {
        id: "perde-t-l-k-k-batch4",
        name: "PERDE TÜL KÜÇÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "perde-t-l-orta-batch4",
        name: "PERDE TÜL ORTA",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "utuleme", price: 350, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "perde-zebra-st-dahi-l-batch4",
        name: "PERDE ZEBRA ST DAHİL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "yikama", price: 153, popular: true }
        ]
    },
    {
        id: "perde-zebra-st-hari-batch4",
        name: "PERDE ZEBRA ST HARİÇ",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "yikama", price: 136, popular: true }
        ]
    },
    {
        id: "perde-keten-batch4",
        name: "PERDE KETEN",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 100, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 85, popular: true }
        ]
    },
    {
        id: "perde-saten-batch4",
        name: "PERDE SATEN",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 100, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 83, popular: true }
        ]
    },
    {
        id: "etek-pi-leli-batch4",
        name: "ETEK PİLELİ",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "si-moki-n-batch4",
        name: "SİMOKİN",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 350, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "ort-batch4",
        name: "ŞORT",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 200, popular: true }
        ]
    },
    {
        id: "yastik-batch4",
        name: "YASTIK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 450, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 300, popular: true }
        ]
    },
    {
        id: "yastik-y-z-batch4",
        name: "YASTIK YÜZÜ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 100, popular: true },
            { type: "hali-yikama", price: 150, popular: false }
        ]
    },
    {
        id: "yatak-rt-s-g-nl-k-batch4",
        name: "YATAK ÖRTÜSÜ GÜNLÜK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 250, popular: false },
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "yatak-rt-s-zel-batch4",
        name: "YATAK ÖRTÜSÜ ÖZEL",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "yorgan-elyaf-k-batch4",
        name: "YORGAN ELYAF ÇK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "yorgan-elyaf-tk-batch4",
        name: "YORGAN ELYAF TK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "yorgan-kaz-t-y-batch4",
        name: "YORGAN KAZ TÜYÜ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 750, popular: true }
        ]
    },
    {
        id: "yorgan-y-z-batch4",
        name: "YORGAN YÜZÜ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 400, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "yorgan-pamuk-y-n-batch4",
        name: "YORGAN PAMUK-YÜN",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 700, popular: true }
        ]
    },
    {
        id: "havlu-batch4",
        name: "HAVLU",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 47, popular: true }
        ]
    },
    {
        id: "battani-ye-battal-batch4",
        name: "BATTANİYE BATTAL",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 700, popular: true },
            { type: "yikama", price: 510, popular: true }
        ]
    },
    {
        id: "ocuk-abi-ye-batch4",
        name: "ÇOCUK ABİYE",
        category: "cocuk-giyim",
        subcategory: "cocuk-ozel-gunler",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "hirka-batch4",
        name: "HIRKA",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "nubuk-elbi-se-batch4",
        name: "NUBUK ELBİSE",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true }
        ]
    },
    {
        id: "mi-nder-y-z-batch4",
        name: "MİNDER YÜZÜ",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "koltuk-rt-s-batch4",
        name: "KOLTUK ÖRTÜSÜ",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true }
        ]
    },
    {
        id: "banyo-ki-li-mi-batch4",
        name: "BANYO KİLİMİ",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "kuru-temizleme", price: 400, popular: true },
            { type: "yikama", price: 340, popular: true }
        ]
    },
    {
        id: "yorgan-ku-t-y-batch4",
        name: "YORGAN KUŞTÜYÜ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 750, popular: true }
        ]
    },
    {
        id: "anta-batch4",
        name: "ÇANTA",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 700, popular: true },
            { type: "yikama", price: 680, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "anta-deri-batch4",
        name: "ÇANTA DERİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "yikama", price: 765, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "anta-s-et-batch4",
        name: "ÇANTA SÜET",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "yikama", price: 765, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    
    // Batch 5 Items (Entries 401-500): 37 items
    {
        id: "ayakkabi-batch5",
        name: "AYAKKABI",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 765, popular: true },
            { type: "lostra", price: 750, popular: false }
        ]
    },
    {
        id: "atlet-batch5",
        name: "ATLET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 100, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 76, popular: true }
        ]
    },
    {
        id: "deri-ayakkabi-batch5",
        name: "DERİ AYAKKABI",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "lostra", price: 750, popular: false }
        ]
    },
    {
        id: "battani-ye-tk-batch5",
        name: "BATTANİYE TK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "battani-ye-yun-ck-batch5",
        name: "BATTANİYE YÜN ÇK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "yikama", price: 680, popular: true }
        ]
    },
    {
        id: "battani-ye-yun-tk-batch5",
        name: "BATTANİYE YÜN TK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "yikama", price: 595, popular: true }
        ]
    },
    {
        id: "bayrak-batch5",
        name: "BAYRAK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    {
        id: "bere-batch5",
        name: "BERE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 127, popular: true }
        ]
    },
    {
        id: "bermuda-batch5",
        name: "BERMUDA",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "bermuda-deri-batch5",
        name: "BERMUDA DERİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 500, popular: false },
            { type: "yikama", price: 510, popular: true }
        ]
    },
    {
        id: "bone-batch5",
        name: "BONE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 127, popular: true }
        ]
    },
    {
        id: "bra-suti-yen-batch5",
        name: "BRA / SÜTİYEN",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 110, popular: true }
        ]
    },
    {
        id: "canta-keten-batch5",
        name: "ÇANTA KETEN",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 425, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "canta-kuma-batch5",
        name: "ÇANTA KUMAŞ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 425, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "ci-cek-batch5",
        name: "ÇİÇEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 127, popular: true }
        ]
    },
    {
        id: "cicek-yaka-batch5",
        name: "ÇİÇEK YAKA",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 127, popular: true }
        ]
    },
    {
        id: "detay-i-leme-batch5",
        name: "DETAY İŞLEME",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    {
        id: "dog-um-elbi-sesi-batch5",
        name: "DOĞUM ELBİSESİ",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 250, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "durumlu-masa-rtus-batch5",
        name: "DURUMLU MASA ÖRTÜSÜ",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "eldi-ven-batch5",
        name: "ELDİVEN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 127, popular: true }
        ]
    },
    {
        id: "esofman-takim-batch5",
        name: "EŞOFMAN TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "esofman-alt-batch5",
        name: "EŞOFMAN ALT",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "esofman-ust-batch5",
        name: "EŞOFMAN ÜST",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "fanila-batch5",
        name: "FANİLA",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    {
        id: "fular-batch5",
        name: "FULAR",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 127, popular: true }
        ]
    },
    {
        id: "gardrop-aylık-batch5",
        name: "GARDROP AYLIK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true }
        ]
    },
    {
        id: "jartiyer-batch5",
        name: "JARTİYER",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 110, popular: true }
        ]
    },
    {
        id: "jeans-pantolon-batch5",
        name: "JEANS PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "kimono-batch5",
        name: "KİMONO",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 250, popular: false },
            { type: "yikama", price: 510, popular: true }
        ]
    },
    {
        id: "kravat-papyon-batch5",
        name: "KRAVAT / PAPYON",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 150, popular: true }
        ]
    },
    {
        id: "kus-eri-batch5",
        name: "KUŞAK / KEMERİ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true }
        ]
    },
    {
        id: "mant-lla-batch5",
        name: "MANTİLLA",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    {
        id: "masa-rtus-batch5",
        name: "MASA ÖRTÜSÜ",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "mayo-bikni-batch5",
        name: "MAYO / BİKİNİ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 127, popular: true }
        ]
    },
    {
        id: "musli-n-batch5",
        name: "MÜSLİN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true }
        ]
    },
    {
        id: "apka-batch5",
        name: "ŞAPKA",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true }
        ]
    },
    {
        id: "ort-mayo-batch5",
        name: "ŞORT / MAYO",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    
    // Batch 6 Items (Entries 501-600): 33 items
    {
        id: "ferace-batch6",
        name: "FERACE",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "yikama", price: 309, popular: true }
        ]
    },
    {
        id: "trenckot-batch6",
        name: "TRENCKOT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "spor-ayakkabi-batch6",
        name: "SPOR AYAKKABI",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 416, popular: true }
        ]
    },
    {
        id: "esofman-batch6",
        name: "EŞOFMAN",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 300, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "kaban-akri-li-k-batch6",
        name: "KABAN AKRİLİK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "yikama", price: 800, popular: true }
        ]
    },
    {
        id: "anorak-batch6",
        name: "ANORAK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "elbi-se-batch6",
        name: "ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 450, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 400, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "kar-i-k-batch6",
        name: "KARDİĞAN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "sort-batch6",
        name: "ŞORT",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 200, popular: true }
        ]
    },
    {
        id: "etek-batch6",
        name: "ETEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 250, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "elbi-se-i-pek-batch6",
        name: "ELBİSE İPEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "ayakkabi-bez-batch6",
        name: "AYAKKABI BEZ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "ayakkabi-kuma-batch6",
        name: "AYAKKABI KUMAŞ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "ayakkabi-s-et-batch6",
        name: "AYAKKABI SÜET",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "boyama", price: 750, popular: false }
        ]
    },
    {
        id: "ocuk-g-mlek-batch6",
        name: "ÇOCUK GÖMLEK",
        category: "cocuk-giyim",
        subcategory: "cocuk-ozel-gunler",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 119, popular: true }
        ]
    },
    {
        id: "ocuk-pantolon-batch6",
        name: "ÇOCUK PANTOLON",
        category: "cocuk-giyim",
        subcategory: "cocuk-ozel-gunler",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 119, popular: true }
        ]
    },
    {
        id: "ocuk-ceket-batch6",
        name: "ÇOCUK CEKET",
        category: "cocuk-giyim",
        subcategory: "cocuk-ozel-gunler",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "fistan-batch6",
        name: "FISTAN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 238, popular: true }
        ]
    },
    {
        id: "g-mlek-pamuk-batch6",
        name: "GÖMLEK PAMUK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "eketler-batch6",
        name: "CEKETLER",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "eaket-denim-batch6",
        name: "CEKET DENİM",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true }
        ]
    },
    {
        id: "abi-ye-etek-batch6",
        name: "ABİYE ETEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 663, popular: true }
        ]
    },
    {
        id: "abi-ye-u-st-batch6",
        name: "ABİYE ÜST",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 663, popular: true }
        ]
    },
    {
        id: "mont-yaga-ur-batch6",
        name: "MONT YAĞMURLUK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "keten-pantolonu-batch6",
        name: "KETEN PANTOLONU",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "poli-ester-pantolon-batch6",
        name: "POLİESTER PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "kar-i-an-i-pek-batch6",
        name: "KARDİGAN İPEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "halı-y-kamasi-m2-batch6",
        name: "HALI YIKAMASI M2",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "hali-yikama", price: 250, popular: true }
        ]
    },
    {
        id: "hali-doku-ma-m2-batch6",
        name: "HALI DOKUMA M2",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        services: [
            { type: "hali-yikama", price: 400, popular: true }
        ]
    },
    {
        id: "keten-g-mle-i-batch6",
        name: "KETEN GÖMLEĞİ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "spor-giyim-batch6",
        name: "SPOR GİYİM",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "spor-eek-batch6",
        name: "SPOR CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true }
        ]
    },
    {
        id: "spor-pantolon-batch6",
        name: "SPOR PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    
    // Batch 7 Items (Entries 601-700): 39 items
    {
        id: "eldi-ven-deri-batch7",
        name: "ELDİVEN DERİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "yikama", price: 190, popular: true },
            { type: "boyama", price: 170, popular: false }
        ]
    },
    {
        id: "eldi-ven-suet-batch7",
        name: "ELDİVEN SÜET",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 400, popular: true },
            { type: "yikama", price: 190, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "esofman-2-li-tak-batch7",
        name: "ESOFMAN 2'Lİ TAK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 300, popular: true }
        ]
    },
    {
        id: "esofman-3-lu-takim-batch7",
        name: "ESOFMAN 3'LU TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 700, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 300, popular: true }
        ]
    },
    {
        id: "esofman-tek-batch7",
        name: "ESOFMAN TEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 300, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "esarp-i-pek-batch7",
        name: "EŞARP İPEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "fantezi-ceket-batch7",
        name: "FANTEZİ CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "futbol-forması-batch7",
        name: "FUTBOL FORMASI",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    {
        id: "gabardin-pantolon-batch7",
        name: "GABARDİN PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "gotik-elbi-se-batch7",
        name: "GOTİK ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 663, popular: true }
        ]
    },
    {
        id: "hırka-i-pek-batch7",
        name: "HIRKA İPEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "i-pek-elbi-se-batch7",
        name: "İPEK ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "i-pek-etek-batch7",
        name: "İPEK ETEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "jakar-kuma-batch7",
        name: "JAKAR KUMAŞ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "jeans-ceket-batch7",
        name: "JEANS CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true }
        ]
    },
    {
        id: "jeans-etek-batch7",
        name: "JEANS ETEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 250, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "jeans-g-mlek-batch7",
        name: "JEANS GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "kombinezon-batch7",
        name: "KOMBİNEZON",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "kordon-g-mlek-batch7",
        name: "KORDON GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "kot-ceket-batch7",
        name: "KOT CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true }
        ]
    },
    {
        id: "kostum-takım-batch7",
        name: "KOSTÜM TAKIM",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 595, popular: true }
        ]
    },
    {
        id: "k-rklu-ceket-batch7",
        name: "KÜRKLU CEKET",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true },
            { type: "yikama", price: 1500, popular: true }
        ]
    },
    {
        id: "k-rklu-kaban-batch7",
        name: "KÜRKLU KABAN",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 2500, popular: true },
            { type: "yikama", price: 1785, popular: true }
        ]
    },
    {
        id: "k-rklu-mont-batch7",
        name: "KÜRKLU MONT",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true },
            { type: "yikama", price: 1500, popular: true }
        ]
    },
    {
        id: "k-rklu-yelek-batch7",
        name: "KÜRKLU YELEK",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "yikama", price: 1071, popular: true }
        ]
    },
    {
        id: "k-rk-batch7",
        name: "KÜRK",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 3000, popular: true },
            { type: "yikama", price: 2142, popular: true }
        ]
    },
    {
        id: "likralı-tulum-batch7",
        name: "LİKRALI TULUM",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "lycra-pantolon-batch7",
        name: "LYCRA PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "maksi-elbi-se-batch7",
        name: "MAKSİ ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "mani-battal-mont-batch7",
        name: "MANİ BATTAL MONT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "utuleme", price: 250, popular: false },
            { type: "yikama", price: 714, popular: true }
        ]
    },
    {
        id: "moda-ceket-batch7",
        name: "MODA CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "nakı-li-etek-batch7",
        name: "NAKIŞLI ETEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "ni-an-elbi-sesi-batch7",
        name: "NİŞAN ELBİSESİ",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 1200, popular: true },
            { type: "utuleme", price: 500, popular: false },
            { type: "yikama", price: 952, popular: true }
        ]
    },
    {
        id: "organze-elbi-se-batch7",
        name: "ORGANZE ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "pijama-elbi-sesi-batch7",
        name: "PİJAMA ELBİSESİ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 238, popular: true }
        ]
    },
    {
        id: "polar-ceket-batch7",
        name: "POLAR CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true }
        ]
    },
    {
        id: "polar-pantolon-batch7",
        name: "POLAR PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "popli-n-g-mlek-batch7",
        name: "POPLİN GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "salopet-batch7",
        name: "SALOPET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "sıfı-r-yakali-g-mlek-batch7",
        name: "SIFIR YAKALI GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    
    // Batch 8 Items (Entries 701-800): 63 items
    {
        id: "kaban-deri-batch8",
        name: "KABAN DERİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "yikama", price: 1750, popular: true }
        ]
    },
    {
        id: "kaban-kapsonlu-batch8",
        name: "KABAN KAPŞONLU",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "kaban-kaz-tuyu-batch8",
        name: "KABAN KAZ TÜYÜ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 544, popular: true }
        ]
    },
    {
        id: "kaban-suet-batch8",
        name: "KABAN SÜET",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1750, popular: true },
            { type: "yikama", price: 1750, popular: true }
        ]
    },
    {
        id: "kaban-yaka-kol-kurklu-batch8",
        name: "KABAN YAKA-KOL KÜRKLÜ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "kaban-yakasi-kurklu-batch8",
        name: "KABAN YAKASI KÜRKLU",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "mont-kayak-batch8",
        name: "MONT KAYAK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 700, popular: true },
            { type: "yikama", price: 700, popular: true }
        ]
    },
    {
        id: "kayak-tak-2-par-batch8",
        name: "KAYAK TAK.2 PAR.",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 1000, popular: true }
        ]
    },
    {
        id: "kayak-pantolonu-batch8",
        name: "KAYAK PANTOLONU",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 500, popular: true }
        ]
    },
    {
        id: "kayak-montuu-batch8",
        name: "KAYAK MONTUU",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 500, popular: true }
        ]
    },
    {
        id: "mont-kosum-batch8",
        name: "MONT KOŞUM",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "mont-spor-batch8",
        name: "MONT SPOR",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "mont-terli-k-batch8",
        name: "MONT TERLİK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "mont-kı-li-k-batch8",
        name: "MONT KIŞLIK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "mont-astar-batch8",
        name: "MONT ASTAR",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "kapsonlu-ceket-batch8",
        name: "KAPŞONLU CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "yikama", price: 350, popular: true }
        ]
    },
    {
        id: "kapsonlu-sweatshirt-batch8",
        name: "KAPŞONLU SWEATSHİRT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "koltukalti-deri-si-batch8",
        name: "KOLTUKALTI DERİSİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 714, popular: true }
        ]
    },
    {
        id: "koltukalti-deri-elbi-se-batch8",
        name: "KOLTUKALTI DERİ ELBİSE",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "yikama", price: 1071, popular: true }
        ]
    },
    {
        id: "koltukalti-deri-ceket-batch8",
        name: "KOLTUKALTI DERİ CEKET",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "yikama", price: 1071, popular: true }
        ]
    },
    {
        id: "koltukalti-deri-pantolon-batch8",
        name: "KOLTUKALTI DERİ PANTOLON",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 714, popular: true }
        ]
    },
    {
        id: "uzun-ceket-batch8",
        name: "UZUN CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "vintage-elbi-se-batch8",
        name: "VİNTAGE ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "vintage-ceket-batch8",
        name: "VİNTAGE CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "vintage-kaban-batch8",
        name: "VİNTAGE KABAN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "vintage-mont-batch8",
        name: "VİNTAGE MONT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "vtakim-batch8",
        name: "VTAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 595, popular: true }
        ]
    },
    {
        id: "yelek-kadin-batch8",
        name: "YELEK KADIN",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 200, popular: true }
        ]
    },
    {
        id: "yelek-erkek-batch8",
        name: "YELEK ERKEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 200, popular: true }
        ]
    },
    {
        id: "yaka-kol-kur-k-batch8",
        name: "YAKA-KOL KÜRK",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "yikama", price: 535, popular: true }
        ]
    },
    {
        id: "takim-elbi-se-kadin-batch8",
        name: "TAKIM ELBİSE KADIN",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 595, popular: true }
        ]
    },
    {
        id: "takim-elbi-se-erkek-batch8",
        name: "TAKIM ELBİSE ERKEK",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "smokin-erkek-batch8",
        name: "SMOKİN ERKEK",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 350, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "smokin-kadin-batch8",
        name: "SMOKİN KADIN",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 350, popular: false },
            { type: "yikama", price: 476, popular: true }
        ]
    },
    {
        id: "uyku-tulum-batch8",
        name: "UYKU TULUM",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 238, popular: true }
        ]
    },
    {
        id: "terzi-tadi-lat-batch8",
        name: "TERZİ TADİLAT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true }
        ]
    },
    {
        id: "ust-balik-agzi-batch8",
        name: "ÜST BALIK AĞZI",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 127, popular: true }
        ]
    },
    {
        id: "ust-gundu-z-batch8",
        name: "ÜST GÜNDÜZ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    {
        id: "ust-gece-batch8",
        name: "ÜST GECE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 238, popular: true }
        ]
    },
    {
        id: "ust-japon-yagligi-batch8",
        name: "ÜST JAPON YAĞLIĞI",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 238, popular: true }
        ]
    },
    {
        id: "ust-kilot-batch8",
        name: "ÜST KILOT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 100, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 85, popular: true }
        ]
    },
    {
        id: "ust-elbise-gece-batch8",
        name: "ÜST ELBİSE GECE",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 663, popular: true }
        ]
    },
    {
        id: "ust-elbise-gundu-z-batch8",
        name: "ÜST ELBİSE GÜNDÜZ",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 450, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 400, popular: true }
        ]
    },
    {
        id: "perde-oto-daki-l-batch8",
        name: "PERDE OTO DAKİL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 125, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 95, popular: true }
        ]
    },
    {
        id: "perde-evsel-daki-l-batch8",
        name: "PERDE EVSEL DAKİL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 125, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 95, popular: true }
        ]
    },
    {
        id: "ust-gundu-z-i-pek-batch8",
        name: "ÜST GÜNDÜZ İPEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "triko-elbi-se-batch8",
        name: "TRİKO ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "triko-ceket-batch8",
        name: "TRİKO CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "triko-pantolon-batch8",
        name: "TRİKO PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "tolek-montuu-batch8",
        name: "TOLEK MONTUU",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "tuz-depolamalı-ceket-batch8",
        name: "TUZ DEPOLAMALI CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true }
        ]
    },
    {
        id: "tula-pantolon-batch8",
        name: "TULA PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "tula-elbi-se-batch8",
        name: "TULA ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "tula-ceket-batch8",
        name: "TULA CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "tula-takim-batch8",
        name: "TULA TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "tutmal-elbi-se-batch8",
        name: "TUTMAL ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "tutmal-ceket-batch8",
        name: "TUTMAL CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "tutmal-pantolon-batch8",
        name: "TUTMAL PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "tutmal-takim-batch8",
        name: "TUTMAL TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "visco-elbi-se-batch8",
        name: "VİSCO ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "visco-ceket-batch8",
        name: "VİSCO CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "visco-pantolon-batch8",
        name: "VİSCO PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "visco-takim-batch8",
        name: "VİSCO TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "ultra-son-isi-tma-batch8",
        name: "ULTRA SON ISITMA",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true }
        ]
    },
    
    // 🏁 FINAL Batch 9 Items (Entries 801-907): 62 items - TÜM EXCEL VERİSİ TAMAMLANDI! 🎉
    {
        id: "peluslar-batch9",
        name: "PELUŞLAR",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true }
        ]
    },
    {
        id: "perde-batch9",
        name: "PERDE",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 80, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 71, popular: true }
        ]
    },
    {
        id: "perde-i-pek-batch9",
        name: "PERDE İPEK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        services: [
            { type: "kuru-temizleme", price: 150, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 119, popular: true }
        ]
    },
    {
        id: "pi-jama-2-par-batch9",
        name: "PİJAMA 2 PAR.",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 107, popular: true }
        ]
    },
    {
        id: "pi-jama-2-par-i-pek-batch9",
        name: "PİJAMA 2 PAR.İPEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true }
        ]
    },
    {
        id: "pi-jama-2-par-saten-batch9",
        name: "PİJAMA 2 PAR.SATEN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true }
        ]
    },
    {
        id: "pi-jama-alt-batch9",
        name: "PİJAMA ALT",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "pi-jama-tek-parc-batch9",
        name: "PİJAMA TEK PARÇ.",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "pi-jama-ust-batch9",
        name: "PİJAMA ÜST",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true }
        ]
    },
    {
        id: "suet-terli-k-batch9",
        name: "SÜET TERLİK",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "terli-k-batch9",
        name: "TERLİK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "yikama", price: 255, popular: true }
        ]
    },
    {
        id: "terli-k-deri-batch9",
        name: "TERLİK DERİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "suet-ayakkabi-batch9",
        name: "SÜET AYAKKABI",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "boyama", price: 750, popular: false }
        ]
    },
    {
        id: "suet-bot-batch9",
        name: "SÜET BOT",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "boyama", price: 750, popular: false }
        ]
    },
    {
        id: "suet-cizme-batch9",
        name: "SÜET ÇİZME",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "boyama", price: 750, popular: false }
        ]
    },
    {
        id: "suet-kovboy-batch9",
        name: "SÜET KOVBOY",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "boyama", price: 750, popular: false }
        ]
    },
    {
        id: "suet-sapo-batch9",
        name: "SÜET ŞAPO",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 400, popular: true },
            { type: "yikama", price: 285, popular: true }
        ]
    },
    {
        id: "deri-terli-k-batch9",
        name: "DERİ TERLİK",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "deri-ayakkabi-batch9",
        name: "DERİ AYAKKABI",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "lostra", price: 750, popular: false }
        ]
    },
    {
        id: "deri-bot-batch9",
        name: "DERİ BOT",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "lostra", price: 750, popular: false }
        ]
    },
    {
        id: "deri-cizme-batch9",
        name: "DERİ ÇİZME",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "lostra", price: 750, popular: false }
        ]
    },
    {
        id: "deri-kovboy-batch9",
        name: "DERİ KOVBOY",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "yikama", price: 595, popular: true },
            { type: "lostra", price: 750, popular: false }
        ]
    },
    {
        id: "deri-sapo-batch9",
        name: "DERİ ŞAPO",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        services: [
            { type: "kuru-temizleme", price: 400, popular: true },
            { type: "yikama", price: 285, popular: true }
        ]
    },
    {
        id: "sweatshirt-batch9",
        name: "SWEATSHİRT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "sweatshirt-kapsonlu-batch9",
        name: "SWEATSHİRT KAPŞONLU",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "tek-taraflı-yuni-form-batch9",
        name: "TEK TARAFLI YUNİFORM",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    {
        id: "ti-fort-batch9",
        name: "TİFORT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true }
        ]
    },
    {
        id: "ti-k-g-mlek-batch9",
        name: "TİK GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "tunik-batch9",
        name: "TUNİK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 238, popular: true }
        ]
    },
    {
        id: "uniform-batch9",
        name: "UNİFORM",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 170, popular: true }
        ]
    },
    {
        id: "uzun-g-mlek-batch9",
        name: "UZUN GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 85, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "vestan-batch9",
        name: "VESTAN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 238, popular: true }
        ]
    },
    {
        id: "vi-kose-elbi-se-batch9",
        name: "VİKOSE ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "vi-kose-ceket-batch9",
        name: "VİKOSE CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "vi-kose-pantolon-batch9",
        name: "VİKOSE PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "vi-kose-takim-batch9",
        name: "VİKOSE TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "y-n-elbi-se-batch9",
        name: "YÜN ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "y-n-ceket-batch9",
        name: "YÜN CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "y-n-pantolon-batch9",
        name: "YÜN PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "y-n-takim-batch9",
        name: "YÜN TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "yatak-ortus-single-batch9",
        name: "YATAK ÖRTÜS SİNGLE",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 340, popular: true }
        ]
    },
    {
        id: "yatak-ortus-double-batch9",
        name: "YATAK ÖRTÜS DOUBLE",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true },
            { type: "utuleme", price: 250, popular: false },
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "yastik-duz-batch9",
        name: "YASTIK DÜZ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 450, popular: true },
            { type: "utuleme", price: 50, popular: false },
            { type: "yikama", price: 300, popular: true }
        ]
    },
    {
        id: "yastik-nakı-li-batch9",
        name: "YASTIK NAKIŞLI",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 340, popular: true }
        ]
    },
    {
        id: "yastik-saten-batch9",
        name: "YASTIK SATEN",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 100, popular: false },
            { type: "yikama", price: 340, popular: true }
        ]
    },
    {
        id: "yastik-i-pek-batch9",
        name: "YASTIK İPEK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "zip-pantolon-batch9",
        name: "ZİP PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true }
        ]
    },
    {
        id: "zip-g-mlek-batch9",
        name: "ZİP GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 60, popular: false },
            { type: "yikama", price: 153, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "zip-ceket-batch9",
        name: "ZİP CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "zip-elbi-se-batch9",
        name: "ZİP ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "zip-takim-batch9",
        name: "ZİP TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    },
    {
        id: "zip-mont-batch9",
        name: "ZİP MONT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 600, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "zip-kaban-batch9",
        name: "ZİP KABAN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 600, popular: true }
        ]
    },
    {
        id: "zip-sweatshirt-batch9",
        name: "ZİP SWEATSHİRT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "yikama", price: 250, popular: true }
        ]
    },
    {
        id: "zoom-elbi-se-batch9",
        name: "ZOOM ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 200, popular: false },
            { type: "yikama", price: 357, popular: true },
            { type: "boyama", price: 450, popular: false }
        ]
    },
    {
        id: "zoom-ceket-batch9",
        name: "ZOOM CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 150, popular: false },
            { type: "yikama", price: 350, popular: true },
            { type: "boyama", price: 500, popular: false }
        ]
    },
    {
        id: "zoom-pantolon-batch9",
        name: "ZOOM PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true },
            { type: "utuleme", price: 70, popular: false },
            { type: "yikama", price: 204, popular: true },
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "zoom-takim-batch9",
        name: "ZOOM TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false },
            { type: "yikama", price: 357, popular: true }
        ]
    }
];

// Category Display Names
const categoryDisplayNames = {
    'erkek-giyim': 'Erkek Giyim',
    'kadin-giyim': 'Kadın Giyim',
    'cocuk-giyim': 'Çocuk Giyim',
    'ev-tekstili': 'Ev Tekstili',
    'ozel-temizleme': 'Özel Temizleme'
};

// Subcategory Display Names
const subcategoryDisplayNames = {
    'erkek-ust-giyim': 'Üst Giyim',
    'erkek-alt-giyim': 'Alt Giyim',
    'erkek-takim-elbise': 'Takım Elbise',
    'kadin-ust-giyim': 'Üst Giyim',
    'kadin-elbise-takim': 'Elbise & Takım',
    'kadin-ozel-giyim': 'Özel Giyim',
    'cocuk-ozel-gunler': 'Özel Günler',
    'hali-kilim': 'Halı & Kilim',
    'mobilya-tekstili': 'Mobilya Tekstili',
    'perde-tul': 'Perde & Tül',
    'yatak-takimi': 'Yatak Takımı',
    'canta-ayakkabi': 'Çanta & Ayakkabi'
};

// Process Display Names
const processDisplayNames = {
    'kuru-temizleme': 'Kuru Temizleme',
    'yikama': 'Yıkama',
    'utuleme': 'Ütüleme',
    'hali-yikama': 'Halı Yıkama',
    'yerinde-temizleme': 'Yerinde Temizleme',
    'leke-cikarma': 'Leke Çıkarma',
    'boyama': 'Boyama',
    'deri-boyama': 'Deri Boyama',
    'hali-tamiri': 'Halı Tamiri',
    'sacak-tamiri': 'Saçak Tamiri',
    'hali-boyama': 'Halı Boyama',
    'antibakteriyel': 'Antibakteriyel',
    'lostra': 'Lostra'
};

// Category counts for sidebar (Updated with Batch 2)
const categoryCounts = {
    'all': multiServicePricingData.length,
    'erkek-giyim': multiServicePricingData.filter(item => item.category === 'erkek-giyim').length,
    'kadin-giyim': multiServicePricingData.filter(item => item.category === 'kadin-giyim').length,
    'cocuk-giyim': multiServicePricingData.filter(item => item.category === 'cocuk-giyim').length,
    'ev-tekstili': multiServicePricingData.filter(item => item.category === 'ev-tekstili').length,
    'ozel-temizleme': multiServicePricingData.filter(item => item.category === 'ozel-temizleme').length
};

// Subcategory counts
const subcategoryCounts = {};
multiServicePricingData.forEach(item => {
    if (!subcategoryCounts[item.subcategory]) {
        subcategoryCounts[item.subcategory] = 0;
    }
    subcategoryCounts[item.subcategory]++;
});

// Export data for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    // Node.js environment
    module.exports = {
        multiServicePricingData,
        categoryDisplayNames,
        subcategoryDisplayNames,
        processDisplayNames,
        categoryCounts,
        subcategoryCounts
    };
} else {
    // Browser environment - attach to window
    window.PricingData = {
        multiServicePricingData,
        categoryDisplayNames,
        subcategoryDisplayNames,
        processDisplayNames,
        categoryCounts,
        subcategoryCounts
    };
}