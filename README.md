# LangChain Course Notes

This guide summarizes the steps covered in the course.

## Section 1: Set up a Python project with UV

Follow these steps to create and configure a Python project using UV.

1. Create a new branch without commit history
   ```bash
   git checkout --orphan <branch-name>
   ```

2. Remove all files using the `rm --rf` command
   ```bash
   rm --rf *
   ```

3. Install UV (package manager for Python created by Rust) using the command
   ```bash
   pip install uv
   ```

4. Initialize UV using the command
   ```bash
   uv init
   ```

5. Add LangChain using the UV as a package manager using the command
   ```bash
   uv add langchain
   ```

6. Create a Virtual Environment for Python using the command
   ```bash
   python -m venv venv
   ```

7. Add necessary packages like `langchain-openai`, `python-dotenv`, `black`, and `sort`
   ```bash
   pip install langchain-openai python-dotenv black sort
   ```

8. Add a `.gitignore` file
   ```bash
   echo "venv/" >> .gitignore
   ```

9. Create a `.env` file with ENV variables that should not be shared and add it as part of `.gitignore`
   ```bash
   echo "ENV_VARIABLES" >> .env
   ```

10. Any missing packages that are present in the `.toml` file can be added using the command
    ```bash
    uv sync
    ```

## Section 2: Using Prompt Templates

In this section, we will use prompt templates to provide a chatbot experience instead of just a single question/answer section.

LangChain chain is the workflow where the output of one can be the input of another.

![alt text](image.png)

We have the information context setup and then we use the prompt template and use the information to the prompt. We create an LLM instance with the chatmodel class of OpenAI by passing the model name, temperature, etc. We using the LangChain chain by Lanchain Expression Language (LCEL) by passing the prompt and llm variable and create a chain. We use the `|` symbol and use the output of the left component as a input of right component. Get the response by calling `chain.invoke` by passing information as the input for the chain.

When we get the response, we get the response as an AIMessage. It contains details like toolcalling, token_usage, etc.

We also learned about the Ollama model. Once we installed Ollama in local, we can use:

- `Ollama list` --> to list the models
- `Ollama pull` --> to pull the model
- `Ollama run` --> to run the model

## Section 3: Integrating with LangSmith

To integrate with LangSmith, create a API key for LangSmith and then use the LangSmith Key in the ENV variable.

- `LANGSMITH_TRACING`
- `LANGSMITH_ENDPOINT`
- `LANGSMITH_API_KEY`
- `LANGSMITH_PROJECT`
- `TAVILY_API_KEY`
- `OPENAI_API_KEY`