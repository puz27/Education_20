# import stripe
#
# stripe.api_key = "sk_test_51NXPaKCn4C5dva66mINywzPgyNFznygCyoFq01lCmrEHwkmEGzEFLfp36l1Nzx1Gt9jJxCOcrfbKY9R3HCxSfkjQ00NkNSsW8K"
#
#
# class Customer:
#
#     def __init__(self, customer_email):
#         self.customer_email = customer_email
#         self.request = None
#
#     def create_customer(self):
#         self.request = stripe.Customer.create(
#             name=self.customer_email,
#             email=self.customer_email,
#             )
#
#     def retrieve_customer(self):
#         return stripe.Customer.retrieve(self.request.id)
#
#
# class PaymentCustomer:
#
#     def __init__(self, customer_id, amount=None):
#         self.amount = amount
#         self.customer_id = customer_id
#         self.request = None
#
#     def create_payment(self):
#         self.request = stripe.PaymentIntent.create(
#             amount=self.amount,
#             currency="usd",
#             automatic_payment_methods={"enabled": True},
#             customer=self.customer_id,
#             )
#
#     def retrieve_payment(self):
#         amount = stripe.PaymentIntent.retrieve(self.customer_id)["amount"]
#         currency = stripe.PaymentIntent.retrieve(self.customer_id)["currency"]
#         return amount, currency
#
