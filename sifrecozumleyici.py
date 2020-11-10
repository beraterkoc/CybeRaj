from random import *

user_pass = input("Şifrenizi Giriniz: ")
password = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'ğ', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'u', 'z', 'y', 'x', 'u',
             'ü', 'ı', 'ö', 'ç', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş',
             'T', 'U', 'Ü', 'V', 'Y', 'Z', 'Q', 'X', 'W', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

guess = ""

while (guess != user_pass):
     guess = ""
     for letter in range(len(user_pass)):
         guess_letter = password[randint(0, 72)]
         guess = str(guess_letter) + str(guess)
         print(guess)
print("Şifreniz: ", guess)