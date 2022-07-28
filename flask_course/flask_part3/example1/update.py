from app import db, Message

juozas = Message.query.get(3)
juozas.name = 'Vaflius'
juozas.email = 'vaflius.com'
db.session.add(juozas)
db.session.commit()
print(Message.query.all())