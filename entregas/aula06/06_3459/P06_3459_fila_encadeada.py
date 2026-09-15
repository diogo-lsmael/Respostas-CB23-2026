from P06_3459_pilha_encadeada import PilhaEncadeada


class FilaEncadeada:
    def __init__(self):
        """Inicializa uma fila vazia usando duas pilhas.

        Complexidade de tempo: O(1).
        """
        self.pilha_entrada = PilhaEncadeada()
        self.pilha_saida = PilhaEncadeada()

    def enfileirar(self, item):
        """Adiciona um item ao final da fila.

        Complexidade de tempo: O(1).
        """
        self.pilha_entrada.push(item)

    def _transferir_se_necessario(self):
        """Transfere os elementos da pilha de entrada para a pilha de saída
        quando a pilha de saída está vazia.

        Complexidade de tempo: O(n), onde n é o número de elementos
        transferidos.
        """
        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

    def desenfileirar(self):
        """Remove e retorna o primeiro item da fila.

        Complexidade de tempo: O(n) no pior caso, devido à transferência
        dos elementos entre as pilhas.
        """
        if self.esta_vazia():
            raise IndexError("Subfluxo de fila: Fila vazia.")
        self._transferir_se_necessario()
        return self.pilha_saida.pop()

    def frente(self):
        """Retorna o primeiro item da fila sem removê-lo.

        Complexidade de tempo: O(n) no pior caso, devido à transferência
        dos elementos entre as pilhas.
        """
        if self.esta_vazia():
            raise IndexError("Fila vazia.")
        self._transferir_se_necessario()
        return self.pilha_saida.topo()

    def esta_vazia(self):
        """Verifica se a fila está vazia.

        Complexidade de tempo: O(1).
        """
        return self.pilha_entrada.esta_vazia() and self.pilha_saida.esta_vazia()

    def __len__(self):
        """Retorna a quantidade de elementos presentes na fila.

        Complexidade de tempo: O(1).
        """
        return len(self.pilha_entrada) + len(self.pilha_saida)

    def __repr__(self):
        """Retorna uma representação dos elementos da fila.

        Complexidade de tempo: O(n), onde n é o número de elementos
        presentes na fila.
        """
        if self.esta_vazia():
            return "Fila Vazia"
        
        elementos = []
        atual = self.pilha_saida._topo
        while atual is not None:
            elementos.append(repr(atual.valor))
            atual = atual.proximo
            
        elementos_entrada = []
        atual = self.pilha_entrada._topo
        while atual is not None:
            elementos_entrada.append(repr(atual.valor))
            atual = atual.proximo
        elementos.extend(reversed(elementos_entrada))
        
        return " <- ".join(elementos)
