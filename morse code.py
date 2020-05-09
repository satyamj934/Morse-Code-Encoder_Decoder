MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
keys=list(MORSE_CODE_DICT.keys())
values=list(MORSE_CODE_DICT.values())

def encrypt(msg):
    msg=msg.upper()
    cipher=''
    for i in msg:
        if i!=' ':
            cipher=cipher+MORSE_CODE_DICT[i]+' '
        else:
            cipher+=' '
    return cipher

def decrypt(msg):
    deciph=''
    citext=''
    
    for i in msg:
        
        if i != ' ':
            citext+=i
            n=0
        elif i==' ':
            n+=1
            if n==2:
                deciph+=' '
            else:
                deciph+=keys[values.index(citext)]
                citext=''
    return deciph

def main():
    message=input('your message : ')
    encrypt_msg=encrypt(message)
    print('your encrypted message is :',encrypt_msg)
    x=input('press 1 and enter to decrypt the same msg and 0 for your own code : ')
    if x=='1':
        f_msg=decrypt(encrypt_msg)
        
    elif x=='0':
        ciph=input('enter your code : ')
    
        f_msg=decrypt(ciph)
    print('your final message is :',f_msg)
    
    
    
       
            
            
          
    