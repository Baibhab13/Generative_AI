from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader =  DirectoryLoader(
    path = 'books',
    glob="*.pdf",
    loader_cls=PyPDFLoader

)

# Load
# docs = loader.load()

#Lazy_load()
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)

# print(len(docs))

# print(docs[1019].page_content)
# print(docs[1019].metadata)