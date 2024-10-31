from azure.cosmos import CosmosClient, exceptions
from dotenv import load_dotenv
import os

# Obtener las variables de entorno
COSMOS_ENDPOINT = 'https://acdbcadexamen.documents.azure.com:443/'
COSMOS_KEY = 'phz50F0ys8zxfREr1FqLD3jsodUhJqfazoTo8BzkHsOOyQwHS2RK1vNeQZHWlAE36XepgSvq1j8OACDbVV90ug=='
DATABASE_NAME = 'GestorProyectosDB'
CONTAINER_USUARIO = 'usuarios'
CONTAINER_PROYECTO = 'proyectos'

# Inicializar el cliente de Cosmos DB
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)

# Crear o obtener la base de datos
try:
    database = client.create_database_if_not_exists(id=DATABASE_NAME)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(DATABASE_NAME)

# Crear o obtener el contenedor usuario
try:
    container_usuario = database.create_container_if_not_exists(
        id=CONTAINER_USUARIO,
        partition_key={'paths': ['/id'], 'kind': 'Hash'},
        offer_throughput=400
    )
except exceptions.CosmosResourceExistsError:
    container_usuario = database.get_container_client(CONTAINER_USUARIO)

# Crear o obtener el contenedor proyecto
try:
    container_proyecto = database.create_container_if_not_exists(
        id=CONTAINER_PROYECTO,
        partition_key={'paths': ['/id'], 'kind': 'Hash'},
        offer_throughput=400
    )
except exceptions.CosmosResourceExistsError:
    container_proyecto = database.get_container_client(CONTAINER_PROYECTO)
    