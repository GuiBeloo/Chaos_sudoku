from typing import List, Tuple

Celula = tuple[int, int]
Clausula = List[int]
Regioes = List[List[Celula]]
Pista = Tuple[int, int, int]
Pistas = List[Pista]

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
            pistas.append(( linha, coluna, valor))

    return n, regioes, pistas        

def validar_instancia(n: int, regioes: Regioes, pistas: Pistas) -> None:
    if n <= 0:
        raise ValueError("O tamanho N deve ser maior que zero.")
    if len(regioes) != n:
        raise ValueError(f"A instancia deve possuir exatamente {n} regiões")

    celulas_encontradas = set()

    for indice,regiao in enumerate(regioes, start=1):
        if len(regiao) != n:
            raise ValueError(f"A região {indice} deve possuir exatamente {n} células")

        for linha, coluna in regiao:
            if not(1 <= linha <= n and 1<= coluna <= n):
                raise ValueError(f"Célula ({linha}, {coluna}) fora dos limites da grade")
            if(linha, coluna) in celulas_encontradas:
                raise ValueError(f"A célula ({linha}, {coluna}) aparece em mais de uma região.")
            celulas_encontradas.add((linha,coluna))

    if len(celulas_encontradas) != n**2:
        raise ValueError("Nem todas as células da grade pertencem a uma região")

    for linha, coluna, valor in pistas:
        if not(1 <= linha <= n and 1 <= coluna <= n and 1 <= valor <= n):
            raise ValueError(f"Pista inválida: ({linha}, {coluna}, {valor})")

def gerar_clausulas_celulas(n:int) -> List[Clausula]:

    clausulas = []

    for i in range(1, n+1):
        for j in range(1, n+1):
            clausula = []
            for k in range(1, n+1):
                clausula.append(id_variavel(i,j,k,n))
            clausulas.append(clausula)

            for k in range(1, n+1):
                for l in range(k+1, n+1):
                    clausulas.append([-id_variavel(i,j,k,n), -id_variavel(i,j,l,n)])    
    return clausulas

def gerar_clausulas_linhas(n: int) -> List[Clausula]:
    clausulas = []

    for i in range (1, n+1):
        for k in range(1, n+1):
            clausula = []
            for j in range(1, n+1):
                clausula.append(id_variavel(i,j,k,n))

            clausulas.append(clausula)

            for j in range(1,n+1):
                for l in range(j+1, n+1):
                    clausulas.append([-id_variavel(i,j,k,n),-id_variavel(i,l,k,n)])
    return clausulas

def gerar_clausulas_colunas(n:int) -> List[Clausula]:
    clausulas = []

    for j in range (1, n+1):
        for k in range(1, n+1):
            clausula = []
            for i in range(1, n+1):
                clausula.append(id_variavel(i,j,k,n))

            clausulas.append(clausula)

            for i in range(1,n+1):
                for l in range(j+1, n+1):
                    clausulas.append([-id_variavel(i,j,k,n),-id_variavel(l,j,k,n)])
    return clausulas

def gerar_clausulas_regioes(n: int, regioes: Regioes) -> List[Clausula]:

    clausulas = []

    for regiao in regioes:
        for k in range(1, n+1):
            clausula = []

            for linha,coluna in regiao:
                clausula.append(id_variavel(linha,coluna,k,n))

            clausulas.append(clausula)

            for a in range(len(regiao)):
                for b in range(a+1, len(regiao)):
                    linha1, coluna1 = regiao[a]
                    linha2, coluna2 = regiao[b]

                    clausulas.append([-id_variavel(linha1,coluna1,k, n),-id_variavel(linha2,coluna2,k, n)])

    return clausulas

if __name__ == "__main__":
    n,regioes, pistas = ler_instancia("instancias/chaos4_01.txt")

    validar_instancia(n, regioes, pistas)

    clausulas_celulas = gerar_clausulas_celulas(n)
    clausulas_linhas = gerar_clausulas_linhas(n)
    clausulas_colunas = gerar_clausulas_colunas(n)
    clausulas_regioes = gerar_clausulas_regioes(n, regioes)

    print("Células:", len(clausulas_celulas))
    print("Linhas:", len(clausulas_linhas))
    print("Colunas:", len(clausulas_colunas))
    print("Regiões:", len(clausulas_regioes))

    total = (
        len(clausulas_celulas)
        + len(clausulas_linhas)
        + len(clausulas_colunas)
        + len(clausulas_regioes)
    )

    print("Total:", total)