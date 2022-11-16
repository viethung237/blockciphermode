
def split(plaintext):
    re_text = []
    plain_hex = ''
    block_text = []
    for i in range(len(plaintext)):
        re_text.append(hex(ord(plaintext[i])))
    for i in range(len(re_text)):
        re_text[i] = re_text[i].replace('0x', '').upper()
        plain_hex += re_text[i]
    for i in range(0, len(plain_hex), 32):
        block_text.append(plain_hex[i:i + 32])
    m = len(block_text) - 1
    n = len(block_text[m])
    if n != 32:
        block_text[m] += '8'
        for i in range(32 - n - 1):
            block_text[m] += '0'
    return block_text


