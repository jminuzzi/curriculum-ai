from __future__ import annotations

import requests
import streamlit as st

try:
    DEFAULT_API_URL = st.secrets['API_URL']
except Exception:
    DEFAULT_API_URL = 'http://127.0.0.1:8000'

st.set_page_config(page_title='Resume Optimizer', page_icon='📄', layout='wide')
st.title('📄 Resume Optimizer')
st.caption('Upload, análise, otimização e preenchimento assistido.')

with st.sidebar:
    st.header('Configuração')
    api_url = st.text_input('API URL', value=DEFAULT_API_URL)
    target_role = st.text_input('Vaga alvo', placeholder='Ex.: Desenvolvedor Python Júnior')

uploaded_file = st.file_uploader('Envie seu currículo (PDF ou TXT)', type=['pdf', 'txt'])

if uploaded_file is not None and st.button('Fazer upload'):
    files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type or 'application/octet-stream')}
    response = requests.post(f'{api_url}/api/upload/', files=files, timeout=60)
    if response.ok:
        data = response.json()
        st.session_state['file_id'] = data['file_id']
        st.success('Upload concluído.')
        st.json(data)
    else:
        st.error(response.text)

file_id = st.session_state.get('file_id') or st.text_input('Ou informe o file_id manualmente')

col1, col2 = st.columns(2)
with col1:
    if st.button('Analisar') and file_id:
        response = requests.post(f'{api_url}/api/analyze/', json={'file_id': file_id, 'target_role': target_role}, timeout=60)
        if response.ok:
            st.subheader('Análise')
            st.json(response.json())
        else:
            st.error(response.text)

with col2:
    if st.button('Otimizar') and file_id:
        response = requests.post(f'{api_url}/api/optimize/', json={'file_id': file_id, 'target_role': target_role}, timeout=60)
        if response.ok:
            data = response.json()
            st.subheader('Currículo otimizado')
            st.code(data['optimized_text'])
            st.caption(f"Salvo em: {data['saved_to']}")
        else:
            st.error(response.text)

st.divider()
st.subheader('Preenchimento assistido')
platform = st.selectbox('Plataforma', ['linkedin', 'gupy', 'catho'])
full_name = st.text_input('Nome completo')
email = st.text_input('E-mail')
phone = st.text_input('Telefone')
summary = st.text_area('Resumo')

if st.button('Executar preenchimento assistido'):
    payload = {
        'platform': platform,
        'full_name': full_name,
        'email': email,
        'phone': phone,
        'summary': summary,
        'dry_run': True,
    }
    response = requests.post(f'{api_url}/api/automate/', json=payload, timeout=60)
    if response.ok:
        st.subheader('Resultado')
        st.json(response.json())
    else:
        st.error(response.text)
