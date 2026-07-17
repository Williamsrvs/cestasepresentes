#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arquivo principal da aplicação Flask

⚠️  APENAS PARA DESENVOLVIMENTO LOCAL ⚠️
Este arquivo utiliza o servidor de desenvolvimento embutido do Flask
(`app.run()`), que não é adequado para produção: ele não é otimizado
para lidar com múltiplas conexões concorrentes e pode ficar indisponível
sob carga real.

Em produção (Railway), a aplicação deve ser iniciada com Gunicorn,
apontando para `wsgi:app`, por exemplo:

    gunicorn --workers=4 --worker-class=sync --bind=0.0.0.0:5000 \
        --timeout=120 --access-logfile=- --error-logfile=- wsgi:app

Para rodar localmente, basta executar: `python3 app.py`
"""

import os
import sys
import threading

# Adicionar o diretório app ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from routes import app, criar_tabelas


def iniciar_setup_em_segundo_plano():
    try:
        criar_tabelas()
    except Exception as e:
        print(f"⚠️  Setup do banco não bloqueou a inicialização: {e}")


if __name__ == '__main__':
    # Bloco executado somente quando rodado diretamente (desenvolvimento local).
    # Em produção, o Gunicorn importa `wsgi:app` e este bloco nunca é executado.

    # Criar tabelas em segundo plano para não travar a subida do servidor
    threading.Thread(target=iniciar_setup_em_segundo_plano, daemon=True).start()
    
    # Determinar ambiente (desenvolvimento ou produção)
    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development'
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    print("\n" + "="*60)
    print("🚀 Iniciando Catálogo Digital")
    print("="*60)
    print(f"Ambiente: {'DESENVOLVIMENTO' if debug_mode else 'PRODUÇÃO'}")
    print(f"Servidor: http://{host}:{port}")
    print("="*60 + "\n")
    
    # Executar aplicação
    app.run(
        host=host,
        port=port,
        debug=debug_mode,
        use_reloader=debug_mode
    )
