# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f"Seu resultado foi: {resultado}")
        print("oK, agora você foi decorada")

        return resultado
    return interna

def  inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)
