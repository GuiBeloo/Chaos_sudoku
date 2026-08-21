from typing import List, Tuple

Celula = tuple[int, int]
Clausula = List[int]
Regioes = List[List[Celula]]


def id_variavel(i: int, j: int, k: int, n:int) -> int:
    return (i-1) * n**2 + (j-1) * n + k