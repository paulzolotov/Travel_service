from dataclasses import dataclass


@dataclass
class InvalidIntDivision(Exception):
    """Исключение, генерирующееся в том случае, если
        число, при добавлении в очередь, не делится на 8 без остатка"""
    message: str
    type: str = 'InvalidIntDivision'

    def __str__(self):
        return f"{self.type} -> {self.message}"


@dataclass
class InvalidIntNumberCount(Exception):
    """Исключение, генерирующееся в том случае, если
        число, при добавлении в очередь, являющийся целым числом,
        имеет больше 4 символов"""
    message: str
    type: str = 'InvalidIntNumberCount'

    def __str__(self):
        return f"{self.type} -> {self.message}"


@dataclass
class InvalidFloat(Exception):
    """Исключение, генерирующееся в том случае, если
       число, при добавлении в очередь, имеет более 3 символов после запятой"""
    message: str
    type: str = 'InvalidFloat'

    def __str__(self):
        return f"{self.type} -> {self.message}"


@dataclass
class InvalidTextLength(Exception):
    """Исключение, генерирующееся в том случае, если
        строка, при добавлении в очередь, имеет длину более 4 символов """
    message: str
    type: str = 'InvalidTextLength'

    def __str__(self):
        return f"{self.type} -> {self.message}"


@dataclass
class DuplicatesInText(Exception):
    """Исключение, генерирующееся в том случае, если
        строка, при добавлении в очередь, имеет дублирующие символы"""
    message: str
    type: str = 'DuplicatesInText'

    def __str__(self):
        return f"{self.type} -> {self.message}"
