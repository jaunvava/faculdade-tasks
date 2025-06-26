# Tutorial Avançado: Uso de `for` e `while` em Python

## Introdução

Os laços (`loops`) são fundamentais para automação e repetição de tarefas em Python. Os dois principais tipos são `for` e `while`. Este tutorial cobre desde conceitos básicos até técnicas avançadas.

---

## 1. Laço `for`

### 1.1. Iterando sobre Sequências

```python
nomes = ["Ana", "Bruno", "Carlos"]
for nome in nomes:
    print(nome)
```

### 1.2. Usando `range()`

```python
for i in range(5):  # 0 a 4
    print(i)
for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)
```

### 1.3. Iterando sobre Dicionários

```python
d = {"a": 1, "b": 2}
for chave, valor in d.items():
    print(f"{chave}: {valor}")
```

### 1.4. List Comprehensions

```python
quadrados = [x**2 for x in range(10)]
```

### 1.5. Enumerate e Zip

```python
lista = ["a", "b", "c"]
for i, valor in enumerate(lista):
    print(i, valor)

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
for n, letra in zip(l1, l2):
    print(n, letra)
```

---

## 2. Laço `while`

### 2.1. Estrutura Básica

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### 2.2. Loops Infinitos e `break`

```python
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando == "sair":
        break
```

### 2.3. `continue` e `else`

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("Loop finalizado normalmente.")
```

---

## 3. Técnicas Avançadas

### 3.1. For Aninhado

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

### 3.2. Compreensões Aninhadas

```python
matriz = [[i*j for j in range(3)] for i in range(3)]
```

### 3.3. Iterando sobre Objetos Personalizados

```python
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.atual < self.limite:
            self.atual += 1
            return self.atual - 1
        else:
            raise StopIteration

for n in Contador(3):
    print(n)
```

---

## 4. Boas Práticas

- Prefira `for` para iterar sobre coleções.
- Use `while` para loops baseados em condição.
- Evite loops infinitos sem necessidade.
- Utilize comprehensions para criar listas, sets e dicionários de forma concisa.

---

## Referências

- [Documentação Oficial Python - for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Documentação Oficial Python - while](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)
