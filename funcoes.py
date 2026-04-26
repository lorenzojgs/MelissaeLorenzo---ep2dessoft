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
    return sum(dados)
