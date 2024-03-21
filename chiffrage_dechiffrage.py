
import random
import base64


def cesar_encryption (message, offset = 1):
	encrypted_message = ""
	count=len(message)-1
	counter=0
	for char in message:
		if counter<count:
			counter+=1
			encrypted_message += chr(ord(char) + int(offset))
		
		print(encrypted_message)
	return encrypted_message

# print (cesar_encryption("I LOVE NATURE", 1)) # J!MPWF!OBUVSF

def cesar_decryption (encrypted_message, offset = 1):
    message = ""

    for char in encrypted_message:
        message += chr(ord(char) - int(offset))
    return message

# print (cesar_decryption("J!MPWF!OBUVSF", 1)) # J!MPWF!OBUVSF

#Function to encode
def encode(key, clear):
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
	return "".join(dec)
# print(encode("sdf", "Hello world")) #w5vDicOSw5_Dk8KGw6rDk8OYw5_DiA==
# print(decode("sdf", "wrvDicOSw5_Dk8KGw6rDk8OYw5_DiA==")) #Hello world