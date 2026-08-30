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
    maior_identificador = n ** 3

    for literal in literais:
        if literal <= 0:
            continue

        if literal > maior_identificador:
            raise ValueError(
                f"Literal inválido no modelo: {literal}. "
                f"O maior identificador permitido é {maior_identificador}"
            )

        linha, coluna, valor = decodificar_variavel(literal, n)

        valor_atual = grade[linha - 1][coluna - 1]

        if valor_atual != 0 and valor_atual != valor:
            raise ValueError(
                f"A célula ({linha}, {coluna}) recebeu mais de um valor no modelo"
            )

        grade[linha - 1][coluna - 1] = valor

    return grade

def validar_solucao(
    grade: list[list[int]],
    grade_regioes: list[list[str]],
    n: int
) -> None:
    valores_esperados = set(range(1, n + 1))

    for indice, linha in enumerate(grade, start=1):
        if set(linha) != valores_esperados:
            raise ValueError(
                f"A linha {indice} não contém exatamente os valores de 1 a {n}"
            )

    for coluna in range(n):
        valores_coluna = {grade[linha][coluna] for linha in range(n)}

        if valores_coluna != valores_esperados:
            raise ValueError(
                f"A coluna {coluna + 1} não contém exatamente os valores de 1 a {n}"
            )

    valores_regioes = {}

    for linha in range(n):
        if len(grade_regioes[linha]) != n:
            raise ValueError(
                f"A linha {linha + 1} da grade de regiões é inválida"
            )

        for coluna in range(n):
            regiao = grade_regioes[linha][coluna]

            if regiao not in valores_regioes:
                valores_regioes[regiao] = []

            valores_regioes[regiao].append(grade[linha][coluna])

    if len(valores_regioes) != n:
        raise ValueError(
            f"A instância deveria possuir exatamente {n} regiões"
        )

    for regiao, valores in valores_regioes.items():
        if len(valores) != n or set(valores) != valores_esperados:
            raise ValueError(
                f"A região {regiao} não contém exatamente os valores de 1 a {n}"
            )


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

def ler_resultado(caminho: str) -> str:
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("s "):
                resultado = linha.split()[1]

                if resultado == "SATISFIABLE":
                    return "SAT"

                if resultado == "UNSATISFIABLE":
                    return "UNSAT"
    raise ValueError("O arquivo não contém um resultado válido do Cadical")

def main() -> None:

    parser = argparse.ArgumentParser(description="Reoconstrói a solução de um Chaos sudoku a partir do modelo do Cadical")

    parser.add_argument("resultado", help ="Arquivo contendo a saída do CadicaL")

    parser.add_argument("instancia",help="Arquivo contendo a instância do Chaos Sudoku")

    argumentos = parser.parse_args()

    resultado = ler_resultado(argumentos.resultado)

    if resultado == "UNSAT":
        print("Resultado: UNSAT")
        print("A instância não possui solução")
        return

    n, grade_regioes = ler_instancia(argumentos.instancia)

    literais = ler_modelo(argumentos.resultado)

    grade = reconstruir_grade(literais, n)

    validar_solucao(grade, grade_regioes, n)

    print("Resultado: SAT")

    exibir_grade(grade)
    exibir_regioes(grade_regioes)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, IndexError) as erro:
        raise SystemExit(f"Erro: {erro}")