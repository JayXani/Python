def firstFunction(*params):
    def secondFunction(*params):
        return f"This's a closure {params}"
    return secondFunction # Estou retornando a função e forçãndo o python guardar na memória

t = firstFunction
print(t()) # Aqui que ocorre o closure, pois é aqui que ele fecha a execução do meu código
