#!/usr/bin/env python3
"""
🏆 CALCULADOR DE PUNTUACIÓN 🏆
==============================

Ejecuta los tests y muestra la puntuación detallada por nivel.

Uso:
    python calcular_puntos.py
    
O:
    pytest test_campana.py -v --tb=no | python calcular_puntos.py
"""

import subprocess
import sys
import os


def ejecutar_tests():
    """Ejecuta pytest y retorna la salida"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "test_campana.py", "-v", "--tb=no"],
        capture_output=True,
        text=True,
        cwd=script_dir
    )
    return result.stdout + result.stderr


def analizar_resultados(output):
    """Analiza la salida de pytest y extrae resultados por nivel"""
    
    # Definir los tests por nivel
    niveles = {
        1: [
            "test_nivel1_crear_campana_basica",
            "test_nivel1_crear_campana_con_fase", 
            "test_nivel1_periodo_invalido_lanza_error"
        ],
        2: [
            "test_nivel2_suena_en_multiplos_del_periodo",
            "test_nivel2_suena_con_fase",
            "test_nivel2_no_suena_en_cero_ni_negativos"
        ],
        3: [
            "test_nivel3_mcd_basico",
            "test_nivel3_mcm_basico",
            "test_nivel3_sincronizar_dos_sin_fase"
        ],
        4: [
            "test_nivel4_sincronizar_tres_campanas",
            "test_nivel4_sincronizar_cuatro_campanas",
            "test_nivel4_lista_vacia_o_una_campana"
        ],
        5: [
            "test_nivel5_contar_campanadas",
            "test_nivel5_momentos_sincronizados",
            "test_nivel5_periodos_grandes_optimizado"
        ]
    }
    
    resultados = {i: {"passed": 0, "failed": 0, "tests": []} for i in range(1, 6)}
    
    for nivel, tests in niveles.items():
        for test_name in tests:
            if f"{test_name} PASSED" in output:
                resultados[nivel]["passed"] += 1
                resultados[nivel]["tests"].append((test_name, "✅"))
            elif f"{test_name} FAILED" in output:
                resultados[nivel]["failed"] += 1
                resultados[nivel]["tests"].append((test_name, "❌"))
            else:
                resultados[nivel]["tests"].append((test_name, "⏸️"))
    
    return resultados


def mostrar_resultados(resultados):
    """Muestra los resultados de forma visual"""
    
    nombres_niveles = {
        1: "Crear Campana Básica",
        2: "Calcular Si Suena en T",
        3: "MCM de Dos Campanas",
        4: "Sincronización Múltiple",
        5: "Casos Edge y Optimización"
    }
    
    print("\n" + "="*70)
    print("🔔 CAMPANADAS DE LAS TENDILLAS - TABLERO DE PUNTUACIÓN 🔔")
    print("="*70)
    
    total_puntos = 0
    total_tests_pasados = 0
    total_tests = 0
    
    for nivel in range(1, 6):
        datos = resultados[nivel]
        puntos_nivel = datos["passed"] * 2
        total_puntos += puntos_nivel
        total_tests_pasados += datos["passed"]
        total_tests += len(datos["tests"])
        
        # Barra de progreso visual
        completados = datos["passed"]
        total = len(datos["tests"])
        barra = "█" * completados + "░" * (total - completados)
        
        print(f"\n┌{'─'*68}┐")
        print(f"│ NIVEL {nivel}: {nombres_niveles[nivel]:<45} │")
        print(f"├{'─'*68}┤")
        print(f"│ Progreso: [{barra}] {completados}/{total} tests          │")
        print(f"│ Puntos: {puntos_nivel}/6                                              │")
        print(f"├{'─'*68}┤")
        
        for test_name, status in datos["tests"]:
            # Acortar nombre del test para que quepa
            nombre_corto = test_name.replace("test_nivel", "").replace("_", " ")[:45]
            print(f"│   {status} {nombre_corto:<60} │")
        
        print(f"└{'─'*68}┘")
    
    # Resumen final
    porcentaje = (total_puntos / 30) * 100
    
    print("\n" + "="*70)
    print("📊 RESUMEN FINAL")
    print("="*70)
    print(f"""
    ┌────────────────────────────────────────┐
    │                                        │
    │   🏆 PUNTUACIÓN TOTAL: {total_puntos:2}/30 puntos   │
    │                                        │
    │   Tests pasados: {total_tests_pasados:2}/{total_tests}              │
    │   Porcentaje: {porcentaje:5.1f}%                 │
    │                                        │
    └────────────────────────────────────────┘
    """)
    
    # Mensaje según puntuación
    if total_puntos == 30:
        print("    🎉 ¡PERFECTO! ¡Has dominado las campanadas!")
    elif total_puntos >= 24:
        print("    ⭐ ¡Excelente trabajo! Ya casi lo tienes.")
    elif total_puntos >= 18:
        print("    👍 ¡Buen progreso! Sigue adelante.")
    elif total_puntos >= 12:
        print("    💪 Vas por buen camino. ¡No te rindas!")
    elif total_puntos >= 6:
        print("    🌱 Has empezado bien. ¡A por el siguiente nivel!")
    else:
        print("    🚀 ¡Empieza por el Nivel 1! Lee los hints del código.")
    
    print()
    return total_puntos


if __name__ == "__main__":
    # Verificar si hay entrada por stdin (pipe)
    if not sys.stdin.isatty():
        output = sys.stdin.read()
    else:
        output = ejecutar_tests()
    
    resultados = analizar_resultados(output)
    mostrar_resultados(resultados)
