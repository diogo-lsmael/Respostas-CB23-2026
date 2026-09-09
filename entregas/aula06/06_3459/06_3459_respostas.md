# Aula 06 — Análise de complexidade

## 1. TAD e estrutura de dados

Um TAD (Tipo Abstrato de Dados) define quais operações podem ser realizadas sobre os dados e qual é o comportamento esperado dessas operações.

A estrutura de dados é a forma utilizada para implementar esse TAD.

Por exemplo, uma pilha pode ser definida como um TAD com operações como `push`, `pop` e `topo`. Neste trabalho, a pilha foi implementada utilizando uma lista simplesmente encadeada.

## 2. Pilha encadeada

A pilha possui um ponteiro para o topo e um contador com a quantidade de elementos.

### `push`

A inserção é feita diretamente no início da lista encadeada.

Complexidade: **O(1)**.

### `pop`

O primeiro nó é removido e o topo passa a apontar para o próximo nó.

Complexidade: **O(1)**.

### `topo`

O elemento do topo é acessado diretamente pelo ponteiro `_topo`.

Complexidade: **O(1)**.

### `esta_vazia`

A operação verifica se o tamanho da pilha é igual a zero.

Complexidade: **O(1)**.

### `len`

O tamanho é mantido em um contador atualizado a cada inserção ou remoção.

Complexidade: **O(1)**.

### `repr`

Para construir a representação da pilha, é necessário percorrer os nós.

Se houver N elementos, são visitados N nós.

Complexidade: **O(N)**.

## 3. Fila utilizando duas pilhas

A fila foi implementada utilizando duas instâncias de `PilhaEncadeada`.

A primeira pilha é utilizada para receber os novos elementos. A segunda é utilizada para fornecer os elementos na ordem correta da fila.

Quando a pilha de saída está vazia, os elementos da pilha de entrada são transferidos para ela.

Por exemplo, depois de inserir:

`1, 2, 3`

a pilha de entrada possui os elementos na ordem inversa de acesso. Ao transferi-los para a pilha de saída, a ordem passa a ser:

`1, 2, 3`

Assim, o primeiro elemento inserido fica no topo da pilha de saída.

## 4. Complexidade da fila

### `enfileirar`

O elemento é colocado diretamente na pilha de entrada.

Complexidade: **O(1)**.

### `desenfileirar`

Se a pilha de saída não estiver vazia, basta retirar seu topo, o que custa O(1).

Se estiver vazia, pode ser necessário transferir elementos da pilha de entrada para a pilha de saída.

Uma transferência de N elementos custa O(N), mas cada elemento é transferido no máximo uma vez de uma pilha para a outra antes de ser removido.

Por isso, considerando uma sequência de operações, o custo amortizado de `desenfileirar` é **O(1)**.

### `frente`

O comportamento é semelhante ao de `desenfileirar`.

Quando a pilha de saída está vazia, pode ocorrer uma transferência de elementos. Depois disso, o primeiro elemento está no topo da pilha de saída.

Complexidade amortizada: **O(1)**.

### `esta_vazia`

A fila está vazia quando as duas pilhas estão vazias.

Complexidade: **O(1)**.

### `len`

O tamanho da fila é obtido somando os tamanhos das duas pilhas.

Complexidade: **O(1)**.

### `repr`

Para construir a representação da fila, é necessário percorrer os elementos.

Complexidade: **O(N)**.

## 5. Complexidade amortizada

A transferência entre as duas pilhas pode custar O(N) em uma operação específica.

Entretanto, cada elemento é transferido da pilha de entrada para a pilha de saída no máximo uma vez antes de ser removido.

Portanto, considerando várias operações, o custo total das transferências é proporcional ao número de elementos processados.

Assim, o custo amortizado das operações `desenfileirar` e `frente` é **O(1)**.
