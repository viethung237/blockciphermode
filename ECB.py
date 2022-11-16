plaintext ='dai hoc bach khoa ha noi'
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()
import aes_function
import split_func

in_plain = []
in_plain = split_func.split(plaintext)
print(in_plain)
out_plain = []
for i in range(len(in_plain)):
    out_plain.append(aes_function.encrypt(in_plain[i],key))
print(out_plain)


