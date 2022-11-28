import aes_function
import split_func
with open('input_e.txt','r',encoding = 'UTF-8') as plaintext, open('out_put_cipher.txt','w',encoding = 'UTF-8') as ciphertext, open('key_e.txt','r',encoding = 'UTF-8') as key :
    pt = plaintext.readlines()
    key = key.read().upper()
    string = ''
    for line in pt :
        string += line
    in_plain = []
    in_plain = split_func.split(string)
    out_plain = ''
    for i in range(len(in_plain)):
        out_plain += aes_function.encrypt(in_plain[i], key)
    ciphertext.write(out_plain)


