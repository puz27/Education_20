import requests
import stripe

# make_payment = "https://stripe.com/docs/api/payment_intents/create"
# get_payment = "https://stripe.com/docs/api/payment_intents/retrieve"

"""
https://stripe.com/docs/api/payment_intents#create_payment_intent
https://justdjango.com/blog/django-stripe-payments-tutorial

stripe.api_key = "sk_test_51NXPaKCn4C5dva66mINywzPgyNFznygCyoFq01lCmrEHwkmEGzEFLfp36l1Nzx1Gt9jJxCOcrfbKY9R3HCxSfkjQ00NkNSsW8K"

stripe.PaymentIntent.create(
  amount=2000,
  currency="usd",
  automatic_payment_methods={"enabled": True},
)
"""
make_payment = "https://stripe.com/docs/api/payment_intents#create_payment_intent"
response = requests.get(make_payment)
print(response.content)

# stripe.api_key = "sk_test_51NXPaKCn4C5dva66mINywzPgyNFznygCyoFq01lCmrEHwkmEGzEFLfp36l1Nzx1Gt9jJxCOcrfbKY9R3HCxSfkjQ00NkNSsW8K"
#
# stripe.PaymentIntent.create(
#   amount=2000,
#   currency="usd",
#   automatic_payment_methods={"enabled": True},
# )
#
# print(stripe)