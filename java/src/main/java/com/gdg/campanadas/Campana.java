package com.gdg.campanadas;

import java.util.List;
import java.util.Map;

/**
 * 🔔 CAMPANADAS DE LAS TENDILLAS 🔔
 * ==================================
 *
 * Día 5 del Bootcamp - Reto TDD
 *
 * CONTEXTO:
 * ---------
 * Las campanas de las Tendillas en Córdoba tienen diferentes periodos.
 * Tu misión es calcular cuándo sonarán todas juntas por primera vez.
 *
 * CONCEPTOS CLAVE:
 * ----------------
 * - Periodo: cada cuántos segundos suena la campana
 * - Fase: desfase inicial en segundos (cuándo empieza a contar)
 * - Una campana suena en el instante T si: (T - fase) es múltiplo del periodo
 *
 * EJEMPLO:
 * --------
 * Campana A: periodo=3, fase=0 → suena en: 3, 6, 9, 12, 15...
 * Campana B: periodo=5, fase=0 → suena en: 5, 10, 15, 20...
 * Primera sincronización: T=15 (MCM de 3 y 5)
 *
 * NIVELES:
 * --------
 * 1. Crear campana con periodo y fase
 * 2. Determinar si suena en un instante T
 * 3. Calcular MCM entre dos campanas
 * 4. Sincronizar múltiples campanas
 * 5. Casos especiales y optimización
 *
 * ¡Buena suerte! 🎯
 */
public class Campana {

    private int periodo;
    private int fase;

    /**
     * NIVEL 1: Crear una campana
     *
     * TODO: Implementa el constructor
     * - Guarda el periodo y la fase como atributos
     * - El periodo debe ser > 0, si no lanza IllegalArgumentException
     * - La fase debe ser >= 0, si no lanza IllegalArgumentException
     *
     * @param periodo Intervalo en segundos entre campanadas
     * @param fase Desfase inicial en segundos (default: 0)
     */
    public Campana(int periodo, int fase) {
        // TU CÓDIGO AQUÍ
    }

    /**
     * Constructor con fase por defecto (0)
     */
    public Campana(int periodo) {
        this(periodo, 0);
    }

    public int getPeriodo() {
        return periodo;
    }

    public int getFase() {
        return fase;
    }

    /**
     * NIVEL 2: Determina si la campana suena en un instante dado
     *
     * Una campana suena en el instante T si:
     * - T > 0
     * - (T - fase) >= 0
     * - (T - fase) es divisible por el periodo
     *
     * @param instante El momento en segundos a comprobar
     * @return true si la campana suena en ese instante, false en caso contrario
     *
     * TODO: Implementa la lógica
     */
    public boolean suenaEn(int instante) {
        // TU CÓDIGO AQUÍ
        return false;
    }

    /**
     * NIVEL 2 (bonus): Calcula la próxima campanada desde un instante dado
     *
     * @param desde Instante desde el que buscar (default: 0)
     * @return El próximo instante > desde en que suena la campana
     */
    public int proximaCampanada(int desde) {
        // TU CÓDIGO AQUÍ
        return 0;
    }

    public int proximaCampanada() {
        return proximaCampanada(0);
    }

    /**
     * NIVEL 3: Calcula el Máximo Común Divisor usando Euclides
     *
     * @param a Primer número entero positivo
     * @param b Segundo número entero positivo
     * @return El MCD de a y b
     *
     * TODO: Implementa el algoritmo de Euclides
     * Pista: mcd(a, b) = mcd(b, a % b) hasta que b sea 0
     */
    public static int mcd(int a, int b) {
        // TU CÓDIGO AQUÍ
        return 0;
    }

    /**
     * NIVEL 3: Calcula el Mínimo Común Múltiplo
     *
     * @param a Primer número entero positivo
     * @param b Segundo número entero positivo
     * @return El MCM de a y b
     *
     * TODO: Implementa usando la fórmula: mcm(a,b) = (a * b) / mcd(a,b)
     */
    public static int mcm(int a, int b) {
        // TU CÓDIGO AQUÍ
        return 0;
    }

    /**
     * NIVEL 3: Encuentra el primer instante > 0 en que dos campanas suenan juntas
     *
     * CASO SIMPLE (ambas con fase=0):
     *     El resultado es el MCM de los periodos
     *
     * CASO CON FASES:
     *     Hay que resolver el sistema de congruencias:
     *     T ≡ fase1 (mod periodo1)
     *     T ≡ fase2 (mod periodo2)
     *
     * @param campana1 Primera campana a sincronizar
     * @param campana2 Segunda campana a sincronizar
     * @return El primer instante > 0 en que ambas suenan, o -1 si es imposible
     */
    public static int sincronizarDos(Campana campana1, Campana campana2) {
        // TU CÓDIGO AQUÍ
        return 0;
    }

    /**
     * NIVEL 4: Encuentra el primer instante > 0 en que TODAS las campanas suenan juntas
     *
     * Estrategia:
     *     1. Si la lista está vacía, retorna -1
     *     2. Si hay una sola campana, retorna su primera campanada
     *     3. Sincroniza las campanas de dos en dos iterativamente
     *
     * @param campanas Lista de campanas
     * @return El primer instante > 0 en que todas suenan, o -1 si es imposible
     */
    public static int sincronizarMultiple(List<Campana> campanas) {
        // TU CÓDIGO AQUÍ
        return 0;
    }

    /**
     * NIVEL 5: Cuenta cuántas veces suena cada campana hasta un instante dado
     *
     * @param campanas Lista de campanas
     * @param hasta Instante límite (inclusive)
     * @return Map con el índice de cada campana y su número de campanadas
     *         Ejemplo: {0: 5, 1: 3, 2: 10}
     */
    public static Map<Integer, Integer> contarCampanadas(List<Campana> campanas, int hasta) {
        // TU CÓDIGO AQUÍ
        return null;
    }

    /**
     * NIVEL 5: Lista todos los momentos en que todas las campanas suenan juntas
     *
     * @param campanas Lista de campanas
     * @param hasta Instante límite (inclusive)
     * @return Lista ordenada de instantes donde todas suenan simultáneamente
     */
    public static List<Integer> momentosSincronizados(List<Campana> campanas, int hasta) {
        // TU CÓDIGO AQUÍ
        return null;
    }
}
