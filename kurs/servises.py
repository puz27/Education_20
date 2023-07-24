import requests
import stripe
from rest_framework import status
from rest_framework.decorators import api_view

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
# make_payment = "https://stripe.com/docs/api/payment_intents#create_payment_intent"
# response = requests.get(make_payment)
# print(response.content)

# params = {
#                 "text": keywords,
#                 "per_page": 100,
#                 "page": page_number,
#                         }

# response = requests.get(make_payment, params=params)
#
stripe.api_key = "sk_test_51NXPaKCn4C5dva66mINywzPgyNFznygCyoFq01lCmrEHwkmEGzEFLfp36l1Nzx1Gt9jJxCOcrfbKY9R3HCxSfkjQ00NkNSsW8K"
#
# stripe.PaymentIntent.create(
#   amount=2000,
#   currency="usd",
#   automatic_payment_methods={"enabled": True},
# )
#
# print(stripe)


@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
      amount=1000,
      currency='USD',
      payment_method_types=['card'],
      receipt_email='test@example.com')
    return request.Response(status=status.HTTP_200_OK, data=test_payment_intent)


test_payment()
