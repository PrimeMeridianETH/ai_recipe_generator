# Install dependencies

# Import dependencies
import openai
import streamlit as st

# Set the OpenAI secret key
openai.api_key = st.secrets['pass']

st.header('AI Recipe Generator')
st.subheader('current version : beta 0.1')

# Set the if, else loop including prompt
article_text = st.text_area('Please enter your available ingredients (include proportions if you can!)')
if len(article_text) > 5:
    temp = st.slider("temperature", 0.2, 0.5, 0.8)
    if st.button ('Generate Recipe'):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Create a recipe. Use only the ingredients provided to design the recipe, as the intended purpose is for someone with limited materials on hand. use only the information (ingredients) here to create the recipe: " + article_text,
            max_tokens = 3000,
            presence_penalty=0.8,
            frequency_penalty=0.6,
            temperature = temp
        )
        res = response["choices"][3]["text"]
        st.info(res)

        st.download_button("Download result", res)
else: st.warning("The supplied information is not large enough")
