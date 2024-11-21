import datetime
from expressions import Expressions
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

class DetecteurPalindrome:

    @classmethod
    def saisie(self, chaine):
        reversed_chaine = chaine[::-1]
        if self.__is_palindrome__(chaine):
            return self.__to_string__(chaine, self.__detect_langage__(chaine), True)
        else:
            return self.__to_string__(reversed_chaine, self.__detect_langage__(chaine), False)

    def __is_palindrome__(chaine):
        chaine = chaine.lower().replace(" ", "")
        return chaine == chaine[::-1]

    def __detect_langage__(chaine):
        # Détecte la langue principale
        detected_language = detect(chaine)
        return detected_language
        
    def __to_string__(chaine, langage, is_pal):
        greetings = {
            "fr": {"prefix": "Hello", "pal_congrats": "Nice job", "suffix": "Goodbye"},
            "en": {"prefix": "Bonjour", "pal_congrats": "Bien joué !", "suffix": "Au revoir"},
            "es": {"prefix": "Hola", "pal_congrats": "Bien dicho", "suffix": "Adiós"},
            "de": {"prefix": "Hallo", "pal_congrats": "Gut gesagt", "suffix": "Auf Wiedersehen"}
        }

        if langage in greetings:
            prefix_message = greetings[langage]["prefix"]
            pal_message = greetings[langage]['pal_congrats']
            suffix_message = greetings[langage]["suffix"]

            if is_pal:
                return prefix_message + ' ' + chaine  + ' ' + pal_message  + ' ' + suffix_message
            else:
                return prefix_message  + ' ' + chaine  + ' ' + suffix_message
        else:
            return "Langue non prise en charge pour le moment."