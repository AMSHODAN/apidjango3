import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
        cpf = CPF()
        return  cpf.validate(numero_do_cpf)

def nome_valido(nome):
        return nome.isalpha()

def rg_valido(rg):
        return len(rg) == 9

def cel_valido(celular):
        '''Valido = 11 12345-1234'''
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo, celular)
        return resposta
            


