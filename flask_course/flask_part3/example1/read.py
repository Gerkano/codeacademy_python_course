from app import db, Message

all_messages = Message.query.all()


for message in all_messages:
    print(message.message)
    print(message.phone)