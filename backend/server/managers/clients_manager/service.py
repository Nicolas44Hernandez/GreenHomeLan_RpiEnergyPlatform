import logging
import pymongo
from flask import Flask
from server.common import ServerException, ErrorCode

logger = logging.getLogger(__name__)


class ClientsManager:
    """Manager for Clients management service"""

    mongodb_client: pymongo.MongoClient
    db_name: pymongo
    mongodb_str: str
    clients_collection_name: str
    clients_collection: str
    connected: bool

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize Clients manager"""
        if app is not None:
            logger.info("initializing the Clients manager")

            self.mongodb_str=app.config["MONGO_STR"]
            self.db_name=app.config["MONGO_DB_NAME"]
            self.clients_collection_name=app.config["MONGO_CLIENTS_COLLECTION_NAME"]
            self.connected=False

            self.connect_to_mongo_db()

    def connect_to_mongo_db(self, reconnection=False):
        """Connect to database"""

        self.connected=False
        self.mongodb_client = pymongo.MongoClient(self.mongodb_str)

        logger.info("Connecting to mongodb service")

        # Check if the database exists
        try:
            dblist = self.mongodb_client.list_database_names()
            if self.db_name not in dblist:            
                raise ServerException(ErrorCode.MONGO_ERROR)                 

            # Check if the collection exists
            mydb = self.mongodb_client[self.db_name]
            collist = mydb.list_collection_names()
            if self.clients_collection_name not in collist:
                raise ServerException(ErrorCode.MONGO_ERROR)
            
            self.clients_collection = self.mongodb_client[self.db_name][self.clients_collection_name]
            self.connected=True
            logger.info("Succefully connected")
        except:
            logger.error("Error in mongodb connection")
            self.connected=False
            if reconnection:
                raise ServerException(ErrorCode.MONGO_ERROR)


    def reconnect_to_mongodb(self):
        """Try to reconnect to database"""
        logger.info("Trying to recconect to mongo service")
        self.connect_to_mongo_db(reconnection=True)


    def get_clients_list(self):
        """Retreive clients list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all clients
        try:
            clients_db = self.clients_collection.find()
            clients = []
            for client in clients_db:
                clients.append(client)
            return clients
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def get_zones_list(self):
        """Retreive zones list from mongo"""
        
        # Retreive clients list
        clients = self.get_clients_list()
        zones = []
        for client in clients:
            if client["zone"] not in zones:
                zones.append(client["zone"])
        return zones
    
    def get_energeticians_list(self):
        """Retreive energeticians list from mongo"""
        
        # Retreive clients list
        clients = self.get_clients_list()
        energeticians = []
        for client in clients:
            if client["energetician"] not in energeticians:
                energeticians.append(client["energetician"])
        return energeticians

    def create_database(self):
        """Create database if doesnt exists"""

        dblist = self.mongodb_client.list_database_names()
        if self.db_name not in dblist:   
            logger.info(f"Creatting database {self.db_name}")         
            #Create database            
        else:
            logger.info(f"Database {self.db_name} already created") 
        mydb = self.mongodb_client[self.db_name]  
        
                
        collist = mydb.list_collection_names()
        if self.clients_collection_name not in collist:
            logger.info(f"Creatting collection {self.clients_collection_name}")
            self.clients_collection = self.mongodb_client[self.db_name][self.clients_collection_name]
    
        # Return the number of clients in the colection
        return self.clients_collection.count_documents({})

    def insert_clients(self, clients):
        """Create multiple clients in database"""
        self.clients_collection.insert_many(clients)
    
    def delete_database(self):
        """Drop collection and database"""
        self.clients_collection.drop()

clients_manager_service: ClientsManager = ClientsManager()
""" Clients manager service singleton"""
