import string
import random
import unittest
from datetime import datetime
from src.detection_palindrome import DetecteurPalindrome
from src.expressions import Expressions

class TestAppFunctions(unittest.TestCase):
    def randomword(self, length=8):
        """Générer un random word de longueur 8 par défaut."""
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    def test_saisie_miroir(self):
        cas = ['chat', 'chien', self.randomword(10)]
        for word in cas:
            with self.subTest(word):
                reversed_word = word[::-1]
                self.assertIn(reversed_word, DetecteurPalindrome.saisie(word))    

    def test_bonjour(self):
        chaine = 'test '
        resultat = DetecteurPalindrome.saisie(chaine)
        self.assertEqual(Expressions.SALUTATION, resultat[:len(Expressions.SALUTATION)])

    def test_au_revoir(self):
        chaine = 'test composé'
        resultat = DetecteurPalindrome.saisie(chaine)
        self.assertEqual(Expressions.ACQUITTANCE, resultat[-len(Expressions.ACQUITTANCE):])
    
    def test_palindrome(self):
        chaineOK = 'nurses run'
        chaineKO = 'test'

        resultatOK = DetecteurPalindrome.saisie(chaineOK)
        resultatKO = DetecteurPalindrome.saisie(chaineKO)

        self.assertIn(chaineOK + ' Bien dit !', resultatOK)
        self.assertNotIn(chaineKO, resultatKO)
        
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