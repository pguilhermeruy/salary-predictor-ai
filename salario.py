import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Tech Salary Predictor", page_icon="📈")
st.title("Tech Salary Predictor - People Analytics") 
st.write("Sistema de Inteligência Artificial para planejamento de Orçamento.")

dados = {
'Anos' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Salario' : [2500, 2700, 3000, 3100, 3400, 3800, 4100, 4900, 5200, 6000]
}
df = pd.DataFrame(dados)

with st.expander("Visualizar Dados Históricos"):
    st.write("Gráfico usado para o treinamento:")
    st.scatter_chart(data=df, x= 'Anos', y= 'Salario')

x = df[['Anos']]
y = df['Salario']

modelo = LinearRegression()
modelo.fit(x, y)

anos_selecionados = st.sidebar.slider("Insira os anos de experiência", 0, 30, 0)

if st.button("Prever Salário"):
    previsao = modelo.predict([[anos_selecionados]])  
    salario_estimado = previsao[0]
    st.metric(label="Salário estimado", value=f"R$ {salario_estimado:.2f}")
    