import os
from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

# Define a function to generate a response from OpenAI API
def generate_response(user_input):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant.You will just Correct the grammatical error of the user input text"},
                {"role": "user", "content": user_input}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Streamlit app setup
st.title("Grammar Corrector")

# Input field for user text
user_input = st.text_area("Provide text for correction:")

# Button to submit and get a response
if st.button("Submit"):
    if user_input:
        response = generate_response(user_input)
        st.subheader("Corrected Text:")
        st.write(response)

        st.download_button(
            label="Download Corrected Text",
            data=response,  # The corrected text
            file_name="corrected_text.txt",  # The name of the file to download
            mime="text/plain"  # MIME type for text files
        )

    else:
        st.error("Please enter some text.")
