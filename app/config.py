import os
from datetime import timedelta
from dotenv import load_dotenv

def carregar_env_robusto(env_path):
    if not os.path.exists(env_path):
        return

    encodings = ['utf-8-sig', 'utf-8', 'latin-1', 'cp1252']
    for encoding in encodings:
        try:
            with open(env_path, 'r', encoding=encoding) as f:
                content = f.read()
            from io import StringIO
            load_dotenv(stream=StringIO(content))
            return
        except UnicodeDecodeError:
            continue

    with open(env_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    from io import StringIO
    load_dotenv(stream=StringIO(content))


# Carregar variáveis de ambiente do .env
# Procura .env na raiz do projeto
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
carregar_env_robusto(env_path)

# Configuração do banco de dados - suporta variáveis de ambiente
db_config = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),  
    'database': os.getenv('MYSQL_DB', 'catalogo_digital'),  
    'port': int(os.getenv('MYSQL_PORT', 3306))
}

class Config:
    # Configuração do banco de dados via variáveis de ambiente
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'catalogo_digital')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))

    # Configurações específicas do MySQL
    MYSQL_CURSORCLASS = 'DictCursor'
    MYSQL_CONNECT_TIMEOUT = int(os.getenv('MYSQL_CONNECT_TIMEOUT', '60'))
    MYSQL_READ_TIMEOUT = int(os.getenv('MYSQL_READ_TIMEOUT', '60'))
    MYSQL_WRITE_TIMEOUT = int(os.getenv('MYSQL_WRITE_TIMEOUT', '60'))
    
    # Configurações do Flask
    # ✅ Corrigido: Garantindo que sempre haja uma SECRET_KEY para evitar o erro ValueError no Railway
    SECRET_KEY = os.getenv('SECRET_KEY', 'Ccap2004@-service-tour')
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'.format(**db_config)    
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    DEBUG = os.getenv('FLASK_ENV', 'development') == 'development'
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'static/uploads')
    ALLOWED_EXTENSIONS = set([item.strip().lower() for item in os.getenv('ALLOWED_EXTENSIONS', 'png,jpg,jpeg').split(',') if item.strip()])
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
    LOG_FILE = os.getenv('LOG_FILE', 'app_errors.log')
    SESSION_COOKIE_HTTPONLY = os.getenv('SESSION_COOKIE_HTTPONLY', 'True').lower() == 'true'
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'True').lower() == 'true'
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE', 'Lax')
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=int(os.getenv('PERMANENT_SESSION_LIFETIME_MINUTES', '30')))
