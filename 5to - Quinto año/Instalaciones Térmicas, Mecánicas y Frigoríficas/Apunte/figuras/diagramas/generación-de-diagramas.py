import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

def plot_diagrams(fluid='Water'):
    # Rango de temperaturas
    T_min, T_max = 273.15, 647.15  # K
    P_min, P_max = 1000, PropsSI('Pcrit', fluid)  # Pa
    
    # Saturación
    T_sat = np.linspace(T_min, PropsSI('Tcrit', fluid), 100)
    P_sat = np.array([PropsSI('P', 'T', T, 'Q', 0, fluid) for T in T_sat])
    v_sat_l = np.array([1 / PropsSI('D', 'T', T, 'Q', 0, fluid) for T in T_sat])
    v_sat_v = np.array([1 / PropsSI('D', 'T', T, 'Q', 1, fluid) for T in T_sat])
    h_sat_l = np.array([PropsSI('H', 'T', T, 'Q', 0, fluid) for T in T_sat])
    h_sat_v = np.array([PropsSI('H', 'T', T, 'Q', 1, fluid) for T in T_sat])
    s_sat_l = np.array([PropsSI('S', 'T', T, 'Q', 0, fluid) for T in T_sat])
    s_sat_v = np.array([PropsSI('S', 'T', T, 'Q', 1, fluid) for T in T_sat])
    
    # Generación de curvas adicionales
    x_values = np.linspace(0.1, 0.9, 5)  # Títulos del vapor
    v_curves = [x * v_sat_l + (1 - x) * v_sat_v for x in x_values]
    h_curves = [x * h_sat_l + (1 - x) * h_sat_v for x in x_values]
    s_curves = [x * s_sat_l + (1 - x) * s_sat_v for x in x_values]
    
    # Diagrama P-v
    plt.figure(figsize=(8,6))
    plt.plot(v_sat_l, P_sat, 'b', label='Líquido Saturado')
    plt.plot(v_sat_v, P_sat, 'r', label='Vapor Saturado')
    for curve in v_curves:
        plt.plot(curve, P_sat, 'g', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel('Volumen específico [m³/kg]')
    plt.ylabel('Presión [Pa]')
    plt.title('Diagrama P-v')
    plt.legend()
    plt.grid()
    plt.show()
    
    # Diagrama T-s
    plt.figure(figsize=(8,6))
    plt.plot(s_sat_l, T_sat, 'b', label='Líquido Saturado')
    plt.plot(s_sat_v, T_sat, 'r', label='Vapor Saturado')
    for curve in s_curves:
        plt.plot(curve, T_sat, 'g', linestyle='dotted')
    plt.xlabel('Entropía [J/kgK]')
    plt.ylabel('Temperatura [K]')
    plt.title('Diagrama T-s')
    plt.legend()
    plt.grid()
    plt.show()
    
    # Diagrama h-s (Mollier)
    plt.figure(figsize=(8,6))
    plt.plot(s_sat_l, h_sat_l, 'b', label='Líquido Saturado')
    plt.plot(s_sat_v, h_sat_v, 'r', label='Vapor Saturado')
    for curve in h_curves:
        plt.plot(s_sat_l, curve, 'g', linestyle='dotted')
    plt.xlabel('Entropía [J/kgK]')
    plt.ylabel('Entalpía [J/kg]')
    plt.title('Diagrama h-s (Mollier)')
    plt.legend()
    plt.grid()
    plt.show()
    
    # Diagrama P-h
    plt.figure(figsize=(8,6))
    plt.plot(h_sat_l, P_sat, 'b', label='Líquido Saturado')
    plt.plot(h_sat_v, P_sat, 'r', label='Vapor Saturado')
    for curve in h_curves:
        plt.plot(curve, P_sat, 'g', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel('Entalpía [J/kg]')
    plt.ylabel('Presión [Pa]')
    plt.title('Diagrama P-h')
    plt.legend()
    plt.grid()
    plt.show()

# Llamar a la función para generar gráficos
plot_diagrams()
