import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env, se existir
env_path = Path(__file__).resolve().parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

# Configuração do banco de dados via variáveis de ambiente
db_config = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'database': os.getenv('MYSQL_DB', 'catalogo_digital'),
    'port': int(os.getenv('MYSQL_PORT', '3306'))
}

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'catalogo_digital')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))

    MYSQL_CONNECT_TIMEOUT = int(os.getenv('MYSQL_CONNECT_TIMEOUT', '60'))
    MYSQL_READ_TIMEOUT = int(os.getenv('MYSQL_READ_TIMEOUT', '60'))
    MYSQL_WRITE_TIMEOUT = int(os.getenv('MYSQL_WRITE_TIMEOUT', '60'))

    SECRET_KEY = os.getenv('SECRET_KEY', 'change-me-to-a-secure-key')
    DEBUG = os.getenv('FLASK_ENV', 'development') == 'development'
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'static/uploads')
    ALLOWED_EXTENSIONS = set(os.getenv('ALLOWED_EXTENSIONS', 'png,jpg,jpeg').split(','))
    WHATSAPP_LOJISTA = os.getenv('WHATSAPP_LOJISTA', '')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'app_errors.log')

    if os.getenv('FLASK_ENV', 'production') == 'production' and SECRET_KEY == 'change-me-to-a-secure-key':
        raise ValueError('SECRET_KEY deve ser definida em produção!')
