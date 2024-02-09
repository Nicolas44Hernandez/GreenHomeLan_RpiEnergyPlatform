from flask.cli import FlaskGroup
from server.app import create_app
from server.managers.clients_manager import clients_manager_service

app = create_app()
cli = FlaskGroup(create_app=create_app)

DEFAULT_CLIENTS = [
    {
        "client_id": '1',
        "zone": '35NNE',
        "energetician": 'E1',
        "id_energetician": '1',
        "contract_class": '6KVA',
        "fai": 'Orange',
        "id_client_fai": '1',
        "name_client_fai": 'MyOrchestrator',
        "ip": '192.168.1.19',
        "port": '5000'
    },
    {
        "client_id": '2',
        "zone": 'Zone 1',
        "energetician": 'E1',
        "id_energetician": '1',
        "contract_class": '6KVA',
        "fai": 'Orange',
        "id_client_fai": '1',
        "name_client_fai": 'MyOrchestrator',
        "ip": '192.168.1.101',
        "port": '80'
    },
    {
        "client_id": '3',
        "zone": 'Zone 1',
        "energetician": 'E1',
        "id_energetician": '2',
        "contract_class": '6KVA',
        "fai": 'Orange',
        "id_client_fai": '2',
        "name_client_fai": 'MyOrchestrator',
        "ip": '192.168.1.102',
        "port": '80'
    },
    {
        "client_id": '4',
        "zone": 'Zone 2',
        "energetician": 'E2',
        "id_energetician": '1',
        "contract_class": '6KVA',
        "fai": 'Orange',
        "id_client_fai": '3',
        "name_client_fai": 'MyOrchestrator',
        "ip": '192.168.1.103',
        "port": '80'
    },
    {
        "client_id": '5',
        "zone": 'Zone 3',
        "energetician": 'E1',
        "id_energetician": '3',
        "contract_class": '6KVA',
        "fai": 'Orange',
        "id_client_fai": '4',
        "name_client_fai": 'MyOrchestrator',
        "ip": '192.168.1.104',
        "port": '80'
    },
    {
        "client_id": '6',
        "zone": 'Zone 4',
        "energetician": 'E1',
        "id_energetician": '4',
        "contract_class": '6KVA',
        "fai": 'Orange',
        "id_client_fai": '5',
        "name_client_fai": 'MyOrchestrator',
        "ip": '192.168.1.105',
        "port": '80'
    },
    {
        "client_id": '7',
        "zone": 'HOME_ORCH3',
        "energetician": 'E1',
        "id_energetician": '5',
        "contract_class": '6KVA',
        "fai": 'Orange',
        "id_client_fai": '7',
        "name_client_fai": 'MyOrchestrator',
        "ip": '192.168.1.49',
        "port": '5000'
    },
]

@cli.command('create')
def create_db():
    """Create database and collection if doesnt exists"""

    # Create database if needed
    nb_clients = clients_manager_service.create_database()

    # Create clients
    if nb_clients != 0:
        print("Database exists, run delete command before re create it")
        return   
     
    print("Database created")
    print("Seeding database")
    clients_manager_service.insert_clients(DEFAULT_CLIENTS)
    
    print("Database successfully created!")

@cli.command('delete')
def delete_db():
    """Delete database and collection if exists"""

    # Delete database and collection
    clients_manager_service.delete_database()    
    print("Database successfully deleted!")


if __name__ == '__main__':
    cli()
