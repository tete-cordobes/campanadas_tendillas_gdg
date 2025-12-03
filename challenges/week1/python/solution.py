"""
Campanadas de las Tendillas - Week 1

Instrucciones:
1. Implementa las funciones marcadas con "# TU CODIGO AQUI"
2. No cambies los nombres de las funciones ni la clase
3. Ejecuta los tests locales antes de hacer push

Para probar localmente:
    pytest test_campana.py -v
"""


class Campana:
    """
    Representa una campana con un periodo y una fase.
    """

    def __init__(self, periodo: int, fase: int = 0):
        """
        NIVEL 1: Crear una campana

        - Guarda el periodo y la fase como atributos
        - El periodo debe ser > 0, si no lanza ValueError
        - La fase debe ser >= 0, si no lanza ValueError
        """
        # TU CODIGO AQUI
        pass

    def suena_en(self, instante: int) -> bool:
        """
        NIVEL 2: Determina si la campana suena en un instante dado

        Una campana suena en el instante T si:
        - T > 0
        - (T - fase) >= 0
        - (T - fase) es divisible por el periodo
        """
        # TU CODIGO AQUI
        pass

    def proxima_campanada(self, desde: int = 0) -> int:
        """
        NIVEL 2 (bonus): Calcula la proxima campanada desde un instante dado
        """
        # TU CODIGO AQUI
        pass


def mcd(a: int, b: int) -> int:
    """
    NIVEL 3: Calcula el Maximo Comun Divisor usando Euclides

    Pista: mcd(a, b) = mcd(b, a % b) hasta que b sea 0
    """
    # TU CODIGO AQUI
    pass


def mcm(a: int, b: int) -> int:
    """
    NIVEL 3: Calcula el Minimo Comun Multiplo

    Formula: mcm(a,b) = (a * b) / mcd(a,b)
    """
    # TU CODIGO AQUI
    pass


def sincronizar_dos(campana1: Campana, campana2: Campana) -> int:
    """
    NIVEL 3: Encuentra el primer instante > 0 en que dos campanas suenan juntas

    CASO SIMPLE (ambas con fase=0):
        El resultado es el MCM de los periodos
    """
    # TU CODIGO AQUI
    pass


def sincronizar_multiple(campanas: list) -> int:
    """
    NIVEL 4: Encuentra el primer instante > 0 en que TODAS las campanas suenan juntas

    - Si la lista esta vacia, retorna -1
    - Si hay una sola campana, retorna su primera campanada (periodo)
    - Varias: aplicar MCM iterativamente
    """
    # TU CODIGO AQUI
    pass


def contar_campanadas(campanas: list, hasta: int) -> dict:
    """
    NIVEL 5: Cuenta cuantas veces suena cada campana hasta un instante dado

    Returns:
        Diccionario {indice: cantidad}
    """
    # TU CODIGO AQUI
    pass


def momentos_sincronizados(campanas: list, hasta: int) -> list:
    """
    NIVEL 5: Lista todos los momentos en que todas las campanas suenan juntas

    Returns:
        Lista ordenada de instantes
    """
    # TU CODIGO AQUI
    pass
