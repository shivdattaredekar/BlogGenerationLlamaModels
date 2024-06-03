# Generate Blogs with Llama 2 Model

This project is a Streamlit application that generates blog posts based on user input using the Llama 2 model. The application allows users to input a topic, specify the number of words, and select the writing style. The Llama 2 model then generates a blog post based on these inputs.

https://github.com/shivdattaredekar/BlogGenerationLlamaModels/assets/46707992/e3a3ba6e-7b22-46d9-8e0d-80ce4dd026fe

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Interactive User Interface**: Simple and intuitive interface built with Streamlit.
- **Customizable Blog Generation**: Users can input the topic, number of words, and writing style.
- **Llama 2 Model Integration**: Utilizes the Llama 2 model for generating high-quality blog posts.

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create and activate a virtual environment** (optional but recommended)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download and place the Llama 2 model**
   - Ensure that you have the Llama 2 model file (`llama-2-7b-chat.ggmlv3.q8_0.bin`) downloaded and placed in the `models` directory.

## Usage

1. **Run the Streamlit application**
    ```bash
    streamlit run app.py
    ```

2. **Interact with the application**
   - Open your web browser and go to `http://localhost:8501`.
   - Enter the blog topic in the input field.
   - Specify the number of words for the blog post.
   - Select the writing style from the dropdown menu.
   - Click on "Generate Blog" to see the generated blog post.

## Configuration

You can configure the model and Streamlit settings by modifying the following sections in the `app.py` file:

- **Model Configuration**:
    ```python
    llm = CTransformers(model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={"temperature": 0.01, "max_new_tokens": 256})
    ```

- **Streamlit Page Configuration**:
    ```python
    st.set_page_config(
        page_title="Generate Blogs",
        page_icon="🧑‍💻",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
    ```

## Dependencies

- **Streamlit**: For building the interactive user interface.
- **Langchain**: For creating prompt templates.
- **langchain_community**: For calling the Llama 2 model.

You can find all dependencies listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or feedback, please contact:

- **Shivdatta Redekar**: [shivdattaredekar@gmail.com](mailto:shivdattaredekar@gmail.com)

