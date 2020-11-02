import re
import random
from program import cpfutil

if __name__ == "__main__":
    cpf = cpfutil.generate()
    cpf_formatado = cpfutil.formater(cpf)
    print(cpf,cpf_formatado) 