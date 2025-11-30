package com.gdg.campanadas;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

/**
 * 🧪 TESTS - CAMPANADAS DE LAS TENDILLAS 🧪
 * ==========================================
 *
 * Batería de tests TDD organizada en 5 niveles.
 * Cada test superado = 2 puntos
 * Total posible: 30 puntos
 *
 * Ejecutar tests:
 *     mvn test
 *     o
 *     gradle test
 *
 * Ejecutar solo un nivel:
 *     mvn test -Dtest=Nivel1Test
 *     mvn test -Dtest=Nivel2Test
 */
public class CampanaTest {

    // ============================================================================
    // NIVEL 1: CREAR CAMPANA BÁSICA (6 puntos)
    // ============================================================================

    @Nested
    @DisplayName("Nivel 1: Construcción básica de campanas")
    class Nivel1Test {

        @Test
        @DisplayName("[2 puntos] Crear una campana con periodo=5 y fase por defecto (0)")
        void testCrearCampanaBasica() {
            Campana campana = new Campana(5);

            assertEquals(5, campana.getPeriodo(), "El periodo debe ser 5");
            assertEquals(0, campana.getFase(), "La fase por defecto debe ser 0");
        }

        @Test
        @DisplayName("[2 puntos] Crear una campana con periodo=3 y fase=2")
        void testCrearCampanaConFase() {
            Campana campana = new Campana(3, 2);

            assertEquals(3, campana.getPeriodo(), "El periodo debe ser 3");
            assertEquals(2, campana.getFase(), "La fase debe ser 2");
        }

        @Test
        @DisplayName("[2 puntos] Crear campana con periodo <= 0 debe lanzar IllegalArgumentException")
        void testPeriodoInvalidoLanzaError() {
            assertThrows(IllegalArgumentException.class, () -> {
                new Campana(0);
            }, "Periodo 0 debe lanzar IllegalArgumentException");

            assertThrows(IllegalArgumentException.class, () -> {
                new Campana(-5);
            }, "Periodo negativo debe lanzar IllegalArgumentException");
        }
    }

    // ============================================================================
    // NIVEL 2: CALCULAR SI SUENA EN INSTANTE T (6 puntos)
    // ============================================================================

    @Nested
    @DisplayName("Nivel 2: Determinar cuándo suena una campana")
    class Nivel2Test {

        @Test
        @DisplayName("[2 puntos] Campana(periodo=3) suena en 3, 6, 9 pero no en 1, 2, 4, 5")
        void testSuenaEnMultiplosDelPeriodo() {
            Campana campana = new Campana(3);

            // Debe sonar
            assertTrue(campana.suenaEn(3), "Debe sonar en t=3");
            assertTrue(campana.suenaEn(6), "Debe sonar en t=6");
            assertTrue(campana.suenaEn(9), "Debe sonar en t=9");

            // No debe sonar
            assertFalse(campana.suenaEn(1), "No debe sonar en t=1");
            assertFalse(campana.suenaEn(2), "No debe sonar en t=2");
            assertFalse(campana.suenaEn(4), "No debe sonar en t=4");
        }

        @Test
        @DisplayName("[2 puntos] Campana(periodo=4, fase=1) suena en 1, 5, 9, 13...")
        void testSuenaConFase() {
            Campana campana = new Campana(4, 1);

            // Debe sonar en fase + k*periodo
            assertTrue(campana.suenaEn(1), "Debe sonar en t=1 (fase)");
            assertTrue(campana.suenaEn(5), "Debe sonar en t=5");
            assertTrue(campana.suenaEn(9), "Debe sonar en t=9");

            // No debe sonar
            assertFalse(campana.suenaEn(2), "No debe sonar en t=2");
            assertFalse(campana.suenaEn(4), "No debe sonar en t=4");
        }

        @Test
        @DisplayName("[2 puntos] Ninguna campana suena en t=0 o instantes negativos")
        void testNoSuenaEnCeroNiNegativos() {
            Campana campana = new Campana(5);

            assertFalse(campana.suenaEn(0), "No debe sonar en t=0");
            assertFalse(campana.suenaEn(-5), "No debe sonar en negativos");
        }
    }

    // ============================================================================
    // NIVEL 3: MCM DE DOS CAMPANAS (6 puntos)
    // ============================================================================

    @Nested
    @DisplayName("Nivel 3: Calcular MCD, MCM y sincronizar dos campanas")
    class Nivel3Test {

        @Test
        @DisplayName("[2 puntos] MCD de varios pares de números")
        void testMcdBasico() {
            assertEquals(4, Campana.mcd(12, 8), "MCD(12, 8) = 4");
            assertEquals(5, Campana.mcd(15, 5), "MCD(15, 5) = 5");
            assertEquals(1, Campana.mcd(7, 11), "MCD(7, 11) = 1 (coprimos)");
            assertEquals(100, Campana.mcd(100, 100), "MCD(100, 100) = 100");
        }

        @Test
        @DisplayName("[2 puntos] MCM de varios pares de números")
        void testMcmBasico() {
            assertEquals(15, Campana.mcm(3, 5), "MCM(3, 5) = 15");
            assertEquals(12, Campana.mcm(4, 6), "MCM(4, 6) = 12");
            assertEquals(7, Campana.mcm(7, 7), "MCM(7, 7) = 7");
            assertEquals(8, Campana.mcm(2, 8), "MCM(2, 8) = 8");
        }

        @Test
        @DisplayName("[2 puntos] Sincronizar dos campanas con fase=0")
        void testSincronizarDosSinFase() {
            Campana c1 = new Campana(3);  // Suena: 3, 6, 9, 12, 15...
            Campana c2 = new Campana(5);  // Suena: 5, 10, 15...

            int resultado = Campana.sincronizarDos(c1, c2);

            assertEquals(15, resultado, "Deben sincronizar en t=15");
            // Verificamos que realmente suenan ambas
            assertTrue(c1.suenaEn(resultado));
            assertTrue(c2.suenaEn(resultado));
        }
    }

    // ============================================================================
    // NIVEL 4: SINCRONIZACIÓN MÚTIPLE (6 puntos)
    // ============================================================================

    @Nested
    @DisplayName("Nivel 4: Sincronizar múltiples campanas")
    class Nivel4Test {

        @Test
        @DisplayName("[2 puntos] Sincronizar tres campanas con fase=0")
        void testSincronizarTresCampanas() {
            Campana c1 = new Campana(2);  // 2, 4, 6, 8, 10, 12...
            Campana c2 = new Campana(3);  // 3, 6, 9, 12...
            Campana c3 = new Campana(4);  // 4, 8, 12...

            int resultado = Campana.sincronizarMultiple(Arrays.asList(c1, c2, c3));

            assertEquals(12, resultado, "MCM(2,3,4) = 12");
            // Verificar
            assertTrue(c1.suenaEn(resultado));
            assertTrue(c2.suenaEn(resultado));
            assertTrue(c3.suenaEn(resultado));
        }

        @Test
        @DisplayName("[2 puntos] Sincronizar cuatro campanas")
        void testSincronizarCuatroCampanas() {
            List<Campana> campanas = Arrays.asList(
                new Campana(2),
                new Campana(3),
                new Campana(5),
                new Campana(7)
            );

            int resultado = Campana.sincronizarMultiple(campanas);

            // MCM(2,3,5,7) = 210
            assertEquals(210, resultado);
            for (Campana c : campanas) {
                assertTrue(c.suenaEn(resultado));
            }
        }

        @Test
        @DisplayName("[2 puntos] Casos edge: lista vacía y una sola campana")
        void testListaVaciaOUnaCampana() {
            // Lista vacía debe retornar -1
            assertEquals(-1, Campana.sincronizarMultiple(Arrays.asList()));

            // Una sola campana retorna su primera campanada
            Campana c = new Campana(7);
            assertEquals(7, Campana.sincronizarMultiple(Arrays.asList(c)));
        }
    }

    // ============================================================================
    // NIVEL 5: CASOS EDGE Y OPTIMIZACIÓN (6 puntos)
    // ============================================================================

    @Nested
    @DisplayName("Nivel 5: Funcionalidades avanzadas y casos especiales")
    class Nivel5Test {

        @Test
        @DisplayName("[2 puntos] Contar cuántas veces suena cada campana")
        void testContarCampanadas() {
            List<Campana> campanas = Arrays.asList(
                new Campana(2),  // 2,4,6,8,10 = 5 veces hasta t=10
                new Campana(3),  // 3,6,9 = 3 veces hasta t=10
                new Campana(5)   // 5,10 = 2 veces hasta t=10
            );

            Map<Integer, Integer> resultado = Campana.contarCampanadas(campanas, 10);

            assertEquals(5, resultado.get(0), "Campana 0 suena 5 veces");
            assertEquals(3, resultado.get(1), "Campana 1 suena 3 veces");
            assertEquals(2, resultado.get(2), "Campana 2 suena 2 veces");
        }

        @Test
        @DisplayName("[2 puntos] Listar todos los momentos de sincronización")
        void testMomentosSincronizados() {
            List<Campana> campanas = Arrays.asList(
                new Campana(3),  // 3,6,9,12,15,18,21,24,27,30
                new Campana(5)   // 5,10,15,20,25,30
            );

            List<Integer> resultado = Campana.momentosSincronizados(campanas, 35);

            // MCM(3,5)=15, así que sincronizan en 15 y 30
            assertEquals(Arrays.asList(15, 30), resultado,
                String.format("Esperado [15, 30], obtenido %s", resultado));
        }

        @Test
        @DisplayName("[2 puntos] El algoritmo debe ser eficiente con números grandes")
        void testPeriodosGrandesOptimizado() {
            List<Campana> campanas = Arrays.asList(
                new Campana(97),
                new Campana(101),
                new Campana(103)
            );

            long inicio = System.currentTimeMillis();
            int resultado = Campana.sincronizarMultiple(campanas);
            long tiempo = System.currentTimeMillis() - inicio;

            // MCM(97, 101, 103) = 97 * 101 * 103 = 1009091
            assertEquals(1009091, resultado,
                String.format("Esperado 1009091, obtenido %d", resultado));
            assertTrue(tiempo < 1000,
                String.format("Debe ejecutarse en menos de 1 segundo, tardó %dms", tiempo));
        }
    }
}
