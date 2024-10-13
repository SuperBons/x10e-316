from pinecone import Pinecone,ServerlessSpec
from embeddings_manager import EmbeddingsCreator
import getpass
import os
import time


class PineconeManager():
    
    def __init__(self):
        # initialize connection to pinecone (get API key at app.pinecone.io)
        if(os.getenv("PINECONE_API_KEY") == None):
            os.environ["PINECONE_API_KEY"] = "PINECONEPAIKEY"
        api_key = os.getenv("PINECONE_API_KEY")
        # configure client
        self.pc = Pinecone(api_key=api_key)
        self.spec = ServerlessSpec(
            cloud="aws", region="us-east-1"
        )
        
    def connect_to_vector_db(self):
        pc = self.pc
        index_name = "xten"
        # check if index already exists (it shouldn't if this is first time)
        if index_name not in pc.list_indexes().names():
            # if does not exist, create index
            pc.create_index(
                index_name,
                dimension=1536,  # dimensionality of embed 3
                metric='cosine',
                spec=self.spec
            )
            # wait for index to be initialized
            while not pc.describe_index(index_name).status['ready']:
                time.sleep(1)

        # connect to index
        self.db = pc.Index(index_name)
        time.sleep(1)
        # view index stats
        self.db.describe_index_stats()
        print("Connection Established")
    
    def update_db(self):
        embedingCreate = EmbeddingsCreator()
        ids,embeddings,metadatas = embedingCreate.populate_index()
        for i in range(0,len(embeddings)):
            self.db.upsert(vectors=zip(ids[i], embeddings[i], metadatas[i]))

pineConeManager = PineconeManager()
pineConeManager.connect_to_vector_db()
pineConeManager.update_db()