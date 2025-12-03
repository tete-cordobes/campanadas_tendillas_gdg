# Week 1: Campanadas de las Tendillas

## Historia

Las campanas de las Tendillas en Córdoba tienen diferentes periodos de sonido. Tu misión es calcular cuándo sonarán todas juntas por primera vez.

## Conceptos Clave

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

## El Reto

Implementa la clase `Campana` (o `campana` en Python) con los siguientes niveles:

### Nivel 1: Crear Campana (6 puntos)
Crea una campana con periodo y fase. Valida que:
- `periodo > 0` (si no, lanza error)
- `fase >= 0` (si no, lanza error)

### Nivel 2: ¿Suena en T? (6 puntos)
Implementa el método `suena_en(instante)` / `suenaEn(instante)` que retorna `true/false`.

### Nivel 3: MCM (6 puntos)
Implementa:
- `mcd(a, b)` - Máximo Común Divisor (Algoritmo de Euclides)
- `mcm(a, b)` - Mínimo Común Múltiplo
- `sincronizar_dos(c1, c2)` / `sincronizarDos(c1, c2)` - Primer instante donde ambas suenan

### Nivel 4: Múltiples Campanas (6 puntos)
Implementa `sincronizar_multiple(campanas)` / `sincronizarMultiple(campanas)`:
- Lista vacía → retorna -1
- Una campana → retorna su primera campanada
- Varias → aplica MCM iterativamente

### Nivel 5: Funciones Avanzadas (6 puntos)
- `contar_campanadas(campanas, hasta)` - Cuenta campanadas por campana
- `momentos_sincronizados(campanas, hasta)` - Lista momentos de sincronización

---

## Ejemplos

### Python
```python
# Nivel 1
campana = Campana(periodo=5)
assert campana.periodo == 5
assert campana.fase == 0

# Nivel 2
campana = Campana(periodo=3)
assert campana.suena_en(3) == True
assert campana.suena_en(4) == False

# Nivel 3
assert mcd(12, 8) == 4
assert mcm(3, 5) == 15
```

### Java
```java
// Nivel 1
Campana campana = new Campana(5);
assertEquals(5, campana.getPeriodo());
assertEquals(0, campana.getFase());

// Nivel 2
Campana campana = new Campana(3);
assertTrue(campana.suenaEn(3));
assertFalse(campana.suenaEn(4));

// Nivel 3
assertEquals(4, Campana.mcd(12, 8));
assertEquals(15, Campana.mcm(3, 5));
```

---

## Matemáticas Útiles

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

## Puntuación

| Puntos | Nivel |
|--------|-------|
| 0-6    | Principiante |
| 7-12   | En progreso |
| 13-18  | Buen nivel |
| 19-24  | Avanzado |
| 25-30  | ¡Maestro de las campanadas! |

**Total: 30 puntos** (2 pts por cada test)
