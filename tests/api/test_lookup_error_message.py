from helium import click, hover, write, highlight, select, \
	attach_file, drag_file, Button, TextField, ComboBox, Config
from helium._impl.util.lang import TemporaryAttrValue
from tests.api import BrowserAT
from tests.api.util import get_data_file

class LookupErrorMessageTest(BrowserAT):
	def get_page(self):
		return 'test_gui_elements.html'
	def test_click_non_existent_str_error_message(self):
		self._check(lambda: click("Non-existent"), "'Non-existent'")
	def test_click_non_existent_button_error_message(self):
		self._check(
			lambda: click(Button("Non-existent")), "Button('Non-existent')"
		)
	def test_hover_non_existent_str_error_message(self):
		self._check(lambda: hover("Non-existent"), "'Non-existent'")
	def test_hover_non_existent_button_error_message(self):
		self._check(
			lambda: hover(Button("Non-existent")), "Button('Non-existent')"
		)
	def test_write_into_non_existent_str_error_message(self):
		self._check(
			lambda: write('Hello', into='Non-existent'), "'Non-existent'"
		)
	def test_write_into_non_existent_text_field_error_message(self):
		self._check(
			lambda: write('Hello', into=TextField('Non-existent')),
			"TextField('Non-existent')"
		)
	def test_highlight_non_existent_str_error_message(self):
		self._check(
			lambda: highlight("Non-existent"), "'Non-existent'"
		)
	def test_highlight_non_existent_button_error_message(self):
		self._check(
			lambda: highlight(Button("Non-existent")), "Button('Non-existent')"
		)
	def test_select_non_existent_str_error_message(self):
		self._check(
			lambda: select("Non-existent", "Option One"), "'Non-existent'"
		)
	def test_select_non_existent_combo_box_error_message(self):
		self._check(
			lambda: select(ComboBox("Non-existent"), "Option One"),
			"ComboBox('Non-existent')"
		)
	def test_attach_file_non_existent_str_error_message(self):
		f = get_data_file('test_file_upload', 'upload_this.png')
		self._check(
			lambda: attach_file(f, to='Non-existent'), "'Non-existent'"
		)
	def test_drag_file_non_existent_str_error_message(self):
		f = get_data_file('test_file_upload', 'upload_this.png')
		self._check(
			lambda: drag_file(f, to='Non-existent'), "'Non-existent'"
		)
	def _check(self, fn, expected_message):
		with TemporaryAttrValue(Config, 'implicit_wait_secs', .1):
			with self.assertRaises(LookupError) as cm:
				fn()
			self.assertEqual(expected_message, str(cm.exception))
