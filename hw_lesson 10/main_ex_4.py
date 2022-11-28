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
        self.dict_encode = {'A': 'C', 'B': 'R', 'C': 'Y', 'D': 'P', 'E': 'T', 'F': 'O', 'G': 'A', 'H': 'B', 'I': 'D',
                            'J': 'E', 'K': 'F', 'L': 'G', 'M': 'H', 'N': 'I', 'O': 'J', 'P': 'K', 'Q': 'L', 'R': 'M',
                            'S': 'N', 'T': 'Q', 'U': 'S', 'V': 'U', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Z', ' ': ' '}
        self.dict_decode = {'C': 'A', 'R': 'B', 'Y': 'C', 'P': 'D', 'T': 'E', 'O': 'F', 'A': 'G', 'B': 'H', 'D': 'I',
                            'E': 'J', 'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R',
                            'N': 'S', 'Q': 'T', 'S': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Z': 'Z', ' ': ' '}

    def _process(self, some_str: str, mapping_dict: dict):
        """Общий 'скелет' выполняемых действий для функций encode и decode"""
        res = []
        for i in some_str.upper():
            res.append(mapping_dict[i])
        return res

    def encode(self, some_str: str):
        return self._process(some_str, self.dict_encode)

    def decode(self, some_str: str):
        return self._process(some_str, self.dict_decode)


cipher = Cipher()
print(''.join(cipher.encode("Hello world")).capitalize())  # Btggj vjmgp
print(''.join(cipher.decode("Fjedhc dn atidsn")).capitalize())  # Kojima is genius
