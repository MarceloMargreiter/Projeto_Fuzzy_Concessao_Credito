

# **Sistema de Concessão de Crédito Automatizado**
**Componente curricular Tópicos Avançados - UNOESC - 2026**


## Tecnologias utilizadas
- Python 3.11.9
- VS Code   ( *IDE (Ambiente de Desenvolvimento Integrado)* )
- matplotlib
- networkx
- numpy
- scipy
- scikit-fuzzy


## Como executar o projeto:

* ### Apontar para onde o repositório será clonado localmente:
Digite no Terminal:
```bash
cd "caminho onde o repositório será clonado. (Ex.: "C:/Nova Pasta")
```

* ### Clonar Projeto
Copiar o endereço do projeto e clonar usando o Terminal do VS Code.
```bash 
Git clone "https://github.com/MarceloMargreiter/Projeto_Fuzzy_Concessao_Credito.git"
```

* ### Acessar o repositório clonado:
```bash
cd .\Projeto_Fuzzy_Concessao_Credito\
```
 

* ### Criar Variável de Ambiente (.venv): 
Digite no Terminal:
```bash
python -m venv .venv
```    

* ### Ativar a Variável criada:

#### **Windows:**  
```bash
.venv\Scripts\activate
```
   
#### **Linux ou MacOS:**   
```bash
source .venv/bin/activate
```
### Atualize o PIP 
PIP é o gerenciador de pacotes Python.
```bash
python.exe -m pip install --upgrade pip
```

* ### Instale os pacotes necessários no ambiente virtual:

```bash
pip install -r requirements.txt
``` 




## Problemas
- Tendo em vista a alta demanda para avaliação e liberação de limite de crédito de uma empresa *Fintech* onde a varredura por dados e análise humana são morrosas, necessita alguma melhoria para melhor atender os seus clientes.


## Requisitos do negócio
- Desenvolver um sistema que receba dois dados: ***Renda Mensal*** e ***Score do Serasa***, e devolva o **Limite de Crédito Sugerido**, e a ***aprovação*** ou ***reprovação*** do crédito conforme análise.

- Método: ***Lógica Fuzzy*** 

 
##  Regras do negócio: 
### 1. Definição dos Termos Linguísticos
#### → Renda Mensal

- **Baixa:** até R$ 25.000
- **Média:** entre R$ 5.000 e R$ 45.000
- **Alta:** acima de R$ 25.000

*Obs.: os valores se sobrepõem para uma melhor avaliação*

### → Score Serasa

- **Baixo:** até 500 pontos
- **Médio:** entre 500 e 800 pontos
- **Alto:** acima de 800 pontos

*Obs.: os valores se sobrepõem para uma melhor avaliação*

### → Status de Crédito

- **Reprovado:** cliente não atende aos critérios mínimos de score e renda.
- **Aprovado:** cliente apresenta condições favoráveis para liberação de crédito.

### → Limite de Crédito (percentual da renda)

- **Muito Baixo:** até 24% da renda mensal
- **Baixo:** entre 24% e 36%
- **Médio:** entre 36% e 48%
- **Alto:** entre 48% e 60%
- **Muito Alto:** acima de 60% (limitado para não comprometer mais que 60% da renda).

*Obs: Os percentuais de avaliação de limite de crédito são pensados para que indivíduos com renda baixa obtenham um compromentimento menor de seu orçamento mensal perante a dívida do empréstimo solicitado, tendo em vista que há um limite para suprir os nível básicos de alimentação, higiene e saúde. Entendendo que pessoas com maior poder aquisitivo poderão assim comprometer um percentual maior de dívida sobre o seu orçamento, garantindo uma melhor taxa de clientes adimplentes.*

### 2. Base de Regras
A lógica fuzzy foi construída com base em combinações entre **renda** e **score**. 

***Exemplos de regras:***

Se a renda é baixa e o score é baixo, então o limite de crédito é muito baixo e o status é reprovado.

Se a renda é baixa e o score é médio, então o limite de crédito é baixo e o status é reprovado.

Se a renda é média e o score é alto, então o limite de crédito é alto e o status é aprovado.

Se a renda é alta e o score é médio, então o limite de crédito é alto e o status é aprovado.

Se a renda é alta e o score é alto, então o limite de crédito é muito alto e o status é aprovado.

Essas regras foram formuladas para refletir a relação entre capacidade de pagamento e risco de inadimplência.

### 3. Funções de Pertinência
***Renda Mensal:*** funções trapezoidais, permitindo transições suaves entre baixa, média e alta.

***Score Serasa:*** funções triangulares, representando faixas bem definidas de risco.

***Limite de Crédito:*** funções triangulares, distribuídas em intervalos percentuais da renda.

***Status de Crédito:*** funções trapezoidais, com duas categorias (aprovado e reprovado), permitindo sobreposição em casos limítrofes.

Dessa forma, o sistema fuzzy consegue não apenas sugerir um limite de crédito proporcional à renda e score, mas também emitir uma decisão final sobre aprovação ou reprovação, garantindo maior robustez na análise.