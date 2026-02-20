import telebot
import random

# Senin Bot API Token'ın
API_TOKEN = '8456039026:AAGCoqbf0AggcHO14TTFAfp0Ieu1cA5xHDI'
bot = telebot.TeleBot(API_TOKEN)

# 🌍 Global Motivasyon Listesi (Hazır bekliyor)
affirmations = [
    "you are capable of achieving greatness! ✨",
    "consistency is the key to success. Keep building! 🚀",
    "your energy creates your reality. Stay positive! 💎",
    "the best way to predict the future is to create it. 🔥",
    "focus on progress, not perfection. 🙌",
    "you are doing an amazing job, keep glowing! 💫"
]

# 1. ✅ Yeni Gelen Karşılama (AKTİF)
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    welcome_text = "Welcome to **Let’s Connect** ✨\nMeet, learn, laugh & glow together 💫"
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

# 2. 💤 Otomatik Motivasyon (Şu an KAPALI / OFF)
@bot.message_handler(func=lambda message: True)
def automatic_motivation(message):
    # Aktif etmek istersen 0 rakamını 20 yap kanka.
    if random.randint(1, 100) <= 0: 
        user_name = message.from_user.first_name
        quote = random.choice(affirmations)
        bot.reply_to(message, f"Hey {user_name}, I just wanted to say: {quote}")

# 3. 📜 Topluluk Kuralları (/rules) - AKTİF
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

# 4. ❓ Yardım Menüsü (/help) - AKTİF
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "**LetsConnect Bot Commands:**\n"
        "/rules - Show community guidelines\n"
        "/help - Show this menu\n"
    )
    bot.reply_to(message, help_text, parse_mode='Markdown')

# Botun kopmasını engelleyen döngü
print("LetsConnect Bot is now running on FPS.ms!")
bot.infinity_polling()