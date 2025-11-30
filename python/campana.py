"""
🔔 CAMPANADAS DE LAS TENDILLAS 🔔
==================================

Día 5 del Bootcamp - Reto TDD

CONTEXTO:
---------
Las campanas de las Tendillas en Córdoba tienen diferentes periodos.
Tu misión es calcular cuándo sonarán todas juntas por primera vez.

CONCEPTOS CLAVE:
----------------
- Periodo: cada cuántos segundos suena la campana
- Fase: desfase inicial en segundos (cuándo empieza a contar)
- Una campana suena en el instante T si: (T - fase) es múltiplo del periodo

EJEMPLO:
--------
Campana A: periodo=3, fase=0 → suena en: 3, 6, 9, 12, 15...
Campana B: periodo=5, fase=0 → suena en: 5, 10, 15, 20...
Primera sincronización: T=15 (MCM de 3 y 5)

NIVELES:
--------
1. Crear campana con periodo y fase
2. Determinar si suena en un instante T
3. Calcular MCM entre dos campanas
4. Sincronizar múltiples campanas
5. Casos especiales y optimización

¡Buena suerte! 🎯
"""


class Campana:
    """
    Representa una campana con un periodo y una fase.
    
    Atributos:
        periodo (int): Intervalo en segundos entre campanadas
        fase (int): Desfase inicial en segundos (default: 0)
    """
    
    def __init__(self, periodo: int, fase: int = 0):
        """
        NIVEL 1: Crear una campana
        
        TODO: Implementa el constructor
        - Guarda el periodo y la fase como atributos
        - El periodo debe ser > 0, si no lanza ValueError
        - La fase debe ser >= 0, si no lanza ValueError
        """
        # TU CÓDIGO AQUÍ
        pass
    
    def suena_en(self, instante: int) -> bool:
        """
        NIVEL 2: Determina si la campana suena en un instante dado
        
        Una campana suena en el instante T si:
        - T > 0
        - (T - fase) >= 0
        - (T - fase) es divisible por el periodo
        
        Args:
            instante: El momento en segundos a comprobar
            
        Returns:
            True si la campana suena en ese instante, False en caso contrario
            
        TODO: Implementa la lógica
        """
        # TU CÓDIGO AQUÍ
        pass
    
    def proxima_campanada(self, desde: int = 0) -> int:
        """
        NIVEL 2 (bonus): Calcula la próxima campanada desde un instante dado
        
        Args:
            desde: Instante desde el que buscar (default: 0)
            
        Returns:
            El próximo instante > desde en que suena la campana
        """
        # TU CÓDIGO AQUÍ
        pass


def mcd(a: int, b: int) -> int:
    """
    NIVEL 3: Calcula el Máximo Común Divisor usando Euclides
    
    Args:
        a, b: Dos números enteros positivos
        
    Returns:
        El MCD de a y b
        
    TODO: Implementa el algoritmo de Euclides
    Pista: mcd(a, b) = mcd(b, a % b) hasta que b sea 0
    """
    # TU CÓDIGO AQUÍ
    pass


def mcm(a: int, b: int) -> int:
    """
    NIVEL 3: Calcula el Mínimo Común Múltiplo
    
    Args:
        a, b: Dos números enteros positivos
        
    Returns:
        El MCM de a y b
        
    TODO: Implementa usando la fórmula: mcm(a,b) = (a * b) / mcd(a,b)
    """
    # TU CÓDIGO AQUÍ
    pass


def sincronizar_dos(campana1: Campana, campana2: Campana) -> int:
    """
    NIVEL 3: Encuentra el primer instante > 0 en que dos campanas suenan juntas
    
    CASO SIMPLE (ambas con fase=0):
        El resultado es el MCM de los periodos
        
    CASO CON FASES:
        Hay que resolver el sistema de congruencias:
        T ≡ fase1 (mod periodo1)
        T ≡ fase2 (mod periodo2)
        
    Args:
        campana1, campana2: Las dos campanas a sincronizar
        
    Returns:
        El primer instante > 0 en que ambas suenan, o -1 si es imposible
    """
    # TU CÓDIGO AQUÍ
    pass


def sincronizar_multiple(campanas: list) -> int:
    """
    NIVEL 4: Encuentra el primer instante > 0 en que TODAS las campanas suenan juntas
    
    Estrategia:
        1. Si la lista está vacía, retorna -1
        2. Si hay una sola campana, retorna su primera campanada
        3. Sincroniza las campanas de dos en dos iterativamente
        
    Args:
        campanas: Lista de objetos Campana
        
    Returns:
        El primer instante > 0 en que todas suenan, o -1 si es imposible
    """
    # TU CÓDIGO AQUÍ
    pass


def contar_campanadas(campanas: list, hasta: int) -> dict:
    """
    NIVEL 5: Cuenta cuántas veces suena cada campana hasta un instante dado
    
    Args:
        campanas: Lista de campanas
        hasta: Instante límite (inclusive)
        
    Returns:
        Diccionario con el índice de cada campana y su número de campanadas
        Ejemplo: {0: 5, 1: 3, 2: 10}
    """
    # TU CÓDIGO AQUÍ
    pass


def momentos_sincronizados(campanas: list, hasta: int) -> list:
    """
    NIVEL 5: Lista todos los momentos en que todas las campanas suenan juntas
    
    Args:
        campanas: Lista de campanas
        hasta: Instante límite (inclusive)
        
    Returns:
        Lista ordenada de instantes donde todas suenan simultáneamente
    """
    # TU CÓDIGO AQUÍ
    pass


# === FUNCIONES DE AYUDA (ya implementadas) ===

def visualizar_campanas(campanas: list, hasta: int = 30) -> str:
    """
    Genera una visualización ASCII de las campanadas.
    Esta función ya está implementada para ayudarte a debuggear.
    """
    if not campanas:
        return "No hay campanas"
    
    lineas = []
    lineas.append(f"Tiempo: " + "".join(f"{i:3}" for i in range(1, hasta + 1)))
    lineas.append("-" * (8 + hasta * 3))
    
    for i, c in enumerate(campanas):
        fila = f"C{i} (p={c.periodo if hasattr(c, 'periodo') else '?'}): "
        for t in range(1, hasta + 1):
            if hasattr(c, 'suena_en') and c.suena_en(t):
                fila += " 🔔"
            else:
                fila += "  ·"
        lineas.append(fila)
    
    return "\n".join(lineas)
