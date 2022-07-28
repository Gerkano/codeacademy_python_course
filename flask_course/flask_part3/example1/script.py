from app import db, Message

db.create_all()  # sukurs mūsų lentelę DB

# Iš karto inicijuosime testams keletą įrašų:
jonas = Message('Jonas', 'jonas@mail.com', 'Kažkoks labai rimtas atsiliepimas.', '927836478364')
antanas = Message('Antanas', 'antanas@mail.lt', 'Antano nuomonė labai svarbi.', '892346')
juozas = Message('Juozas', 'juozukas@friends.lt', 'Aš labai piktas, nes blogai.', '12392834678264354')
bronius = Message('Bronius', 'bronka@yahoo.com', 'Aš tai linksmas esu, man patinka.', '3948576')

# Pridėsime šiuos veikėjus į mūsų DB
db.session.add_all([jonas, antanas, juozas, bronius])
# .commit išsaugo pakeitimus
db.session.commit()

print(jonas.id)
print(antanas.id)
print(bronius.id)
print(juozas.id)
