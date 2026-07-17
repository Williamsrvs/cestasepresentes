#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Entry point WSGI para produção.

Este módulo expõe a instância da aplicação Flask (`app`) para que
servidores WSGI de produção, como o Gunicorn, consigam carregá-la.

Em produção, o servidor deve ser iniciado com Gunicorn, por exemplo:

    gunicorn --workers=4 --worker-class=sync --bind=0.0.0.0:5000 \
        --timeout=120 --access-logfile=- --error-logfile=- wsgi:app

Não execute este arquivo diretamente. Para desenvolvimento local,
utilize `python3 app.py`.
"""

from app.routes import app
