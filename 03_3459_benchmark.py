import random
import time

from AP_03_ordenacao import selection_sort, divide_and_conquer_sort, quick_sort


algoritmos = {
    "Selection Sort": selection_sort,
    "Merge Sort": divide_and_conquer_sort,
    "Quick Sort": quick_sort
}


def caso_medio(n):
    lista = []

    for i in range(n):
        lista.append(random.randint(-1000000, 1000000))

    return lista


def pior_caso(nome, n):
    if nome == "Quick Sort":
        return list(range(n))

    return list(range(n, 0, -1))


def medir_tempo(algoritmo, lista, repeticoes):
    soma = 0

    for i in range(repeticoes):
        copia = lista.copy()

        inicio = time.perf_counter()
        algoritmo(copia)
        fim = time.perf_counter()

        soma += fim - inicio

    return soma / repeticoes


def benchmark(tamanhos, repeticoes):
    print()
    print("=" * 65)
    print("        BENCHMARK DE ALGORITMOS DE ORDENACAO")
    print("=" * 65)
    print(f"Repeticoes por teste: {repeticoes}")
    print()

    print(f"{'Algoritmo':<20} {'N':>8} {'Cenario':>15} {'Tempo (s)':>15}")
    print("-" * 65)

    for nome in algoritmos:
        algoritmo = algoritmos[nome]

        for n in tamanhos:
            lista = caso_medio(n)
            tempo = medir_tempo(algoritmo, lista, repeticoes)

            print(
                f"{nome:<20} {n:>8} "
                f"{'Caso Medio':>15} {tempo:>15.8f}"
            )

            lista = pior_caso(nome, n)
            tempo = medir_tempo(algoritmo, lista, repeticoes)

            print(
                f"{nome:<20} {n:>8} "
                f"{'Pior Caso':>15} {tempo:>15.8f}"
            )

    print("-" * 65)
    print()


tamanhos = [100, 500, 1000, 5000]
repeticoes = 50

benchmark(tamanhos, repeticoes)