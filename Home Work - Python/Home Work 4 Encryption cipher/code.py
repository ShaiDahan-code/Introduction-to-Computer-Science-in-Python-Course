"""
Student: Shai Dahan
ID: 209462712
Assignment no. 1
Program: code.py
"""

from random import sample
alphabet = "abcdefghijklmnopqrstuvwxyz"

IO = input("Enter 'k' to cread a key: \nEnter 'e' for encrypt a key: \nEnter 'd' for decrypt to key: ").lower()
key = {}
random_key = sample(set(alphabet), 26)
for i in range(0, 26):
    key[alphabet[i]] = random_key[i]
while True:
    if IO == "k" or IO == "e" or IO == "d": # to check if Input every times is k,e.
        
        if IO == "k":# if unput is k so cread a key and write it to key.txt
            key = {}
            random_key = sample(set(alphabet), 26)#make the random
            for i in range(0, 26):# cread the new dict 
                key[alphabet[i]] = random_key[i]
            file = open("key.txt", "w")
            file.write("".join(random_key))
            file.close()
            IO = input("Enter a letter to contienu, or press anything else to exit: ").lower() # recvie the next IO
            
        if IO == "e":# if input is "e" so encrypt the text from plaintext to ciphertext
            str1 = ""
            read = open("plaintext.txt", "r").read().lower()# first read the text 
            for i in read:# this is to delet all what is not alphabet
                if i in alphabet or i == " ":
                    if i == " ":
                        str1 += " "
                    str1 += i  
                else:
                    continue
                cip = open("ciphertext.txt", "w")
                for letter in str1:# and here it's write the text with the code we cread
                    if letter == " ":
                        cip.write(" ")
                    else:
                        cip.write(key[letter])
            IO = input("Enter a letter to contienu, or press anything else to exit: ").lower() # recvie the next IO
        letter = ""
        if IO == "d": # if unput is "d" so decrypt the text from ciphertext to decrypted
            decrypted = open("decrypted.txt", "w")
            ciph = open("ciphertext.txt", "r").read().lower()
            for letter in ciph or letter == " ": # wrote the normal text that we wanna know
                if letter == " ":
                    decrypted.write(" ")
                else:
                    decrypted.write(key[letter])
            IO = input("Enter a letter to contienu, or press anything else to exit: ").lower()
    else:
        break
    