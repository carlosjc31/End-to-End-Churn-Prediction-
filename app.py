import streamlit as st
import joblib
import pandas as pd
import numpy as np

# --- 1. CONFIGURAÇÃO DA PÁGINA (OBRIGATÓRIO SER O PRIMEIRO COMANDO ST) ---
st.set_page_config(
    page_title="Sistema de Previsão de Churn",
    page_icon="🔮",
    layout="wide" # Dica de Pro: Deixa o site mais largo e bonito
)

# --- 2. Carregar o Modelo Salvo ---
@st.cache_resource
def load_model():
    # Tenta carregar o modelo. Se não achar, avisa o usuário (tratamento de erro profissional)
    try:
        return joblib.load('modelo_churn.joblib')
    except FileNotFoundError:
        st.error("Erro: O arquivo 'modelo_churn.joblib' não foi encontrado. Rode o notebook de treino primeiro!")
        return None

model = load_model()

# --- 3. Interface do Usuário ---
st.title("🔮 Detector de Risco de Churn")
st.markdown("""
<style>
    .big-font { font-size:20px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Insira os dados do cliente para calcular a probabilidade de cancelamento.</p>', unsafe_allow_html=True)
st.divider() # Linha divisória bonita

# Layout em Colunas (Parece muito mais profissional)
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Dados Cadastrais")
    genero = st.selectbox('Gênero', ['M', 'F'])
    idade = st.slider('Idade', 18, 80, 30)
    estado = st.selectbox('Estado', ['SP', 'RJ', 'MG', 'RS', 'SC']) 
    plano = st.selectbox('Plano Atual', ['Basico', 'Premium', 'Familia'])

with col2:
    st.subheader("📊 Comportamento de Uso")
    valor_mensal = st.number_input('Valor Mensal (R$)', min_value=0.0, value=59.90, step=10.0)
    meses_contrato = st.number_input('Meses de Contrato', min_value=0, value=12)
    media_consumo = st.number_input('Média de Consumo (GB)', min_value=0.0, value=10.0)
    chamadas_suporte = st.number_input('Total de Chamadas ao Suporte', min_value=0, value=0)

# Criar o DataFrame para a IA
input_df = pd.DataFrame({
    'genero': [genero],
    'idade': [idade],
    'estado': [estado],
    'plano': [plano],
    'valor_mensal': [valor_mensal],
    'meses_contrato': [meses_contrato],
    'media_consumo_gb': [media_consumo],
    'total_chamadas_suporte': [chamadas_suporte]
})

# Botão de Ação (Centralizado)
st.write("")
if st.button('🚀 Calcular Risco de Churn', use_container_width=True):
    if model:
        # Fazer a previsão
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)
        
        churn_prob = probability[0][1] # Pega a chance de ser 1
        
        st.divider()
        st.subheader("Resultado da Análise")
        
        # Mostrador visual (Progress Bar)
        st.progress(int(churn_prob * 100))
        
        if churn_prob > 0.5:
            st.error(f"🚨 **ALERTA DE CHURN!**")
            st.metric(label="Probabilidade de Saída", value=f"{churn_prob:.1%}", delta="-Risco Alto")
            st.write("💡 **Sugestão:** O cliente apresenta sinais claros de insatisfação. Ofereça um upgrade gratuito ou desconto imediato.")
        else:
            st.success(f"✅ **CLIENTE SEGURO**")
            st.metric(label="Probabilidade de Saída", value=f"{churn_prob:.1%}", delta="Seguro")
            st.write("💡 **Sugestão:** O cliente está engajado. Ótimo momento para oferecer produtos adicionais (Cross-sell).")
    else:
        st.warning("O modelo não foi carregado corretamente.")

