import re
import random

def get_digit(cpf: str) -> int:
    len_cpf = len(cpf) + 1
    
    multiplic = []
    for cpf_index,multiplicacao in enumerate(range(len_cpf,1,-1)):
        multiplic.append(int(cpf[cpf_index]) * multiplicacao )
    total_sum = sum(multiplic)
    digit = 11 - (total_sum % 11)
    return digit if digit <= 9 else 0
def get_digit_one(cpf: str) -> int:
    return get_digit(cpf[:9])

def get_digit_two(cpf: str) -> int:
    return get_digit(cpf[:10])

#limpar cpf
def remove_not_number(cpf: str) -> str:
    return re.sub(r'\D','',cpf)

#checar se o valor tem 11 caracteres
def character_count(value: str) -> bool:
    return len(value) == 11

#chega se é uma sequencia  
def is_sequence(value: str) -> bool:
    return value[0] * len(value) == value
     
def validate(cpf: str) -> bool:
    clean_cpf = remove_not_number(cpf)

    if not character_count(clean_cpf):
       return False

    if is_sequence(clean_cpf):
      return False

    digit_one = get_digit_one(clean_cpf)
    digit_two = get_digit_two(clean_cpf)

    new_cpf = f'{clean_cpf[:9]}{digit_one}{digit_two}'

    if new_cpf == clean_cpf:
        return True
    return False
def generate() -> str:
    nine_digits =''.join([str(random.randint(0,9)) for x in range(9)])
    digit_one = get_digit_one(nine_digits)
    digit_two = get_digit_two(f'{nine_digits}{digit_one}')
    new_cpf = f'{nine_digits}{digit_one}{digit_two}'
    return new_cpf
def formater(cpf: str)-> str:
    return  f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9: ]}'
