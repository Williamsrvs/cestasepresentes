
import os

# As credenciais abaixo usam variáveis de ambiente (com fallback para os
# valores anteriores, para não quebrar ambientes que ainda não configuraram
# as variáveis no Railway). Configure MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD,
# MYSQL_DB, MYSQL_PORT e SECRET_KEY nas variáveis de ambiente do serviço para
# remover completamente as credenciais do código-fonte.
db_config = {
    'host': os.environ.get('MYSQL_HOST', 'auth-db1937.hstgr.io'),
    'user': os.environ.get('MYSQL_USER', 'u799109175_cestas_present'),
    'password': os.environ.get('MYSQL_PASSWORD', 'Q1k2v1y5@2025'),
    'database': os.environ.get('MYSQL_DB', 'u799109175_cestas_present'),
    'port': int(os.environ.get('MYSQL_PORT', 3306))
}
class Config:
    # As credenciais usam variáveis de ambiente, com fallback para os valores
    # anteriores. Configure-as no Railway para removê-las do código-fonte.
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'auth-db1937.hstgr.io')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'u799109175_cestas_present')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Q1k2v1y5@2025')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'u799109175_cestas_present')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))


    # Configurações específicas do Flask-MySQLdb
    MYSQL_CURSORCLASS = 'DictCursor'
    MYSQL_CONNECT_TIMEOUT = 60
    MYSQL_READ_TIMEOUT = 60
    MYSQL_WRITE_TIMEOUT = 60
    
    # Configurações SSL (se necessário)
    # MYSQL_SSL_DISABLED = False
    # MYSQL_SSL_CA = None
    # MYSQL_SSL_CERT = None
    # MYSQL_SSL_KEY = None
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Q1k2v1y5@2025-service-tour')
    DEBUG = os.environ.get('FLASK_ENV', 'production') != 'production'
    UPLOAD_FOLDER = 'static/uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}