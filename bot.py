import telebot
from telebot import types
import random
import os

# ВСТАВИЛА ТОКЕН ПРЯМО В КОД, СУКА!
TOKEN = "8930361189:AAGDVIZ-rpWUvz8Q7lNzvhcvZDyDBp7h1T4"
bot = telebot.TeleBot(TOKEN)

WORDS = {
    "notice": "замечать",
    "hide": "скрывать",
    "resent": "возмущаться",
    "restore": "восстанавливать",
    "according to": "согласно чему-то",
    "improve": "улучшить",
    "mood": "настроение",
    "interlocutor": "собеседник",
    "succeed": "преуспевать",
    "state": "состояние",
    "can't help myself": "ничего не могу поделать",
    "certain": "определенный",
    "vigorously": "энергично",
    "pull myself together": "собраться/взять себя в руки",
    "encourage": "подбодрить",
    "to be able": "быть способным",
    "describe": "описать",
    "embarrassed": "смущен",
    "interact": "взаимодействовать",
    "stranger": "незнакомец"
}

words_list = list(WORDS.keys())
user_data = {}

def generate_question():
    correct_word = random.choice(words_list)
    correct_translation = WORDS[correct_word]
    all_translations = list(WORDS.values())
    other_translations = [t for t in all_translations if t != correct_translation]
    wrong_options = random.sample(other_translations, 3)
    options = [correct_translation] + wrong_options
    random.shuffle(options)
    return correct_word, correct_translation, options

def create_buttons(options):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [types.KeyboardButton(opt) for opt in options]
    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start'])
def start_bot(message):
    user_id = message.chat.id
    word, correct, options = generate_question()
    user_data[user_id] = {"correct": correct}
    markup = create_buttons(options)
    bot.send_message(user_id, f"ПЕРЕВЕДИ СЛОВО:\n\n**{word}**", parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def check_answer(message):
    user_id = message.chat.id
    answer = message.text.strip()
    if user_id not in user_data:
        bot.send_message(user_id, "Нажми /start")
        return
    correct = user_data[user_id]["correct"]
    if answer == correct:
        bot.send_message(user_id, f"✅ ПРАВИЛЬНО! 🎉")
    else:
        bot.send_message(user_id, f"❌ НЕПРАВИЛЬНО!\nПравильно: **{correct}**")
    word, correct, options = generate_question()
    user_data[user_id]["correct"] = correct
    markup = create_buttons(options)
    bot.send_message(user_id, f"**{word}**", parse_mode="Markdown", reply_markup=markup)

print("✅ БОТ ЗАПУЩЕН, СУКА!")
bot.polling(none_stop=True)
