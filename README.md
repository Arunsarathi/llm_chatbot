# Lucy Chatbot Companion

Lucy Chatbot Companion is a sleek, customizable AI chatbot interface built with Streamlit and OpenAI's GPT models. It offers a dynamic and modern user experience with enhanced CSS styling, animations, and intuitive API management.

## [Demo](https://llmchatbotlucy.streamlit.app/)

You can explore the live demo of Lucy Chatbot on Streamlit by clicking [here](https://llmchatbotlucy.streamlit.app/).

## Features

- **Customizable and Modern UI**: Clean and stylish CSS design with animated elements for a polished, interactive experience.
- **Model Selection**: Switch between "gpt-3.5-turbo" and "gpt-4" models as needed.
- **API Key Management**: Securely enter and store your OpenAI API key, with options to clear and re-enter keys.
- **Response Length Control**: Adjust response length for more concise or detailed answers.
- **Conversation History**: Access past conversations with animations for a fluid user experience.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Launch the app using Streamlit:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter Your OpenAI API Key**:
   - Go to the sidebar and enter your OpenAI API key to start. The key is stored securely in the session.
   - You can clear the key anytime by pressing "Clear API Key."

2. **Choose a Model and Response Length**:
   - Use the sidebar to select between "gpt-3.5-turbo" and "gpt-4" models.
   - Adjust the response length slider to control how detailed the responses are.

3. **Interact with Lucy**:
   - Enter your question in the input box and click "Submit."
   - View Lucy's response and continue the conversation.
   - Previous interactions are saved in the conversation history for easy reference.

## Project Structure

- **app.py**: Main application file with Streamlit UI and OpenAI integration.
- **assets/**: Directory for static assets like images.
- **requirements.txt**: File listing required Python packages.

## Custom CSS Styling

The application uses custom CSS for an enhanced look and feel. Here's a breakdown of some key style elements:

- **Background**: Light grey (`#f5f7fa`) for a soft, clean interface.
- **Buttons**: Modern button design with pulse animation on hover for a professional look.
- **Animations**: Smooth fade-in effects for titles, messages, and other UI elements.

You can modify the CSS in the `<style>` block within `app.py` to further customize the UI.

## Dependencies

The following libraries are required to run the application:
- **Streamlit**: For building the interactive web app.
- **OpenAI**: For accessing the GPT models.

Install them with:
```bash
pip install streamlit openai
```

## Contributing

Feel free to contribute by forking the repository, making improvements, and submitting a pull request. Contributions are welcome for new features, bug fixes, and enhancements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Enjoy interacting with Lucy, your modern chatbot companion!
