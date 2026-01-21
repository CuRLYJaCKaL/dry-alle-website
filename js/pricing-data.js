/* 
 * DryAlle Design System - Pricing Data Module
 * Fiyat Listesi - Ocak 2026
 */

// Fiyat Verileri
const multiServicePricingData = [
    {
        id: "takim-elbise",
        name: "TAKIM ELBİSE",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        image: "asset/products/takim-elbise.jpg",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 375, popular: false }
        ]
    },
    {
        id: "smokin",
        name: "SMOKİN",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        image: "asset/products/smokin.jpg",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 500, popular: false }
        ]
    },
    {
        id: "ceket",
        name: "CEKET",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/ceket.jpg",
        services: [
            { type: "kuru-temizleme", price: 450, popular: true },
            { type: "utuleme", price: 225, popular: false }
        ]
    },
    {
        id: "yelek",
        name: "YELEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/yelek.jpg",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 175, popular: false }
        ]
    },
    {
        id: "sisme-yelek",
        name: "ŞİŞME YELEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/sisme-yelek.jpg",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false }
        ]
    },
    {
        id: "gomlek",
        name: "GÖMLEK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/gomlek.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "kazak",
        name: "KAZAK",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/kazak.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "pantolon",
        name: "PANTOLON",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        image: "asset/products/pantolon.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "etek",
        name: "ETEK",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        image: "asset/products/etek.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "bluz",
        name: "BLUZ",
        category: "kadin-giyim",
        subcategory: "kadin-ust-giyim",
        image: "asset/products/bluz.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "hirka",
        name: "HIRKA",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/hirka.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "suveter",
        name: "SÜVETER",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/suveter.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "tisort",
        name: "TİŞÖRT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/tisort.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "bayan-elbise",
        name: "BAYAN ELBİSE",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        image: "asset/products/bayan-elbise.jpg",
        services: [
            { type: "kuru-temizleme", price: 500, popular: true },
            { type: "utuleme", price: 250, popular: false }
        ]
    },
    {
        id: "abiye",
        name: "ABİYE",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        image: "asset/products/abiye.jpg",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 500, popular: false }
        ]
    },
    {
        id: "gelinlik",
        name: "GELİNLİK",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        image: "asset/products/gelinlik.jpg",
        services: [
            { type: "kuru-temizleme", price: 2500, popular: true },
            { type: "utuleme", price: 1250, popular: false }
        ]
    },
    {
        id: "nisankina-kiyafeti",
        name: "NİŞAN-KINA KIYAFETİ",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        image: "asset/products/nisankina-kiyafeti.jpg",
        services: [
            { type: "kuru-temizleme", price: 2500, popular: true },
            { type: "utuleme", price: 1250, popular: false }
        ]
    },
    {
        id: "gece-elbisesi",
        name: "GECE ELBİSESİ",
        category: "kadin-giyim",
        subcategory: "kadin-ozel-giyim",
        image: "asset/products/gece-elbisesi.jpg",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "utuleme", price: 400, popular: false }
        ]
    },
    {
        id: "kus-tuyu-mont-kaban",
        name: "KUŞ TÜYÜ MONT- KABAN",
        category: "dis-giyim",
        subcategory: "mont-kaban",
        image: "asset/products/kus-tuyu-mont-kaban.jpg",
        services: [
            { type: "kuru-temizleme", price: 900, popular: true },
            { type: "utuleme", price: 450, popular: false }
        ]
    },
    {
        id: "mont",
        name: "MONT",
        category: "dis-giyim",
        subcategory: "mont-kaban",
        image: "asset/products/mont.jpg",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 375, popular: false }
        ]
    },
    {
        id: "kaban",
        name: "KABAN",
        category: "dis-giyim",
        subcategory: "mont-kaban",
        image: "asset/products/kaban.jpg",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 375, popular: false }
        ]
    },
    {
        id: "pardesu",
        name: "PARDESÜ",
        category: "dis-giyim",
        subcategory: "mont-kaban",
        image: "asset/products/pardesu.jpg",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 375, popular: false }
        ]
    },
    {
        id: "trenckot",
        name: "TRENÇKOT",
        category: "dis-giyim",
        subcategory: "mont-kaban",
        image: "asset/products/trenckot.jpg",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 375, popular: false }
        ]
    },
    {
        id: "esofman-takim",
        name: "EŞOFMAN TAKIM",
        category: "erkek-giyim",
        subcategory: "erkek-takim-elbise",
        image: "asset/products/esofman-takim.jpg",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false }
        ]
    },
    {
        id: "esofman-alt",
        name: "EŞOFMAN ALT",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        image: "asset/products/esofman-alt.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "esofman-ust",
        name: "EŞOFMAN ÜST",
        category: "erkek-giyim",
        subcategory: "erkek-alt-giyim",
        image: "asset/products/esofman-ust.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "sweat",
        name: "SWEAT",
        category: "erkek-giyim",
        subcategory: "erkek-ust-giyim",
        image: "asset/products/sweat.jpg",
        services: [
            { type: "kuru-temizleme", price: 350, popular: true },
            { type: "utuleme", price: 175, popular: false }
        ]
    },
    {
        id: "atki",
        name: "ATKI",
        category: "aksesuar",
        subcategory: "aksesuar-genel",
        image: "asset/products/atki.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "sapka",
        name: "ŞAPKA",
        category: "aksesuar",
        subcategory: "aksesuar-genel",
        image: "asset/products/sapka.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "eldiven",
        name: "ELDİVEN",
        category: "aksesuar",
        subcategory: "aksesuar-genel",
        image: "asset/products/eldiven.jpg",
        services: [
            { type: "kuru-temizleme", price: 300, popular: true },
            { type: "utuleme", price: 150, popular: false }
        ]
    },
    {
        id: "yorgan-elyaf",
        name: "YORGAN ELYAF",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "asset/products/yorgan-elyaf.jpg",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 375, popular: false }
        ]
    },
    {
        id: "yorgan-yun",
        name: "YORGAN YÜN",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "asset/products/yorgan-yun.jpg",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 500, popular: false }
        ]
    },
    {
        id: "yorgan-pamuk",
        name: "YORGAN PAMUK",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "asset/products/yorgan-pamuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 500, popular: false }
        ]
    },
    {
        id: "yorgan-kus-tuyu",
        name: "YORGAN KUŞ TÜYÜ",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "asset/products/yorgan-kus-tuyu.jpg",
        services: [
            { type: "kuru-temizleme", price: 1250, popular: true },
            { type: "utuleme", price: 625, popular: false }
        ]
    },
    {
        id: "battaniye-normal",
        name: "BATTANİYE NORMAL",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "asset/products/battaniye-normal.jpg",
        services: [
            { type: "kuru-temizleme", price: 750, popular: true },
            { type: "utuleme", price: 375, popular: false }
        ]
    },
    {
        id: "battaniye-battal",
        name: "BATTANİYE BATTAL",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "asset/products/battaniye-battal.jpg",
        services: [
            { type: "kuru-temizleme", price: 900, popular: true },
            { type: "utuleme", price: 450, popular: false }
        ]
    },
    {
        id: "battaniye-yun",
        name: "BATTANİYE YÜN",
        category: "ev-tekstili",
        subcategory: "yatak-takimi",
        image: "asset/products/battaniye-yun.jpg",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 500, popular: false }
        ]
    },
    {
        id: "tul-perde-kucuk",
        name: "TÜL PERDE KÜÇÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/tul-perde-kucuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false }
        ]
    },
    {
        id: "tul-perde-orta",
        name: "TÜL PERDE ORTA",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/tul-perde-orta.jpg",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "utuleme", price: 400, popular: false }
        ]
    },
    {
        id: "tul-perde-buyuk",
        name: "TÜL PERDE BÜYÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/tul-perde-buyuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 500, popular: false }
        ]
    },
    {
        id: "tul-perde-battal",
        name: "TÜL PERDE BATTAL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/tul-perde-battal.jpg",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 750, popular: false }
        ]
    },
    {
        id: "guneslik-kucuk",
        name: "GÜNEŞLİK KÜÇÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/guneslik-kucuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 600, popular: true },
            { type: "utuleme", price: 300, popular: false }
        ]
    },
    {
        id: "guneslik-orta",
        name: "GÜNEŞLİK ORTA",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/guneslik-orta.jpg",
        services: [
            { type: "kuru-temizleme", price: 800, popular: true },
            { type: "utuleme", price: 400, popular: false }
        ]
    },
    {
        id: "guneslik-buyuk",
        name: "GÜNEŞLİK BÜYÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/guneslik-buyuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 500, popular: false }
        ]
    },
    {
        id: "guneslik-battal",
        name: "GÜNEŞLİK BATTAL",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/guneslik-battal.jpg",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 750, popular: false }
        ]
    },
    {
        id: "fon-perde-tk-kucuk",
        name: "FON PERDE TK KÜÇÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/fon-perde-tk-kucuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 1000, popular: true },
            { type: "utuleme", price: 500, popular: false }
        ]
    },
    {
        id: "fon-perde-ck-kucuk",
        name: "FON PERDE ÇK KÜÇÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/fon-perde-ck-kucuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 750, popular: false }
        ]
    },
    {
        id: "fon-perde-tk-buyuk",
        name: "FON PERDE TK BÜYÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/fon-perde-tk-buyuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 1500, popular: true },
            { type: "utuleme", price: 750, popular: false }
        ]
    },
    {
        id: "fon-perde-ck-buyuk",
        name: "FON PERDE ÇK BÜYÜK",
        category: "ev-tekstili",
        subcategory: "perde-tul",
        image: "asset/products/fon-perde-ck-buyuk.jpg",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true },
            { type: "utuleme", price: 1000, popular: false }
        ]
    },
    {
        id: "deri-mont",
        name: "DERİ MONT",
        category: "ozel-temizleme",
        subcategory: "deri-kurk",
        image: "asset/products/deri-mont.jpg",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true },
            { type: "utuleme", price: 1000, popular: false }
        ]
    },
    {
        id: "deri-ceket",
        name: "DERİ CEKET",
        category: "ozel-temizleme",
        subcategory: "deri-kurk",
        image: "asset/products/deri-ceket.jpg",
        services: [
            { type: "kuru-temizleme", price: 2000, popular: true },
            { type: "utuleme", price: 1000, popular: false }
        ]
    },
    {
        id: "kurk-kisa",
        name: "KÜRK KISA",
        category: "ozel-temizleme",
        subcategory: "deri-kurk",
        image: "asset/products/kurk-kisa.jpg",
        services: [
            { type: "kuru-temizleme", price: 2500, popular: true },
            { type: "utuleme", price: 1250, popular: false }
        ]
    },
    {
        id: "kurk-uzun",
        name: "KÜRK UZUN",
        category: "ozel-temizleme",
        subcategory: "deri-kurk",
        image: "asset/products/kurk-uzun.jpg",
        services: [
            { type: "kuru-temizleme", price: 3000, popular: true },
            { type: "utuleme", price: 1500, popular: false }
        ]
    }
];

// Kategori görüntüleme isimleri
const categoryDisplayNames = {
    "erkek-giyim": "Erkek Giyim",
    "kadin-giyim": "Kadın Giyim",
    "dis-giyim": "Dış Giyim",
    "ev-tekstili": "Ev Tekstili",
    "ozel-temizleme": "Özel Temizleme",
    "aksesuar": "Aksesuar"
};

// Alt kategori görüntüleme isimleri
const subcategoryDisplayNames = {
    "erkek-takim-elbise": "Takım Elbise",
    "erkek-ust-giyim": "Üst Giyim",
    "erkek-alt-giyim": "Alt Giyim",
    "kadin-ust-giyim": "Üst Giyim",
    "kadin-ozel-giyim": "Özel Giyim",
    "mont-kaban": "Mont & Kaban",
    "yatak-takimi": "Yatak & Yorgan",
    "perde-tul": "Perde & Tül",
    "deri-kurk": "Deri & Kürk",
    "aksesuar-genel": "Aksesuar"
};

// Hizmet türü görüntüleme isimleri
const processDisplayNames = {
    "kuru-temizleme": "Kuru Temizleme",
    "utuleme": "Ütüleme"
};

// Kategori sayıları (dinamik hesaplanacak)
let categoryCounts = {};
let subcategoryCounts = {};

// PricingData modülü - Tüm verileri global olarak sunar
window.PricingData = {
    multiServicePricingData,
    categoryDisplayNames,
    subcategoryDisplayNames,
    processDisplayNames,
    categoryCounts,
    subcategoryCounts
};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        multiServicePricingData,
        categoryDisplayNames,
        subcategoryDisplayNames,
        processDisplayNames
    };
}
