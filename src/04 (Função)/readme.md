# Tutorial Completo: Uso de Funções em Python

## O que é uma Função?
Uma função é um bloco de código reutilizável que realiza uma tarefa específica. Em Python, funções ajudam a organizar o código, tornando-o mais legível e modular.

---

## Criando uma Função
Para definir uma função, usamos a palavra-chave `def`:

```python
def saudacao():
    print("Olá, mundo!")
```

### Chamando a Função
Para executar a função, basta chamá-la pelo nome:

```python
saudacao()
```

---

## Parâmetros e Argumentos
Funções podem receber dados de entrada chamados **parâmetros**.

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

### Chamando com Argumentos
```python
saudacao("João")
```

---

## Retornando Valores
Funções podem retornar valores usando a palavra-chave `return`.

```python
def soma(a, b):
    return a + b
```

### Usando o Retorno
```python
resultado = soma(3, 5)
print(resultado)  # Saída: 8
```

---

## Tipos de Parâmetros
1. **Parâmetros Padrão**:
   ```python
   def saudacao(nome="Visitante"):
       print(f"Olá, {nome}!")
   ```

2. **Parâmetros Nomeados**:
   ```python
   def exibir_dados(nome, idade):
       print(f"Nome: {nome}, Idade: {idade}")
   exibir_dados(idade=25, nome="Ana")
   ```

3. **Parâmetros Variáveis**:
   ```python
   def listar_itens(*itens):
       for item in itens:
           print(item)
   listar_itens("Maçã", "Banana", "Laranja")
   ```

---

## Funções Lambda
Funções anônimas ou **lambda** são úteis para operações simples.

```python
dobro = lambda x: x * 2
print(dobro(4))  # Saída: 8
```

---

## Boas Práticas
- Use nomes descritivos para funções e parâmetros.
- Documente suas funções com **docstrings**:
  ```python
  def soma(a, b):
      """Retorna a soma de dois números."""
      return a + b
  ```

- Mantenha funções curtas e focadas em uma única tarefa.

---

## Conclusão
Funções são fundamentais para escrever código limpo e eficiente.
