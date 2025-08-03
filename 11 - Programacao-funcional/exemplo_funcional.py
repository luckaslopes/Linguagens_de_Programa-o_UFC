def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro não negativo usando recursão.

    Args:
        n: O número inteiro não negativo para o qual calcular o fatorial.

    Returns:
        O fatorial de n.

    Raises:
        ValueError: Se n for um número inteiro negativo.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fatorial é definido apenas para números inteiros não negativos.")
    if n == 0:
        return 1  
    else:
        return n * fatorial(n - 1)  
def calcular_fatoriais_para_lista(numeros: list[int]) -> list[int]:
    """
    Calcula os fatoriais para uma lista de números usando uma função de alta ordem (map).

    Args:
        numeros: Uma lista de números inteiros não negativos.

    Returns:
        Uma lista contendo os fatoriais dos números de entrada.
    """
    return list(map(fatorial, numeros))

if __name__ == "__main__":
    print("--- Cálculo de Fatorial Funcional ---")

    numero_para_calcular = 5
    try:
        resultado = fatorial(numero_para_calcular)
        print(f"O fatorial de {numero_para_calcular} é: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")

    print("\n--- Calculando Fatoriais para uma Lista ---")

    lista_de_numeros = [0, 1, 4, 6, 3]
    print(f"Lista original de números: {lista_de_numeros}")
    try:
        lista_de_fatoriais = calcular_fatoriais_para_lista(lista_de_numeros)
        print(f"Fatoriais da lista: {lista_de_fatoriais}")
    except ValueError as e:
        print(f"Erro: {e}")

    print("\n--- Exemplo de Tratamento de Erro ---")
    numero_negativo = -2
    try:
        fatorial(numero_negativo)
    except ValueError as e:
        print(f"Tentando calcular o fatorial de {numero_negativo}: {e}")

    invalid_type = 2.5
    try:
        fatorial(invalid_type)
    except ValueError as e:
        print(f"Tentando calcular o fatorial de {invalid_type}: {e}")