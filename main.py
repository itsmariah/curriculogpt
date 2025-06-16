import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="CurriculoGPT")

st.title("CurriculoGPT - Seu currículo com inteligência!")
st.markdown("Otimize seu resumo profissional e carta de apresentação com IA.")

# 1 - Entradas do usuário
nome = st.text_input("Nome completo:")
formacao = st.text_area("Formação acadêmica:")
experiencias = st.text_area("Experiências profissionais:")
habilidades = st.text_area("Habilidades e competências:")

# 2 - Configuração da API Gemini
try:
    genai.configure(api_key=st.secrets["api_keys"]["GEMINI_API_KEY"])
    model = genai.GenerativeModel("models/text-bison-001")
except:
    st.error("Erro ao carregar a chave da API. Verifique o arquivo secrets.toml")

# 3 - Geração do Resumo Profissional
if st.button("Gerar Resumo Profissional"):
    if nome and formacao and experiencias and habilidades:
        with st.spinner("Gerando resumo profissional..."):
            prompt_resumo = f"""
            Crie um resumo profissional com base nesses dados:
            Nome: {nome}
            Formação: {formacao}
            Experiências: {experiencias}
            Habilidades: {habilidades}
            Seja direto, profissional e impactante.
            """
            response = model.generate_content(prompt_resumo)
            st.subheader("Resumo Profissional:")
            st.markdown(response.text)
    else:
        st.warning("Por favor, preencha todos os campos antes de gerar o resumo.")

# 4 - Geração da Carta de Apresentação
if st.button("Gerar Carta de Apresentação"):
    if nome and formacao and experiencias and habilidades:
        with st.spinner("Gerando carta de apresentação..."):
            prompt_carta = f"""
            Crie uma carta de apresentação personalizada com os dados abaixo:
            Nome: {nome}
            Formação: {formacao}
            Experiências: {experiencias}
            Habilidades: {habilidades}
            A carta deve ser amigável, mas profissional, como se fosse enviada para uma empresa de tecnologia.
            """
            response = model.generate_content(prompt_carta)
            st.subheader("Carta de Apresentação:")
            st.markdown(response.text)
    else:
        st.warning("Preencha todos os campos antes de gerar a carta.")
