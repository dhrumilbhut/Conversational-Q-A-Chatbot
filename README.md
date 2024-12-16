# Conversational RAG with PDF Uploads and Chat History 📚💬

Welcome to the **Conversational RAG with PDF Uploads and Chat History** project! This Streamlit web app allows you to upload PDF files and interact with their content through a conversational interface. The app leverages advanced language models and retrieval-augmented generation (RAG) techniques to provide accurate and context-aware answers to your questions.

## Features ✨

- **Upload PDF Files**: Easily upload multiple PDF files to the app.
- **Conversational Interface**: Ask questions about the content of the uploaded PDFs and get concise, context-aware answers.
- **Chat History Management**: Maintain a history of your chat sessions for a seamless conversational experience.
- **Customizable Prompts**: Use custom prompts to tailor the behavior of the language model.

## Getting Started 🚀

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/conversational-rag-chatbot.git
    cd conversational-rag-chatbot
    ```

2. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a [.env](http://_vscodecontentref_/0) file in the project directory.
    - Add your Hugging Face token:
      ```env
      HF_TOKEN=your_huggingface_token
      ```

### Running the App

1. **Start the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open your browser** and navigate to `http://localhost:8501` to access the app.

## Usage 🛠️

1. **Enter your Groq API key** in the provided input field.
2. **Upload PDF files** using the file uploader.
3. **Ask questions** about the content of the uploaded PDFs in the text input field.
4. **View the assistant's responses** and chat history.

## Project Structure 📁

- [app.py](http://_vscodecontentref_/1): Main application file.
- [style.css](http://_vscodecontentref_/2): Custom CSS for styling the Streamlit app.
- [requirements.txt](http://_vscodecontentref_/3): List of required Python libraries.
- [.env](http://_vscodecontentref_/4): Environment variables file (not included in the repository).

## Customization 🎨

You can customize the prompts used by the language model to better suit your needs. The prompts are defined in the [app.py](http://_vscodecontentref_/5) file:

- **Contextualize Question Prompt**:
    ```python
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question"
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as it is."
    )
    ```

- **Answer Question Prompt**:
    ```python
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences at most. and keep "
        "the answer concise."
        "\n\n"
        "{context}"
    )
    ```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License.

## Acknowledgements 🙏

- [Streamlit](https://streamlit.io/)
- [Hugging Face](https://huggingface.co/)
- [LangChain](https://github.com/langchain-ai/langchain)

---

Made with ❤️ by [Your Name](https://github.com/yourusername)