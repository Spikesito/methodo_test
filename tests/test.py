import string
import random
import unittest
from src.detection_palindrome import DetecteurPalindrome

class TestAppFunctions(unittest.TestCase):
    def randomword(self, length=8):
        """Générer un random word de longueur 8 par défaut."""
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    def test_saisie_miroir(self):
        cas = ['chat', 'chien', self.randomword(10)]
        for word in cas:
            with self.subTest(word):
                reversed_word = word[::-1]
                self.assertEqual(reversed_word, DetecteurPalindrome.saisie(word))

if __name__ == "__main__":
    unittest.main()














# from src.initial import is_valid_input, is_palindrome


    # def test_is_valid_input(self):
    #     # Cas d'entrée non valide
    #     self.assertFalse(is_valid_input(""))  # Chaîne vide
    #     self.assertFalse(is_valid_input("   "))  # Espaces uniquement

    #     # Cas d'entrée valide
    #     self.assertTrue(is_valid_input("Bonjour"))  # non vide
    #     self.assertTrue(is_valid_input("    Palindrome   "))  # espaces

    # def test_is_palindrome(self):
    #     # Cas de palindrome
    #     self.assertTrue(is_palindrome("kayak"))
    #     self.assertTrue(is_palindrome("Aibohphobia"))  # casse
    #     self.assertTrue(is_palindrome("nurses run"))  # espaces

    #     # Cas non palindrome
    #     self.assertFalse(is_palindrome("Python"))
    #     self.assertFalse(is_palindrome("Hello World"))