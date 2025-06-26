# Tutorial Avançado de Recursividade em Python

A recursividade é uma técnica poderosa onde uma função chama a si mesma para resolver problemas complexos de forma elegante. Este tutorial explora conceitos avançados, otimizações e exemplos práticos.

---

## 1. Conceitos Fundamentais

- **Caso Base:** Condição que encerra a recursão.
- **Chamada Recursiva:** Função chama a si mesma com um subproblema menor.

```python
def fatorial(n):
    if n == 0:
        return 1  # Caso base
    return n * fatorial(n - 1)  # Chamada recursiva
```

---

## 2. Pilha de Execução e Stack Overflow

Cada chamada recursiva adiciona um novo frame à pilha de execução. Recursão sem caso base pode causar `RecursionError`.

```python
import sys
print(sys.getrecursionlimit())  # Limite padrão: 1000
```

---

## 3. Recursão de Cauda (Tail Recursion)

Python não otimiza recursão de cauda, mas é importante conhecer:

```python
def tail_fatorial(n, acumulador=1):
    if n == 0:
        return acumulador
    return tail_fatorial(n - 1, n * acumulador)
```

---

## 4. Recursão Mútua

Funções que se chamam mutuamente.

```python
def par(n):
    if n == 0:
        return True
    return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    return par(n - 1)
```

---

## 5. Recursão em Estruturas de Dados

### 5.1. Listas Aninhadas

```python
def soma_lista(lista):
    total = 0
    for item in lista:
        if isinstance(item, list):
            total += soma_lista(item)
        else:
            total += item
    return total

print(soma_lista([1, [2, [3, 4]], 5]))  # Saída: 15
```

### 5.2. Árvores Binárias

```python
class No:
    def __init__(self, valor, esq=None, dir=None):
        self.valor = valor
        self.esq = esq
        self.dir = dir

def soma_arvore(no):
    if no is None:
        return 0
    return no.valor + soma_arvore(no.esq) + soma_arvore(no.dir)
```

---

## 6. Memoização (Otimização de Recursão)

Evita recomputação de subproblemas.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

---

## 7. Exemplos Avançados

### 7.1. Permutações

```python
def permutacoes(lista):
    if len(lista) <= 1:
        return [lista]
    resultado = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]
        for p in permutacoes(resto):
            resultado.append([lista[i]] + p)
    return resultado
```

### 7.2. Backtracking: Sudoku Solver

```python
def resolver(tabuleiro):
    for i in range(9):
        for j in range(9):
            if tabuleiro[i][j] == 0:
                for num in range(1, 10):
                    if valido(tabuleiro, i, j, num):
                        tabuleiro[i][j] = num
                        if resolver(tabuleiro):
                            return True
                        tabuleiro[i][j] = 0
                return False
    return True
```

---

## 8. Dicas e Boas Práticas

- Sempre defina um caso base claro.
- Use memoização para evitar recomputações.
- Prefira recursão para problemas naturalmente recursivos (árvores, grafos).
- Para problemas lineares, prefira loops para evitar estouro de pilha.

---

## 9. Referências

- [Documentação Oficial Python](https://docs.python.org/pt-br/3/tutorial/datastructures.html#recursion)
- [PEP 218 – Recursion](https://peps.python.org/pep-0218/)

---

A recursividade é uma ferramenta poderosa, mas deve ser usada com cuidado para garantir eficiência e legibilidade do código.
