msg="UDZ WKLV VLGH"
#encryptrd message
Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for key in range(len(Letters)):
    translated=''
    for ch in msg:
        if ch in Letters:
            num=Letters.find(ch)
            num=num-key
            if num<0:
                num=num+len(Letters)
            translated=translated+Letters[num]
        else:
            translated=translated+ch
    print('Hackinig key is %s: %s'%(key,translated))
