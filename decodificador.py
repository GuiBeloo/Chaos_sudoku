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

def main() -> None:

    parser = argparse.ArgumentParser(description="Reoconstrói a solução de um Chaos sudoku a partir do modelo do Cadical")

    parser.add_argument("resultado", help ="Arquivo contendo a saida do Cadical")

    parser.add_argument("n", type=int, help="Tamanho N da grade")

    argumentos = parser.parse_args()

    literais = ler_modelo(argumentos.resultado)

    grade = reconstruir_grade(literais, argumentos.n)

    exibir_grade(grade)

if __name__ == "__main__":
    main()