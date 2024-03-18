from tkinter import *
import random
import base64


def cesar_encryption (message, offset = 1):
    encrypted_message = ""

    for char in message:
        encrypted_message += chr(ord(char) + offset)
    return encrypted_message

print (cesar_encryption("I LOVE NATURE", 1)) # J!MPWF!OBUVSF

def cesar_decryption (encrypted_message, offset = 1):
    message = ""

    for char in encrypted_message:
        message += chr(ord(char) - offset)
    return message

print (cesar_decryption("J!MPWF!OBUVSF", 1)) # J!MPWF!OBUVSF

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

# alphabet_initial_codage_cesar={
# 1:"a",  2:"b",  3:"c",
# 4:"d",  5:"e",  6:"f",
# 7:"g",  8:"h",  9:"i",
# 10:"j", 11:"k", 12:"l",
# 13:"m", 14:"n", 15:"o",
# 16:"p", 17:"q", 18:"r",
# 19:"s", 20:"t", 21:"u",
# 22:"v", 23:"w", 24:"x",
# 25:"y", 26:"z", 27:" ",
# 28:".", 29:",", 30:"!",
# 31:"?", 32:"'", 33:"-",
# 34:";", 35:"(", 36:")"
# }

# def codage(shift, plainText, encrypted):
#     step = int(shift)
#     message_initial = plainText
 
#     alphabet_code_codage_cesar={
# "a":(1+step)%26,    "b":(2+step)%26,    "c":(3+step)%26,
# "d":(4+step)%26,    "e":(5+step)%26,    "f":(6+step)%26,
# "g":(7+step)%26,    "h":(8+step)%26,    "i":(9+step)%26,
# "j":(10+step)%26,   "k":(11+step)%26,   "l":(12+step)%26,
# "m":(13+step)%26,   "n":(14+step)%26,   "o":(15+step)%26,
# "p":(16+step)%26,   "q":(17+step)%26,   "r":(18+step)%26,
# "s":(19+step)%26,   "t":(20+step)%26,   "u":(21+step)%26,
# "v":(22+step)%26,   "w":(23+step)%26,   "x":(24+step)%26,
# "y":(25+step)%26,   "z":(26+step)%26,   " ":27,
# ".":28,             ",":29,             "!":30,
# "?":31,             "'":32,             "-":33,
# ";":34,             "(":35,             ")":36
#     }
 
#     message_liste=list(message_initial.strip())
#     message_intermediaire=[]
 
#     for i in message_liste :
#         for k in (alphabet_initial_codage_cesar):
#             if(alphabet_initial_codage_cesar[k]) == i: message_intermediaire.append(k)
 
#     message_final_l=[]
 
#     for i in message_intermediaire :
#         for k in (alphabet_code_codage_cesar):
#             if(alphabet_code_codage_cesar[k]) == i: message_final_l.append(k)
 
#     message_final="".join(message_final_l)
 
#     encrypted.delete(1.0, END)
#     encrypted.insert(1.0,message_final)
 
# WIDTH=450
# HEIGHT=150
 
# main_win = Tk()
# main_win.title('Codage de César')
# main_win.geometry(str(WIDTH)+'x'+str(HEIGHT)+'+300+100')
 
# #Saisie du décalage d'alphabet
# decalage_t = Label(main_win, text='Décalage à partir du "a" (entre 0 et 25)')
# decalage_t.place(x = 10,y = 10)
 
# decalage_v = Entry(main_win, width = 5)
# decalage_v.place(x = 230,y = 10)
# decalage_v.focus()
 
# #Saisie du message à coder
# a_coder_t = Label(main_win, text='Message à coder')
# a_coder_t.place(x = 10,y = 40)
 
# a_coder_v = Entry(main_win, width = 35)
# a_coder_v.place(x = 230,y = 40)
# a_coder_v.focus()
 
# #Codage
# code_b = Button(main_win, text='Coder', width = 20, justify = 'left', command=codage)
# code_b.place(x = 10,y = 70)
 
# code = Entry(main_win, width = 35)
# code.place(x = 230, y = 70)
 
# main_win.mainloop()