#! /usr/local/bin/python3

'''
Декодировать в строку байтовое значение b'r\xc3\xa9sum\xc3\xa9'
Затем результат преобразовать в байтовый вид в кодировке «uft-8» и затем результат снова
декодировать в строку с применением кодировки «utf-16». Результаты каждой операции с пояснениями выводить на печать
'''


b_str = b'r\xc3\xa9sum\xc3\xa9'
print(f'Current string - {b_str}')
decode_str = b_str.decode()
print(f'Decode string - {decode_str}')
utf8_b_str = decode_str.encode('utf-8')
print(f'Encode bytes string to utf-8 - {utf8_b_str}')
utf16_str = b_str.decode('utf-16')
print(f'Decode string to utf-16 - {utf16_str}')
