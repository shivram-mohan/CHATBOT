import streamlit as st
import openai
from streamlit_chat import message


openai.api_key = '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'

st.title("My Chatbot UI")
response_container  = st.container()
container = st.container
#its in this format
#  openai.api_key = open('key.txt','r').read().strip('\n')
st.write("Hello World!")

if 'messages' not in st.session_state:
    st.session_state.messages=[{"role": "system", "content": "You are a helpful assistant."}]
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []


# Codeium: Refactor |Explain| Generate Docstring
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    st.session_state['past'].append(prompt)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["messages"]
    )
    response = completion.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": response})
    st.session_state['generated'].append(response)
    return response


container = st.container()
with container:
    with st.form(key="my_form", clear_on_submit= True):
        user_input = st.text_area("You:", key="input", height = 100 )
        submit_button = st.form_submit_button(label = "Send")
        if submit_button and user_input:
            output = generate_response(user_input)
            # st.write(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
