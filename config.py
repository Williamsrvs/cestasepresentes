
db_config = {
    'host': 'auth-db1937.hstgr.io',
    'user': 'u799109175_cestas_present',
    'password': 'Q1k2v1y5@2025',  
    'database': 'u799109175_cestas_present',  
    'port': 3306
}
class Config:
    # ✅ REMOVIDA A BARRA NO FINAL
    MYSQL_HOST = 'auth-db1937.hstgr.io'
    MYSQL_USER = 'u799109175_cestas_present'
    MYSQL_PASSWORD = 'Q1k2v1y5@2025'
    MYSQL_DB = 'u799109175_cestas_present'
    MYSQL_PORT = 3306

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
    
    # Configurações do Flask
    SECRET_KEY = 'Q1k2v1y5@2025-service-tour'
    DEBUG = True
    UPLOAD_FOLDER = 'static/uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}