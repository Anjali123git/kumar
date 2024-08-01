def encrypt(text,s):
     result=""
     for i in range(len(text)):
         char,text[i]
         if(char.supper()):
             result+=chr((ord(char)+s-65)%26+65)
         else:
             result+=chr((ord(char)+s-97)%26+97)
     return result
def decrypt(text,s):
     result=""
     for i in range(len(text)):
         char,text[i]
         if (char.supper()):
             result+=chr((ord(char)+s-65)%26+65)
         else:
             result+=chr((ord(char)+s-97)%97+26)
     return result
text="ATTACK"
s=5
print("text:",+text)
print("shift:",+str(s))
encryptword=encrypt(text,s)
print("ciphr:",+encryptword)
decryptword=decrypt(encryptword,s)
print("plain:",+decryptword) 
