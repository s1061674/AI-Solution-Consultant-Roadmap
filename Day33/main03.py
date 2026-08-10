class Email:
    def send(self):
        print("Email sent")

class SMS:
    def send(self):
        print("SMS sent")

def send_message(message):
    message.send()

send_message(Email())
send_message(SMS())
