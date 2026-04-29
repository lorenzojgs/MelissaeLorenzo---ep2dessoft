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


def calcula_pontos_sequencia_alta(dados):
   
    if (1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados):
        return 30
    
    if (2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados):
        return 30
    
    return 0

# teste
def calcula_pontos_full_house(dados_rolados):
    dicio_full_house = {}

    for num in dados_rolados:
        if num in dicio_full_house:
            dicio_full_house[num] += 1
        else:
            dicio_full_house[num] = 1

    for num in range(1,7):
        if num not in dados_rolados:
            dicio_full_house[num] = 0

    valores = list(dicio_full_house.values())
    soma = 0

    if 2 in valores and 3 in valores:
        for num, valor in dicio_full_house.items():
            if valor == 2 or valor == 3:
                soma += num*valor
    return soma

def calcula_pontos_quadra(dados):
    contagem = {}

    for num in dados:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1

    for valor in contagem.values():
        if valor >= 4:
            return sum(dados)

    return 0