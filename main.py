import os
import telegram
import random

def main_tank(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        if update.message:
            message = update.message
        else:
            message = update.edited_message
        chat_id = message.chat.id
        bot.sendMessage(chat_id=chat_id, text=give_a_tank(message.text))
        # bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "okay"

def give_a_tank(text):
    filename = 'lyrics_3.txt'
    output = []
    with open(filename, "r") as searchfile:
        lines = searchfile.readlines()
        for i,line in enumerate(lines):
            if line is not None:
                if text.lower() in line.lower():
                    try:
                        output.append(lines[i+1])
                    except: pass
    try:
        sort_output = list(set(output))
        if len(sort_output) > 1:
            index = random.randint(0, len(sort_output)-1)
        else:
            index = 0

        myset = sort_output[index]
        if '#' not in myset:
            return(myset)
        else:
            return('Мы переступили черту. Молодости конец')
    except: return("не пачкай клетчатые страницы пока слова недостаточно хороши")
