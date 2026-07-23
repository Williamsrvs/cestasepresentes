#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arquivo de Configuração - Production Ready
Separa configurações de desenvolvimento e produção
"""

import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

class Config:
    """Configurações base"""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    DEBUG = False
    TESTING = False
    
    # MySQL
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'catalogo_digital')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    
    # Flask-MySQLdb
    MYSQL_CURSORCLASS = 'DictCursor'
    MYSQL_CONNECT_TIMEOUT = 60
    MYSQL_READ_TIMEOUT = 60
    MYSQL_WRITE_TIMEOUT = 60
    
    # Upload
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    # Session
    PERMANENT_SESSION_LIFETIME = 86400  # 24 horas
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    
    # WhatsApp
    WHATSAPP_LOJISTA = os.getenv('WHATSAPP_LOJISTA', '5582981090042')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'app_errors.log')


class DevelopmentConfig(Config):
    """Configurações de Desenvolvimento"""
    
    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = False  # Permite sem HTTPS em desenvolvimento


class ProductionConfig(Config):
    """Configurações de Produção"""
    
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True  # Requer HTTPS
    
    # Força variáveis de ambiente em produção
    SECRET_KEY = os.getenv('SECRET_KEY')
    if not SECRET_KEY or SECRET_KEY == 'dev-key-change-in-production':
        raise ValueError("SECRET_KEY deve ser configurada em produção!")


class TestingConfig(Config):
    """Configurações de Teste"""
    
    DEBUG = True
    TESTING = True
    MYSQL_DB = 'catalogo_digital_test'


# Seleciona configuração baseada no ambiente
config_name = os.getenv('FLASK_ENV', 'development').lower()

if config_name == 'production':
    config = ProductionConfig
elif config_name == 'testing':
    config = TestingConfig
else:
    config = DevelopmentConfig

print(f"[CONFIG] Ambiente: {config_name.upper()} | Debug: {config.DEBUG}")
