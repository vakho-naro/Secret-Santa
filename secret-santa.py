import random
import smtplib


player_lst = []


while True:
    stop = input('want to create player? press n to stop, otherwise press anything ')
    if stop == 'n':
        break
    players_dict = {}

    name = input(" enter player's name: ")
    email = input("enter player's email: ")

    players_dict["name"] = name
    players_dict['email'] = email
    player_lst.append(players_dict)


player_names = [name['name'] for name in player_lst]


gift_list = []


def secret_santa(player_list: list, gift_names: list):
    for player in player_list:   
        if player_list[-1]['name'] == gift_names[-1] and len(gift_names) == 1:
            gift_list.clear()
            gift_names.clear
            gift_names = [name['name'] for name in player_lst]
            secret_santa(player_list, gift_names)
        else:   
            x = gift_names.pop(random.randrange(len(gift_names)))
            if x == player['name']:
                gift_names.append(x)
                y = gift_names.pop(random.randrange(len(gift_names[:-1])))
                gift_list.append((player['email'], y))

            else:
                gift_list.append((player['email'], x))


secret_santa(player_lst, player_names)
print(gift_list)


sender_email = ''
password = ''  # password and email required

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
subject = 'Secret Santa'
print('login succes')
for item in gift_list:
    msg = f'Subject: {subject}\n\n you are secret santa of : {item[1]}'
    server.sendmail(sender_email, item[0], msg)
print('massages sent')

