import string
import random
import unittest
from datetime import datetime
from src.detection_palindrome import DetecteurPalindrome
from src.expressions import Expressions
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

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

    def test_detect_french(self):
        input_text = "Bonjour, comment ça va ?"
        result = detect_language(input_text)
        self.assertEqual(result["detected_language"], "fr")
    
    def test_detect_english(self):
        input_text = "Hello, how are you?"
        result = detect_language(input_text)
        self.assertEqual(result["detected_language"], "en")
    
    def test_short_input(self):
        input_text = "!"
        result = detect_language(input_text)
        self.assertIn("error", result)

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

    # def test_greetings(self):
    #     day = "21/11/2024 15:30:45"
    #     evening = "21/11/2024 19:30:45"
    #     day = datetime.strptime(day, "%d/%m/%Y %H:%M:%S")
    #     evening = datetime.strptime(evening, "%d/%m/%Y %H:%M:%S")

    #     self.assertEqual("Bonne journée", DetecteurPalindrome.get_greeting(day))
    #     self.assertEqual("Bonne soirée", DetecteurPalindrome.get_greeting(evening))


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