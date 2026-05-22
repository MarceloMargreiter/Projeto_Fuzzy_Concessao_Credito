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
limite_credito['muito_baixo'] = fuzz.trimf(limite_credito.universe, [0, 0, 25]) # limite inferior um pouco maior que a média.
limite_credito['baixo'] = fuzz.trimf(limite_credito.universe, [15, 40, 50])
limite_credito['medio'] = fuzz.trimf(limite_credito.universe, [40, 50, 85])
limite_credito['alto'] = fuzz.trimf(limite_credito.universe, [50, 85, 100])
limite_credito['muito_alto'] = fuzz.trimf(limite_credito.universe, [85, 100, 100]) # limite superior um pouco menor que a média.    

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

#Entrada de dados
Renda_Informada = 7000
Score_Informado = 100
simulacao.input['Score'] = Score_Informado   
simulacao.input['Renda'] = Renda_Informada


#Cálculo do resultado
simulacao.compute()
print(f"\nRenda: R${Renda_Informada:.0f} \nLimite de Crédito (%): {simulacao.output['Credito']:.2f}% da renda mensal \nLimite de Crédito Liberado (R$): R$ {round((simulacao.output['Credito'] / 100) * Renda_Informada, -2):.0f}\n")

# #Visualização dos gráficos de pertinência
# score_serasa.view(simulacao)
# renda_mensal.view(simulacao)
# limite_credito.view(simulacao)
# plt.show()

