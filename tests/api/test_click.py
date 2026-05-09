from helium import click, Button, Config
from helium._impl.util.lang import TemporaryAttrValue
from tests.api import BrowserAT

class ClickTest(BrowserAT):
	def get_page(self):
		return 'test_click.html'
	def test_click(self):
		click("Click me!")
		self.assertEqual('Success!', self.read_result_from_browser())
	def test_click_non_existent_element(self):
		with TemporaryAttrValue(Config, 'implicit_wait_secs', .1):
			with self.assertRaises(LookupError):
				click("Non-existent")
	def test_click_non_existent_str_error_message(self):
		with TemporaryAttrValue(Config, 'implicit_wait_secs', .1):
			with self.assertRaises(LookupError) as cm:
				click("Non-existent")
			self.assertEqual("'Non-existent'", str(cm.exception))
	def test_click_non_existent_button_error_message(self):
		with TemporaryAttrValue(Config, 'implicit_wait_secs', .1):
			with self.assertRaises(LookupError) as cm:
				click(Button("Non-existent"))
			self.assertEqual("Button('Non-existent')", str(cm.exception))