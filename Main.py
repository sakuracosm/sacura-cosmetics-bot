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
          'items': {'ac1': {'name': 'Pair Acne Cream 24g',
                            'price': 181000,
                            'description': '🔥 Pair Acne Cream\n'
                                           '\n'
                                           'Akne, yallig‘lanish va qizarishga qarshi yapon kremi.'}}},
 'wash': {'title': '🫧 Yuz yuvish',
          'items': {'wa1': {'name': 'Melano CC Deep Clear',
                            'price': 204000,
                            'description': '🫧 Melano CC Deep Clear\n\nVitamin C bilan yuz yuvish vositasi.'},
                    'wa2': {'name': 'Melano CC Deep Clear 200g',
                            'price': 193000,
                            'description': '🫧 Melano CC Deep Clear 200g\n\nKatta hajmli yuz yuvish vositasi.'},
                    'wa3': {'name': 'Detclear Bright & Peel Fruits Enzyme Powder Wash',
                            'price': 192000,
                            'description': '🫧 Detclear Enzyme Powder Wash\n\nEnzyme powder yuz yuvish vositasi.'},
                    'wa4': {'name': 'Clearasil Medicated Facial Wash Strong Type',
                            'price': 132000,
                            'description': '🫧 Clearasil Medicated Facial Wash\n'
                                           '\n'
                                           'Aknega moyil teri uchun yuz yuvish vositasi.'},
                    'wa5': {'name': 'Perfect Whip Senka Perfect',
                            'price': 163000,
                            'description': '🫧 Perfect Whip\n\nMashhur yapon yuz yuvish penkasi.'},
                    'wa6': {'name': 'AHA Wash Cleansing',
                            'price': 145000,
                            'description': '🫧 AHA Wash Cleansing\n\nAHA kislotali yuz yuvish vositasi.'},
                    'wa7': {'name': 'Cleansing Research AHA Oil Cleansing',
                            'price': 181000,
                            'description': '🫧 Cleansing Research AHA Oil Cleansing\n'
                                           '\n'
                                           'Makiyaj va SPF tozalash uchun cleansing oil.'},
                    'wa8': {'name': 'Attenir Skin Clear Cleanse Oil 175ml',
                            'price': 277000,
                            'description': '🫧 Attenir Skin Clear Cleanse Oil\n\nPremium cleansing oil.'},
                    'wa9': {'name': 'Kose Sekkisei Brightening Cleansing Oil',
                            'price': 301000,
                            'description': '🫧 Kose Sekkisei Brightening Cleansing Oil\n'
                                           '\n'
                                           'Yorqinlik uchun cleansing oil.'},
                    'wa10': {'name': 'Kose Sekkisei Brightening Foam Cleanser',
                             'price': 301000,
                             'description': '🫧 Kose Sekkisei Brightening Foam Cleanser\n'
                                            '\n'
                                            'Yorqinlik uchun foam cleanser.'},
                    'wa11': {'name': 'Curel Sebum Trouble Care Foaming Facial Cleanser',
                             'price': 205000,
                             'description': '🫧 Curel Sebum Trouble Care Foaming Facial Cleanser\n'
                                            '\n'
                                            'Yog‘li va sezuvchan teri uchun.'}}},
 'makeup': {'title': '💄 Tone-Up / Tonal',
            'items': {'mk1': {'name': 'Tfit Luminare Skip Tone Up Cream',
                              'price': 240000,
                              'description': '💄 Tfit Luminare Skip Tone Up Cream\n\nTone-up effektli krem.'},
                      'mk2': {'name': 'MAQuillage Essence Liquid EX 30ml',
                              'price': 362000,
                              'description': '💄 MAQuillage Essence Liquid EX\n\nPremium tonal asos.'},
                      'mk3': {'name': 'Moist Labo BB Whitening Cream',
                              'price': 181000,
                              'description': '💄 Moist Labo BB Whitening Cream\n\nBB tonal krem.'},
                      'mk4': {'name': 'Kansosan Moisture Protect Powder',
                              'price': 205000,
                              'description': '💄 Kansosan Moisture Protect Powder\n\nNamlikni saqlovchi powder.'},
                      'mk5': {'name': 'Kansosan Skincare Moisture Base Cover',
                              'price': 181000,
                              'description': '💄 Kansosan Skincare Moisture Base Cover\n'
                                             '\n'
                                             'Makiyaj bazasi va namlantirish uchun.'},
                      'mk6': {'name': 'Lits Moist C UV Primer',
                              'price': 193000,
                              'description': '💄 Lits Moist C UV Primer\n\nSPF himoya va makeup bazasi.'},
                      'mk7': {'name': 'Primavista Skin Protect Base Ultra Oily Skin',
                              'price': 362000,
                              'description': '💄 Primavista Skin Protect Base\n\nYog‘li teri uchun makeup bazasi.'},
                      'mk8': {'name': 'C Heroine Make Mascara',
                              'price': 193000,
                              'description': '💄 Heroine Make Mascara\n\nMashhur yapon tush.'},
                      'mk9': {'name': 'Schick Hydro Silk Face & Beauty',
                              'price': 277000,
                              'description': '💄 Schick Hydro Silk Face & Beauty\n\nYuz uchun beauty razor.'}}},
 'hair': {'title': '💇 Soch parvarishi',
          'items': {'hair1': {'name': 'Serapie Shampoo Set',
                              'price': 383000,
                              'description': '💇 Serapie Shampoo\n\n2 talik soch parvarishi seti.'},
                    'hair2': {'name': 'ULULIS Premium Black Serum Oil',
                              'price': 229000,
                              'description': '🖤 ULULIS Premium Black Serum Oil\n'
                                             '\n'
                                             'Quruq va shikastlangan sochlar uchun premium serum oil.'},
                    'hair3': {'name': 'Nile Scalp Hair Lotion',
                              'price': 241000,
                              'description': '💇 Nile Scalp Hair Lotion\n'
                                             '\n'
                                             'Bosh terisi va soch ildizlari parvarishi uchun.'},
                    'hair4': {'name': 'Golden Jojoba Oil',
                              'price': 240000,
                              'description': '💇 Golden Jojoba Oil\n\nSoch va teri parvarishi uchun jojoba yog‘i.'},
                    'hair5': {'name': 'Coolist Scalp Cooler',
                              'price': 229000,
                              'description': '💇 Coolist Scalp Cooler\n\nBosh terisi uchun sovutuvchi mahsulot.'},
                    'hair6': {'name': 'Shiseido Fino Premium Touch',
                              'price': 217000,
                              'description': '💇 Shiseido Fino Premium Touch\n\nMashhur yapon soch maskasi.'}}},
 'body': {'title': '🧼 Tana parvarishi',
          'items': {'body1': {'name': 'White Conc Body Shampoo 360ml',
                              'price': 181000,
                              'description': '🧼 White Conc Body Shampoo\n\nTana uchun yuvish vositasi.'},
                    'body2': {'name': 'Biore U Body Wash',
                              'price': 96000,
                              'description': '🧼 Biore U Body Wash\n\nKundalik tana yuvish vositasi.'},
                    'body3': {'name': 'Leivy Goat Milk Body Shampoo',
                              'price': 169000,
                              'description': '🧼 Leivy Goat Milk Body Shampoo\n'
                                             '\n'
                                             'Echki suti bilan tana yuvish vositasi.'},
                    'body4': {'name': 'Argelan Organic Body Soap',
                              'price': 169000,
                              'description': '🧼 Argelan Organic Body Soap\n\nOrganik tana sovuni.'},
                    'body5': {'name': '&Honey Body Wash',
                              'price': 217000,
                              'description': '🧼 &Honey Body Wash\n\nAsal komponentli tana yuvish vositasi.'}}},
 'hand_lip': {'title': "✋ Qo'l / Lab parvarishi",
              'items': {'ha1': {'name': 'Yuskin Hand Cream',
                                'price': 301000,
                                'description': '✋ Yuskin Hand Cream\n\nQuruq qo‘llar uchun namlantiruvchi krem.'},
                        'ha2': {'name': 'Yuskin Hana Sakura',
                                'price': 123000,
                                'description': '✋ Yuskin Hana Sakura\n\nSakura hidli qo‘l kremi.'},
                        'ha3': {'name': 'Neutrogena Intense Repair Cica Hand Cream',
                                'price': 132000,
                                'description': '✋ Neutrogena Intense Repair Cica Hand Cream\n'
                                               '\n'
                                               'Quruq qo‘llar uchun cica krem.'},
                        'ha4': {'name': 'Colorful Fruit Hand Cream Set',
                                'price': 170000,
                                'description': '✋ Colorful Fruit Hand Cream Set\n\nQo‘l krem seti.'},
                        'ha5': {'name': 'Curel Lip Care Cream',
                                'price': 123000,
                                'description': '💋 Curel Lip Care Cream\n\nLab parvarishi uchun krem.'}}},
 'mask': {'title': '🧖\u200d♀️ Niqoblar',
          'items': {'mask1': {'name': 'Medcube PDRN Pink Collagen Gel Mask',
                              'price': 263000,
                              'description': '🧖\u200d♀️ Medcube PDRN Pink Collagen Gel Mask\n\nKollagenli gel niqob.'},
                    'mask2': {'name': 'Lululun Precious Red',
                              'price': 120000,
                              'description': '🧖\u200d♀️ Lululun Precious Red\n\nYuz uchun sheet mask.'},
                    'mask3': {'name': 'Lululun Hydra AZ Mask Azelaic Acid',
                              'price': 169000,
                              'description': '🧖\u200d♀️ Lululun Hydra AZ Mask\n\nAzelaic acid bilan sheet mask.'},
                    'mask4': {'name': 'Lululun Hydra Extra Mask Exosome',
                              'price': 169000,
                              'description': '🧖\u200d♀️ Lululun Hydra Extra Mask Exosome\n\nExosome bilan sheet mask.'},
                    'mask5': {'name': 'NILE Clay Pack',
                              'price': 265000,
                              'description': '🧖\u200d♀️ NILE Clay Pack\n'
                                             '\n'
                                             'Gil asosidagi yuz niqobi. Teshikchalarni tozalash va ortiqcha yog‘ni '
                                             'kamaytirishga yordam beradi.'}}},
 'deodorant': {'title': '🌿 Deodorant',
               'items': {'deo1': {'name': 'Soft Stone Double Deonatulle',
                                  'price': 205000,
                                  'description': '🌿 Soft Stone Double Deonatulle\n\nMashhur yapon deodoranti.'},
                         'deo2': {'name': 'Decodo Deodorant',
                                  'price': 169000,
                                  'description': '🌿 Decodo Deodorant\n\nDeodorant mahsuloti.'},
                         'deo3': {'name': 'Dr.School Foot Spray',
                                  'price': 120000,
                                  'description': '🌿 Dr.School Foot Spray\n\nOyoq uchun spray.'},
                         'deo4': {'name': 'Rifurea Mentholatum',
                                  'price': 169000,
                                  'description': '🌿 Rifurea Mentholatum\n'
                                                 '\n'
                                                 'Terlash va hidga qarshi parvarish mahsuloti.'}}},
 'supplement': {'title': "💊 Qo'shimchalar",
                'items': {'sup1': {'name': 'DHC Collagen',
                                   'price': 277000,
                                   'description': '💊 DHC Collagen\n\nGo‘zallik uchun kollagen qo‘shimchasi.'},
                          'sup2': {'name': 'Tarix Beauty Charge',
                                   'price': 112000,
                                   'description': '💊 Tarix Beauty Charge\n\nGo‘zallik qo‘shimchasi.'}}},
 'other': {'title': '✨ Boshqa',
           'items': {'ot1': {'name': 'Biore Burun Patch',
                             'price': 72000,
                             'description': '✨ Biore Burun Patch\n\nQora nuqtalar uchun burun patch.'}}}}

def price_format(price):
    return f"{price:,}".replace(",", " ")


def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("🛍 Mahsulotlar", callback_data="products"),
        InlineKeyboardButton("🧺 Savat", callback_data="cart")
    )
    markup.add(
        InlineKeyboardButton("🎁 Aksiyalar", callback_data="sales"),
        InlineKeyboardButton("📞 Bog'lanish", callback_data="contact")
    )
    return markup


def replace_message(call, text, markup=None):
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
    except Exception:
        bot.send_message(call.message.chat.id, text, reply_markup=markup)
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception:
            pass


def find_product(item_id):
    for cat_id, category in catalog.items():
        if item_id in category["items"]:
            return category["items"][item_id], cat_id
    return None, None


@bot.message_handler(commands=["start"])
def start(message):
    text = """🇯🇵 Sakura Cosmetics

Yaponiya go'zallik sirlarini bir joyga jamladik ✨

💖 Original Yaponiya kosmetikasi
📦 Ishonchli qadoqlash
🚚 BTS markazigacha yetkazib berish

🌸 O'zingizga mos mahsulotni tanlang 👇"""
    bot.send_message(message.chat.id, text, reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "products":
        bot.answer_callback_query(call.id, "Mahsulotlar ochilmoqda...")
        markup = InlineKeyboardMarkup()
        for cat_id, cat in catalog.items():
            markup.add(InlineKeyboardButton(cat["title"], callback_data=cat_id))
        markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="back"))
        replace_message(call, "🛍 Kategoriyani tanlang:", markup)

    elif call.data in catalog:
        category = catalog[call.data]
        markup = InlineKeyboardMarkup()
        for item_id, item in category["items"].items():
            markup.add(InlineKeyboardButton(item["name"], callback_data=f"item_{item_id}"))
        markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="products"))
        replace_message(call, f"{category['title']}\n\nMahsulotni tanlang:", markup)

    elif call.data.startswith("item_"):
        item_id = call.data.replace("item_", "")
        product, back_category = find_product(item_id)
        if product is None:
            bot.answer_callback_query(call.id, "Mahsulot topilmadi")
            return

        text = f"""{product.get('description', product['name'])}

💰 Narxi: {price_format(product['price'])} so'm

📦 BTS markazigacha yetkazib beriladi"""

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("➕ Savatga qo'shish", callback_data=f"add_{item_id}"))
        markup.add(InlineKeyboardButton("🧺 Savat", callback_data="cart"))
        markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data=back_category))

        photo_path = product.get("photo")
        if photo_path:
            try:
                with open(photo_path, "rb") as photo:
                    bot.send_photo(call.message.chat.id, photo, caption=text, reply_markup=markup)
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                except Exception:
                    pass
            except Exception:
                replace_message(call, text, markup)
        else:
            replace_message(call, text, markup)

    elif call.data.startswith("add_"):
        item_id = call.data.replace("add_", "")
        user_id = call.from_user.id
        if user_id not in carts:
            carts[user_id] = []
        carts[user_id].append(item_id)
        bot.answer_callback_query(call.id, "Mahsulot savatga qo'shildi ✅")

    elif call.data == "cart":
        show_cart(call)
    elif call.data == "clear_cart":
        carts[call.from_user.id] = []
        replace_message(call, "🧺 Savat tozalandi.", main_menu())
    elif call.data == "checkout":
        start_checkout(call)
    elif call.data == "confirm_order":
        confirm_order(call)
    elif call.data == "cancel_order":
        replace_message(call, "❌ Buyurtma bekor qilindi.", main_menu())
    elif call.data == "sales":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="back"))
        replace_message(call, "🎁 Yaqin kunlarda yangi aksiyalar qo'shiladi.", markup)
    elif call.data == "contact":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="back"))
        replace_message(call, "📞 Bog'lanish\n\nTelegram: @yaponiyakosmetologiya", markup)
    elif call.data == "back":
        text = """🇯🇵 Sakura Cosmetics

💖 Original Yaponiya kosmetikasi
📦 Ishonchli qadoqlash
🚚 BTS markazigacha yetkazib berish

🌸 O'zingizga mos mahsulotni tanlang 👇"""
        replace_message(call, text, main_menu())


def show_cart(call):
    user_id = call.from_user.id
    if user_id not in carts or len(carts[user_id]) == 0:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="back"))
        replace_message(call, "🧺 Savatingiz bo'sh.", markup)
        return

    text = "🧺 SAVATINGIZ\n\n"
    total = 0
    for item_id in carts[user_id]:
        item, _ = find_product(item_id)
        if item:
            text += f"• {item['name']} — {price_format(item['price'])} so'm\n"
            total += item["price"]
    text += f"\n💰 Jami: {price_format(total)} so'm"

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 Buyurtma berish", callback_data="checkout"))
    markup.add(InlineKeyboardButton("🗑 Savatni tozalash", callback_data="clear_cart"))
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="back"))
    replace_message(call, text, markup)


def start_checkout(call):
    user_id = call.from_user.id
    if user_id not in carts or len(carts[user_id]) == 0:
        bot.answer_callback_query(call.id, "Savatingiz bo'sh")
        return
    orders[user_id] = {}
    msg = bot.send_message(call.message.chat.id, """🛒 Buyurtmangiz deyarli tayyor!

👤 Ism va familiyangizni kiriting:""")
    bot.register_next_step_handler(msg, get_customer_name)


def get_customer_name(message):
    user_id = message.from_user.id
    orders[user_id]["name"] = message.text
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("📲 Raqamni yuborish", request_contact=True))
    msg = bot.send_message(message.chat.id, """📞 Telefon raqamingizni yuboring

👇 Tugmani bosib yuborishingiz mumkin
yoki
✍️ Qo'lda yozishingiz mumkin""", reply_markup=markup)
    bot.register_next_step_handler(msg, get_customer_phone)


def get_customer_phone(message):
    user_id = message.from_user.id
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
    orders[user_id]["phone"] = phone
    msg = bot.send_message(message.chat.id, "🏢 Sizga eng yaqin BTS filialini yozing:", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_customer_bts)


def get_customer_bts(message):
    user_id = message.from_user.id
    orders[user_id]["bts"] = message.text
    cart_items = carts.get(user_id, [])
    text_items = ""
    total = 0
    for item_id in cart_items:
        item, _ = find_product(item_id)
        if item:
            text_items += f"• {item['name']} — {price_format(item['price'])} so'm\n"
            total += item["price"]
    orders[user_id]["items"] = text_items
    orders[user_id]["total"] = total

    summary = f"""🧾 BUYURTMA TASDIQLASH

👤 Ism: {orders[user_id]['name']}
📞 Telefon: {orders[user_id]['phone']}
🏢 BTS: {orders[user_id]['bts']}

🛍 Mahsulotlar:
{text_items}
💰 Jami: {price_format(total)} so'm"""
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ Tasdiqlash", callback_data="confirm_order"))
    markup.add(InlineKeyboardButton("❌ Bekor qilish", callback_data="cancel_order"))
    bot.send_message(message.chat.id, summary, reply_markup=markup)


def confirm_order(call):
    user_id = call.from_user.id
    if user_id not in orders:
        bot.answer_callback_query(call.id, "Buyurtma topilmadi. Qaytadan buyurtma bering.")
        return
    global order_counter
    order_counter += 1
    order_id = order_counter
    order = orders[user_id]
    username = call.from_user.username

    if username:
        tg_user = f"@{username}"
    else:
        tg_user = "Yo'q"
    
    admin_text = f"""🛒 YANGI BUYURTMA #{order_id}

👤 Ism: {order['name']}
📞 Telefon: {order['phone']}
📱 Telegram: {tg_user}
🏢 BTS: {order['bts']}

🛍 Mahsulotlar:
{order['items']}
💰 Jami: {price_format(order['total'])} so'm"""
    bot.send_message(ADMIN_ID, admin_text)
    bot.edit_message_text(f"""✅ Buyurtmangiz qabul qilindi!

🆔 Buyurtma raqami: #{order_id}

📦 Operator tez orada siz bilan bog'lanadi.""", call.message.chat.id, call.message.message_id)
    carts[user_id] = []
    orders.pop(user_id, None)


print("Bot ishga tushdi...")
bot.infinity_polling(skip_pending=True)
