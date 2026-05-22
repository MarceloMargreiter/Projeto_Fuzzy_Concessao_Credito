import numpy as np  
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import scipy as sp

#Antecedentes / Variáveis de entrada
score_serasa = ctrl.Antecedent(np.arange(0, 101, 1), 'Score')
renda_mensal = ctrl.Antecedent(np.arange(0, 50001, 1), 'Renda')

#Consequente / Variável de saída
limite_credito = ctrl.Consequent(np.arange(0, 101, 1), 'Credito')


#Funções de pertinência para score serasa
score_serasa['baixo'] = fuzz.trimf(score_serasa.universe, [0, 0, 50])
score_serasa['medio'] = fuzz.trimf(score_serasa.universe, [25, 50, 75])
score_serasa['alto'] = fuzz.trimf(score_serasa.universe, [50, 100, 100])    

#Funções de pertinência para renda mensal
renda_mensal['baixa'] = fuzz.trapmf(renda_mensal.universe, [0, 0, 3000, 6000])
renda_mensal['media'] = fuzz.trapmf(renda_mensal.universe, [3000, 6000, 10000, 20000])
renda_mensal['alta'] = fuzz.trapmf(renda_mensal.universe, [10000, 20000, 100000, 100000])     

#Funções de pertinência para limite de crédito (será o % da renda mensal)
limite_credito['muito_baixo'] = fuzz.trimf(limite_credito.universe, [0, 12, 24]) 
limite_credito['baixo'] = fuzz.trimf(limite_credito.universe, [12, 24, 36])
limite_credito['medio'] = fuzz.trimf(limite_credito.universe, [24, 36, 48])
limite_credito['alto'] = fuzz.trimf(limite_credito.universe, [36, 48, 70])
limite_credito['muito_alto'] = fuzz.trimf(limite_credito.universe, [48, 70, 70]) # limite superior um pouco menor para näo comprometer mais que 70% da renda mensal.    

#Regras Fuzzy
regra1 = ctrl.Rule(score_serasa['baixo'] & renda_mensal['baixa'], limite_credito['muito_baixo'])
regra2 = ctrl.Rule(score_serasa['baixo'] & renda_mensal['media'], limite_credito['baixo'])
regra3 = ctrl.Rule(score_serasa['baixo'] & renda_mensal['alta'], limite_credito['alto']) 
regra4 = ctrl.Rule(score_serasa['medio'] & renda_mensal['baixa'], limite_credito['baixo'])
regra5 = ctrl.Rule(score_serasa['medio'] & renda_mensal['media'], limite_credito['medio'])
regra6 = ctrl.Rule(score_serasa['medio'] & renda_mensal['alta'], limite_credito['alto'])
regra7 = ctrl.Rule(score_serasa['alto'] & renda_mensal['baixa'], limite_credito['medio'])
regra8 = ctrl.Rule(score_serasa['alto'] & renda_mensal['media'], limite_credito['alto'])
regra9 = ctrl.Rule(score_serasa['alto'] & renda_mensal['alta'], limite_credito['muito_alto'])
#As regras foram formuladas pensando que o cliente com renda baixa nao pode comprometer seu orcamento como um cliente com alta renda.
#Criado 9 regras para compor todas as combinaçoes possiveis usando a lógica 'E' (&).

#Sistema Fuzzy
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9]) 

#Simulação
simulacao = ctrl.ControlSystemSimulation(sistema_controle)  

# Entrada de dados
Renda_Informada = float(input("\nDigite a renda mensal (R$): "))

# Loop para validar o Score
while True:
    Score_Informado = float(input("Digite o Score Serasa (0 a 100 pts): "))
    if 0 <= Score_Informado <= 100:
        # Passando para o sistema fuzzy somente quando válido
        simulacao.input['Score'] = Score_Informado
        simulacao.input['Renda'] = Renda_Informada
        break
    else:
        print("Erro: O Score deve estar entre 0 e 100 pontos. Tente novamente.")

# Cálculo do resultado
simulacao.compute()

# Saída formatada
limite_percentual = simulacao.output['Credito']
limite_reais = round((limite_percentual / 100) * Renda_Informada, -2)

print(f"\nRenda: R${Renda_Informada:.0f} "
      f"\nScore Serasa: {Score_Informado:.0f} pts "
      f"\nLimite de Crédito (%): {limite_percentual:.2f}% da renda mensal "
      f"\nLimite de Crédito Liberado (R$): R$ {limite_reais:.0f}\n")

# #Visualização dos gráficos de pertinência
# score_serasa.view(simulacao)
# renda_mensal.view(simulacao)
# limite_credito.view(simulacao)
# plt.show()

