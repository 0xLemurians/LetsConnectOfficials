import telebot
import random

# Bot API Token'ın
API_TOKEN = '8546686763:AAG9I0nSMtePHdNZzrO9LehS8VC0K4MA3Fw'
bot = telebot.TeleBot(API_TOKEN)

# 🌍 Motivasyon Sözleri (PASİF - Kodun içinde duruyor)
affirmations = [
    "you are capable of achieving greatness! ✨",
    "consistency is the key to success. Keep building! 🚀",
    "your energy creates your reality. Stay positive! 💎",
    "focus on progress, not perfection. 🙌",
    "you are doing an amazing job, keep glowing! 💫"
]

# 1. ✅ SADECE HOŞ GELDİN MESAJI (AKTİF)
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    welcome_text = "Welcome to **Let’s Connect** ✨\nMeet, learn, laugh & glow together 💫"
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

# 2. 💤 Otomatik Etkileşim (PASİF - Şu an Kapalı %0)
@bot.message_handler(func=lambda message: True)
def auto_interaction(message):
    # Aktif etmek için 0'ı 20 yapman yeterli kanka.
    if random.randint(1, 100) <= 0:
        user_name = message.from_user.first_name
        quote = random.choice(affirmations)
        bot.reply_to(message, f"Hey {user_name}, {quote}")

# Botun çalıştığını gösteren log
print("LetsConnect Global AI: 'Only Welcome' mode is active!")
bot.infinity_polling()
