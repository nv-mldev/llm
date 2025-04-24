from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from openai import embeddings

if __name__ == "__main__":
    print("loading initiated")
    loader = TextLoader("kodiaq.txt")
    docs = loader.load()
    print("loading the docs completed")

    print("starting the text splitting using character based splitting")
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.split_documents(documents=docs)
    print(f"created {len(texts)} chunks")
    print("using OpenAI embeddings")
    embeddings = OpenAIEmbeddings()

    print("Ingesting the data to Pinecone Vector DB")
    PineconeVectorStore.from_documents(documents=texts, embedding=embeddings, index_name =  )




