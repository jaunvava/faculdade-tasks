# Tutorial: Uso de Conjuntos em Python

Os conjuntos (`set`) em Python são coleções não ordenadas de elementos únicos. Eles são úteis para operações como união, interseção e diferença.

## Criando um Conjunto

Você pode criar um conjunto usando a função `set()` ou com chaves `{}`:

```python
# Criando conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = set([3, 4, 5, 6])

print(conjunto1)  # Saída: {1, 2, 3, 4}
print(conjunto2)  # Saída: {3, 4, 5, 6}
```

## Operações Básicas

### Adicionar e Remover Elementos

```python
conjunto = {1, 2, 3}
conjunto.add(4)  # Adiciona o elemento 4
conjunto.remove(2)  # Remove o elemento 2

print(conjunto)  # Saída: {1, 3, 4}
```

### União, Interseção e Diferença

```python
a = {1, 2, 3}
b = {3, 4, 5}

# União
print(a | b)  # Saída: {1, 2, 3, 4, 5}

# Interseção
print(a & b)  # Saída: {3}

# Diferença
print(a - b)  # Saída: {1, 2}
```

### Verificar Pertinência

```python
conjunto = {1, 2, 3}
print(2 in conjunto)  # Saída: True
print(4 in conjunto)  # Saída: False
```

## Conjuntos Imutáveis

Python também possui conjuntos imutáveis chamados `frozenset`:

```python
imutavel = frozenset([1, 2, 3])
print(imutavel)  # Saída: frozenset({1, 2, 3})
```

## Conclusão

Os conjuntos são uma ferramenta poderosa para manipular coleções de dados únicos. Experimente usá-los para simplificar operações que envolvem elementos distintos!
