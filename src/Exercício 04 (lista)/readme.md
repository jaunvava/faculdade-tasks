# O tipo de dado lista tem ainda mais métodos. Aqui estão apresentados todos os métodos de objetos do tipo lista:

- list.append(x)
Adiciona um item ao fim da lista. Similar a a[len(a):] = [x].

- list.extend(iterable)
Estende a lista, adicionando no fim todos os elementos do argumento iterável passado como parâmetro. Similar a a[len(a):] = iterable.

- list.insert(i, x)
Insere um item em uma dada posição. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim a.insert(0, x) insere um elemento na frente da lista e a.insert(len(a), x) e equivale a a.append(x).

- list.remove(x)
Remove o primeiro item encontrado na lista cujo valor é igual a x. Se não existir valor igual, uma exceção ValueError é levantada.

- list.pop([i])
Remove o item na posição fornecida na lista e retorna. Se nenhum índice for especificado, a.pop() remove e retorna o último item da lista. Levanta um IndexError se a lista estiver vazia ou o índice estiver fora do intervalo da lista.

- list.clear()
Remove todos os itens de uma lista. Similar a del a[:].

- list.index(x[, start[, end]])
Devolve o índice base-zero do primeiro item cujo valor é igual a x, levantando ValueError se este valor não existe.

- Os argumentos opcionais start e end são interpretados como nas notações de fatiamento e são usados para limitar a busca para uma subsequência específica da lista. O índice retornado é calculado relativo ao começo da sequência inteira e não referente ao argumento start.

- list.count(x)
Devolve o número de vezes em que x aparece na lista.

- list.sort(*, key=None, reverse=False)
Ordena os itens na lista (os argumentos podem ser usados para personalizar a ordenação, veja a função sorted() para maiores explicações).

- list.reverse()
Inverte a ordem dos elementos na lista.

- list.copy()
Devolve uma cópia rasa da lista. Similar a a[:].