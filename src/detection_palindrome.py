import datetime
from expressions import Expressions

class DetecteurPalindrome:
    
    @classmethod
    def saisie(self, chaine):
        reversed_chaine = chaine[::-1]
        if self.__is_palindrome__(chaine):
            return Expressions.SALUTATION + ' '+ chaine + ' Bien dit ! ' + Expressions.ACQUITTANCE
        else:
            return Expressions.SALUTATION + ' ' + reversed_chaine + ' ' + Expressions.ACQUITTANCE
    
    def __is_palindrome__(chaine):
        chaine = chaine.lower().replace(" ", "")
        return chaine == chaine[::-1]