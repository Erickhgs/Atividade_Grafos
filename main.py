# -*- coding: utf-8 -*-
from graph import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == n):
                break
            g.M[l][c] = int(i)
            if int(i) != 0:
                g.L[l].append(c)
            
            c += 1
        l += 1
    
    return g

def main():
    # Carrega o grafo
    g = load_from("pcv177.txt")
    
    # Imprime informações básicas
    g.print()
    n = g.num_comp()
    print("Número de Componentes:", n)
    
    # Testa BFS
    print("\nTestando BFS:")
    source = 0
    D, pred = g.bfs(source)
    print(f"Distâncias a partir de {source}:", D)
    print("Predecessores:", pred)
    
    # Testa caminho com BFS
    print("\nCaminhos a partir de BFS:")
    for target in range(g.num_vertices):
        g.print_caminho(source, target, pred)
    
    # Testa DFS recursivo
    print("\nTestando DFS recursivo:")
    pred_dfs_rec = g.dfs()
    print("Predecessores DFS recursivo:", pred_dfs_rec)
    
    # Testa DFS iterativo
    print("\nTestando DFS iterativo:")
    pred_dfs_iter = g.dfs_iterativo(source)
    print("Predecessores DFS iterativo:", pred_dfs_iter)

if __name__ == "__main__":
    main()
