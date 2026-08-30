# Chaos Sudoku SAT

Projeto da disciplina de Lógica para Ciência da Computação.

O objetivo é formalizar o problema Chaos Sudoku em Lógica Proposicional,
gerar sua formulação em formato DIMACS CNF e resolvê-la utilizando um SAT solver.

## Chaos Sudoku

O Chaos Sudoku é uma variante do Sudoku em que os blocos tradicionais são
substituídos por regiões irregulares.

Para uma grade de tamanho N x N:

- cada célula contém exatamente um valor de 1 a N;
- cada valor aparece exatamente uma vez em cada linha;
- cada valor aparece exatamente uma vez em cada coluna;
- cada valor aparece exatamente uma vez em cada região.

Cada instância possui N regiões, cada uma contendo exatamente N células.

Neste projeto, as regiões também devem ser ortogonalmente conectadas.

## Variáveis proposicionais

A variável:

`x_(i,j,k)`

representa que a célula da linha `i` e coluna `j` contém o valor `k`.

A codificação utilizada no formato DIMACS é:

`id(i,j,k) = (i - 1) * N² + (j - 1) * N + k`

Portanto, uma instância de tamanho N possui `N³` variáveis proposicionais.

## Formato das instâncias

Os arquivos de entrada possuem o seguinte formato:

```text
N
<grade N x N contendo os identificadores das regiões>
quantidade_de_pistas
linha coluna valor
...
```

Exemplo:

```text
4
A A C C
D A A C
D B B C
D D B B
3
1 1 1
2 3 4
4 2 2
```

As coordenadas das pistas são indexadas a partir de 1.

## Estrutura do projeto

- `gerador.py`: lê uma instância e gera a fórmula em DIMACS CNF;
- `decodificador.py`: reconstrói e valida a solução retornada pelo SAT solver;
- `instancias/`: arquivos de entrada utilizados nos experimentos;
- `.gitignore`: ignora arquivos temporários, CNFs e saídas do solver.

## Requisitos

- Python 3;
- CaDiCaL.

O CaDiCaL deve estar disponível no terminal através do comando:

```bash
cadical
```

## Gerando a fórmula CNF

Para gerar a fórmula de uma instância:

```bash
python3 gerador.py instancias/chaos5_01.txt > chaos5_01.cnf
```

O arquivo gerado segue o formato DIMACS CNF.

Por exemplo, para uma instância 5 x 5 sem pistas:

```text
p cnf 125 1100
```

## Executando o CaDiCaL

Execute:

```bash
cadical chaos5_01.cnf > chaos5_01.out
```

O resultado será `SATISFIABLE` caso exista uma solução e
`UNSATISFIABLE` caso a instância seja inconsistente.

## Reconstruindo a solução

Para uma instância SAT:

```bash
python3 decodificador.py chaos5_01.out instancias/chaos5_01.txt
```

O programa reconstrói a grade a partir dos literais positivos do modelo
retornado pelo CaDiCaL e verifica se a solução respeita as restrições de
linhas, colunas e regiões.

Exemplo de saída:

```text
Resultado: SAT

Solução:
5 4 3 2 1
4 3 2 1 5
3 2 1 5 4
2 1 5 4 3
1 5 4 3 2

Regiões:
A A B C C
D A B B C
D A A B C
D E E B C
D D E E E
```

Para uma instância sem solução:

```text
Resultado: UNSAT
A instância não possui solução
```

## Fluxo de execução

O fluxo completo é:

```text
arquivo de instância
        |
        v
    gerador.py
        |
        v
   arquivo CNF
        |
        v
     CaDiCaL
        |
        v
 arquivo de saída
        |
        v
 decodificador.py
        |
        v
 solução reconstruída
```

## Instâncias experimentais

Foram utilizadas instâncias de tamanhos 4 x 4 até 8 x 8, além de uma
instância 4 x 4 propositalmente inconsistente para verificar o
comportamento UNSAT da formulação.
