class ConvertTemp:
    """
    Универсальный интерфейс по представлению температуры в шкалах
    Цельсия/Кельвина/Фаренгейта.
    Также, он поддерживает конвертацию значений
    температуры между этими шкалами.
    """
    @staticmethod
    def celsius_to_kelvin(temp: float) -> float:
        return temp + 273.15

    @staticmethod
    def kelvin_to_celsius(temp: float) -> float:
        return temp - 273.15

    @staticmethod
    def fahrenheit_to_celsius(temp: float) -> float:
        return (temp - 32) * (5 / 9)

    @staticmethod
    def celsius_to_fahrenheit(temp: float) -> float:
        return temp * (9 / 5) + 32

    @staticmethod
    def fahrenheit_to_kelvin(temp: float) -> float:
        return (temp - 32) * (5 / 9) + 273.15

    @staticmethod
    def kelvin_to_fahrenheit(temp: float) -> float:
        return (temp - 273.15) * (9 / 5) + 32
