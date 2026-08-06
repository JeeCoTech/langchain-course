# Building a RAG Pipeline

## Setup

1. Initialize the repository and install dependencies with `uv`:
   - `uv sync`

2. Create a `.env` file with the following variables:
   - `LANGSMITH_TRACING=`
   - `LANGSMITH_ENDPOINT=`
   - `LANGSMITH_API_KEY=`
   - `LANGSMITH_PROJECT=`
   - `TAVILY_API_KEY=`
   - `OPENAI_API_KEY=`
   - `PINECONE_API_KEY=`
   - `INDEX_NAME=`

3. Log in to Pinecone and create:
   - a new API key
   - a new index

4. Use `mediumblog1.txt` as the sample text document for ingestion.

---

## Section 1: Ingestion (Data Indexing)

Build the ingestion pipeline to index document chunks into Pinecone.

Steps:

- Use `UnstructuredLoader` to load the source file.
- Use `CharacterTextSplitter` to split text into chunks.
- Use `OpenAIEmbeddings` to create embeddings.
- Use `PineconeVectorStore` to store chunks in the index.

Typical flow:

1. Create the loader with the file path, chunk size, and chunking strategy.
2. Load documents with `loader.load()`.
3. Split documents with `text_splitter.split_documents()`.
4. Initialize embeddings with `OpenAIEmbeddings(...)`.
5. Upload chunks to the Pinecone index using `PineconeVectorStore`.

After running the ingestion script, the document chunks should be stored in Pinecone.

---

## Section 2: Retrieval without LCEL

Implement retrieval using the Pinecone vector store and a prompt to the LLM, without LCEL logic.

Steps:

- Import and initialize required libraries:
  - `dotenv`
  - `langchain_core.prompts`
  - `langchain_core.messages`
  - `langchain_openai`
  - `langchain_pinecone`

- Initialize the embeddings model.
- Load the Pinecone vector store with `PineconeVectorStore`, using the index name and embeddings.
- Implement `retrieval_chain_without_lcel`:
  1. Retrieve relevant document chunks using the retriever.
  2. Format the retrieved document text into a context string.
  3. Format the prompt with the context and user question.
  4. Call the LLM and return the response.

---

## Section 3: 2-Step RAG with LCEL

Build a retrieval chain that uses LCEL and a more structured pipeline.

Steps:

- Import `RunnablePassthrough` from `langchain.runnables`.
- Use `itemgetter` to access items without iteration.
- Create `create_retrieval_chain_with_lcel()`:
  - Build a chain with `RunnablePassthrough` for the question and retriever.
  - Format retrieved docs using a pipe splitter.
  - Apply a prompt template.
  - Call the LLM.
  - Parse output with `StrOutputParser` (or similar output parser).

This creates a multi-step RAG pipeline that retrieves documents, formats them, and generates answers with the LLM.
