import aes_function
import split_func
import aes_decrypt
with open('encrypt_data.txt','w',encoding = 'UTF-8') as plaintext, open('out_put_cipher.txt','r',encoding = 'UTF-8') as ciphertext, open('key_e.txt','r',encoding = 'UTF-8') as key :
    pt_de = ciphertext.readline()
    cipher = []
    for i in range(0,len(pt_de),32):
        cipher.append(pt_de[i:i+32])
    key = key.read().upper()
    origin_data = ''
    for i in range(len(cipher)):
        origin_data += aes_decrypt.decrypt(cipher[i],key)
    origin_data = split_func.return_text(origin_data)
    plaintext.write(origin_data)
