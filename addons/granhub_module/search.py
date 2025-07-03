from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os

# 1. Define a schema for your documents
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)

# 2. Create an index directory
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

# 3. Create the index
ix = create_in("indexdir", schema)

# 4. Add documents to the index
writer = ix.writer()
writer.add_document(title="First Document", path="/a", content="This is the first document in Granhub.")
writer.add_document(title="Second Document", path="/b", content="Another document.")
writer.add_document(title="Third Document", path="/c", content="A third document.")
writer.commit()

# 5. Search the index
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("python")
    results = searcher.search(query)
    for hit in results:
        print(f"Title: {hit['title']}, Path: {hit['path']}")

    query = QueryParser("content", ix.schema).parse("Granhub")
    results = searcher.search(query)
    for hit in results:
        print(f"Title: {hit['title']}, Path: {hit['path']}")