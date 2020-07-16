import random
import smtplib, ssl
import json

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "alexcanto436@gmail.com"  # Enter your address
receiver_email = "alexcanto_@hotmail.com"  # Enter receiver address
password ="Bananamonkey_00"
lista_dias=['Segunda-Feira','Terca-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sabado','Domingo']
lista_pratos=["Esparguete a bolonhesa","Bifinhos com cogumelos","Empadao","Arroz c/ bifes","Massa c/ atum","Mc","Pizza","Salmao","Atum","Frango a Bras","Frango Assado","Carne Estufada","Atum e Ovos","Peito de Frango"]
dictio = {}
formatted_str = ""
text="""\
Subject: Ementa da Semana

Segue a Ementa da Semana.

"""




for x in lista_dias:
    random_num = random.choice(lista_pratos)
    if x in dictio.keys():
        dictio[x].append(random_num)
    else:
        dictio[x]=[random_num]
    lista_pratos.remove(random_num)

    random_num2 = random.choice(lista_pratos)
    if x in dictio.keys():
        dictio[x].append(random_num2)
    else:
        dictio[x]=[random_num2]
    lista_pratos.remove(random_num2)

for key in dictio.keys():
    formatted_str = formatted_str + key + ":\n"
    for value in dictio[key]:
        formatted_str = formatted_str + "\t" + value + "\n"
    formatted_str = formatted_str + "\n\n" 

print(formatted_str)
var=formatted_str
message=text+var

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("mail enviado")


