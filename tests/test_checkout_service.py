import unittest
from unittest.mock import Mock

from src.models import CartItem, Order
from src.pricing import PricingService, PricingError
from src.checkout import CheckoutService, ChargeResult

class TestCheckoutService(unittest.TestCase):
	def setUp(self):
		self.payments = Mock()
		self.email = Mock()
		self.fraud = Mock()
		self.repo = Mock()
		self.pricing = Mock()
		self.checkout = CheckoutService(self.payments, self.email, self.fraud, self.repo, self.pricing)

	def test_invalid_user(self):
		user_id = "  "
		token = "asdf"
		country = "CL"
		check = self.checkout.checkout(user_id, [], token, country)
		self.assertEqual(check, "INVALID_USER")

	def test_invalid_cart(self):
		self.pricing.total_cents.side_effect = PricingError("qty must be > 0")
		user_id = "User1"
		token = "asdf"
		country = "CL"
		check = self.checkout.checkout(user_id, [], token, country)
		self.assertEqual(check, "INVALID_CART:qty must be > 0")

	def test_fraud_score(self):
		self.fraud.score.return_value = 80
		self.pricing.total_cents.return_value = 5000
		user_id = "User1"
		token = "asdf"
		country = "CL"
		check = self.checkout.checkout(user_id, [], token, country)
		self.assertEqual(check, "REJECTED_FRAUD")

	def test_payment_failed(self):
		self.fraud.score.return_value = 70
		self.pricing.total_cents.return_value = 5000
		self.payments.charge.return_value = ChargeResult(ok=False, reason="card_declined")
		user_id = "User1"
		token = "asdf"
		country = "CL"
		check = self.checkout.checkout(user_id, [], token, country)
		self.assertEqual(check, "PAYMENT_FAILED:card_declined")

	def test_order(self):
		self.fraud.score.return_value = 70
		self.pricing.total_cents.return_value = 5000
		self.payments.charge.return_value = ChargeResult(ok=True, charge_id="ch_1")
		user_id = "User1"
		token = "asdf"
		country = "CL"
		check = self.checkout.checkout(user_id, [], token, country)
		self.assertTrue(check.startswith("OK:"))
		self.repo.save.assert_called_once()
		self.email.send_receipt.assert_called_once()
		saved_order = self.repo.save.call_args[0][0]
		self.assertEqual(saved_order.user_id, "User1")
		self.assertEqual(saved_order.total_cents, 5000)
		self.assertEqual(saved_order.country, "CL")
	

