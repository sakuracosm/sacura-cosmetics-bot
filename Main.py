import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

TOKEN = "8815956212:AAFphga9M6MZcp9PH86tOQeuWuJIso4FzGo"
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 685052577

carts = {}
orders = {}
order_counter = 1000

PHOTO_DIR = "/storage/emulated/0/Spflar/"
CREAM_DIR = "/storage/emulated/0/Kremlar/"
LOTION_DIR = "/storage/emulated/0/Tonerlar/"
catalog = {'spf': {'title': '☀️ SPF',
         'items': {'spf1': {'name': 'Hada Labo Koi-Gokujyun All In One UV Gel',
                            'price': 238000,
                            'photo': '/storage/emulated/0/Spflar/hada_labo_uv_gel.png',
                            'description': '💙 Hada Labo Koi-Gokujyun All In One UV Gel SPF50+ PA++++ (90g)\n'
                                           '\n'
                                           '☀️ Quyoshdan himoya, namlantirish va teri parvarishini birlashtirgan '
                                           'premium yapon UV geli.\n'
                                           '\n'
                                           '✨ SPF50+ PA++++ — UVA va UVB nurlaridan kuchli himoya\n'
                                           '💧 3 xil gialuron kislotasi terini chuqur namlaydi\n'
                                           '🍋 Vitamin C hosilasi teri rangini yorqinlashtirishga yordam beradi\n'
                                           '🌿 Yengil gel tekstura tez singadi\n'
                                           "🫧 Yog'li his va yopishqoqlik qoldirmaydi\n"
                                           '💄 Makiyaj ostiga baza sifatida ham mos\n'
                                           "🌞 Yuz va bo'yin uchun qo'llash mumkin\n"
                                           '\n'
                                           '📦 Hajmi: 90 g\n'
                                           '🇯🇵 Original Yaponiya mahsuloti'},
                   'spf2': {'name': 'Skin Aqua Super Moisture UV Gel Pump',
                            'price': 178000,
                            'photo': '/storage/emulated/0/Spflar/skin_aqua_pump.png',
                            'description': '💙 Skin Aqua Super Moisture UV Gel Pump SPF50+ PA++++ (140g)\n'
                                           '\n'
                                           '☀️ Katta hajmli, namlovchi va butun oila uchun mos SPF geli.\n'
                                           '\n'
                                           '✨ SPF50+ PA++++ yuqori darajadagi himoya\n'
                                           '💧 3 turdagi gialuron kislotasi bilan boyitilgan\n'
                                           '🌊 Super Waterproof formula\n'
                                           '🫧 Sovun bilan oson yuviladi\n'
                                           '👩 Yuz va tana uchun mos\n'
                                           '💄 Makiyaj ostida qulay ishlatiladi\n'
                                           '\n'
                                           '📦 Hajmi: 140 g\n'
                                           '🇯🇵 Original Yaponiya mahsuloti'},
                   'spf3': {'name': 'AYURA Water Feel UV Gel',
                            'price': 349000,
                            'photo': '/storage/emulated/0/Spflar/ayura_water_feel_uv_gel.png',
                            'description': '💙 AYURA Water Feel UV Gel SPF50+ PA++++ (75g)\n'
                                           '\n'
                                           '✨ Premium darajadagi yengil UV-gel va teri parvarishi.\n'
                                           '\n'
                                           '☀️ SPF50+ PA++++ kuchli quyoshdan himoya\n'
                                           '💧 Suvdek yengil water-gel tekstura\n'
                                           '🌿 Terini namlaydi va tinchlantiradi\n'
                                           '🫧 Tez shimiladi, yopishqoqlik qoldirmaydi\n'
                                           '🚫 Oqartirib yubormaydi\n'
                                           '💄 Makiyaj ostida mukammal ishlaydi\n'
                                           '👩 Barcha teri turlari uchun mos\n'
                                           '\n'
                                           '📦 Hajmi: 75 g\n'
                                           '🇯🇵 Original Yaponiya mahsuloti'},
                   'spf4': {'name': 'Skin Aqua Tone Up UV Essence Cool Mint',
                            'price': 167000,
                            'photo': '/storage/emulated/0/Spflar/skin_aqua_cool_mint.png',
                            'description': '💙 Skin Aqua Tone Up UV Essence Cool Mint SPF50+ PA++++ (80g)\n'
                                           '\n'
                                           '❄️ Sovutuvchi effekt va tabiiy yorqinlik beruvchi tone-up SPF.\n'
                                           '\n'
                                           '☀️ SPF50+ PA++++ yuqori himoya\n'
                                           '❄️ Cool Mint sovutuvchi effekti\n'
                                           "✨ Teri rangini yanada tiniq ko'rsatadi\n"
                                           '💧 Namlikni saqlashga yordam beradi\n'
                                           '🫧 Tez singadi va yopishqoq emas\n'
                                           '💄 Makiyaj ostiga mos\n'
                                           '👩 Barcha teri turlari uchun mos\n'
                                           '\n'
                                           '📦 Hajmi: 80 g\n'
                                           '🇯🇵 Original Yaponiya mahsuloti'},
                   'spf5': {'name': 'Skin Aqua Tone Up UV Essence Lavender',
                            'price': 167000,
                            'photo': '/storage/emulated/0/Spflar/skin_aqua_lavender.jpg',
                            'description': '💜 Skin Aqua Tone Up UV Essence Lavender SPF50+ PA++++ (80g)\n'
                                           '\n'
                                           "✨ Oqartirmasdan teri rangini tekis va yorqin ko'rsatadigan mashhur tone-up "
                                           'SPF.\n'
                                           '\n'
                                           '☀️ SPF50+ PA++++ kuchli himoya\n'
                                           '💜 Lavanda pigmentlari teri rangini balanslaydi\n'
                                           "✨ Xiralik va sarg'ish tusni kamaytiradi\n"
                                           '💧 Terini namlangan holda saqlaydi\n'
                                           '💄 Makiyaj ostiga ideal baza\n'
                                           '👩 Barcha teri turlari uchun mos\n'
                                           '\n'
                                           '📦 Hajmi: 80 g\n'
                                           '🇯🇵 Original Yaponiya mahsuloti'},
                   'spf6': {'name': 'Skin Aqua Tone Up UV Essence Rose',
                            'price': 178000,
                            'photo': '/storage/emulated/0/Spflar/skin_aqua_rose.png',
                            'description': '🩷 Skin Aqua Tone Up UV Essence Rose SPF50+ PA++++ (80g)\n'
                                           '\n'
                                           "🌸 Teringa sog'lom, jonli va yorqin ko'rinish beruvchi tone-up SPF.\n"
                                           '\n'
                                           '☀️ SPF50+ PA++++ yuqori himoya\n'
                                           '🌸 Rose tone-up effekti\n'
                                           "✨ Teri rangini yanada yorqin ko'rsatadi\n"
                                           '💧 Namlovchi tarkib bilan boyitilgan\n'
                                           "🚫 Yog'li his qoldirmaydi\n"
                                           '💄 Makiyaj ostiga juda mos\n'
                                           '👩 Kundalik foydalanish uchun ideal\n'
                                           '\n'
                                           '📦 Hajmi: 80 g\n'
                                           '🇯🇵 Original Yaponiya mahsuloti'},
                   'spf7': {'name': 'Cover UV Milk Sana',
                            'price': 181000,
                            'photo': '/storage/emulated/0/Spflar/cover_uv_milk_sana.png',
                            'description': '🤍 SANA Wrinkle UV Milk SPF43 PA+++ (50g)\n'
                                           '\n'
                                           '✨ Quyoshdan himoya va anti-age parvarishni birlashtirgan premium UV milk.\n'
                                           '\n'
                                           '☀️ SPF43 PA+++ ishonchli himoya\n'
                                           '💖 Retinol komponenti bilan boyitilgan\n'
                                           '🌱 Fermentlangan soya ekstrakti\n'
                                           '💧 Gialuron kislotasi namlik beradi\n'
                                           '✨ Mayda ajin va teshikchalarni tabiiy yopadi\n'
                                           '💄 Makiyaj ustidan ham foydalanish mumkin\n'
                                           '👩 Barcha teri turlari uchun mos\n'
                                           '\n'
                                           '📦 Hajmi: 50 g\n'
                                           '🇯🇵 Original Yaponiya mahsuloti'},
                   'spf8': {'name': 'MIEUFA SPF Spray',
                            'price': 181000,
                            'photo': '/storage/emulated/0/Spflar/mieufa_spf_spray.png',
                            'description': '🌿 MIEUFA Fresh Monday Morning SPF50+ PA++++ (80g)\n'
                                           '\n'
                                           "☀️ Soch va teri uchun mo'ljallangan premium UV himoya spreyi.\n"
                                           '\n'
                                           '✨ SPF50+ PA++++ yuqori himoya\n'
                                           '💇 Sochlarni quyoshdan himoya qiladi\n'
                                           '👩 Yuz va tana uchun ham mos\n'
                                           '💧 Namlik beradi va quritmaydi\n'
                                           '🎒 Sumkada olib yurish uchun qulay\n'
                                           '🌸 Fresh Monday Morning yoqimli aromati\n'
                                           '\n'
                                           '📦 Hajmi: 80 g\n'
                                           '🇯🇵 Original Yaponiya mahsuloti'}}},
"cream": {
"title": "🧴 Kremlar",
"items": {

    "cr1": {
        "name": "AQUALABEL Special Gel Cream Brightening",
        "price": 264000,
        "photo": CREAM_DIR + "aqualabel_brightening.png",
        "description": """💙 AQUALABEL Special Gel Cream Brightening (90g)

✨ Oqartirish, namlantirish va qarishga qarshi parvarishni birlashtirgan premium yapon all-in-one gel krem.

🌿 Loson, emulsiya, serum, krem va maska vazifasini bitta mahsulotda bajaradi
💧 Terini uzoq vaqt nam holatda saqlaydi
✨ Teri rangini yanada tiniq va yorqin ko'rsatishga yordam beradi
🌸 Xiralik va charchagan teri ko'rinishini kamaytiradi
🫧 Yengil gel tekstura tez singadi
🚫 Yog'li his qoldirmaydi
💄 Makiyaj ostiga juda mos
🌞 Ertalab va kechqurun foydalanish mumkin
🛡️ Teri himoya qatlamini qo'llab-quvvatlaydi
👩 Normal, quruq va aralash teri uchun mos
✨ Kundalik parvarish uchun ideal

📦 Hajmi: 90 g

🇯🇵 Original Yaponiya mahsuloti"""
    },

    "cr2": {
        "name": "Moisture Mild White",
        "price": 263000,
        "photo": CREAM_DIR + "moisture_mild_white.png",
       "description": """🤍 Moisture Mild White

✨ Oqartirish va namlantirishni birlashtirgan yapon parvarish kremi.

💧 Terini chuqur namlaydi
✨ Teri rangining bir tekis bo'lishiga yordam beradi
🌿 Xiralik va quruqlikni kamaytiradi
🫧 Yengil va yoqimli tekstura
⚡ Tez singadi
🚫 Yog'li his qoldirmaydi
💄 Makiyaj ostiga mos
🌙 Kechki va kunduzgi parvarish uchun mos
👩 Nozik teri uchun ham tavsiya etiladi
✨ Teriga sog'lom va yorqin ko'rinish beradi
💧 Namlikni uzoq vaqt saqlashga yordam beradi

📦 Hajmi: 100 g

🇯🇵 Original Yaponiya mahsuloti"""
    },

    "cr3": {
        "name": "Melano CC Gel Cream",
        "price": 263000,
        "photo": CREAM_DIR + "melano_cc_gel.png",
       "description": """🍋 Melano CC Gel Cream (100g)

✨ Yaponiyaning mashhur Vitamin C gel-kremi. Pigmentatsiya, akne izlari va teri rangining notekisligiga qarshi parvarish uchun mo'ljallangan.

🍋 Vitamin C hosilasi bilan boyitilgan
✨ Akne izlari va qora dog'lar ko'rinishini kamaytirishga yordam beradi
🌞 Quyoshdan keyingi pigmentatsiyaga qarshi parvarish
💧 Terini namlaydi va yumshatadi
🌿 Yengil gel-krem tekstura
🫧 Tez singadi va yopishqoq emas
🚫 Yog'li qatlam qoldirmaydi
💄 Makiyaj ostiga mos
✨ Teri rangini yanada yorqin va sog'lom ko'rsatadi
👩 Yog'li, aralash va normal teri uchun mos
🌙 Ertalab va kechqurun foydalanish mumkin

📦 Hajmi: 100 g

🇯🇵 Original Yaponiya mahsuloti"""
    },

    "cr4": {
        "name": "Heparin Cream",
        "price": 265000,
        "photo": CREAM_DIR + "heparin_cream.png",
       "description": """💗 Heparin Cream (90g)

💧 Juda quruq, namliksiz va tortishadigan teri uchun maxsus yapon namlantiruvchi krem.

✨ Heparinoid tarkibi bilan boyitilgan
💧 Terini chuqur namlaydi va namlikni uzoq saqlaydi
🛡️ Teri himoya qatlamini mustahkamlashga yordam beradi
🌿 Quruqlik va po'st tashlashni kamaytiradi
✨ Terini yumshoq va silliq qiladi
☁️ Qalin bo'lishiga qaramay tez singadi
🚫 Yopishqoq his qoldirmaydi
👩 Nozik va sezgir teri uchun ham mos
🌙 Kechki parvarish uchun ideal
☀️ Kundalik foydalanish mumkin
🧴 Yuz, bo'yin va quruq tana qismlariga qo'llash mumkin

📦 Hajmi: 90 g

🇯🇵 Original Yaponiya mahsuloti"""
    },

    "cr5": {
        "name": "Utena Simple Balance All In One Gel",
        "price": 145000,
        "photo": CREAM_DIR + "utena_simple_balance.png",
        "description": """💙 Utena Simple Balance All In One Gel

✨ Loson, serum va kremni birlashtirgan qulay all-in-one gel.

💧 Terini chuqur namlaydi
🌿 Yumshoq va silliq ko'rinish beradi
⚡ Tez singadi va og'irlik hissini qoldirmaydi
🚫 Yog'li qatlam hosil qilmaydi
✨ Kundalik parvarishni soddalashtiradi
🫧 Yengil gel tekstura
💄 Makiyaj ostiga mos
🌙 Ertalab va kechqurun foydalanish mumkin
👩 Normal, quruq va aralash teri uchun mos
💰 Sifat va narx jihatidan juda yaxshi tanlov

📦 Hajmi: 100 g

🇯🇵 Original Yaponiya mahsuloti"""
    },

    "cr6": {
        "name": "NILE All In One Gel Cream",
        "price": 265000,
        "photo": CREAM_DIR + "nile_all_in_one_gel.png",
        "description": """🖤 NILE All In One Gel Cream

✨ Erkaklar uchun ishlab chiqilgan premium yapon all-in-one gel krem.

💧 Loson, serum va krem vazifasini bitta mahsulotda bajaradi
🌿 Soqol olishdan keyingi parvarish uchun mos
✨ Terini namlaydi va yumshatadi
🛡️ Tashqi muhit ta'siridan himoya qilishga yordam beradi
⚡ Tez singadi va vaqt tejaydi
🚫 Yog'li qatlam qoldirmaydi
🚫 Yopishqoq emas
💧 Namlikni uzoq vaqt saqlaydi
👨 Erkaklar terisi uchun maxsus formula
🌙 Ertalab va kechqurun foydalanish mumkin
🎯 Minimal parvarish bilan maksimal natija

📦 Hajmi: 100 g

🇯🇵 Original Yaponiya mahsuloti"""
    },

    "cr7": {
        "name": "Ninocure",
        "price": 175000,
        "photo": CREAM_DIR + "ninocure.png",
        "description": """💗 Ninocure

✨ Qo'l, tirsak, tizza va boshqa dag'allashgan teri qismlarini parvarish qilish uchun mo'ljallangan mashhur yapon kremi.

💧 Terini chuqur namlaydi
🌿 Dag'allashgan va quruq terini yumshatishga yordam beradi
✨ Teri yuzasini silliqroq ko'rinishga keltiradi
🛡️ Teri himoya qatlamini qo'llab-quvvatlaydi
💗 Quruqlik sababli paydo bo'ladigan noqulaylikni kamaytiradi
🫧 Tez singadi
🚫 Yopishqoq his qoldirmaydi
👩 Kundalik foydalanish uchun mos
🧴 Tirsak, tizza, qo'l va boshqa quruq joylarga qo'llash mumkin
✨ Terini yumshoq va parvarishlangan holatda saqlashga yordam beradi

📦 Hajmi: 30 g

🇯🇵 Original Yaponiya mahsuloti"""
    }
}

},
 'lotion': {'title': '💧 Lotion / Toner','items': {
                              "lo1": {
    "name": "Curel Lotion III 150ml",
    "price": 277000,
    "photo": LOTION_DIR + "curel_lotion_iii.png",
    "description": """💧 Curel Lotion III (150ml)

✨ Juda quruq va sezgir teri uchun yaratilgan premium yapon namlantiruvchi lotion.

💧 Ceramide funksiyasini qo'llab-quvvatlaydi
🌿 Terining himoya qatlamini mustahkamlashga yordam beradi
🛡️ Quruqlik va tashqi ta'sirlardan himoya qiladi
✨ Terini yumshoq va silliq qiladi
💧 Chuqur namlantiradi
🚫 Xushbo'y moddalar qo'shilmagan
🚫 Rang beruvchilar qo'shilmagan
👩 Sezgir teri uchun mos
🌙 Ertalab va kechqurun foydalanish mumkin
💄 Keyingi parvarish bosqichlari uchun terini tayyorlaydi

📦 Hajmi: 150 ml

🇯🇵 Original Yaponiya mahsuloti"""
},
                              "lo2": {
    "name": "Keana Rice Toner",
    "price": 289000,
    "photo": LOTION_DIR + "keana_rice_toner.png",
    "description": """🌾 Keana Rice Toner

✨ Guruch ekstrakti asosidagi mashhur yapon toner.

🌾 Guruch fermentlari bilan boyitilgan
💧 Terini chuqur namlaydi
✨ Kengaygan teshikchalar ko'rinishini kamaytirishga yordam beradi
🌿 Terini yumshatadi
🫧 Yengil va yoqimli tekstura
🚫 Yog'li his qoldirmaydi
✨ Teri rangini sog'lom ko'rsatadi
👩 Quruq va aralash teri uchun mos
💄 Makiyajdan oldin ishlatish mumkin
🌙 Kundalik foydalanish uchun ideal

📦 Hajmi: 300 ml

🇯🇵 Original Yaponiya mahsuloti"""
}
    }
},
                      "lo3": {
    "name": "Hada Labo Gokujyun Premium Hyaluronic Milky Lotion",
    "price": 181000,
    "photo": LOTION_DIR + "hada_labo_premium_milky_lotion.png",
    "description": """💛 Hada Labo Gokujyun Premium Hyaluronic Milky Lotion (140ml)

✨ Hada Labo'ning eng mashhur premium namlantiruvchi losonlaridan biri.

💧 Bir nechta turdagi Hyaluronic Acid bilan boyitilgan
🌿 Terini chuqur namlaydi
✨ Namlikni uzoq vaqt ushlab turishga yordam beradi
🛡️ Teri himoya qatlamini qo'llab-quvvatlaydi
☁️ Yengil milky tekstura
🚫 Xushbo'y moddalar qo'shilmagan
🚫 Rang beruvchilar qo'shilmagan
👩 Quruq va namliksiz teri uchun ideal
🌙 Ertalab va kechqurun foydalanish mumkin
💄 Keyingi krem yoki serum uchun mukammal baza

📦 Hajmi: 140 ml

🇯🇵 Original Yaponiya mahsuloti"""
},
 'serum': {'title': '💧 Serumlar',
           'items': {'ser1': {'name': 'Hada Bisei Brightening Facial Serum 30ml',
                              'price': 181000,
                              'description': '💧 Hada Bisei Brightening Facial Serum\n'
                                             '\n'
                                             'Teri rangini yorqinlashtirish va dog‘larni kamaytirishga yordam beruvchi '
                                             'serum.'}}},
 'eye': {'title': "👁 Ko'z / Kiprik parvarishi",
         'items': {'eye1': {'name': 'Nameraka Honpo Wrinkle Eye Cream N',
                            'price': 181000,
                            'description': '👁 Nameraka Honpo Wrinkle Eye Cream N\n'
                                           '\n'
                                           'Ko‘z atrofi ajinlari va quruqligi uchun bestseller krem.'},
                   'eye2': {'name': 'Hada Labo Eye Cream',
                            'price': 181000,
                            'description': '👁 Hada Labo Eye Cream\n\nKo‘z atrofi terisini namlantirish uchun.'},
                   'eye3': {'name': 'Quality 1st Eye Sheet Derma Laser',
                            'price': 169000,
                            'description': '👁 Quality 1st Eye Sheet Derma Laser\n\nKo‘z atrofi uchun sheet parvarish.'},
                   'eye4': {'name': 'Bio Lucia Eyelash Serum 6ml',
                            'price': 301000,
                            'description': '👁 Bio Lucia Eyelash Serum\n\nKiprik parvarishi uchun serum.'}}},
 'acne': {'title': '🔥 Akne parvarishi',
          '
