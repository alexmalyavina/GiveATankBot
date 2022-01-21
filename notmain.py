import os
import telegram
import random

# #it works let's break
# def give_a_tank(text):
#     filename = 'notlyrics.txt'
#     output = []
#     with open(filename, "r") as searchfile:
#         lines = searchfile.readlines()
#         for i,line in enumerate(lines):
#             if text.lower() in line.lower():
#                 if lines[i+1] != []:
#                     output.append(lines[i+1])
#                 # else:
#     sort_output = list(set(output))
#     index = random.randint(0, len(sort_output)-1)
#                 # output.append('error [] string')
#     try:
#         myset = sort_output[index]
#         if '[' not in myset:
#             return(myset)
#         else:
#             return('Мы переступили черту. Молодости конец (пустой списоку)')
#
#     except: return("не пачкай клетчатые страницы пока слова недостаточно хороши")


# def main_tank(request):
#     bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
#     if request.method == "POST":
#         update = telegram.Update.de_json(request.get_json(force=True), bot)
#         chat_id = update.message.chat.id
#         # Reply with the same message
#         bot.sendMessage(chat_
# id=chat_id, text = give_a_tank(update.message.text)
#         # bot.sendMessage(chat_id=chat_id, text=update.message.text)
#     return "okay"

def give_a_tank(text):
    filename = 'notlyrics.txt'
    output = []
    # output_add = []


    with open(filename, "r") as searchfile:
        lines = searchfile.readlines()
        for i,line in enumerate(lines):
            if text.lower() in line.lower():
                if lines[i+1] != []:
                    if '[' not in lines[i+1]:
                        output.append(lines[i+1])
                    else:
                        output.append(lines[i+2])

                    # output_add.append(lines[i+3])

                # elif (for j in'['in line[i+1]):
                #     print('I find []')
                    # output.append(lines[i+3])
    sort_output = list(set(output))
    index = random.randint(0, len(sort_output)-1)
                # output.append('error [] string')
    try:
        myset = sort_output[index]
        if '[' not in myset:
            return(myset)
        else:

            return('Мы переступили черту. Молодости конец (пустой список)')

    except: return("не пачкай клетчатые страницы пока слова недостаточно хороши")
print('Или, голодая, поделиться последней рубахой?')
print(give_a_tank('Или, голодая, поделиться последней рубахой?'))
