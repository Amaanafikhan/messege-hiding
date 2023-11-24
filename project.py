

import cv2
import os

def encrypt(img, message):
    d = {chr(i): i for i in range(255)}
    m, n, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n, m, z = n + 1, m + 1, (z + 1) % 3

    cv2.imwrite("Encryptedmsg.jpg", img)

def decrypt(img, password):
    c = {i: chr(i) for i in range(255)}
    message = ""
    n, m, z = 0, 0, 0

    pas = input("Enter passcode for Decryption")

    if password == pas:
        for _ in range(len(msg)):
            message += c[img[n, m, z]]
            n, m, z = n + 1, m + 1, (z + 1) % 3
        print("Decryption message", message)
    else:
        print("Not a valid key")

img = cv2.imread("aman.jpg")
msg = input("Enter secret message")
password = input("Enter password")

encrypt(img, msg)
os.system("start Encryptedmsg.jpg")

decrypt(img, password)


