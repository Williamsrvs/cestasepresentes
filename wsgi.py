#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WSGI entry point para produção
Use com Gunicorn: gunicorn wsgi:app
"""

import sys
import os

# Adicionar o diretório app ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from routes import app

if __name__ == "__main__":
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', '5000'))
    app.run(host=host, port=port)
