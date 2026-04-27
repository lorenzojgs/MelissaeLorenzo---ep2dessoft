import random

def rolar_dados(quantidade):
    resultados = []

    for _ in range(quantidade):
        
        dado = random.randint(1, 6)
        resultados.append(dado)

    return resultados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
 
    dado = dados_rolados.pop(dado_para_guardar)
    

    dados_no_estoque.append(dado)
    
    
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
  
    dado = dados_no_estoque.pop(dado_para_remover)
    
   
    dados_rolados.append(dado)
    
    
    return [dados_rolados, dados_no_estoque]


def calcula_pontos_regra_simples(dados):
    pontos = {}
    
    for i in range(1, 7):
        pontos[i] = dados.count(i) * i
    
    return pontos

def calcula_pontos_soma(dados):
    soma = 0
    for valor in dados:
        soma += valor
    return soma


def calcula_pontos_sequencia_baixa(dados):
    valores = set(dados)
    if {1, 2, 3, 4}.issubset(valores) or {2, 3, 4, 5}.issubset(valores) or {3, 4, 5, 6}.issubset(valores):
        return 15
    return 0

def calcula_pontos_regra_simples(dados):
    pontos = {}
    
    for i in range(1, 7):
        pontos[i] = dados.count(i) * i
    
    return pontos

def calcula_pontos_soma(dados):
    soma = 0
    for valor in dados:
        soma += valor
    return soma

def calcula_pontos_sequencia_baixa(dados):
    sequencias = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    
    for seq in sequencias:
        encontrou = True
        for numero in seq:
            if numero not in dados:
                encontrou = False
                break
        if encontrou:
            return 15
    
    return 0


