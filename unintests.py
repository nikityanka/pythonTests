import unittest
from cc import validate_input

class TestCCFunctions(unittest.TestCase):

    def test_empty_input(self):
        """Тест на пустое значение"""
        result, message = validate_input("")
        self.assertFalse(result)
        self.assertEqual(message, "Пустое значение")

    def test_incorrect_length(self):
        """Тест на неверную длину"""
        result, message = validate_input("123456789012345")
        self.assertFalse(result)
        self.assertEqual(message, "Неверная длина")

    def test_non_digit_input(self):
        """Тест на ввод с нецифровыми символами"""
        result, message = validate_input("123456789012345a")
        self.assertFalse(result)
        self.assertEqual(message, "Ввод должен содержать только цифры")

    def test_correct_input(self):
        """Тест на корректный ввод"""
        result, message = validate_input("1234567890123456")
        self.assertTrue(result)
        self.assertEqual(message, "Ввод корректен")

    def test_exit_input(self):
        """Тест на выход (если функция поддерживает выход по какому-то значению)"""
        # Для этого теста нужно знать, как функция обрабатывает выход
        # Например, если выход по пустой строке
        result, message = validate_input("")
        self.assertFalse(result)
        self.assertEqual(message, "Пустое значение")

if __name__ == '__main__':
    unittest.main()
