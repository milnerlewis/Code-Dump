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
    
def test_convert():
    assert currencyConvert("") == False
    assert currencyConvert("£1") == False
    assert currencyConvert("1") == 1.23
    assert currencyConvert(1) == 1.23
    assert currencyConvert(13.28) == 16.33