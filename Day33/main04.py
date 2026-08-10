class Payment:
    def Pay(self):
        print("Payment processing")

class CreditCard(Payment):
    def Pay(self):
        print("Paid by credit card")

class PayPal:
    def Pay(self):
        print("Paid by PayPal")

def process_payment(payment):
    payment.Pay()

payments = [Payment(), CreditCard(), PayPal()]

for payment in payments:
    process_payment(payment)
