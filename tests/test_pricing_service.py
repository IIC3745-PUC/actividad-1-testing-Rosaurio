import unittest
from unittest.mock import Mock

from src.models import CartItem, Order
from src.pricing import PricingService, PricingError

class TestPricingService(unittest.TestCase):
	def setUp(self):
		self.pricing_service = PricingService()

	def test_subtotal_cents_correct(self):
		item1 = CartItem("Pan", 200, 5)
		item2 = CartItem("Bebida", 1500, 2)
		subtotal = self.pricing_service.subtotal_cents([item1,item2])
		self.assertEqual(subtotal, 4000)

	def test_invalid_qty(self):
		item = CartItem("Pan", 200, 0)
		with self.assertRaises(PricingError):
			self.pricing_service.subtotal_cents([item])

	def test_invalid_price(self):
		item = CartItem("Pan", -1, 2)
		with self.assertRaises(PricingError):
			self.pricing_service.subtotal_cents([item])

	def test_cupon_vacio(self):
		subtotal = 2000
		cupon = ""
		total = self.pricing_service.apply_coupon(subtotal, cupon)
		self.assertEqual(total, 2000)

	def test_cupon_10(self):
		subtotal = 2000
		cupon = "SAVE10"
		total = self.pricing_service.apply_coupon(subtotal, cupon)
		self.assertEqual(total, 1800)

	def test_cupon_2000(self):
		subtotal = 4000
		cupon = "CLP2000"
		total = self.pricing_service.apply_coupon(subtotal, cupon)
		self.assertEqual(total, 2000)

	def test_cupon_invalid(self):
		subtotal = 4000
		cupon = "CLP20000"
		with self.assertRaises(PricingError):
			self.pricing_service.apply_coupon(subtotal, cupon)

	def test_tax_CL(self):
		subtotal = 20000
		country = "CL"
		tax = self.pricing_service.tax_cents(subtotal, country)
		self.assertEqual(tax, 3800)


	def test_tax_US(self):
		subtotal = 20000
		country = "US"
		tax = self.pricing_service.tax_cents(subtotal, country)
		self.assertEqual(tax, 0)

	def test_tax_EU(self):
		subtotal = 20000
		country = "EU"
		tax = self.pricing_service.tax_cents(subtotal, country)
		self.assertEqual(tax, 4200)

	def test_tax_invalid(self):
		subtotal = 20000
		country = "AS"
		with self.assertRaises(PricingError):
			self.pricing_service.tax_cents(subtotal, country)

	def test_shipping_CL_0(self):
		subtotal = 20000
		country = "CL"
		shipping = self.pricing_service.shipping_cents(subtotal, country)
		self.assertEqual(shipping, 0)

	def test_shipping_CL_2500(self):
		subtotal = 2000
		country = "CL"
		shipping = self.pricing_service.shipping_cents(subtotal, country)
		self.assertEqual(shipping, 2500)

	def test_shipping_EU(self):
		subtotal = 20000
		country = "EU"
		shipping = self.pricing_service.shipping_cents(subtotal, country)
		self.assertEqual(shipping, 5000)

	def test_ship_invalid(self):
		subtotal = 20000
		country = "AS"
		with self.assertRaises(PricingError):
			self.pricing_service.shipping_cents(subtotal, country)

	def test_total_cents(self):
		item1 = CartItem("Pan", 200, 5)
		item2 = CartItem("Bebida", 1500, 2)
		cupon = ""
		country = "CL"
		total = self.pricing_service.total_cents([item1,item2], cupon, country)
		self.assertEqual(total, 7260)

