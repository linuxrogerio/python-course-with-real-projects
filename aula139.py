# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        retorno = super(MinhaString, self).upper()
        print('DEPOIS DO UPPER')
        return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A(object):
    atributo_a = 'Valor A'

    def __init__(self, atributo):
        self.atributo = atributo
        

    def metodo(self):
        print('A')

class B(A):
    atributo_b = "Valor B"

    def __init__(self, atributo):
        super().__init__(atributo)
        ...

    def metodo(self):
        print('B')

class C(B):
    atributo_c = "Valor C"

    def metodo(self):
        # super().metodo() # B
        # super(B, self).metodo() # A
        # super(A, self).metodo() # object
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C()
print(c.atributo)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
