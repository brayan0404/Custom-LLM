"""
voy a crear una aplicacion que me permita fijar desde la interfaz
los siguientes datos del modelo.

-La temperatura
-La instrucion del Template

Mas adelante me permitirá fijar:
-El tipo de memoria
    -dependiendo de si escoge un tipo de memoria que elija los 
    parametros de esa memoria, por ejemplo el numero de mensajes
    que quiere guardar.

"""

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


st.title("Custom LLM")

openai_api_key = st.sidebar.text_input("Coloca tu Api de OpenAI")
model_name = st.sidebar.selectbox("Large Language Model", ["text-davinci-003", "gpt-3.5-turbo"])
temperature = st.sidebar.slider("Elige la temperature", 0.0,1.0)
instructions = st.sidebar.text_area("Comportamiento")


def response(user_text):
    llm = OpenAI(
        temperature=temperature,
        model_name = model_name,
        openai_api_key=openai_api_key, 
        )
    
    prompt = PromptTemplate(
        input_variables=["input"],
       template = instructions + "  {input}. Asistente: "
    )

    #final_promp = prompt.format(input=user_text)
    chain = LLMChain(
        llm=llm, 
        prompt=prompt,
        )
    st.info(chain.run(user_text))
    
with st.form("forms"):
    user_input = st.text_input("En que te puedo ayudar", )
    if st.form_submit_button("Enviar"):
        response(user_input)