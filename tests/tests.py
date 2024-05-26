import os
import sys
from pathlib import Path
import pytest

# Расчёт пути к родительской директории
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parent_dir)
# Проверка наличия родительской директории в sys.path
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


from streamlit.testing.v1 import AppTest

def test_positive():
    at = AppTest.from_file(parent_dir+"/main.py").run()
    at.button[0].click().run()
    assert at.markdown[2].value == "Result: positive 0.9754959940910339"


def test_negative():
    at = AppTest.from_file(parent_dir+"/main.py").run()
    at.text_input[0].input("i hate you").run()   # Set the initial value of the text input
    at.button[0].click().run()
    assert at.markdown[2].value == 'Result: negative 0.9209097027778625'
