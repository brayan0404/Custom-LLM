import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


st.title("Custom LLM")
st.text("Observa como afectan los parametros que configuras en el llm")

openai_api_key = st.sidebar.text_input("Coloca tu Api de OpenAI")
if openai_api_key == False:
    st.sidebar.warning("Coloca tu clave de OpenAI")

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
