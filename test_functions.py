from task import (
    is_prime, 
    primes, 
    checksum, 
    pipeline
)

def test_is_prime():
    """"Тест первой функции для простых чисел"""
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(19) is True
    assert is_prime(97) is True
    
def test_primes():
    """"Тест для функции primes на длину генерации списка"""
    assert len(primes(1000)) == 1000
    
def test_checksum():
    """Тест на корректность расчёта контрольной суммы"""
    assert checksum([1, 2, 6, 24]) == 6012369
    
def test_pipeline():
    """"Тест на правильный конечный результат"""
    assert pipeline(100) == 7785816
    