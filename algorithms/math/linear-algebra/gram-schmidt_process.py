# encoding: utf-8

"""
Gram-Schmidt Orthogonalization Process
Autor:
    Jørgen Pedersen Gram & Erhard Schmidt
Colaborador:
    Paulino Fonseca Veloso Junior (pfvjpoli@usp.br)
Tipo:
    math
Descrição:
    Método para ortogonalizção de um conjunto de vetores linearmente independentes(LI) de um espaço com produto interno definido.
Complexidade:  
    O(m*n²) = O(n²)
    n: numero de vezes que o processo é aplicado
    m: numero de multiplicações em cada ortogonalização
Dificuldade:
    medio
Referências: 
    [1] https://edisciplinas.usp.br/pluginfile.php/5449415/mod_resource/content/1/aula4.pdf
"""

def dot(v,u):
    m = 0
    for i in range(len(v)):
        m = m + v[i]*u[i]
    return m

def projection(v,u):
    w = dot(v,u)/(dot(u,u))
    u_new = [i * w for i in u]
    return u_new

def orthogonal(base):
    base_orth = [0]*len(base)
    base_orth[0] = base[0]
    for i in range(1,len(base)):
        base_orth[i] = base[i]      
        for j in range(i):
            base_orth[i] = [v_i - u_i for v_i, u_i in zip(base_orth[i], projection(base[i],base_orth[j]))]
    return base_orth

base=[[1.0,1.0,0.0],[2.0,2.0,3.0]]

print(orthogonal(base))

