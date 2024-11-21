import datetime

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def get_time_based_greeting():
    current_hour = datetime.datetime.now().hour
    if 4 <= current_hour < 18:
        return "Bonne journée"
    else:
        return "Bonne soirée l'ami"
    
def is_valid_input(user_input):
    return bool(user_input.replace(" ", ""))

def main():
    print("Bonjour!")
    while True:
        user_input = input("Entrez un mot ou une phrase ('exit' pour quitter) : ")
        if not is_valid_input(user_input):
            print("Veuillez entrer un mot ou une phrase non vide")
            continue
        if user_input.lower() == "exit":
            print(get_time_based_greeting())
            break
        elif is_palindrome(user_input):
            print("Bien dit !")
        else:
            print(user_input)

if __name__ == "__main__":
    main()