import streamlit as st
import google.generativeai as gemini

# Configure the API key for the Generative AI model
file = open("gemini_api_key.txt")
key = file.read()
gemini.configure(api_key=key)

# Initialize the GenerativeModel
model = gemini.GenerativeModel(model_name='gemini-1.5-pro-latest',
                               system_instruction="""You are an AI/ML/Data Science Tutor,
                               consider you have to answers the user only for only datascience related query"""
                              )

st.title("🧠 AI/ML/Data Science Tutor")

# Function to interact with the model and generate responses
def generate_response(user_query):
    ai_response = model.generate_content(user_query)
    return ai_response.text

# Main Streamlit app
def main():
    st.sidebar.title("Options")
    user_query = st.text_input("Enter your query:")
    if st.button("Ask"):
        st.write("User:", user_query)
        ai_response = generate_response(user_query)
        st.write("AI Tutor:", ai_response)

if __name__ == "__main__":
    main()
