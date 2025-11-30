# 🔔 Campanadas de las Tendillas

## Día 5 - Reto TDD

Las campanas de las Tendillas en Córdoba tienen diferentes periodos de sonido. Tu misión es calcular cuándo sonarán todas juntas por primera vez.

---

## 📋 Conceptos Clave

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| **Periodo** | Cada cuántos segundos suena | periodo=3 → suena cada 3s |
| **Fase** | Desfase inicial | fase=2 → empieza en t=2 |
| **MCM** | Mínimo Común Múltiplo | MCM(3,5)=15 |

### ¿Cuándo suena una campana?

Una campana suena en el instante T si:
```
T > 0
(T - fase) >= 0
(T - fase) es divisible por periodo
```

**Ejemplo:**
- Campana A: periodo=3, fase=0 → suena en: 3, 6, 9, 12, **15**, 18...
- Campana B: periodo=5, fase=0 → suena en: 5, 10, **15**, 20...
- Primera sincronización: **T=15**

---

## 🎯 Niveles del Reto

| Nivel | Objetivo | Puntos |
|-------|----------|--------|
| 1 | Crear campana con periodo y fase | 6 pts |
| 2 | Calcular si suena en instante T | 6 pts |
| 3 | MCM entre dos campanas | 6 pts |
| 4 | Sincronizar múltiples campanas | 6 pts |
| 5 | Casos edge y optimización | 6 pts |

**Total: 30 puntos** (2 pts por cada test)

---

## 🚀 Cómo Empezar

### Versión Python

#### 1. Abre el archivo `python/campana.py`

Encontrarás funciones con `# TU CÓDIGO AQUÍ`. Esa es tu zona de trabajo.

#### 2. Ejecuta los tests

```bash
cd python

# Todos los tests
pytest test_campana.py -v

# Solo un nivel específico
pytest test_campana.py -v -k "nivel1"
pytest test_campana.py -v -k "nivel2"

# Ver puntuación detallada
python calcular_puntos.py
```

### Versión Java

#### 1. Abre el archivo `java/src/main/java/com/gdg/campanadas/Campana.java`

Encontrarás métodos con `// TU CÓDIGO AQUÍ`. Esa es tu zona de trabajo.

#### 2. Ejecuta los tests

```bash
cd java

# Con Maven
mvn test

# Solo un nivel específico
mvn test -Dtest=Nivel1Test
mvn test -Dtest=Nivel2Test
```

---

## 📖 Guía por Nivel

### Nivel 1: Crear Campana

**Python:**
```python
def __init__(self, periodo: int, fase: int = 0):
    # Guardar atributos
    # Validar: periodo > 0, fase >= 0
    # Si no cumple, lanzar ValueError
```

**Java:**
```java
public Campana(int periodo, int fase) {
    // Guardar atributos
    // Validar: periodo > 0, fase >= 0
    // Si no cumple, lanzar IllegalArgumentException
}
```

### Nivel 2: ¿Suena en T?

**Python:**
```python
def suena_en(self, instante: int) -> bool:
    # T debe ser > 0
    # (T - fase) debe ser >= 0
    # (T - fase) % periodo == 0
```

**Java:**
```java
public boolean suenaEn(int instante) {
    // T debe ser > 0
    // (T - fase) debe ser >= 0
    // (T - fase) % periodo == 0
}
```

### Nivel 3: MCM

**Python:**
```python
def mcd(a, b):
    # Algoritmo de Euclides
    # while b: a, b = b, a % b
    # return a

def mcm(a, b):
    # mcm = (a * b) / mcd(a, b)
```

**Java:**
```java
public static int mcd(int a, int b) {
    // Algoritmo de Euclides
    // while (b != 0) { int temp = b; b = a % b; a = temp; }
    // return a;
}

public static int mcm(int a, int b) {
    // mcm = (a * b) / mcd(a, b)
}
```

### Nivel 4: Múltiples Campanas

**Python:**
```python
def sincronizar_multiple(campanas):
    # Lista vacía → -1
    # Una campana → su primera campanada
    # Varias → aplicar MCM iterativamente
```

**Java:**
```java
public static int sincronizarMultiple(List<Campana> campanas) {
    // Lista vacía → -1
    // Una campana → su primera campanada
    // Varias → aplicar MCM iterativamente
}
```

### Nivel 5: Funciones Extra
- Contar cuántas veces suena cada campana
- Listar todos los momentos de sincronización

---

## 💡 Tips

1. **Lee bien los comentarios** en los archivos de código
2. **Un test a la vez**: no intentes pasar todos de golpe
3. **El MCM es la clave**: si entiendes MCM, el resto fluye
4. **Usa las funciones de visualización** para debuggear (Python)

---

## 🧮 Matemáticas Útiles

### Algoritmo de Euclides (MCD)
```
MCD(48, 18):
48 = 18 × 2 + 12
18 = 12 × 1 + 6
12 = 6 × 2 + 0
→ MCD = 6
```

### Fórmula del MCM
```
MCM(a, b) = (a × b) / MCD(a, b)
MCM(12, 8) = (12 × 8) / 4 = 24
```

---

## 🏆 Evaluación

```
0-6 pts   → 🌱 Principiante
7-12 pts  → 💪 En progreso  
13-18 pts → 👍 Buen nivel
19-24 pts → ⭐ Avanzado
25-30 pts → 🎉 ¡Maestro de las campanadas!
```

---

¡Buena suerte! 🔔
