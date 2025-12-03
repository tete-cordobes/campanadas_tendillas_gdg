# Week 1: Solución - Campanadas de las Tendillas

> **NOTA:** Este archivo contiene pistas y la solución completa. Solo consultar si estás atascado.

---

## Pistas por Nivel

### Nivel 1: Crear Campana

<details>
<summary>Pista 1</summary>

Guarda `periodo` y `fase` como atributos de la clase.

</details>

<details>
<summary>Pista 2</summary>

Usa `ValueError` (Python) o `IllegalArgumentException` (Java) para validaciones.

</details>

### Nivel 2: ¿Suena en T?

<details>
<summary>Pista 1</summary>

Primero verifica que `T > 0`, luego que `(T - fase) >= 0`.

</details>

<details>
<summary>Pista 2</summary>

Usa el operador módulo: `(T - fase) % periodo == 0`

</details>

### Nivel 3: MCM

<details>
<summary>Pista 1 - MCD</summary>

Algoritmo de Euclides:
```
mientras b != 0:
    temp = b
    b = a % b
    a = temp
retorna a
```

</details>

<details>
<summary>Pista 2 - MCM</summary>

`MCM(a, b) = (a * b) / MCD(a, b)`

</details>

### Nivel 4: Múltiples Campanas

<details>
<summary>Pista</summary>

Aplica MCM iterativamente:
```
resultado = periodo de primera campana
para cada campana restante:
    resultado = mcm(resultado, campana.periodo)
```

</details>

### Nivel 5: Funciones Avanzadas

<details>
<summary>Pista - Contar campanadas</summary>

Para una campana con fase=0: `cantidad = hasta // periodo`
Con fase: cuenta desde la primera campanada.

</details>

---

## Solución Completa

### Python

<details>
<summary>Ver solución Python</summary>

```python
class Campana:
    def __init__(self, periodo: int, fase: int = 0):
        if periodo <= 0:
            raise ValueError("El periodo debe ser > 0")
        if fase < 0:
            raise ValueError("La fase debe ser >= 0")
        self.periodo = periodo
        self.fase = fase

    def suena_en(self, instante: int) -> bool:
        if instante <= 0:
            return False
        diff = instante - self.fase
        return diff >= 0 and diff % self.periodo == 0

    def proxima_campanada(self, desde: int = 0) -> int:
        if desde < self.fase:
            return self.fase if self.fase > 0 else self.periodo
        diff = desde - self.fase
        campanadas_pasadas = diff // self.periodo
        return self.fase + (campanadas_pasadas + 1) * self.periodo


def mcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def mcm(a: int, b: int) -> int:
    return (a * b) // mcd(a, b)


def sincronizar_dos(campana1: Campana, campana2: Campana) -> int:
    # Caso simple: ambas con fase 0
    if campana1.fase == 0 and campana2.fase == 0:
        return mcm(campana1.periodo, campana2.periodo)

    # Caso con fases: buscar iterativamente
    mcm_periodos = mcm(campana1.periodo, campana2.periodo)
    for t in range(1, mcm_periodos * max(campana1.periodo, campana2.periodo) + 1):
        if campana1.suena_en(t) and campana2.suena_en(t):
            return t
    return -1


def sincronizar_multiple(campanas: list) -> int:
    if not campanas:
        return -1
    if len(campanas) == 1:
        return campanas[0].proxima_campanada(0) if hasattr(campanas[0], 'proxima_campanada') else campanas[0].periodo

    # Caso simple: todas con fase 0
    if all(c.fase == 0 for c in campanas):
        resultado = campanas[0].periodo
        for c in campanas[1:]:
            resultado = mcm(resultado, c.periodo)
        return resultado

    # Caso con fases
    resultado = sincronizar_dos(campanas[0], campanas[1])
    for c in campanas[2:]:
        temp = Campana(resultado, 0)
        resultado = sincronizar_dos(temp, c)
    return resultado


def contar_campanadas(campanas: list, hasta: int) -> dict:
    resultado = {}
    for i, c in enumerate(campanas):
        count = 0
        for t in range(1, hasta + 1):
            if c.suena_en(t):
                count += 1
        resultado[i] = count
    return resultado


def momentos_sincronizados(campanas: list, hasta: int) -> list:
    if not campanas:
        return []

    momentos = []
    for t in range(1, hasta + 1):
        if all(c.suena_en(t) for c in campanas):
            momentos.append(t)
    return momentos
```

</details>

### Java

<details>
<summary>Ver solución Java</summary>

```java
public class Campana {
    private int periodo;
    private int fase;

    public Campana(int periodo, int fase) {
        if (periodo <= 0) {
            throw new IllegalArgumentException("El periodo debe ser > 0");
        }
        if (fase < 0) {
            throw new IllegalArgumentException("La fase debe ser >= 0");
        }
        this.periodo = periodo;
        this.fase = fase;
    }

    public Campana(int periodo) {
        this(periodo, 0);
    }

    public int getPeriodo() { return periodo; }
    public int getFase() { return fase; }

    public boolean suenaEn(int instante) {
        if (instante <= 0) return false;
        int diff = instante - fase;
        return diff >= 0 && diff % periodo == 0;
    }

    public int proximaCampanada(int desde) {
        if (desde < fase) {
            return fase > 0 ? fase : periodo;
        }
        int diff = desde - fase;
        int campanadasPasadas = diff / periodo;
        return fase + (campanadasPasadas + 1) * periodo;
    }

    public int proximaCampanada() {
        return proximaCampanada(0);
    }

    public static int mcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static int mcm(int a, int b) {
        return (a * b) / mcd(a, b);
    }

    public static int sincronizarDos(Campana c1, Campana c2) {
        if (c1.fase == 0 && c2.fase == 0) {
            return mcm(c1.periodo, c2.periodo);
        }
        int mcmPeriodos = mcm(c1.periodo, c2.periodo);
        for (int t = 1; t <= mcmPeriodos * Math.max(c1.periodo, c2.periodo); t++) {
            if (c1.suenaEn(t) && c2.suenaEn(t)) {
                return t;
            }
        }
        return -1;
    }

    public static int sincronizarMultiple(List<Campana> campanas) {
        if (campanas == null || campanas.isEmpty()) return -1;
        if (campanas.size() == 1) return campanas.get(0).periodo;

        boolean todasFaseCero = campanas.stream().allMatch(c -> c.fase == 0);
        if (todasFaseCero) {
            int resultado = campanas.get(0).periodo;
            for (int i = 1; i < campanas.size(); i++) {
                resultado = mcm(resultado, campanas.get(i).periodo);
            }
            return resultado;
        }

        int resultado = sincronizarDos(campanas.get(0), campanas.get(1));
        for (int i = 2; i < campanas.size(); i++) {
            Campana temp = new Campana(resultado, 0);
            resultado = sincronizarDos(temp, campanas.get(i));
        }
        return resultado;
    }

    public static Map<Integer, Integer> contarCampanadas(List<Campana> campanas, int hasta) {
        Map<Integer, Integer> resultado = new HashMap<>();
        for (int i = 0; i < campanas.size(); i++) {
            int count = 0;
            for (int t = 1; t <= hasta; t++) {
                if (campanas.get(i).suenaEn(t)) count++;
            }
            resultado.put(i, count);
        }
        return resultado;
    }

    public static List<Integer> momentosSincronizados(List<Campana> campanas, int hasta) {
        List<Integer> momentos = new ArrayList<>();
        if (campanas == null || campanas.isEmpty()) return momentos;

        for (int t = 1; t <= hasta; t++) {
            boolean todasSuenan = true;
            for (Campana c : campanas) {
                if (!c.suenaEn(t)) {
                    todasSuenan = false;
                    break;
                }
            }
            if (todasSuenan) momentos.add(t);
        }
        return momentos;
    }
}
```

</details>

---

## Tests Privados (Ejemplo)

Los tests privados que se ejecutan en el workflow son similares a:

```json
[
  {"periodo": 3, "fase": 0, "instante": 9, "expected_suena": true},
  {"periodo": 5, "fase": 2, "instante": 7, "expected_suena": true},
  {"periodo": 4, "fase": 1, "instante": 6, "expected_suena": false},
  {"mcd_a": 24, "mcd_b": 36, "expected_mcd": 12},
  {"mcm_a": 6, "mcm_b": 8, "expected_mcm": 24}
]
```
