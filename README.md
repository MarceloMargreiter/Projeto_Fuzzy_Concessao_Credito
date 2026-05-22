

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
- Desenvolver um sistema que receba dois dados: ***Renda Mensal*** e ***Score do Serasa***, e devolva o **Limite de Crédito Sugerido**.

- Método: ***Lógica Fuzzy*** 



##  Regras do negócio: 
