def decodificar_variavel(identificador: int, n: int) -> tuple[int,int,int]:
    identificador -=1 

    i = identificador // (n**2)
    resto = identificador % (n ** 2)

    j = resto // n
    k = resto % n

    return i+1, j+1, k+1

if __name__ == "__main__":
    print(decodificar_variavel(1,4))
    print(decodificar_variavel(5,4))
    print(decodificar_variavel(28,4))
    print(decodificar_variavel(64,4))