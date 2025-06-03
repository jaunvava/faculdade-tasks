# Guia Completo de Estudos: Manipulação de Arquivos em Python

## 1. Introdução

A manipulação de arquivos permite ler, escrever, atualizar e excluir dados armazenados em arquivos no sistema operacional. Python oferece suporte nativo para trabalhar com arquivos de texto e binários.

---

## 2. Abrindo Arquivos

```python
arquivo = open('exemplo.txt', 'r')  # modos: 'r', 'w', 'a', 'b', 'x'
```

- `'r'`: leitura (padrão)
- `'w'`: escrita (sobrescreve)
- `'a'`: acrescenta ao final
- `'b'`: modo binário
- `'x'`: cria novo arquivo

**Dica:** Use `with` para gerenciar arquivos automaticamente.

```python
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
```

---

## 3. Lendo Arquivos

- `.read()`: lê todo o conteúdo
- `.readline()`: lê uma linha
- `.readlines()`: lê todas as linhas em uma lista

```python
with open('exemplo.txt', 'r') as f:
    print(f.read())
```

---

## 4. Escrevendo em Arquivos

- `.write()`: escreve texto
- `.writelines()`: escreve lista de strings

```python
with open('exemplo.txt', 'w') as f:
    f.write('Olá, mundo!\n')
```

---

## 5. Acrescentando Dados

```python
with open('exemplo.txt', 'a') as f:
    f.write('Nova linha\n')
```

---

## 6. Trabalhando com Arquivos Binários

```python
with open('imagem.png', 'rb') as f:
    dados = f.read()
```

---

## 7. Manipulação de Arquivos com `os` e `shutil`

- Renomear: `os.rename('antigo.txt', 'novo.txt')`
- Remover: `os.remove('arquivo.txt')`
- Copiar: `shutil.copy('origem.txt', 'destino.txt')`

---

## 8. Dicas e Boas Práticas

- Sempre feche arquivos (use `with`)
- Trate exceções com `try...except`
- Prefira caminhos absolutos ou use `os.path`

---

## 9. Exemplos Práticos

### Ler e imprimir cada linha

```python
with open('exemplo.txt', 'r') as f:
    for linha in f:
        print(linha.strip())
```

### Copiar conteúdo de um arquivo para outro

```python
with open('origem.txt', 'r') as origem, open('destino.txt', 'w') as destino:
    destino.write(origem.read())
```

---

## 10. Referências

- [Documentação Oficial Python - Arquivos](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Módulo os](https://docs.python.org/pt-br/3/library/os.html)
- [Módulo shutil](https://docs.python.org/pt-br/3/library/shutil.html)
