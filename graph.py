# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.M = [[0 for _ in range(n)] for _ in range(n)]
        self.L = [ [] for _ in range(n)]

    def print(self):
        print("Número de Vértices: " + str(self.num_vertices))
        print("Matriz de adjacência:")
        for row in self.M:
            print(row)
        print("Lista de Adjacência:")
        print(self.L)
    
    def num_comp(self):
        pred = self.dfs()
        num = 0
        for v in range(self.num_vertices):
            if(pred[v] == -1):
                num += 1
        return num
    
    def dfs(self):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        for v in range(self.num_vertices):
            if(visitados[v] == False):
                self.dfs_rec(v, visitados, pred)
                
        return pred
        
        
    def dfs_rec(self, v, visitados, pred):
        print("Vertice: " + str(v))
        visitados[v] = True
        for u in self.L[v]:
            if(visitados[u] == False):
                pred[u] = v
                self.dfs_rec(u, visitados, pred)

    def dfs_iterativo(self, start):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        stack = [start]
        visitados[start] = True

        while stack:
            v = stack.pop()
            print("Vertice: " + str(v))
            for u in reversed(self.L[v]):
                if not visitados[u]:
                    visitados[u] = True
                    pred[u] = v
                    stack.append(u)
        
        return pred
    
    def bfs(self, source):
        visitados = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        D = [-1 for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        visitados[source] = True
        D[source] = 0
        
        while(Q.empty() == False):
            v = Q.get()
            print("Vertice:" + str(v))
            for u in self.L[v]:
                if(visitados[u] == False):
                    Q.put(u)
                    visitados[u] = True
                    D[u] = D[v] + 1
                    pred[u] = v
        
        return D, pred
    
    def print_caminho(self, s, t, pred):
        if(s == t):
            print("Caminho: " + str(s))
        elif(pred[t] == -1):
            print("Não existe caminho entre " + str(s) + " e " + str(t))
        else:
            caminho = []
            atual = t
            while atual != -1:
                caminho.append(atual)
                atual = pred[atual]
            caminho.reverse()
            if caminho[0] != s:
               print("Não existe caminho entre " + str(s) + " e " + str(t))
            else:
                print("Caminho: ", end="")
                for i in caminho:
                    print(str(i) + " ", end="")
                print()