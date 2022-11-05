#!/usr/bin/python
# Python program to encrypt a string
import string
alphabates = string.ascii_lowercase
alphabates = "abcdefghijklmnopqrstuvwxyz"

def encrypt(string, shift = 4):
	encrypted_string = ""
	for c in string:
		index = alphabates.index(c)
		shifted_index = (index + shift) % len(alphabates)
		encrypted_string += alphabates[shifted_index]
	return encrypted_string
print(encrypt("ranjitswain"))
