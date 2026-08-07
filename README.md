# Document Reader Using RAG

This project demonstrates how to build a document-based RAG application with LangChain, OpenAI, Tavily, and a vector store such as Pinecone or Chroma.

## 1. Project goal

The application reads documentation, stores it in a searchable vector database, and answers questions using an LLM. The workflow is:

1. Crawl documentation
2. Extract and clean the text
3. Split the text into chunks
4. Create embeddings
5. Store embeddings in a vector database
6. Retrieve the most relevant chunks for the user question
7. Generate an answer with an LLM
8. Display the answer and sources in a UI

## 2. Setup

### Install dependencies

Run:

```bash
uv sync
```

### Create a `.env` file

Create a `.env` file in the project root with the following values:

```env
LANGSMITH_TRACING=
LANGSMITH_ENDPOINT=
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=
TAVILY_API_KEY=
OPENAI_API_KEY=
PINECONE_API_KEY=
INDEX_NAME=
```

### Create a Pinecone index

Before running the ingestion pipeline:

1. Log in to Pinecone
2. Create a new API key
3. Create a new index
4. Copy the index name into `INDEX_NAME`

## 3. Step-by-step guide to understand the code

### Step 1: Understand the ingestion flow

The ingestion part is responsible for converting raw documents into indexed vectors.

In this stage:

- Import the required packages
- Create an SSL context with `certifi`
- Initialize OpenAI embeddings
- Initialize a vector store such as Pinecone or Chroma
- Use Tavily tools such as `TavilyCrawl`, `TavilyMap`, and `TavilyExtract` to crawl and extract documentation
- Split the content into smaller chunks using `RecursiveCharacterTextSplitter`
- Generate embeddings for each chunk
- Insert the chunks into the vector store

Typical file responsibility:

- `ingestion.py`: crawl, extract, chunk, embed, and index documents

### Step 2: Understand the retrieval flow

The retrieval part is responsible for finding the most relevant chunks for a user query.

In this stage:

- Load the embedding model
- Load the vector store
- Accept the user question
- Run a similarity search
- Retrieve the top relevant documents
- Pass those documents to the LLM as context

Typical file responsibility:

- `retrieval.py` or similar: retrieve relevant documents and build the answer context

### Step 3: Understand the LLM agent flow

The LLM agent combines the user question with the retrieved context to create a final answer.

In this stage:

- Initialize the chat model
- Define a system prompt
- Create an agent or chain
- Send the question and context to the model
- Return the answer and the source documents

### Step 4: Understand the UI flow

The UI lets users interact with the RAG system.

In this stage:

- Use Streamlit to build the chat page
- Store chat messages in session state
- Show the user’s question and the model’s answer
- Show source documents below the answer
- Allow the user to continue the conversation

Typical file responsibility:

- `main.py` or similar: user interface and chat flow

## 4. Key code items to learn

- `TavilyCrawl`, `TavilyMap`, `TavilyExtract`: used to collect documentation content
- `RecursiveCharacterTextSplitter`: splits documents into smaller chunks
- `OpenAIEmbeddings`: converts text into embeddings
- `PineconeVectorStore` or `Chroma`: stores and retrieves embeddings
- `init_chat_model`: initializes the LLM chat model
- `streamlit`: builds the web-based chat interface

## 5. End-to-end flow

```text
Documentation source
  -> crawl and extract
  -> split into chunks
  -> create embeddings
  -> store in vector database
  -> retrieve relevant context
  -> generate answer with LLM
  -> show answer and sources in UI
```

## 6. How to run the project

1. Run the ingestion step to build the vector index
2. Start the app
3. Ask questions about the documentation

Example commands:

```bash
uv sync
```

If your project uses a separate ingestion script and app script, run them as described in your local project files.

## 7. Notes

- Batch size should be chosen carefully to avoid rate limit errors
- Use a reasonable chunk size and overlap
- Keep the retrieved context relevant before sending it to the LLM
- If Pinecone is not required, Chroma can be used instead
