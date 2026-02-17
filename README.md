# 🔮 End-to-End Churn Prediction System

## 💼 O Problema de Negócio
Uma empresa de Telecomunicações enfrenta uma taxa de cancelamento (Churn) elevada. O objetivo deste projeto foi desenvolver uma solução completa de Dados para identificar clientes em risco e permitir ações preventivas do time de Marketing.

## 🛠️ A Solução (Arquitetura)
Diferente de abordagens tradicionais baseadas apenas em notebooks, este projeto simula um ambiente corporativo real:
1. **Engenharia de Dados:** Banco MySQL dockerizado para simular o ERP transacional.
2. **ETL & SQL:** Extração e agregação de dados complexos (logs de uso) via SQL Window Functions.
3. **Machine Learning:** Pipeline Scikit-Learn com Random Forest (Recall de 98% na validação).
4. **Deploy:** Aplicação Web interativa em Streamlit para uso do usuário final.

## 🚀 Como Rodar
1. Suba o banco de dados:
   `docker-compose up -d`
2. Gere os dados simulados:
   `python gerar_dados.py`
3. Instale as dependências:
   `pip install -r requirements.txt`
4. Execute o App:
   `streamlit run app.py`

## 📊 Resultados
O modelo focou na métrica de **Recall**, priorizando a identificação da maior quantidade possível de cancelamentos reais para maximizar a retenção de receita.

## 📷 Screenshots
<img width="825" height="869" alt="image" src="https://github.com/user-attachments/assets/19fb962a-0f69-4250-bcad-214d2ee6d4ff" />
