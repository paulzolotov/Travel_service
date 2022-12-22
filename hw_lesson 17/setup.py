from setuptools import setup, find_packages
import pathlib
from os import path

HERE = pathlib.Path(__file__).parent.resolve()
long_description = (HERE / 'README.md').read_text(encoding='utf-8')
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs]
setup(name='zolotov_converter_temp',
      version='0.1',
      description='Interface for representing temperature in Celsius / Kelvin / Fahrenheit.',
      url='https://github.com/paulzolotov/TMS_hw/tree/homework/hw_lesson%2017',
      author=' Pavel Zolotov ',
      author_email='saiwa@mail.ru',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3.8, <4',
      install_requires=install_requires,
      zip_safe=False)
