#import dependencies 
import openai
import streamlit as st
from streamlit_chat import message


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
           background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 



def generate_response(prompt):
	completions = openai.Completion.create(
		engine = "text-davinci-003",
		prompt = prompt,
		max_tokens = 1024,
		temperature = 0.5,
		n = 1,	
		stop = None
	)

	message = completions.choices[0].text
	return message

st.title("Smart Assistant")
st.header("Can be dumb if needed :)")
st.subheader("Hey, I am your Smart Assistant so you can use few shot, chain of thought prompting, personality or role prompting. In case you were living under the rock( don't know much about OpenAI, GPT etc) then ask me anything in just a good old search engine way:")

if 'generated' not in st.session_state:
	st.session_state['generated'] = [] 
	
if 'past' not in st.session_state:
	st.session_state['past'] = []

def get_text():
	input_text = st.text_input("Write your text in box below and just hit enter ","",key="input")
	return input_text 

user_input = get_text()

if user_input:
	output = generate_response(user_input)
	st.session_state.past.append(user_input)
	st.session_state.generated.append(output)


if st.session_state['generated']:
	for i in range(len(st.session_state['generated'])-1,-1,-1):
		message(st.session_state["generated"][i], key=str(i))
		message(st.session_state['past'][i],is_user=True, key=str(i) + '_user')








		
