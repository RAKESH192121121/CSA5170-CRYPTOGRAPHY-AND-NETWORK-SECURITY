def encrypt_text(plaintext,n):
    ans =  ""
    #iterate over the given text
    for i in range(len(plaintext)):
        ch=plaintext[i]
        #check if space is there then simply add  space
        if(ch==" "):
           ans+=" "
           #check if a character is uppercase then encrypt it accordingly
        elif(ch.isupper()):
           ans+=chr((ord(ch)+n-65)%26+65)
          #check if the character is lower case then encrypt it
        else:
            ans+=chr((ord(ch)+n-97)%26+97)
    return ans
plaintext="HELLO EVERYONE"
n=1
print("plain text is : "+plaintext)
print("shift pattern is : "+str(n))
print("Ciper text is :"+encrypt_text(plaintext,n))
