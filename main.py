import os
import telegram
import random

def main_tank(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=give_a_tank(update.message.text))
        # bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "okay"

def give_a_tank(text):
    filename = 'lyrics.txt'
    output = []
    with open(filename, "r") as searchfile:
        lines = searchfile.readlines()
        for i,line in enumerate(lines):
            if text.lower() in line.lower():
                if lines[i+1] != []:
                    output.append(lines[i+1])
                # else:
    sort_output = list(set(output))
    index = random.randint(0, len(sort_output)-1)
                # output.append('error [] string')
    try:
        myset = sort_output[index]
        if '[' not in myset:
            return(myset)
        else:
            return('Мы переступили черту. Молодости конец')
    except: return("не пачкай клетчатые страницы пока слова недостаточно хороши")
