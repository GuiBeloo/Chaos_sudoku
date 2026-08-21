from typing import List, Tuple

Celula = tuple[int, int]
Clausula = List[int]
Regioes = List[List[Celula]]


def id_variavel(i: int, j: int, k: int, n:int) -> int:
    return (i-1) * n**2 + (j-1) * n + k

def ler_instancia(caminho: str):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]

    n = int(linhas[0])

    grade_regioes = []

    for i in range(1, n+1):
        grade_regioes.append(linhas[i].split())

    regioes_por_nome = {}

    for i in range(n):
        for j in range(n):
            nome_regiao = grade_regioes[i][j]

            if nome_regiao not in regioes_por_nome:
                regioes_por_nome[nome_regiao] = []

            regioes_por_nome[nome_regiao].append((i+1, j+1))  

        regioes = list(regioes_por_nome.values())

        quantidade_pistas = int(linhas[n+1])

        pistas = []

        for indice in range(n+2, n+2+quantidade_pistas):
            linhas, coluna, valor = map(int, linhas[indice].split())      
            pistas.append((linha,coluna,valor))

    return n, regioes, pistas        

if __name__ == "__main__":
    n,regioes, pistas = ler_instancia("instancias/chaos4_01.txt")

    print(f"N: {n}")
    print(f"Regiões: {regioes}")
    print(f"Pistas: {pistas}")