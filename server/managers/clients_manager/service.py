import logging
import pymongo
from flask import Flask
from server.common import ServerException, ErrorCode

logger = logging.getLogger(__name__)


class ClientsManager:
    """Manager for Clients management service"""

    mongodb_client: pymongo.MongoClient
    db_name: set
    clients_collection_name: str
    clients_collection: str

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize Clients manager"""
        if app is not None:
            logger.info("initializing the Clients manager")

            self.db_name=app.config["MONGO_DB_NAME"]
            self.clients_collection_name=app.config["MONGO_CLIENTS_COLLECTION_NAME"]

            try:
                self.mongodb_client = pymongo.MongoClient(app.config["MONGO_STR"])

                # Check if the database exists
                dblist = self.mongodb_client.list_database_names()
                if self.db_name not in dblist:
                    raise ServerException(ErrorCode.MONGO_ERROR)                 

                # Check if the collection exists
                mydb = self.mongodb_client[self.db_name]
                collist = mydb.list_collection_names()
                if self.clients_collection_name not in collist:
                    raise ServerException(ErrorCode.MONGO_ERROR)
                
                self.clients_collection = self.mongodb_client[self.db_name][self.clients_collection_name]

            except:
                logger.error("Error in MongoDB connection")


    def get_clients_list(self):
        """Retreive clients list from mongo"""

        # Find all clients
        try:
            clients_db = self.clients_collection.find()
            clients = []
            for client in clients_db:
                clients.append(client)
            return clients
        except:
            raise ServerException(ErrorCode.MONGO_ERROR)

        # Check if the collection exists


clients_manager_service: ClientsManager = ClientsManager()
""" Clients manager service singleton"""
