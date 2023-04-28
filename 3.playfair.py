def decrypt():
    #enter your encrypted message(string) below
    encrypted_message=input("enter the message to be decrypted:").strip()
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #enter the key value
    k=int(input("enter the key to decrypt;"))
    decrypted_message=""
    for ch in encrypted_message:
        if ch in letters:
            position=letters.find(ch)
            new=(position-k)%26
            new_char=letters[new]
            decrypted_message+=new_char
        else:
            decrypted_message+=ch
    print(decrypted_message)
decrypt()
