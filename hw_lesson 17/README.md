# Zolotov_converter_temp

Zolotov_converter_temp is a Python library, which is a universal interface 
for representing temperature in Celsius / Kelvin / Fahrenheit. 
Also, it supports value conversion temperatures between these scales.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install zolotov_converter_temp
```

## Usage

```python
from zolotov_converter_temp import ConvertTemp

# returns 86.0
ConvertTemp.kelvin_to_fahrenheit(303.15)

# returns 59.0
t1 = ConvertTemp()
t1.celsius_to_fahrenheit(15)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)