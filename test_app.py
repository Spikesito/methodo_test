import unittest
from initial import is_valid_input, is_palindrome  # Assurez-vous que le script principal est nommé `app.py`

class TestAppFunctions(unittest.TestCase):
    def test_is_valid_input(self):
        # Cas d'entrée non valide
        self.assertFalse(is_valid_input(""))  # Chaîne vide
        self.assertFalse(is_valid_input("   "))  # Espaces uniquement

        # Cas d'entrée valide
        self.assertTrue(is_valid_input("Bonjour"))  # non vide
        self.assertTrue(is_valid_input("    Palindrome   "))  # espaces

    def test_is_palindrome(self):
        # Cas de palindrome
        self.assertTrue(is_palindrome("kayak"))
        self.assertTrue(is_palindrome("Aibohphobia"))  # casse
        self.assertTrue(is_palindrome("nurses run"))  # espaces

        # Cas non palindrome
        self.assertFalse(is_palindrome("Python"))
        self.assertFalse(is_palindrome("Hello World"))

if __name__ == "__main__":
    unittest.main()