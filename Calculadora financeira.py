# Vamos calcular o crescimento do investimento ao longo do tempo com aportes mensais.
# Cenário 1: Rentabilidade (renda fixa conservadora)
# Cenário 2: Rentabilidade (renda mista)

# Calculadora de Investimentos

def calcular_investimento(montante_inicial, aporte_mensal, taxa_juros_anual, meses, meta_renda_mensal):
    """
    Calcula o crescimento do investimento ao longo do tempo com aportes mensais.

    Args:
        montante_inicial (float): Valor inicial do investimento.
        aporte_mensal (float): Valor do aporte mensal.
        taxa_juros_anual (float): Taxa de juros anual.
        meses (int): Número de meses para calcular o investimento.
        meta_renda_mensal (float): Meta de renda mensal desejada.

    Returns:
        tuple: (meses_para_meta, saldo_final, historico_saldo)
    """
    # Converte taxa de juros anual para mensal
    taxa_juros_mensal = (1 + taxa_juros_anual) ** (1/12) - 1
    saldo = montante_inicial
    historico_saldo = []

    for mes in range(meses):
        saldo = saldo * (1 + taxa_juros_mensal) + aporte_mensal
        historico_saldo.append(saldo)

        # Calcular a renda mensal aproximada com base em uma retirada de 0,5% do saldo total 
        renda_mensal = saldo * 0.005
        if renda_mensal >= meta_renda_mensal:
            return mes, saldo, historico_saldo

    return None, saldo, historico_saldo

# Definição das variáveis iniciais
montante_inicial = 1000  # Valor inicial do investimento
aporte_mensal = 500  # Valor do aporte mensal
taxa_juros_anual_1 = 0.1065  # Taxa de juros anual para o cenário 1
taxa_juros_anual_2 = 0.1075  # Taxa de juros anual para o cenário 2
meses = 360  # Número de meses para calcular o investimento
meta_renda_mensal = 1500  # Meta de renda mensal desejada

# Cenário 1: (renda fixa)
meses_1, saldo_final_1, historico_1 = calcular_investimento(montante_inicial, aporte_mensal, taxa_juros_anual_1, meses, meta_renda_mensal)

# Cenário 2: (renda mista)
meses_2, saldo_final_2, historico_2 = calcular_investimento(montante_inicial, aporte_mensal, taxa_juros_anual_2, meses, meta_renda_mensal)

# Printar informações finais
print("Resultados:")
print(f"Cenário 1 renda fixa (Taxa de juros anual: {taxa_juros_anual_1*100:.2f}%): {meses_1} meses ({meses_1/12:.2f} anos) para alcançar a meta de R$ {meta_renda_mensal} com saldo final de R$ {saldo_final_1:.2f}")
print(f"Cenário 2 renda mista (Taxa de juros anual: {taxa_juros_anual_2*100:.2f}%): {meses_2} meses ({meses_2/12:.2f} anos) para alcançar a meta de R$ {meta_renda_mensal} com saldo final de R$ {saldo_final_2:.2f}")

teste
