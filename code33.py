import random
import string
def genpass(length, digit = True, special = True):
    char = string.ascii_letters
    if digit:
        char += string.digits
    if special:
        char += string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password
def main():
    print("Password Generator")
    try:
        length = int(input("Enter thr password length: "))
        if length <= 0:
            print("Negative number.. Please Enter the Positive number for password!!!...")
            return
        digit = input("Digits (Yes/No): ").lower() == "Yes"
        special = input("Special Character (Yes/No): ").lower() == "Yes"
        password = genpass(length,digit,special)
        print(password)
    except valerror:
        print("Kindly the valid password length of an integer!!!")
if __name__ =="__main__":
    main()



        
