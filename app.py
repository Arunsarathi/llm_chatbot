import streamlit as st
import openai

# Custom CSS for modern styling, animations, and background images
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main-title {
        font-size: 3rem;
        color: #007bff;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
        animation: fadeInDown 1s ease-in-out;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .input-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        animation: fadeInUp 1s ease-in-out;
    }
    .response-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        color: #343a40;
        opacity: 0;
        animation: fadeIn 1s forwards;
    }
    .stTextInput label {
        font-size: 1.2rem;
        font-weight: bold;
        color: #007bff;
    }
    .stButton button {
        background-color: #007bff;
        color: #ffffff;
        border-radius: 12px;
        font-size: 1rem;
        padding: 8px 16px;
        border: none;
        box-shadow: 0px 4px 10px rgba(0, 123, 255, 0.5);
        animation: pulse 1.5s infinite;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .conversation-history {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
    }
    .user-message {
        background-color: #e7f1ff;
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 10px;
        color: #0056b3;
        animation: fadeInRight 0.5s ease-in-out;
    }
    .bot-message {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 10px;
        color: #343a40;
        animation: fadeInLeft 0.5s ease-in-out;
    }
    /* Animations */
    @keyframes fadeIn {
        to {
            opacity: 1;
        }
    }
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    @keyframes fadeInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    @keyframes pulse {
        0% {
            box-shadow: 0 0 10px rgba(0, 123, 255, 0.4);
        }
        50% {
            box-shadow: 0 0 20px rgba(0, 123, 255, 0.6);
        }
        100% {
            box-shadow: 0 0 10px rgba(0, 123, 255, 0.4);
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Main Title with Animation
st.markdown('<div class="main-title">🤖 Meet Lucy: Your Modern Chatbot Companion</div>', unsafe_allow_html=True)

# Sidebar with GIF instead of a static image
st.sidebar.image("https://media.giphy.com/media/3o7aD6syaCDMBP4sTS/giphy.gif", use_column_width=True)  # Add your GIF URL here
st.sidebar.title("🔧 Settings")

# Check if API key is already in session state
if 'api_key' not in st.session_state:
    st.session_state['api_key'] = ""

# API Key input only if it's not already stored
if not st.session_state['api_key']:
    api_key_input = st.sidebar.text_input("OpenAI API Key", type="password", placeholder="Enter your OpenAI API key here")
    if api_key_input:
        st.session_state['api_key'] = api_key_input  # Store the API key in session state
        st.success("API Key saved successfully!")
else:
    st.sidebar.write("🔒 API Key stored securely.")
    
# Clear API Key button
if st.sidebar.button("Clear API Key"):
    st.session_state['api_key'] = ""
    st.sidebar.warning("API Key cleared! Please re-enter to continue.")

model = st.sidebar.selectbox(
    "Select Model",
    options=["gpt-3.5-turbo", "gpt-4"],
    help="Choose the OpenAI model you want to use."
)

# Slider for controlling response length
response_length = st.sidebar.slider(
    "Response Length",
    min_value=50,
    max_value=500,
    value=150,
    step=10,
    help="Select the length of the response in number of tokens."
)

# Initialize session state for storing questions and answers
if 'qa_history' not in st.session_state:
    st.session_state.qa_history = []

# Initialize session state for input handling separately
if 'temp_input' not in st.session_state:
    st.session_state.temp_input = ""

# Input field for user question with improved UI
st.markdown('<div class="input-box">', unsafe_allow_html=True)
st.session_state.temp_input = st.text_input("You: ", value=st.session_state.temp_input, placeholder="Ask anything to Lucy...")
st.markdown('</div>', unsafe_allow_html=True)

# Define function to get response from OpenAI GPT
def get_response(api_key, model, user_input, response_length):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": user_input}],
        max_tokens=response_length
    )
    return response.choices[0].message['content']

# Submit button with modern look
if st.button('Submit', key='submit'):
    user_input = st.session_state.temp_input
    api_key = st.session_state['api_key']  # Retrieve the stored API key
    
    if api_key and user_input:  # Check for API key and user input
        try:
            response = get_response(api_key, model, user_input, response_length)
            st.session_state.qa_history.append({"question": user_input, "answer": response})
            st.markdown(f'<div class="response-box"><b>Lucy:</b> {response}</div>', unsafe_allow_html=True)
            # Clear the input field by resetting temp_input
            st.session_state.temp_input = ""  # Automatically clear input after submission
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        if not api_key:
            st.warning("Please enter your OpenAI API key.")
        if not user_input:
            st.warning("Please enter a question.")

# Display the history of questions and answers with animation
if st.session_state.qa_history:
    st.markdown('<div class="conversation-history">', unsafe_allow_html=True)
    st.markdown("### Conversation History")
    for qa in st.session_state.qa_history:
        st.markdown(f'<div class="user-message"><b>You:</b> {qa["question"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-message"><b>Lucy:</b> {qa["answer"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

