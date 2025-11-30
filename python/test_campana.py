"""
🧪 TESTS - CAMPANADAS DE LAS TENDILLAS 🧪
==========================================

Batería de tests TDD organizada en 5 niveles.
Cada test superado = 2 puntos
Total posible: 30 puntos

Ejecutar tests:
    pytest test_campana.py -v

Ejecutar solo un nivel:
    pytest test_campana.py -v -k "nivel1"
    
Ver puntuación:
    python calcular_puntos.py
"""

import pytest
from campana import (
    Campana, 
    mcd, 
    mcm, 
    sincronizar_dos, 
    sincronizar_multiple,
    contar_campanadas,
    momentos_sincronizados
)


# ============================================================================
# NIVEL 1: CREAR CAMPANA BÁSICA (6 puntos)
# ============================================================================

class TestNivel1_CrearCampana:
    """
    Nivel 1: Construcción básica de campanas
    
    Objetivos:
    - Crear campanas con periodo y fase
    - Validar que periodo > 0
    - Validar que fase >= 0
    """
    
    def test_nivel1_crear_campana_basica(self):
        """
        [2 puntos] Crear una campana con periodo=5 y fase por defecto (0)
        """
        campana = Campana(periodo=5)
        
        assert campana.periodo == 5, "El periodo debe ser 5"
        assert campana.fase == 0, "La fase por defecto debe ser 0"
    
    def test_nivel1_crear_campana_con_fase(self):
        """
        [2 puntos] Crear una campana con periodo=3 y fase=2
        """
        campana = Campana(periodo=3, fase=2)
        
        assert campana.periodo == 3, "El periodo debe ser 3"
        assert campana.fase == 2, "La fase debe ser 2"
    
    def test_nivel1_periodo_invalido_lanza_error(self):
        """
        [2 puntos] Crear campana con periodo <= 0 debe lanzar ValueError
        """
        with pytest.raises(ValueError):
            Campana(periodo=0)
        
        with pytest.raises(ValueError):
            Campana(periodo=-5)


# ============================================================================
# NIVEL 2: CALCULAR SI SUENA EN INSTANTE T (6 puntos)
# ============================================================================

class TestNivel2_SuenaEn:
    """
    Nivel 2: Determinar cuándo suena una campana
    
    Fórmula: suena en T si (T - fase) >= 0 y (T - fase) % periodo == 0
    """
    
    def test_nivel2_suena_en_multiplos_del_periodo(self):
        """
        [2 puntos] Campana(periodo=3) suena en 3, 6, 9 pero no en 1, 2, 4, 5
        """
        campana = Campana(periodo=3)
        
        # Debe sonar
        assert campana.suena_en(3) == True, "Debe sonar en t=3"
        assert campana.suena_en(6) == True, "Debe sonar en t=6"
        assert campana.suena_en(9) == True, "Debe sonar en t=9"
        
        # No debe sonar
        assert campana.suena_en(1) == False, "No debe sonar en t=1"
        assert campana.suena_en(2) == False, "No debe sonar en t=2"
        assert campana.suena_en(4) == False, "No debe sonar en t=4"
    
    def test_nivel2_suena_con_fase(self):
        """
        [2 puntos] Campana(periodo=4, fase=1) suena en 1, 5, 9, 13...
        """
        campana = Campana(periodo=4, fase=1)
        
        # Debe sonar en fase + k*periodo
        assert campana.suena_en(1) == True, "Debe sonar en t=1 (fase)"
        assert campana.suena_en(5) == True, "Debe sonar en t=5"
        assert campana.suena_en(9) == True, "Debe sonar en t=9"
        
        # No debe sonar
        assert campana.suena_en(2) == False, "No debe sonar en t=2"
        assert campana.suena_en(4) == False, "No debe sonar en t=4"
    
    def test_nivel2_no_suena_en_cero_ni_negativos(self):
        """
        [2 puntos] Ninguna campana suena en t=0 o instantes negativos
        """
        campana = Campana(periodo=5)
        
        assert campana.suena_en(0) == False, "No debe sonar en t=0"
        assert campana.suena_en(-5) == False, "No debe sonar en negativos"


# ============================================================================
# NIVEL 3: MCM DE DOS CAMPANAS (6 puntos)
# ============================================================================

class TestNivel3_MCM:
    """
    Nivel 3: Calcular MCD, MCM y sincronizar dos campanas
    
    El MCM nos dice cuándo coinciden dos campanas con fase 0
    """
    
    def test_nivel3_mcd_basico(self):
        """
        [2 puntos] MCD de varios pares de números
        """
        assert mcd(12, 8) == 4, "MCD(12, 8) = 4"
        assert mcd(15, 5) == 5, "MCD(15, 5) = 5"
        assert mcd(7, 11) == 1, "MCD(7, 11) = 1 (coprimos)"
        assert mcd(100, 100) == 100, "MCD(100, 100) = 100"
    
    def test_nivel3_mcm_basico(self):
        """
        [2 puntos] MCM de varios pares de números
        """
        assert mcm(3, 5) == 15, "MCM(3, 5) = 15"
        assert mcm(4, 6) == 12, "MCM(4, 6) = 12"
        assert mcm(7, 7) == 7, "MCM(7, 7) = 7"
        assert mcm(2, 8) == 8, "MCM(2, 8) = 8"
    
    def test_nivel3_sincronizar_dos_sin_fase(self):
        """
        [2 puntos] Sincronizar dos campanas con fase=0
        """
        c1 = Campana(periodo=3)  # Suena: 3, 6, 9, 12, 15...
        c2 = Campana(periodo=5)  # Suena: 5, 10, 15...
        
        resultado = sincronizar_dos(c1, c2)
        
        assert resultado == 15, "Deben sincronizar en t=15"
        # Verificamos que realmente suenan ambas
        assert c1.suena_en(resultado) == True
        assert c2.suena_en(resultado) == True


# ============================================================================
# NIVEL 4: SINCRONIZACIÓN MÚTIPLE (6 puntos)
# ============================================================================

class TestNivel4_SincronizacionMultiple:
    """
    Nivel 4: Sincronizar múltiples campanas
    
    Hay que aplicar MCM iterativamente o resolver congruencias
    """
    
    def test_nivel4_sincronizar_tres_campanas(self):
        """
        [2 puntos] Sincronizar tres campanas con fase=0
        """
        c1 = Campana(periodo=2)  # 2, 4, 6, 8, 10, 12...
        c2 = Campana(periodo=3)  # 3, 6, 9, 12...
        c3 = Campana(periodo=4)  # 4, 8, 12...
        
        resultado = sincronizar_multiple([c1, c2, c3])
        
        assert resultado == 12, "MCM(2,3,4) = 12"
        # Verificar
        assert c1.suena_en(resultado) == True
        assert c2.suena_en(resultado) == True
        assert c3.suena_en(resultado) == True
    
    def test_nivel4_sincronizar_cuatro_campanas(self):
        """
        [2 puntos] Sincronizar cuatro campanas
        """
        campanas = [
            Campana(periodo=2),
            Campana(periodo=3),
            Campana(periodo=5),
            Campana(periodo=7)
        ]
        
        resultado = sincronizar_multiple(campanas)
        
        # MCM(2,3,5,7) = 210
        assert resultado == 210
        for c in campanas:
            assert c.suena_en(resultado) == True
    
    def test_nivel4_lista_vacia_o_una_campana(self):
        """
        [2 puntos] Casos edge: lista vacía y una sola campana
        """
        # Lista vacía debe retornar -1
        assert sincronizar_multiple([]) == -1
        
        # Una sola campana retorna su primera campanada
        c = Campana(periodo=7)
        assert sincronizar_multiple([c]) == 7


# ============================================================================
# NIVEL 5: CASOS EDGE Y OPTIMIZACIÓN (6 puntos)
# ============================================================================

class TestNivel5_CasosAvanzados:
    """
    Nivel 5: Funcionalidades avanzadas y casos especiales
    """
    
    def test_nivel5_contar_campanadas(self):
        """
        [2 puntos] Contar cuántas veces suena cada campana
        """
        campanas = [
            Campana(periodo=2),  # 2,4,6,8,10 = 5 veces hasta t=10
            Campana(periodo=3),  # 3,6,9 = 3 veces hasta t=10
            Campana(periodo=5),  # 5,10 = 2 veces hasta t=10
        ]
        
        resultado = contar_campanadas(campanas, hasta=10)
        
        assert resultado[0] == 5, "Campana 0 suena 5 veces"
        assert resultado[1] == 3, "Campana 1 suena 3 veces"
        assert resultado[2] == 2, "Campana 2 suena 2 veces"
    
    def test_nivel5_momentos_sincronizados(self):
        """
        [2 puntos] Listar todos los momentos de sincronización
        """
        campanas = [
            Campana(periodo=3),  # 3,6,9,12,15,18,21,24,27,30
            Campana(periodo=5),  # 5,10,15,20,25,30
        ]
        
        resultado = momentos_sincronizados(campanas, hasta=35)
        
        # MCM(3,5)=15, así que sincronizan en 15 y 30
        assert resultado == [15, 30], f"Esperado [15, 30], obtenido {resultado}"
    
    def test_nivel5_periodos_grandes_optimizado(self):
        """
        [2 puntos] El algoritmo debe ser eficiente con números grandes
        """
        import time
        
        campanas = [
            Campana(periodo=97),
            Campana(periodo=101),
            Campana(periodo=103),
        ]
        
        inicio = time.time()
        resultado = sincronizar_multiple(campanas)
        tiempo = time.time() - inicio
        
        # MCM(97, 101, 103) = 97 * 101 * 103 = 1009091
        assert resultado == 1009091, f"Esperado 1009091, obtenido {resultado}"
        assert tiempo < 1.0, f"Debe ejecutarse en menos de 1 segundo, tardó {tiempo:.2f}s"
