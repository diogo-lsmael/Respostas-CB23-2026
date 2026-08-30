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

        try:
            algoritmo(copia)
        except RecursionError:
            return None

        fim = time.perf_counter()

        soma += fim - inicio

    return soma / repeticoes


def benchmark(tamanhos, repeticoes):
    print()
    print("=" * 70)
    print("             BENCHMARK DE ALGORITMOS DE ORDENACAO")
    print("=" * 70)
    print(f"Repeticoes por teste: {repeticoes}")
    print()

    print(
        f"{'Algoritmo':<20}"
        f"{'N':>8}"
        f"{'Cenario':>15}"
        f"{'Tempo (s)':>15}"
    )

    print("-" * 70)

    for nome, algoritmo in algoritmos.items():

        for n in tamanhos:

            # Caso medio
            lista = caso_medio(n)
            tempo = medir_tempo(algoritmo, lista, repeticoes)

            if tempo is None:
                print(
                    f"{nome:<20}"
                    f"{n:>8}"
                    f"{'Caso Medio':>15}"
                    f"{'RecursionError':>15}"
                )
            else:
                print(
                    f"{nome:<20}"
                    f"{n:>8}"
                    f"{'Caso Medio':>15}"
                    f"{tempo:>15.8f}"
                )

            # Pior caso
            lista = pior_caso(nome, n)
            tempo = medir_tempo(algoritmo, lista, repeticoes)

            if tempo is None:
                print(
                    f"{nome:<20}"
                    f"{n:>8}"
                    f"{'Pior Caso':>15}"
                    f"{'RecursionError':>15}"
                )
            else:
                print(
                    f"{nome:<20}"
                    f"{n:>8}"
                    f"{'Pior Caso':>15}"
                    f"{tempo:>15.8f}"
                )

        print("-" * 70)

    print()


tamanhos = [100, 500, 1000, 5000]
repeticoes = 10

benchmark(tamanhos, repeticoes)
