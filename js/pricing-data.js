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
        image: "https://images.unsplash.com/photo-1621976360623-004223992275?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000001?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=400&auto=format&fm=webp&q=75", 
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
        image: "https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1542295669297-4d352b042bca?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1685278463552-51396b0a6287?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1606800052052-a08af7148866?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1576869842043-928d2afe2480?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1540574163026-643ea20ade25?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000002?w=400&auto=format&fm=webp&q=75",
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
        image: "https://plus.unsplash.com/premium_photo-1670475326413-f69f74397650?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-f6g7h8i9j000f7890?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 1000, popular: false }
        ]
    },
    {
        id: "mi-nder-tadi-lat-d-meleme-batch2",
        name: "MİNDER TADİLAT/DÜĞMELEME",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-j6k7l8m9n000f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1551334787-21e2d38b3d9e?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1595516966504-797e68c1c89e?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-u1v2w3x4y500f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1503341504253-dff4815485f1?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 150, popular: false }
        ]
    },
    {
        id: "overlok-y-n-batch2",
        name: "OVERLOK YÜN",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        image: "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 200, popular: false }
        ]
    },
    {
        id: "pantolon-boyama-batch2",
        name: "PANTOLON BOYAMA",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        image: "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "boyama", price: 300, popular: false }
        ]
    },
    {
        id: "pantolon-grubu-batch2",
        name: "PANTOLON GRUBU",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        image: "https://images.unsplash.com/photo-1583623733237-4d9153fb1824?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "pelu-mont-batch2",
        name: "PELUŞ MONT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-1445205170230-053b83016050?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1554995207-c18c203602cb?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1726543210987?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 450, popular: true }
        ]
    },
    {
        id: "robte-ambir-batch2",
        name: "ROBTEŞAMBIR",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-1722109876543?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 300, popular: true }
        ]
    },
    {
        id: "sandalye-temi-zleme-yarim-batch2",
        name: "SANDALYE TEMİZLEME YARIM",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        image: "https://images.unsplash.com/photo-1550972958-d17c476b78f2?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "apka-boyama-batch2",
        name: "ŞAPKA BOYAMA",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-a1b2c3d4e500f7890?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "boyama", price: 200, popular: false }
        ]
    },
    {
        id: "stor-batch2",
        name: "STOR",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "https://images.unsplash.com/photo-1560184897-ae75f418493e?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yikama", price: 153, popular: true }
        ]
    },
    {
        id: "tadi-lat-batch2",
        name: "TADİLAT",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        image: "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true }
        ]
    },
    {
        id: "takim-elbi-se-batch2",
        name: "TAKIM ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        image: "https://images.unsplash.com/photo-1617137984095-74e4e5e3613f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1621759711492-c4803e1db95b?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true }
        ]
    },
    {
        id: "tuhafi-ye-i-p-d-me-vs-demesi-batch2",
        name: "TUHAFİYE İP/ DÜĞME VS. ÖDEMESİ",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        image: "https://images.unsplash.com/photo-1724321098765?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000707?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1664151100543-831e51069d1f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000009?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 350, popular: true }
        ]
    },
    {
        id: "vi-skon-yastik-batch2",
        name: "VİSKON YASTIK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "https://images.unsplash.com/photo-730000000708?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1727654321098?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 1000, popular: true }
        ]
    },
    {
        id: "yatak-ba-li-i-tek-batch2",
        name: "YATAK BAŞLIĞI TEK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "https://images.unsplash.com/photo-1505693314120-0d443867891c?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 750, popular: true }
        ]
    },
    {
        id: "yatak-pedi-batch2",
        name: "YATAK PEDİ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "https://images.unsplash.com/photo-1556911261-6bd341186b2f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1631049035463-0c1b2c00cd15?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 2500, popular: true }
        ]
    },
    {
        id: "yatak-yikama-tek-batch2",
        name: "YATAK YIKAMA TEK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "https://images.unsplash.com/photo-1540992419738-e3e6ee117e4b?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 2000, popular: true }
        ]
    },
    {
        id: "yeri-nde-hali-yikama-batch2",
        name: "YERİNDE HALI YIKAMA",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yerinde-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "yorgan-tek-ki-i-li-k-y-n-pamuk-batch2",
        name: "YORGAN TEK KİŞİLİK YÜN /PAMUK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "https://images.unsplash.com/photo-1549497538-303791108f95?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1545259741-2ea3ebf61fa0?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "zebra-t-l-batch2",
        name: "ZEBRA TÜL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yikama", price: 450, popular: true }
        ]
    },
    {
        id: "ceket-batch2",
        name: "CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-1557804506-669a67965ba0?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1542272454315-7ad86d1b8ed8?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000010?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1723210987654?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000008?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1520975954732-35dd22299614?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yikama", price: 425, popular: true }
        ]
    },
    {
        id: "pardes-batch3",
        name: "PARDESÜ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-1506629905607-bb5c12c3c04a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1585487000143-66b1526316f7?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1604445759020-96c93fa61557?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1564362286575-5e7c0dd6e7e4?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1612336307429-8a898d10e223?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000709?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1525457136159-8878648a7ad0?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1487222477894-8943e31ef7b2?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000717?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1589755814680-461c8b7fbc2b?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1589635020161-67a31d5b93e0?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1566479179817-be0b9f71c8c9?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1578852428516-6d13d4ea2969?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1529636798458-92182e662485?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1548883354-c4e3ab3ac5c4?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1565402748461-9d1acca80e5f?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 200, popular: true }
        ]
    },
    {
        id: "hali-nepal-batch3",
        name: "HALI NEPAL",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-730000000011?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 300, popular: true }
        ]
    },
    {
        id: "hali-shagy-batch3",
        name: "HALI SHAGY",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-1507652313519-d4e9174996dd?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 250, popular: true }
        ]
    },
    {
        id: "hali-step-batch3",
        name: "HALI STEP",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-730000000012?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 350, popular: true }
        ]
    },
    {
        id: "hali-maki-ne-y-n-batch3",
        name: "HALI MAKİNE YÜNÜ",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 250, popular: true }
        ]
    },
    {
        id: "battani-ye-batch3",
        name: "BATTANİYE",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1620799140188-3b2a02fd9a77?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1584464491033-06628f3a6b7b?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1566568897286-8cbc0c61fc5d?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1586440913080-97f5f5e7d5d7?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1587691592099-24045742c181?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1631889993959-41b4e9c6e3c5?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1629903652409-9b34c5bb4b20?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000713?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1564540574859-0dfb63985925?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000716?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000724?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1548777123-48b458ae8503?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1594736797933-d0d5ad6ad9c9?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1517991104123-1d56a6e81ed9?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1530587191325-3db32d826c18?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1563298723-dcfebaa392e3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1536431311719-398b6704d4cc?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1507038732509-8b4d20e31eec?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1583496661160-fb5886a13d24?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1562157873-818bc0726f68?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-f6g7h8i9j001f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1493666438817-866a91353ca9?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1728765432109?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000730?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000714?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1489171078254-c3365d6e359f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1580058572462-c61e6551e6c4?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000701?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1560563410-4dc4d41eb8d7?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000722?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true }
        ]
    },
    {
        id: "mi-nder-y-z-batch4",
        name: "MİNDER YÜZÜ",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        image: "https://plus.unsplash.com/premium_photo-1705843600829-15448713dcb1?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "koltuk-rt-s-batch4",
        name: "KOLTUK ÖRTÜSÜ",
        category: "ev-tekstili",
        subcategory: "mobilya-tekstili",
        image: "https://images.unsplash.com/photo-1738858363243-fa738c9bab55?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true }
        ]
    },
    {
        id: "banyo-ki-li-mi-batch4",
        name: "BANYO KİLİMİ",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-j6k7l8m9n001f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000007?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1622470953794-aa9c70b0fb9d?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1725432109876?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1571508508669-f9c18df0e138?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1540062768-0e1b88c9439e?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1525926929834-d6cc6c595d5d?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1578928375647-4db6db47c1f8?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000311?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000003?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1606108294687-efc93b0beb2b?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1563206767-5b18f218e8de?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000101?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1553735903-3d9b5e0a8ae4?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000726?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1516826957135-700dedea698c?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-a1b2c3d4e501f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000013?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1540479859555-17af45c78602?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1594736797933-d0ecedb717e0?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1562137369-1a1a0bc66744?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1599740490944-601ef84aba32?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1565084888279-aca607ecce0c?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-u1v2w3x4y501f7890?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true }
        ]
    },
    {
        id: "jartiyer-batch5",
        name: "JARTİYER",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        image: "https://images.unsplash.com/photo-1729876543210?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000102?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1560472355-536de3962603?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000001?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1589756823695-278bc8766896?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1562771379-eafdca7a02f8?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1539185441755-769473a23570?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1575428652377-a2d80e2277fc?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1560269999-cef6ebd23ad3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1668028554853-f83cac89ce0f?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yikama", price: 309, popular: true }
        ]
    },
    {
        id: "trenckot-batch6",
        name: "TRENCKOT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-f6g7h8i9j002f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1605833227154-3877aa1f1ab8?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000703?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1623609163859-ca93c959b98a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1620975686657-d718b88ce86a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000719?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1651047666890-8eab731ee345?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1571945153237-4929e783af4a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1567207877210-e8bb99098b9e?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1503919005314-30d93d07d823?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1564859228273-274232fdb516?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1505022610485-0249ba5b3675?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1620451334581-1ccebce2f2d2?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000700?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1544441893-675973e31985?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1675489757010-e97edf0b8f3e?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1578041089447-2ffc6fa20138?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000103?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000739?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1571019612922-0ba824358c0b?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1565564040510-6b9bf33b6c1a?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 250, popular: true }
        ]
    },
    {
        id: "hali-doku-ma-m2-batch6",
        name: "HALI DOKUMA M2",
        category: "ev-tekstili",
        subcategory: "hali-kilim",
        image: "https://images.unsplash.com/photo-1577563908411-5077b6dc7624?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "hali-yikama", price: 400, popular: true }
        ]
    },
    {
        id: "keten-g-mle-i-batch6",
        name: "KETEN GÖMLEĞİ",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-u1v2w3x4y502f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1578681994506-b8f463449011?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1566479179817-fb2cfe3b95c6?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1587554801582-8b67bbf87cfa?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000201?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000501?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1607453998774-d533f65dac99?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1580657018950-c7f7d6a6d990?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000734?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1548861216-17dd1ac80d5f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1714338733982-9b7fabf5db88?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000720?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1742794572842-6836a8d0b11b?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000704?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000741?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1612423284934-2850a4ea6b0f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000104?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1574180045827-681f8a1a9622?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1490114538077-0a7f8cb49891?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1519058082700-08a0b56da9b4?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1624378515195-6bbdb73dff1a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1544957992-20514f595d6f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1614252369475-531eba835eb1?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000301?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1580169980201-5c064f8f8045?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 3000, popular: true },
            { type: "yikama", price: 2142, popular: true }
        ]
    },
    {
        id: "likralı-tulum-batch7",
        name: "LİKRALI TULUM",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        image: "https://images.unsplash.com/photo-730000000744?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1580357954932-9ab60251977c?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1554898291-1541914077c5?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1636565024907-6f105fd5b52e?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1717777918255-ac7f0c913fb0?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1722109876543-a1b2c3d4e5f6?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1574180566232-aaad1b5b8450?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1615873968403-89e068629265?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1723210987654-b2c3d4e5f6a7?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1571019612845-b9c5a150f7c9?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "yikama", price: 1750, popular: true }
        ]
    },
    {
        id: "kaban-kapsonlu-batch8",
        name: "KABAN KAPŞONLU",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-730000000321?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000705?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000725?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1583743814966-8936f37f4678?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000322?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1607345366928-199ea26cfe3e?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000746?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000071?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000072?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000721?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000738?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000702?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000312?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1543076447-215ad9ba6923?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000006?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1582142306909-195724d2fed7?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1615412704336-86740e7273ee?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1581101767703-c9547ab3fc25?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "yikama", price: 1071, popular: true }
        ]
    },
    {
        id: "koltukalti-deri-pantolon-batch8",
        name: "KOLTUKALTI DERİ PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        image: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000732?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1678935908871-a72d8380baaa?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000743?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000021?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000718?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000022?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1649976390492-324d0c60beed?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1618477247222-acbdb0e159b3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1516205651411-aef33a44f7c2?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1600850056064-a8b380df8395?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000004?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1592853625511-ad0edcc69c07?w=400&auto=format&fm=webp&q=75",
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
        subcategory: "erkek-alt-giyim",
        image: "https://images.unsplash.com/photo-1607562076644-eaa0a80a3064?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-a1b2c3d4e502f7890?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 200, popular: true }
        ]
    },
    {
        id: "ust-balik-agzi-batch8",
        name: "ÜST BALIK AĞZI",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-f6g7h8i9j003f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000061?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1617171728-5bf6e67dec0a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1612722432474-b971cdcea546?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1628009658182-6df033109021?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1581833971358-2c8b550f87b3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000740?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1565814329452-e1efa11c5b89?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000105?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-a1b2c3d4e503f7890?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1617127365659-c47fa864d8bc?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1608234807415-564d1455dc07?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000106?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-8000000000005?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1594938598668-9bc89d789e3f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1609963733027-903686e51c01?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000041?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000031?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000032?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000706?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000737?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000710-c3d4e5f6a7b8?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1607554621516-6433573e7978?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1562040506-a9b32cb51b94?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true }
        ]
    },
    {
        id: "perde-batch9",
        name: "PERDE",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "https://images.unsplash.com/photo-1699805135173-3087dab73dc9?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000728?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000747?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1607532792764-d99e8d4f0de6?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 650, popular: true }
        ]
    },
    {
        id: "pi-jama-2-par-saten-batch9",
        name: "PİJAMA 2 PAR.SATEN",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-730000000729?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true }
        ]
    },
    {
        id: "pi-jama-alt-batch9",
        name: "PİJAMA ALT",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        image: "https://images.unsplash.com/photo-730000000202?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "pi-jama-tek-parc-batch9",
        name: "PİJAMA TEK PARÇ.",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-730000000742?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 250, popular: true }
        ]
    },
    {
        id: "pi-jama-ust-batch9",
        name: "PİJAMA ÜST",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&auto=format&fm=webp&q=75",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true }
        ]
    },
    {
        id: "suet-terli-k-batch9",
        name: "SÜET TERLİK",
        category: "ozel-temizleme",
        subcategory: "canta-ayakkabi",
        image: "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000735?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1560769629-975ec94e6a86?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000731?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000733?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1529958030586-3aae4ca485ff?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1553735558-a3c8c8105fc7?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000736?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1552902865-b72c031ac5ea?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000711?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000723?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1521336575822-6da63fb45455?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1599585297038-d93bb5a09f33?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1583691921979-37e96bb62b5b?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000062?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000203?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000521?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1582125169590-59f4985fb32a?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000063?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000033?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000042?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1581803118522-7b72a50f7e9f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1604135307399-86cbc62ac8ac?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1725432109876-d4e5f6a7b8c9?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1616806841781-e333e21b7341?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1544922280-ad14c68bd1fd?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000727?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000715?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000712?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000522?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000002?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000745?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000043?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1562157873-818bc0726f68?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000023?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1612832020347-b89c38293dd6?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000502?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000302?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-1562157873-818bc0726f68?w=400&auto=format&fm=webp&q=75",
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
        image: "https://images.unsplash.com/photo-730000000003?w=400&auto=format&fm=webp&q=75",
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