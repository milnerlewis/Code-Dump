import pytest

def currencyConvert(value):
    try:
        float(value)
    except:
        return False
    else:
        gbp = float(value)
        usd = round((gbp * 1.23), 2)
        return usd
    
@pytest.mark.parametrize("value, expected", [
    ("", False),
    ("£1", False),
    (1, 1.23),
    (13.28, 16.33)
])

def test_convert():
    assert currencyConvert(value) == expected