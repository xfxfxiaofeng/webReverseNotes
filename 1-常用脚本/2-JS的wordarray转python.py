# 将 JS 中的 WordArray 转换为 16 字节的 key 和 iv
def int_list_to_bytes(word_list):
    result = b''
    for word in word_list:
        result += word.to_bytes(4, byteorder='big')  # CryptoJS 是大端
    return result