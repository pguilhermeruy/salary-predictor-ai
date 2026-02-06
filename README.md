# 💰 Tech Salary Predictor - People Analytics
🔗 **Acesse o Projeto Online:** [Clique aqui para testar](https://salary-predictor-ai-guilhermeruy.streamlit.app/)

Uma ferramenta de Inteligência Artificial voltada para RH e Gestão, desenvolvida para estimar budgets de contratação de forma baseada em dados (Data Driven).

## Objetivo
Prever automaticamente a faixa salarial ideal para um candidato com base no tempo de experiência, auxiliando na definição de propostas justas e competitivas. O sistema analisa:
- Anos de Experiência
- Tendência de mercado (Histórico)

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Streamlit:** Para construção da interface web e dashboards de métricas.
- **Scikit-Learn:** Para implementação do algoritmo de Regressão Linear.
- **Pandas:** Para estruturação dos dados históricos de mercado.

## Como Funciona
O modelo utiliza um algoritmo de **Regressão Linear Simples**. Ele foi treinado com uma base de dados histórica para identificar a correlação entre "Tempo de Experiência" e "Remuneração". Com isso, o sistema traça uma linha de tendência capaz de projetar salários para qualquer nível de senioridade inserido na ferramenta.

## Como Executar Localmente
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Execute a aplicação:
   ```bash
   streamlit run salario.md

https://salary-predictor-ai-guilhermeruy.streamlit.app/

