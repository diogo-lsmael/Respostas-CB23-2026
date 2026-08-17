# python 3

import argparse
import random
import statistics
import sys
import time

from AP_03_ordenacao import (
    selection_sort,
    divide_and_conquer_sort,
    quick_sort,
)


# Algoritmos que serão avaliados
ALGORITMOS = {
    "Selection Sort": selection_sort,
    "Merge Sort": divide_and_conquer_sort,
    "Quick Sort": quick_sort,
}


def gerar_caso_medio(n):
    return [random.randint(-10**6, 10**6) for _ in range(n)]


def gerar_pior_caso(nome_algoritmo, n):

    if nome_algoritmo == "Quick Sort":
        return list(range(n))

    return list(range(n, 0, -1))


def medir_tempo_medio(algoritmo, dados, repeticoes):

    tempos = []

    for _ in range(repeticoes):
        copia = dados.copy()

        inicio = time.perf_counter()

        algoritmo(copia)

        fim = time.perf_counter()

        tempos.append(fim - inicio)

    return statistics.mean(tempos)


def executar_benchmark(tamanhos, repeticoes):

    print("=" * 72)
    print(f"{'BENCHMARK DE ALGORITMOS DE ORDENAÇÃO':^72}")
    print(f"{repeticoes} REPETIÇÕES POR TESTE".center(72))
    print("=" * 72)

    print(
        f"{'Algoritmo':<20}"
        f"{'N':>8}"
        f"{'Cenário':>16}"
        f"{'Tempo Médio (s)':>22}"
    )

    print("-" * 72)

    for nome, algoritmo in ALGORITMOS.items():

        for n in tamanhos:
            dados_medio = gerar_caso_medio(n)

            tempo_medio = medir_tempo_medio(
                algoritmo,
                dados_medio,
                repeticoes
            )

            print(
                f"{nome:<20}"
                f"{n:>8}"
                f"{'Caso Médio':>16}"
                f"{tempo_medio:>22.8f}"
            )

            # -------------------------
            # PIOR CASO
            # -------------------------
            dados_pior = gerar_pior_caso(nome, n)

            tempo_pior = medir_tempo_medio(
                algoritmo,
                dados_pior,
                repeticoes
            )

            print(
                f"{nome:<20}"
                f"{n:>8}"
                f"{'Pior Caso':>16}"
                f"{tempo_pior:>22.8f}"
            )


def ler_argumentos():

    parser = argparse.ArgumentParser(
        description="Benchmark de algoritmos de ordenação."
    )

    parser.add_argument(
        "-n",
        "--tamanhos",
        nargs="+",
        type=int,
        default=[100, 500, 1000, 5000],
        help="Tamanhos das entradas. "
             "Padrão: 100 500 1000 5000"
    )

    parser.add_argument(
        "-k",
        "--repeticoes",
        type=int,
        default=50,
        help="Número de repetições. Padrão: 50"
    )

    return parser.parse_args()


if __name__ == "__main__":

    args = ler_argumentos()
    sys.setrecursionlimit(
        max(10000, max(args.tamanhos) * 2 + 100)
    )

    executar_benchmark(
        args.tamanhos,
        args.repeticoes
    )