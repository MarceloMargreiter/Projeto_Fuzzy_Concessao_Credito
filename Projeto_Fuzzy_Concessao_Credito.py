import numpy as np  
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import scipy as sp

#Antecedentes / Variáveis de entrada
score_serasa = ctrl.Antecedent(np.arange(0, 1001, 1), 'Score')
renda_mensal = ctrl.Antecedent(np.arange(0, 100001, 1), 'Renda')
status_credito = ctrl.Consequent(np.arange(0, 101, 1), 'Status')


#Consequente / Variável de saída
limite_credito = ctrl.Consequent(np.arange(0, 101, 1), 'Credito')


#Funções de pertinência para score serasa
score_serasa['baixo'] = fuzz.trimf(score_serasa.universe, [0, 0, 500])
score_serasa['medio'] = fuzz.trimf(score_serasa.universe, [0, 500, 1000])
score_serasa['alto'] = fuzz.trimf(score_serasa.universe, [500, 1000, 1000])  

#Funçoes de pertinência para status de crédito
status_credito['reprovado'] = fuzz.trapmf(status_credito.universe, [0, 0, 30, 70])
status_credito['aprovado'] = fuzz.trapmf(status_credito.universe, [30, 70, 100, 100])


#Funções de pertinência para renda mensal
renda_mensal['baixa'] = fuzz.trapmf(renda_mensal.universe, [0, 0, 5000, 25000])
renda_mensal['media'] = fuzz.trapmf(renda_mensal.universe, [5000, 20000, 30000, 45000])
renda_mensal['alta'] = fuzz.trapmf(renda_mensal.universe, [25000, 45000, 100000, 100000])     


#Funções de pertinência para limite de crédito (será o % da renda mensal na parcela)
limite_credito['muito_baixo'] = fuzz.trimf(limite_credito.universe, [0, 12, 24]) 
limite_credito['baixo'] = fuzz.trimf(limite_credito.universe, [12, 24, 36])
limite_credito['medio'] = fuzz.trimf(limite_credito.universe, [24, 36, 48])
limite_credito['alto'] = fuzz.trimf(limite_credito.universe, [36, 48, 60])
limite_credito['muito_alto'] = fuzz.trimf(limite_credito.universe, [48, 60, 60]) # limite superior inferior a 100% para näo comprometer muito mais que 60% da renda mensal.    



#Regras Fuzzy
regra1 = ctrl.Rule(renda_mensal['baixa'] & score_serasa['baixo'], limite_credito['muito_baixo'])
regra2 = ctrl.Rule(renda_mensal['baixa'] & score_serasa['medio'], limite_credito['baixo'])
regra3 = ctrl.Rule(renda_mensal['baixa'] & score_serasa['alto'], limite_credito['medio']) 
regra4 = ctrl.Rule(renda_mensal['media'] & score_serasa['baixo'], limite_credito['baixo'])
regra5 = ctrl.Rule(renda_mensal['media'] & score_serasa['medio'], limite_credito['medio'])
regra6 = ctrl.Rule(renda_mensal['media'] & score_serasa['alto'], limite_credito['alto'])
regra7 = ctrl.Rule(renda_mensal['alta'] & score_serasa['baixo'], limite_credito['baixo'])
regra8 = ctrl.Rule(renda_mensal['alta'] & score_serasa['medio'], limite_credito['alto'])
regra9 = ctrl.Rule(renda_mensal['alta'] & score_serasa['alto'], limite_credito['muito_alto'])
#As regras foram formuladas pensando que o cliente com renda baixa nao pode comprometer seu orcamento como um cliente com alta renda.
#Criado 9 regras para compor todas as combinaçoes possiveis usando a lógica 'E' (&).

# Critérios: score muito baixo ou renda baixa tendem a reprovar
regra10 = ctrl.Rule(score_serasa['baixo'] & renda_mensal['baixa'], status_credito['reprovado'])
regra11 = ctrl.Rule(score_serasa['baixo'] & renda_mensal['media'], status_credito['reprovado'])
regra12 = ctrl.Rule(score_serasa['medio'] & renda_mensal['baixa'], status_credito['reprovado'])
regra13 = ctrl.Rule(score_serasa['alto'] & renda_mensal['media'], status_credito['aprovado'])
regra14 = ctrl.Rule(score_serasa['alto'] & renda_mensal['alta'], status_credito['aprovado'])
regra15 = ctrl.Rule(score_serasa['medio'] & renda_mensal['alta'], status_credito['aprovado'])


#Sistema Fuzzy
sistema_controle = ctrl.ControlSystem([
    regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9,
    regra10, regra11, regra12, regra13, regra14, regra15
])


#Simulação
simulacao = ctrl.ControlSystemSimulation(sistema_controle)  


# Entrada de dados
# Loop para validar a renda mensal, em caso de digitação errada, aceitando somente valores positivos (maior que 0(zero)).
while True:
    Renda_Informada = float(input("\nDigite a renda mensal (R$): "))
    if Renda_Informada > 0:
        break
    else:
        print("A renda mensal deve ser um valor positivo. Tente novamente.")

# Loop para validar o Score, em caso de digitaçao errada, Score entre 0 e 1000pts.
while True:
    Score_Informado = float(input("Digite o Score Serasa (0 a 1000 pts): "))
    if 0 <= Score_Informado <= 1000:
        simulacao.input['Score'] = Score_Informado
        simulacao.input['Renda'] = Renda_Informada
        break
    else:
        print("O Score deve estar entre 0 e 1000 pontos. Tente novamente.")



# Cálculo Fuzzy
simulacao.compute()



# Saída formatada
limite_percentual = simulacao.output['Credito']
limite_reais = round((limite_percentual / 100) * Renda_Informada, 2)

# Avaliação de status
status_final = simulacao.output['Status']
resultado = "Liberação de crédito APROVADA!" if status_final >= 40 else "Liberação de crédito REPROVADA!"

print(
    f"\nRenda informada: R${Renda_Informada:.0f}"
    f"\nScore Serasa informado: {Score_Informado:.0f} pts"
    f"\nLimite de Crédito (%): {limite_percentual:.1f}% da renda mensal"
    f"\nLimite da Parcela Mensal (R$): R$ {limite_reais:.2f}"
    f"\nValor Limite Total de Crédito Liberado (R$): R$ {round(limite_reais * 12, -2):.0f}"
    f"\nStatus da análise de crédito: {resultado}\n"
)


#Visualização dos gráficos 
score_serasa.view(simulacao)
renda_mensal.view(simulacao)
limite_credito.view(simulacao)
status_credito.view(simulacao)
plt.show()
