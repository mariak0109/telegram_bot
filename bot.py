{\rtf1\ansi\ansicpg1251\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red51\green124\blue2;}
{\*\expandedcolortbl;;\cspthree\c0\c0\c0;\cspthree\c32590\c53834\c14969;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf2 import telebot\
from telebot import types\
import random\
import os\
\
# \uc0\u1041 \u1045 \u1056 \u1045 \u1052  \u1058 \u1054 \u1050 \u1045 \u1053  \u1048 \u1047  \u1055 \u1045 \u1056 \u1045 \u1052 \u1045 \u1053 \u1053 \u1067 \u1061  \u1057 \u1056 \u1045 \u1044 \u1067  (\u1076 \u1083 \u1103  Railway)\
TOKEN = os.environ.get("TOKEN")\
bot = telebot.TeleBot(TOKEN)\
\
# \uc0\u1058 \u1042 \u1054 \u1048  \u1057 \u1051 \u1054 \u1042 \u1040 \
WORDS = \{\
    "notice": "\uc0\u1079 \u1072 \u1084 \u1077 \u1095 \u1072 \u1090 \u1100 ",\
    "hide": "\uc0\u1089 \u1082 \u1088 \u1099 \u1074 \u1072 \u1090 \u1100 ",\
    "resent": "\uc0\u1074 \u1086 \u1079 \u1084 \u1091 \u1097 \u1072 \u1090 \u1100 \u1089 \u1103 ",\
    "restore": "\uc0\u1074 \u1086 \u1089 \u1089 \u1090 \u1072 \u1085 \u1072 \u1074 \u1083 \u1080 \u1074 \u1072 \u1090 \u1100 ",\
    "according to": "\uc0\u1089 \u1086 \u1075 \u1083 \u1072 \u1089 \u1085 \u1086  \u1095 \u1077 \u1084 \u1091 -\u1090 \u1086 ",\
    "improve": "\uc0\u1091 \u1083 \u1091 \u1095 \u1096 \u1080 \u1090 \u1100 ",\
    "mood": "\uc0\u1085 \u1072 \u1089 \u1090 \u1088 \u1086 \u1077 \u1085 \u1080 \u1077 ",\
    "interlocutor": "\uc0\u1089 \u1086 \u1073 \u1077 \u1089 \u1077 \u1076 \u1085 \u1080 \u1082 ",\
    "succeed": "\uc0\u1087 \u1088 \u1077 \u1091 \u1089 \u1087 \u1077 \u1074 \u1072 \u1090 \u1100 ",\
    "state": "\uc0\u1089 \u1086 \u1089 \u1090 \u1086 \u1103 \u1085 \u1080 \u1077 ",\
    "can't help myself": "\uc0\u1085 \u1080 \u1095 \u1077 \u1075 \u1086  \u1085 \u1077  \u1084 \u1086 \u1075 \u1091  \u1087 \u1086 \u1076 \u1077 \u1083 \u1072 \u1090 \u1100 ",\
    "certain": "\uc0\u1086 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1077 \u1085 \u1085 \u1099 \u1081 ",\
    "vigorously": "\uc0\u1101 \u1085 \u1077 \u1088 \u1075 \u1080 \u1095 \u1085 \u1086 ",\
    "pull myself together": "\uc0\u1089 \u1086 \u1073 \u1088 \u1072 \u1090 \u1100 \u1089 \u1103 /\u1074 \u1079 \u1103 \u1090 \u1100  \u1089 \u1077 \u1073 \u1103  \u1074  \u1088 \u1091 \u1082 \u1080 ",\
    "encourage": "\uc0\u1087 \u1086 \u1076 \u1073 \u1086 \u1076 \u1088 \u1080 \u1090 \u1100 ",\
    "to be able": "\uc0\u1073 \u1099 \u1090 \u1100  \u1089 \u1087 \u1086 \u1089 \u1086 \u1073 \u1085 \u1099 \u1084 ",\
    "describe": "\uc0\u1086 \u1087 \u1080 \u1089 \u1072 \u1090 \u1100 ",\
    "embarrassed": "\uc0\u1089 \u1084 \u1091 \u1097 \u1077 \u1085 ",\
    "interact": "\uc0\u1074 \u1079 \u1072 \u1080 \u1084 \u1086 \u1076 \u1077 \u1081 \u1089 \u1090 \u1074 \u1086 \u1074 \u1072 \u1090 \u1100 ",\
    "stranger": "\uc0\u1085 \u1077 \u1079 \u1085 \u1072 \u1082 \u1086 \u1084 \u1077 \u1094 "\
\}\
\
words_list = list(WORDS.keys())\
user_data = \{\}\
\
def generate_question():\
    correct_word = random.choice(words_list)\
    correct_translation = WORDS[correct_word]\
    all_translations = list(WORDS.values())\
    other_translations = [t for t in all_translations if t != correct_translation]\
    wrong_options = random.sample(other_translations, 3)\
    options = [correct_translation] + wrong_options\
    random.shuffle(options)\
    return correct_word, correct_translation, options\
\
def create_buttons(options):\
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)\
    buttons = [types.KeyboardButton(opt) for opt in options]\
    markup.add(*buttons)\
    return markup\
\
@bot.message_handler(commands=['start'])\
def start_bot(message):\
    user_id = \cf3 message.chat.id\cf2 \
    word, correct, options = generate_question()\
    user_data[user_id] = \{"correct": correct\}\
    markup = create_buttons(options)\
    bot.send_message(user_id, f"\uc0\u1055 \u1045 \u1056 \u1045 \u1042 \u1045 \u1044 \u1048  \u1057 \u1051 \u1054 \u1042 \u1054 :\\n\\n**\{word\}**", parse_mode="Markdown", reply_markup=markup)\
\
@bot.message_handler(func=lambda message: True)\
def check_answer(message):\
    user_id = \cf3 message.chat.id\cf2 \
    answer = message.text.strip()\
    if user_id not in user_data:\
        bot.send_message(user_id, "\uc0\u1053 \u1072 \u1078 \u1084 \u1080  /start")\
        return\
    correct = user_data[user_id]["correct"]\
    if answer == correct:\
        bot.send_message(user_id, f"\uc0\u9989  \u1055 \u1056 \u1040 \u1042 \u1048 \u1051 \u1068 \u1053 \u1054 ! \u55356 \u57225 ")\
    else:\
        bot.send_message(user_id, f"\uc0\u10060  \u1053 \u1045 \u1055 \u1056 \u1040 \u1042 \u1048 \u1051 \u1068 \u1053 \u1054 !\\n\u1055 \u1088 \u1072 \u1074 \u1080 \u1083 \u1100 \u1085 \u1086 : **\{correct\}**")\
    word, correct, options = generate_question()\
    user_data[user_id]["correct"] = correct\
    markup = create_buttons(options)\
    bot.send_message(user_id, f"**\{word\}**", parse_mode="Markdown", reply_markup=markup)\
\
print("\uc0\u9989  \u1041 \u1054 \u1058  \u1047 \u1040 \u1055 \u1059 \u1065 \u1045 \u1053 , \u1057 \u1059 \u1050 \u1040 !")\
bot.polling(none_stop=True)}