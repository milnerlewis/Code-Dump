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
    
@pytest.mark.parametrize("parVal, parExp", [
    (1, 1.23),
    (0, 0),
    ("potato", False),
    ("100", 123)
])

def test_currencyConvert(parVal, parExp):
    assert currencyConvert(parVal) == parExp