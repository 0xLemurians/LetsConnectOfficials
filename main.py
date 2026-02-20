import telebot
import random

# Yeni Bot API Token'ın
API_TOKEN = '8546686763:AAG9I0nSMtePHdNZzrO9LehS8VC0K4MA3Fw'
bot = telebot.TeleBot(API_TOKEN)

# 🌍 Motivasyon Sözleri (Şu an pasif, ileride açarız)
affirmations = [
    "you are capable of achieving greatness! ✨",
    "consistency is the key to success. Keep building! 🚀",
    "your energy creates your reality. Stay positive! 💎",
    "focus on progress, not perfection. 🙌",
    "you are doing an amazing job, keep glowing! 💫"
]

# 1. ✅ Yeni Üye Karşılama
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    welcome_text = "Welcome to **Let’s Connect** ✨\nMeet, learn, laugh & glow together 💫"
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

# 2. 📜 Kurallar Komutu (/rules)
@bot.message_handler(commands=['rules'])
def send_rules(message):
    rules_text = """
📌 **LetsConnect Community Rules**

1️⃣ **Be Respectful:** Treat everyone with kindness.
2️⃣ **No Spam:** Avoid irrelevant links or flooding.
3️⃣ **Value First:** Focus on networking and knowledge.
4️⃣ **Language:** Please use English for global communication.

Stay focused and keep building! 🚀
    """
    bot.reply_to(message, rules_text, parse_mode='Markdown')

# 3. ❓ Yardım Komutu (/help)
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "**LetsConnect Bot Commands:**\n"
        "/rules - Show community guidelines\n"
        "/help - Show this menu"
    )
    bot.reply_to(message, help_text, parse_mode='Markdown')

# 4. 💤 Otomatik Etkileşim (Şu an Kapalı - %0)
@bot.message_handler(func=lambda message: True)
def auto_interaction(message):
    # Eğer %20 şansla konuşmasını istersen 0'ı 20 yap kanka.
    if random.randint(1, 100) <= 0:
        user_name = message.from_user.first_name
        quote = random.choice(affirmations)
        bot.reply_to(message, f"Hey {user_name}, {quote}")

print("LetsConnect Global AI is active with the NEW Token!")
bot.infinity_polling()
