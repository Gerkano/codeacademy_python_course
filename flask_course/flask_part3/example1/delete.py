from app import db, Message

jonas = Message.query.get(1)
db.session.delete(jonas)
db.session.commit()
print(Message.query.all())
