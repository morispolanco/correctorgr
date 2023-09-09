import streamlit as st
import openai

st.title('Corrector gramatical y de puntuación')

openai.api_key = st.sidebar.text_input('Ingresa tu API Key de OpenAI', type='password')

texto = st.text_area('Ingresa el texto a corregir')

if st.button('Corregir texto'):
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'Corrige los errores gramaticales y de puntuación en este texto: {texto}',
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    correccion = response.choices[0].text.strip()
    
    st.text_area('Texto corregido', value=correccion, height=400)
