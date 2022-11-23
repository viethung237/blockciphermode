import aes_function
def cal(plaintext):
    plaintext = aes_function.hextobin(plaintext)
    plaintext = aes_function.bintodec(int(plaintext))
    plaintext = plaintext + 1
    plaintext = bin(plaintext).replace('0b','');
    if(len(plaintext) < 128 ):
        for i in range(128 - len(plaintext)):
            plaintext = '0' + plaintext
        return aes_function.bintohex(plaintext)
    else:
        return aes_function.bintohex(plaintext)
