import unittest
from unittest.mock import patch
import cc

class TestCurrencyConverter(unittest.TestCase):
    @patch('cc.requests.get')
    def test_valid_conversion(self, mock_get):
        mock_get.return_value.json.return_value = {
            "rates": {"USD": 1, "EUR": 0.85, "GBP": 0.75}
        }
        
        with patch('builtins.input', side_effect=["10 USD EUR", "Q"]):
            with self.assertRaises(SystemExit):
                cc.convert_currency()

    @patch('cc.requests.get')
    def test_invalid_currency_code(self, mock_get):
        mock_get.return_value.json.return_value = {
            "rates": {"USD": 1, "EUR": 0.85, "GBP": 0.75}
        }
        
        with patch('builtins.input', side_effect=["10 USD XYZ", "Q"]):
            with self.assertRaises(SystemExit):
                cc.convert_currency()

    @patch('cc.requests.get')
    def test_invalid_input_format(self, mock_get):
        mock_get.return_value.json.return_value = {
            "rates": {"USD": 1, "EUR": 0.85, "GBP": 0.75}
        }
        
        with patch('builtins.input', side_effect=["10USD EUR", "Q"]):
            with self.assertRaises(SystemExit):
                cc.convert_currency()

    @patch('cc.requests.get')
    def test_show_currencies(self, mock_get):
        mock_get.return_value.json.return_value = {
            "rates": {"USD": 1, "EUR": 0.85, "GBP": 0.75}
        }
        
        with patch('builtins.input', side_effect=["SHOW", "Q"]):
            with self.assertRaises(SystemExit):
                cc.convert_currency()

if __name__ == "__main__":
    unittest.main()
