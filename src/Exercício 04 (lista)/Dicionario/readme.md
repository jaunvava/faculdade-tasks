# Tutorial: Como Usar Dicionários em Python

Os dicionários em Python são estruturas de dados que armazenam pares de chave-valor. Eles são úteis para organizar e acessar dados de forma eficiente.

## Criando um Dicionário

```python
# Exemplo de dicionário
meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}
```

## Acessando Valores

```python
# Acessar um valor usando a chave
print(meu_dicionario["nome"])  # Saída: João
```

## Adicionando ou Atualizando Valores

```python
# Adicionar uma nova chave-valor
meu_dicionario["profissão"] = "Engenheiro"

# Atualizar um valor existente
meu_dicionario["idade"] = 26
```

## Removendo Itens

```python
# Remover um item usando a chave
del meu_dicionario["cidade"]

# Remover e retornar um valor
idade = meu_dicionario.pop("idade")
```

## Iterando sobre um Dicionário

```python
# Iterar pelas chaves
for chave in meu_dicionario:
    print(chave)

# Iterar pelos valores
for valor in meu_dicionario.values():
    print(valor)

# Iterar por chaves e valores
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
```

## Métodos Úteis

- `len(dicionario)`: Retorna o número de itens.
- `dicionario.keys()`: Retorna as chaves.
- `dicionario.values()`: Retorna os valores.
- `dicionario.items()`: Retorna pares chave-valor.

## Exemplo Completo

```python
# Criando um dicionário
contatos = {
    "João": "joao@email.com",
    "Maria": "maria@email.com"
}

# Adicionando um contato
contatos["Pedro"] = "pedro@email.com"

# Atualizando um contato
contatos["Maria"] = "maria@novoemail.com"

# Removendo um contato
del contatos["João"]

# Iterando pelos contatos
for nome, email in contatos.items():
    print(f"{nome}: {email}")
```

Com esses conceitos, você pode usar dicionários para resolver diversos problemas de forma eficiente!