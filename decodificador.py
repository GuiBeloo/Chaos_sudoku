import argparse

def decodificar_variavel(identificador: int, n: int) -> tuple[int,int,int]:
    identificador -=1 

    i = identificador // (n**2)
    resto = identificador % (n ** 2)

    j = resto // n
    k = resto % n

    return i+1, j+1, k+1

def ler_modelo(caminho: str) -> list[int]:
    literais = []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("v "):
                valores = linha.split()[1:]

                for valor in valores:
                    literal = int(valor)

                    if literal != 0: 
                        literais.append(literal)
    return literais   

def reconstruir_grade(literais: list[int], n: int) -> list[list[int]]:
    grade = [[0 for _ in range(n)] for _ in range(n)]

    for literal in literais:
        if literal > 0:
            linha, coluna, valor = decodificar_variavel(literal, n)

            grade[linha - 1][coluna - 1] = valor
    return grade

def exibir_grade(grade: list[list[int]]) -> None: 
    for linha in grade:
        print(" ".join(map(str, linha)))

def ler_instancia(caminho: str) -> tuple[int, list[list[str]]]:

    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]

    n = int(linhas[0])
    grade_regioes = []

    for i in range(1, n+1):
        grade_regioes.append(linhas[i].split())
    return n, grade_regioes

def exibir_regioes(grade_regioes: list[list[str]]) -> None:
    print("\nRegiões:")

    for linha in grade_regioes:
        print(" ".join(linha))

def exibir_grade(grade: list[list[int]]) -> None:
    print("Solução:")

    for linha in grade:
        print(" ".join(map(str,linha)))

def main() -> None:

    parser = argparse.ArgumentParser(description="Reoconstrói a solução de um Chaos sudoku a partir do modelo do Cadical")

    parser.add_argument("resultado", help ="Arquivo contendo a saída do CadicaL")

    parser.add_argument("instancia",help="Arquivo contendo a instância do Chaos Sudoku")

    argumentos = parser.parse_args()

    n, grade_regioes = ler_instancia(argumentos.instancia)

    literais = ler_modelo(argumentos.resultado)

    grade = reconstruir_grade(literais, n)

    exibir_grade(grade)
    exibir_regioes(grade_regioes)


if __name__ == "__main__":
    main()