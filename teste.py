import matplotlib.pyplot as plt
import numpy as np

def plotar_degradacao_por_ciclos():
    # --- Parâmetros Configuráveis ---
    cycles_per_day = 2  # Média de ciclos de descarga por dia
    simulation_years = 30  # Quantos anos simular
    

    # Bateria LiFePO4
    lifepo4_initial_capacity_percent = 100
    lifepo4_eol_capacity_percent = 80
    # Vida útil em ciclos até EoL (assumindo uma DoD que resulte nisso)
    lifepo4_cycles_to_eol = 5000 # Exemplo: 5000 ciclos para 80% DoD

    # Supercapacitor (CDA 2.85V 3400F ou similar)
    supercap_initial_capacity_percent = 100
    supercap_eol_capacity_percent = 80
    # Vida útil em ciclos até EoL
    supercap_cycles_to_eol = 500000 # Exemplo conservador para EDLC de qualidade

    # --- Cálculos ---
    days_in_year = 365.25 # Média para anos bissextos
    years_array = np.arange(0, simulation_years + 1)
    total_cycles_over_time = years_array * cycles_per_day * days_in_year

    # LiFePO4
    # Perda de capacidade por ciclo
    lifepo4_capacity_loss_per_cycle = (lifepo4_initial_capacity_percent - lifepo4_eol_capacity_percent) / lifepo4_cycles_to_eol
    # Capacidade restante ao longo do tempo
    capacidade_lifepo4 = lifepo4_initial_capacity_percent - (lifepo4_capacity_loss_per_cycle * total_cycles_over_time)
    # Garante que a capacidade não caia abaixo do EoL definido no gráfico
    capacidade_lifepo4 = np.maximum(capacidade_lifepo4, lifepo4_eol_capacity_percent)

    # Supercapacitor
    # Perda de capacidade por ciclo
    supercap_capacity_loss_per_cycle = (supercap_initial_capacity_percent - supercap_eol_capacity_percent) / supercap_cycles_to_eol
    # Capacidade restante ao longo do tempo
    capacidade_supercap = supercap_initial_capacity_percent - (supercap_capacity_loss_per_cycle * total_cycles_over_time)
    # Garante que a capacidade não caia abaixo do EoL definido no gráfico
    capacidade_supercap = np.maximum(capacidade_supercap, supercap_eol_capacity_percent)


    # --- Anos para atingir EoL (aproximado) ---
    lifepo4_years_to_eol = lifepo4_cycles_to_eol / (cycles_per_day * days_in_year)
    supercap_years_to_eol = supercap_cycles_to_eol / (cycles_per_day * days_in_year)

    print(f"Anos estimados para LiFePO4 atingir EoL ({lifepo4_eol_capacity_percent}% cap.) a {cycles_per_day} ciclos/dia: {lifepo4_years_to_eol:.2f} anos")
    print(f"Anos estimados para Supercapacitor atingir EoL ({supercap_eol_capacity_percent}% cap.) a {cycles_per_day} ciclos/dia: {supercap_years_to_eol:.2f} anos")


    # --- Plotagem ---
    plt.figure(figsize=(12, 7))

    plt.plot(years_array, capacidade_lifepo4,
             label=f'Bateria LiFePO4 ({lifepo4_cycles_to_eol:,} ciclos até EoL)',
             marker='o')
    plt.plot(years_array, capacidade_supercap,
             label=f'Supercapacitor ({supercap_cycles_to_eol:,} ciclos até EoL)',
             marker='x')

    plt.title(f'Degradação Estimada da Capacidade por Ciclos ({cycles_per_day} ciclos/dia)')
    plt.xlabel('Anos de Operação')
    plt.ylabel('Capacidade Retida (%)')
    plt.ylim(min(lifepo4_eol_capacity_percent, supercap_eol_capacity_percent) - 5, 105)
    plt.axhline(y=80, color='gray', linestyle='--', label='Nível de EoL Comum (80%)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    plotar_degradacao_por_ciclos()
