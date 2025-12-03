import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;

/**
 * Campanadas de las Tendillas - Week 1
 *
 * Instrucciones:
 * 1. Implementa los metodos marcados con "// TU CODIGO AQUI"
 * 2. No cambies los nombres de los metodos ni la clase
 * 3. Ejecuta los tests locales antes de hacer push
 *
 * Para probar localmente:
 *     mvn test
 */
public class Campana {

    private int periodo;
    private int fase;

    /**
     * NIVEL 1: Crear una campana
     *
     * - Guarda el periodo y la fase como atributos
     * - El periodo debe ser > 0, si no lanza IllegalArgumentException
     * - La fase debe ser >= 0, si no lanza IllegalArgumentException
     */
    public Campana(int periodo, int fase) {
        // TU CODIGO AQUI
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
     */
    public boolean suenaEn(int instante) {
        // TU CODIGO AQUI
        return false;
    }

    /**
     * NIVEL 2 (bonus): Calcula la proxima campanada desde un instante dado
     */
    public int proximaCampanada(int desde) {
        // TU CODIGO AQUI
        return 0;
    }

    public int proximaCampanada() {
        return proximaCampanada(0);
    }

    /**
     * NIVEL 3: Calcula el Maximo Comun Divisor usando Euclides
     *
     * Pista: mcd(a, b) = mcd(b, a % b) hasta que b sea 0
     */
    public static int mcd(int a, int b) {
        // TU CODIGO AQUI
        return 0;
    }

    /**
     * NIVEL 3: Calcula el Minimo Comun Multiplo
     *
     * Formula: mcm(a,b) = (a * b) / mcd(a,b)
     */
    public static int mcm(int a, int b) {
        // TU CODIGO AQUI
        return 0;
    }

    /**
     * NIVEL 3: Encuentra el primer instante > 0 en que dos campanas suenan juntas
     *
     * CASO SIMPLE (ambas con fase=0):
     *     El resultado es el MCM de los periodos
     */
    public static int sincronizarDos(Campana campana1, Campana campana2) {
        // TU CODIGO AQUI
        return 0;
    }

    /**
     * NIVEL 4: Encuentra el primer instante > 0 en que TODAS las campanas suenan juntas
     *
     * - Si la lista esta vacia, retorna -1
     * - Si hay una sola campana, retorna su primera campanada (periodo)
     * - Varias: aplicar MCM iterativamente
     */
    public static int sincronizarMultiple(List<Campana> campanas) {
        // TU CODIGO AQUI
        return 0;
    }

    /**
     * NIVEL 5: Cuenta cuantas veces suena cada campana hasta un instante dado
     *
     * @return Map con {indice: cantidad}
     */
    public static Map<Integer, Integer> contarCampanadas(List<Campana> campanas, int hasta) {
        // TU CODIGO AQUI
        return null;
    }

    /**
     * NIVEL 5: Lista todos los momentos en que todas las campanas suenan juntas
     *
     * @return Lista ordenada de instantes
     */
    public static List<Integer> momentosSincronizados(List<Campana> campanas, int hasta) {
        // TU CODIGO AQUI
        return null;
    }
}
