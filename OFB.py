plaintext ='dai hoc bach khoa ha noi chuong trinh he thong nhung & Iot'
key = '0f1571c947d9e8590cb7add6af7f6798'
IV = '0123456789abcdeffedcba9876543210'
key = key.upper()
IV = IV.upper()
import aes_function
import split_func
plain = split_func.split(plaintext)
non_key = aes_function.encrypt(key,IV)
cipher_text = aes_function.xor_hex(non_key, plain[0])
block_text = []
block_text.append(cipher_text)
for i in range(1,len(plain)):
    non_key = aes_function.encrypt(non_key,key)
    block_text.append(aes_function.xor_hex(non_key,plain[i]))
print(block_text)