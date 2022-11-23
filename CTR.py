plaintext ='dai hoc bach khoa ha noi chuong trinh he thong nhung & Iot'
key = '0f1571c947d9e8590cb7add6af7f6798'
Counter = '0123456789abcdeffedcba9876543210'
key = key.upper()
Counter = Counter.upper()
import aes_function
import split_func
import generate_ctr
block_text = []
plain = split_func.split(plaintext)
for i in range(len(plain)):
    pre_text = aes_function.encrypt(Counter,key)
    block_text.append(aes_function.xor_hex(plain[i],pre_text))
    Counter = generate_ctr.cal(Counter)

print(block_text)