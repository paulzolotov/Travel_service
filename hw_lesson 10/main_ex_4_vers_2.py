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

    def _process(self, some_str: str, a: int, b: int):
        """Общий 'скелет' выполняемых действий для функций encode и decode"""
        res = []
        for i in some_str.upper():
            ind = self.list_mapping[a].find(i)
            res.append(self.list_mapping[b][ind])
        return res

    def encode(self, some_str: str):
        return self._process(some_str, 0, 1)

    def decode(self, some_str: str):
        return self._process(some_str, 1, 0)


cipher = Cipher()
print(''.join(cipher.encode("Hello world") ).capitalize())  # Btggj vjmgp
print(''.join(cipher.decode("Fjedhc dn atidsn")).capitalize())  # Kojima is genius
