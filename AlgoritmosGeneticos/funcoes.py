def func_obj_cb(individuo):
    """ Computa a função objetiva no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias
        
    return:
        Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo) 
