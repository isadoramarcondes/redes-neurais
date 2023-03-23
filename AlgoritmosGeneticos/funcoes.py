import random

def gene_cb():
    """ Gera um gene válido para o problema das caixas binárias
    Return
        Um valor zero ou um,.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    
    return gene

def gene_nb(valor_max_caixa):
    """ Gera um gene válido para o problema das caixas não-binárias
    
    Args:
        valor_max_caixa: valor maximo que a caixa pode assumir
    
    Return
        Um valor de 0 a 'valor_maximo_caixa' (incluso).
    """
    gene = random.randint(0, valor_max_caixa)
    
    return gene

def individuo_cb(n):
    """ Gera um indivíduo para o problema das caixas binárias
    
    Args.:
        n: número de genes do indivíduo.
    
    return
        Uma lista com n genes. Cada gene é um valor zero ou um
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo

def individuo_nb(numero_genes, valor_max_caixa):
    """Gera um individuo válido para o problema das caixas não binárias
    Args:
        numero_genes: número de genes na lista que representa o individuo
        valor_max_caixa: Valor máximo que a caixa pode assumir
    Returns:
        Uma lista que representa um individuo válido para o problema das caixas não binárias
    """
    individuo =[]
    for _ in range(numero_genes):
        gene = gene_nb(valor_max_caixa)
        individuo.append(gene)
    return individuo

def populacao_cb(tamanho, n):
    """ Cria uma população no problema das caixas binárias.
    Args:
        tamanho: tamanho da população
        n: número de genes
    
    Returns:
        Uma lista onde cada item é um individuo. Um individuo é uma lista com n genes
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao

def populacao_nb(tamanho_pop, numero_genes,valor_max_caixa):
    """Cria uma poulação de individuos para o problema das caixas não binárias
    Args:
        tamanho_pop: número de individuos da população
        numero_genes: número de genes do individuo
        valor_max_caixa: valor máximo que a caixa pode ter
    Return:
        Uma lista onde cada item representa um individuo
    """
    populacao = []
    for _ in range(tamanho_pop):
        individuo = individuo_nb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    return populacao

def selecao_roleta_max(populacao, fitness):
    """Seleciona individuos de uma população usando o método da roleta.
    Nota: apenas funciona para problemas de maximização.
    Args:
        população: lista com todos os individuos da população
        fitness: valor da função objetivo dos individuos da população
    Return:
        população dos individuos seleciolados
    """
    populacao_selecionada = random.choices(populacao, weights = fitness, k=len(populacao))
    return populacao_selecionada

def cruzamento_ponto_simples(mae,pai):
    """operador que só corta em  um ponto a lista
    
    Args:
        pai: uma lista representando um individuo
        mãe: uma lista representando um individuo
    
    Return:
        Duas listas, sendo que cada uma representa um filho dos paos que foram os argumentos.
    """
    ponto_de_corte = random.randint(1, len(mae)-1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2
    
def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias
    Args:
        individuo: uma lista representando um individuo no problema das caixas binárias
    Return:
        Um individuo com gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    
    return individuo
def mutacao_nb(individuo,valor_max_caixa):
    """Realiza a mutação do individuo
    Args:
        individo: individuo que deve sofrer a mutação
        valor_max_caixa: valor máximo que a caixa pode assumir 
    Return:
        indviduo que sofreu a mutação
    """
    gene_a_ser_mutado=random.randint(0,len(individuo)-1)
    individuo[gene_a_ser_mutado]= gene_nb(valor_max_caixa)
    return individuo

def func_obj_cb(individuo):
    """ Computa a função objetiva no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias
        
    return:
        Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo) 

def func_obj_nb(individuo):
    """Calcula o fitness do individuo para o problema das caixas não binárias
    Args:
        individuo: lista que representa um individuo dentro do problema das caixas não binárias
        
    Return:
        Um valor que representa o fitness do individuo
    """
    fitness = sum(individuo)
    return fitness

def func_obj_pop_cb(populacao):
    """Calcula a funcao objetivo para todos membros de uma população
    
    Args:
        população: lista com todos os individuos da população
        
    Return:
        Lista de valores representando a fitness de cada individuo da população
    """
    fitness = []
    for individuo in populacao:
        fobj = func_obj_cb(individuo)
        fitness.append(fobj)
    return fitness

def func_obj_pop_nb(populacao):
    """Calcula o fitness da população completa
    Args:
        populacao:lista com todos os individuos em ordem
    """
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = func_obj_nb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop