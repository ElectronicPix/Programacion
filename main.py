def mayusculas(f: callable):
    def envoltura(*args, **kwargs): #wapper
        resultado = f(*args, **kwargs)
        return resultado.upper()
    return envoltura

@mayusculas
def saludo():
    return "hola mundo"


print(saludo()) # HOLA MUNDO