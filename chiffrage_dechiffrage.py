
import random
import base64


def cesar_encryption (message, offset = 1):
	encrypted_message = ""
	for char in message:
		if(char.isupper()):
			newcharNumer=ord(char)+offset
			if newcharNumer> ord('Z'):
				newcharNumer = newcharNumer-26

			encrypted_message += chr(newcharNumer)
		elif(char.islower()):
			newcharNumer=ord(char)+offset
			if newcharNumer> ord('z'):
				newcharNumer = newcharNumer-26
			encrypted_message += chr(newcharNumer)
				

		# print(encrypted_message)
		else:
			if  ord(char) == 10:
				pass
			else:
				encrypted_message += char
			
	return encrypted_message

# print(cesar_encryption("I LOVE NATURE  yes", 1)) # J!MPWF!OBUVSF

def cesar_decryption (encrypted_message, offset = 1):
	message = ""
	
	for char in encrypted_message:
		if(char.isupper()):
			newcharNumer=ord(char)-offset
			if newcharNumer< ord('A'):
				newcharNumer = newcharNumer-26

			message += chr(newcharNumer)
		elif(char.islower()):
			newcharNumer=ord(char)-offset
			if newcharNumer< ord('a'):
				newcharNumer = newcharNumer-26
			message += chr(newcharNumer)

		else:
			if ord(char) == 10:
				pass
			else:
				message += char
	return message

# print (cesar_decryption("J MPWF OBUVSF", 1)) # J!MPWF!OBUVSF

#Function to encode
def encode(key, clear):
	clear = clear.replace("\n", "")
	enc = []

	for i in range(len(clear)):

		key_c = key[i % len(key)]
		enc_c = chr((ord(clear[i]) +
				ord(key_c)) % 256)

		enc.append(enc_c)

	return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode
def decode(key, enc):
	dec = []

	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(enc[i]) -
					ord(key_c)) % 256)

		dec.append(dec_c)
	return "".join(dec).replace("\n", "")
print(encode("sdf", "Hello world")) #w5vDicOSw5_Dk8KGw6rDk8OYw5_DiA==
print(decode("sdf", "wrvDicOSw5_Dk8KGw6rDk8OYw5_DiA==")) #Hello world