import os
import re
import sys
import tkinter as tk
from tkinter import filedialog

def atualizar_senha_env(caminho_env, nova_senha):
    """
    Atualiza a variável MYSQL_PASSWORD no arquivo preservando o restante do conteúdo.
    """
    # Tentar diferentes encodings comuns
    encodings = ['utf-8', 'latin-1', 'cp1252']
    conteudo = None
    encoding_usado = None

    for enc in encodings:
        try:
            with open(caminho_env, 'r', encoding=enc) as f:
                conteudo = f.read()
                encoding_usado = enc
                break
        except UnicodeDecodeError:
            continue

    if conteudo is None:
        print("\n❌ Erro: Não foi possível ler o arquivo devido à codificação de texto.")
        return False

    # Regex para encontrar a linha MYSQL_PASSWORD=...
    padrao = r'(MYSQL_PASSWORD\s*=\s*)(.*)'
    
    if re.search(padrao, conteudo):
        # Substitui o valor mantendo a chave e o sinal de igual
        novo_conteudo = re.sub(padrao, rf'\1{nova_senha}', conteudo)
        
        try:
            with open(caminho_env, 'w', encoding=encoding_usado) as f:
                f.write(novo_conteudo)
            print(f"\n✅ Sucesso: Senha atualizada no arquivo:\n   {caminho_env}")
            return True
        except Exception as e:
            print(f"\n❌ Erro ao escrever no arquivo: {e}")
            return False
    else:
        print("\n❌ Erro: A variável MYSQL_PASSWORD não foi encontrada dentro do arquivo.")
        print("Verifique se o arquivo selecionado é o correto.")
        return False

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw() # Esconde a janela principal do tkinter
    
    print("\nAbri uma janela para você selecionar o arquivo de configuração...")
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo de configuração (ex: .env ou Cestas e Presentes.env)",
        filetypes=[("Arquivos ENV", "*.env"), ("Todos os arquivos", "*.*")]
    )
    root.destroy()
    return caminho

if __name__ == "__main__":
    print("\n" + "="*60)
    print("   ATUALIZADOR DE SENHA (SELEÇÃO MANUAL)")
    print("="*60)
    
    try:
        # Abre a janela para o usuário escolher o arquivo
        caminho_env = selecionar_arquivo()
        
        if not caminho_env:
            print("\n⚠️  Operação cancelada: Nenhum arquivo foi selecionado.")
            sys.exit(0)
            
        print(f"Arquivo selecionado: {caminho_env}")
        
        nova_senha = input("\nDigite a nova senha do banco de dados: ").strip()
        
        if nova_senha:
            atualizar_senha_env(caminho_env, nova_senha)
        else:
            print("\n⚠️  Ação cancelada: Nenhuma senha foi digitada.")
            
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")
    
    print("\n" + "="*60)
    input("\nPressione Enter para sair...")
