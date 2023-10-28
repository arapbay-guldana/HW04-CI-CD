import random
from typing import List
import sys

def is_prime(x: int) -> bool:
    """"Функция проверки простоты"""
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def primes(count: int) -> List[int]:
    """Функция генерации списка простых чисел"""
    prime_list = []
    num = 2
    while len(prime_list) < count:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

def checksum(x: List[int]) -> int:
    """"Функция расчёта контрольной суммы"""
    checksum_value = 0
    for num in x:
        checksum_value = ((checksum_value + num) * 113) % 10_000_007
    return checksum_value

def pipeline(initial_seed: int) -> int:
    """"Функция, которая выполняет все требуемые действия и возвращает контрольную сумму результата"""
    random.seed(100)
    prime_list = primes(1000)
    random.shuffle(prime_list)
    return checksum(prime_list)

if __name__ == "__main__":
    """"Основной блок, который печатает результат"""    
    initial_seed = int(sys.argv[1])
    result = pipeline(initial_seed)
    print(result)