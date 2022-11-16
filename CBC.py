plaintext ='dai hoc bach khoa ha noi chuong trinh he thong nhung & Iot'
key = '0f1571c947d9e8590cb7add6af7f6798'
IV = '0123456789abcdeffedcba9876543210'
key = key.upper()
IV = IV.upper()
import aes_function
import split_func
plain = []
cipher =[]
plain = split_func.split(plaintext)
print(plain)
pre_text = aes_function.xor_hex(plain[0],IV)
print(pre_text)
cbc_text  = aes_function.encrypt(pre_text,key)
cipher.append(cbc_text)
for i in range(1,len(plain)):
    input_text = aes_function.xor(cbc_text,plain[i])
    output_text = aes_function.encrypt(input_text,key)
    cipher.append(output_text)
    cbc_tex = output_text
print(cipher)


