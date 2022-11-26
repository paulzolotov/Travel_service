"""
4* Реализовать кодирование и декодирование ключевых слов для латинского алфавита согласно
указанному соответствию (маппингу).
Шифр (используйте данное соответствие букв при решении задания)
* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
Пример:
cipher = Cipher()
cipher.encode("Hello world")
"Btggj vjmgp"

cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
"""


class Cipher:

    def __init__(self):
        self.list_mapping = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ ', 'CRYPTOABDEFGHIJKLMNQSUVWXZ ']

    def encode(self, some_str: str):
        res = []
        for i in some_str.upper():
            ind = self.list_mapping[0].find(i)
            res.append(self.list_mapping[1][ind])
        print(''.join(res).capitalize())

    def decode(self, some_str: str):
        res = []
        for i in some_str.upper():
            ind = self.list_mapping[1].find(i)
            res.append(self.list_mapping[0][ind])
        print(''.join(res).capitalize())


cipher = Cipher()
cipher.encode("Hello world")  # Btggj vjmgp
cipher.decode("Fjedhc dn atidsn")  # Kojima is genius