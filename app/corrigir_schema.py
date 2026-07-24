import os
import sys
import tkinter as tk
from tkinter import filedialog

def corrigir_schema_sql(caminho_sql):
    """
    Corrige o erro de sintaxe (falta de vírgula) no arquivo schema.sql.
    """
    # Tentar diferentes encodings comuns
    encodings = ['utf-8', 'latin-1', 'cp1252']
    conteudo = None
    encoding_usado = None

    for enc in encodings:
        try:
            with open(caminho_sql, 'r', encoding=enc) as f:
                conteudo = f.read()
                encoding_usado = enc
                break
        except UnicodeDecodeError:
            continue

    if conteudo is None:
        print("\n❌ Erro: Não foi possível ler o arquivo devido à codificação de texto.")
        return False

    # 1. Corrigir falta de vírgula na tbl_cadastrar_usuario
    # Procura por: senha_usuario VARCHAR(100)\n    repetir_senha
    # Substitui por: senha_usuario VARCHAR(100),\n    repetir_senha
    erro_virgula = r'(senha_usuario VARCHAR\(100\))(\s+repetir_senha)'
    if re.search(erro_virgula, conteudo):
        conteudo = re.sub(erro_virgula, r'\1,\2', conteudo)
        print("✅ Correção aplicada: Vírgula adicionada em tbl_cadastrar_usuario.")
    
    # 2. Corrigir erro de sintaxe na linha 136 (nome_cliente,s)
    erro_s_extra = r'(nome_cliente,)(s)(\s+dp\.telefone)'
    if re.search(erro_s_extra, conteudo):
        conteudo = re.sub(erro_s_extra, r'\1\3', conteudo)
        print("✅ Correção aplicada: Letra 's' extra removida na linha 136.")

    # 3. Corrigir erro de sintaxe na linha 172 (vírgula sobrando antes do FROM)
    erro_virgula_from = r'(pe\.dt_registro,)(\s+FROM)'
    if re.search(erro_virgula_from, conteudo):
        conteudo = re.sub(erro_virgula_from, r'pe.dt_registro\2', conteudo)
        print("✅ Correção aplicada: Vírgula extra removida antes do FROM na linha 172.")

    try:
        with open(caminho_sql, 'w', encoding=encoding_usado) as f:
            f.write(conteudo)
        print(f"\n✅ Sucesso: Arquivo schema.sql corrigido e salvo!")
        return True
    except Exception as e:
        print(f"\n❌ Erro ao escrever no arquivo: {e}")
        return False

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    print("\nSelecione o arquivo 'schema.sql' dentro da pasta 'app' do seu projeto...")
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo schema.sql",
        filetypes=[("Arquivos SQL", "*.sql"), ("Todos os arquivos", "*.*")]
    )
    root.destroy()
    return caminho

if __name__ == "__main__":
    import re
    print("\n" + "="*60)
    print("   CORRETOR DE SINTAXE DO BANCO DE DADOS (SCHEMA.SQL)")
    print("="*60)
    
    try:
        caminho_sql = selecionar_arquivo()
        
        if not caminho_sql:
            print("\n⚠️  Operação cancelada: Nenhum arquivo foi selecionado.")
            sys.exit(0)
            
        corrigir_schema_sql(caminho_sql)
            
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada.")
    
    print("\n" + "="*60)
    input("\nPressione Enter para sair...")
