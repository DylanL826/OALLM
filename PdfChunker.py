from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
import constants

file_path = constants.OA_pdf_file_path
loader = PyPDFLoader(file_path)
pages = []
raw_text = ''
api_key = constants.openAI_API_Key
for page in loader.lazy_load():
    pages.append(page)
    raw_text += page.page_content

vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings(api_key=api_key))
docs = vector_store.similarity_search("Beta Blocker", k=2)

for doc in docs:
    print(f'Page {doc.metadata["page"]}: {doc.page_content[:300]}\n')
# OpenAI embeddings to vectorize document
# https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html
