class _No:
    def __init__(self, valor):
        """Cria um nó com um valor e sem próximo nó.

        Complexidade de tempo: O(1).
        """
        self.valor = valor
        self.proximo = None


class PilhaEncadeada:
    def __init__(self):
        """Inicializa uma pilha vazia.

        Complexidade de tempo: O(1).
        """
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        """Adiciona um item ao topo da pilha.

        Complexidade de tempo: O(1).
        """
        novo_no = _No(item)
        novo_no.proximo = self._topo
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        """Remove e retorna o item que está no topo da pilha.

        Complexidade de tempo: O(1).
        """
        if self.esta_vazia():
            raise IndexError("Subfluxo de pilha: Pilha vazia.")
        valor_removido = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return valor_removido

    def topo(self):
        """Retorna o item que está no topo da pilha sem removê-lo.

        Complexidade de tempo: O(1).
        """
        if self.esta_vazia():
            raise IndexError("Pilha vazia.")
        return self._topo.valor

    def esta_vazia(self):
        """Verifica se a pilha está vazia.

        Complexidade de tempo: O(1).
        """
        return self._topo is None

    def __len__(self):
        """Retorna a quantidade de elementos presentes na pilha.

        Complexidade de tempo: O(1).
        """
        return self._tamanho

    def __repr__(self):
        """Retorna uma representação dos elementos da pilha.

        Complexidade de tempo: O(n), onde n é o número de elementos
        presentes na pilha.
        """
        elementos = []
        atual = self._topo
        while atual is not None:
            elementos.append(repr(atual.valor))
            atual = atual.proximo
        return " -> ".join(elementos) if elementos else "Pilha Vazia"
