# GDG Advent Challenges

Repositorio oficial de retos semanales de programacion del GDG.

## Estructura del Repositorio

```
├── .github/
│   └── workflows/
│       └── tests_challenge_week1.yml
├── README.md
└── challenges/
    └── week1/
        ├── challenge.md          # Descripcion del reto
        ├── solution.md           # Pistas y solucion (spoiler!)
        ├── python/
        │   └── solution.py       # Plantilla Python
        └── java/
            └── solution.java     # Plantilla Java
```

---

## Como Participar

### 1. Crea tu rama

Desde la rama `main`, crea tu propia rama siguiendo el formato:

```bash
git checkout main
git pull origin main
git checkout -b tu_usuario_week1_solution
```

**Formato del nombre:** `username_weekX_solution`

Ejemplos:
- `jgarcia_week1_solution`
- `maria_week1_solution`

### 2. Implementa tu solucion

1. Ve a la carpeta del lenguaje que prefieras:
   - Python: `challenges/week1/python/solution.py`
   - Java: `challenges/week1/java/solution.java`

2. Lee el reto en `challenges/week1/challenge.md`

3. Implementa las funciones marcadas con `# TU CODIGO AQUI` o `// TU CODIGO AQUI`

4. **NO cambies los nombres de las funciones ni la clase**

### 3. Prueba localmente (opcional pero recomendado)

**Python:**
```bash
cd challenges/week1/python
# Si tienes los tests locales
pytest -v
```

**Java:**
```bash
cd challenges/week1/java
javac solution.java
# Si tienes tests locales con Maven
mvn test
```

### 4. Sube tus cambios y crea un PR

```bash
git add challenges/week1/python/solution.py  # o java/solution.java
git commit -m "feat: Week 1 solution - tu_usuario"
git push origin tu_usuario_week1_solution
```

Luego ve a GitHub y crea un **Pull Request** hacia `main`.

### 5. Espera los resultados

- Cada vez que hagas push, se ejecutaran automaticamente los tests privados
- Podras ver los resultados en la pestana "Actions" de tu PR
- Los tests mostraran que pruebas pasaron y cuales fallaron

---

## Sistema de Puntuacion

- Cada reto tiene varios niveles de dificultad
- Cada test pasado suma puntos
- El **leaderboard** se calcula segun:
  1. Numero de tests pasados
  2. Hora de creacion del PR (en caso de empate)

---

## Reglas Importantes

1. **NO hagas merge de tu PR** - Los PRs son solo para evaluar tu solucion
2. **NO copies soluciones** de otros participantes
3. **Usa solo el lenguaje de tu eleccion** (Python o Java por semana)
4. **Respeta el naming** de tu rama: `username_weekX_solution`


## FAQ

### ¿Puedo usar librerias externas?
Depende del reto. Lee las instrucciones en `challenge.md`.

### ¿Puedo hacer varios PRs?
Si, pero solo el ultimo sera evaluado.

### ¿Como veo mi puntuacion?
Mira los resultados de los Actions en tu PR.

### ¿Puedo hacer PRs para ambos lenguajes?
Si! Crea una rama por cada uno:
- `usuario_week1_python`
- `usuario_week1_java`

---

## Contacto

¿Dudas? Contacta a los organizadores del GDG de Córdoba

---

¡Buena suerte! 🚀 y al turrón!
