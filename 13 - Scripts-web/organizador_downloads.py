import os
import shutil
from collections import defaultdict

def organizar_pasta(pasta_origem):
    """
    Organiza arquivos em uma pasta movendo-os para subpastas baseadas em seus tipos.

    Args:
        pasta_origem (str): O caminho completo para a pasta a ser organizada.
    """
    if not os.path.isdir(pasta_origem):
        print(f"Erro: A pasta '{pasta_origem}' não existe ou não é um diretório válido.")
        return

    print(f"Iniciando a organização da pasta: '{pasta_origem}'")

    extensoes_map = defaultdict(lambda: "Outros")
    extensoes_map.update({

        ".pdf": "Documentos", ".doc": "Documentos", ".docx": "Documentos",
        ".txt": "Documentos", ".odt": "Documentos", ".xls": "Documentos",
        ".xlsx": "Documentos", ".ppt": "Documentos", ".pptx": "Documentos",

        ".jpg": "Imagens", ".jpeg": "Imagens", ".png": "Imagens",
        ".gif": "Imagens", ".bmp": "Imagens", ".tiff": "Imagens",
        ".webp": "Imagens", ".svg": "Imagens",

        ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos",
        ".mkv": "Videos", ".flv": "Videos", ".wmv": "Videos",

        ".mp3": "Audios", ".wav": "Audios", ".aac": "Audios",
        ".flac": "Audios", ".ogg": "Audios",

        ".exe": "Executaveis", ".msi": "Executaveis", ".dmg": "Executaveis",
        ".app": "Executaveis", ".deb": "Executaveis", ".rpm": "Executaveis",

        ".zip": "Compactados", ".rar": "Compactados", ".7z": "Compactados",
        ".tar": "Compactados", ".gz": "Compactados", ".bz2": "Compactados",

        ".py": "Codigos", ".js": "Codigos", ".html": "Codigos",
        ".css": "Codigos", ".java": "Codigos", ".c": "Codigos",
        ".cpp": "Codigos", ".php": "Codigos", ".json": "Codigos",
        ".xml": "Codigos",
    })

    arquivos_organizados = 0
    arquivos_ignorados = 0

    for nome_arquivo in os.listdir(pasta_origem):
        caminho_completo_arquivo = os.path.join(pasta_origem, nome_arquivo)

        if os.path.isdir(caminho_completo_arquivo) or nome_arquivo == os.path.basename(__file__):
            arquivos_ignorados += 1
            continue

        nome, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower() 
        categoria = extensoes_map[extensao]
        pasta_destino_categoria = os.path.join(pasta_origem, categoria)

        if not os.path.exists(pasta_destino_categoria):
            os.makedirs(pasta_destino_categoria)
            print(f"  Criada subpasta: '{categoria}'")

        caminho_destino_arquivo = os.path.join(pasta_destino_categoria, nome_arquivo)

        try:
            shutil.move(caminho_completo_arquivo, caminho_destino_arquivo)
            print(f"  Movido: '{nome_arquivo}' para '{categoria}/'")
            arquivos_organizados += 1
        except Exception as e:
            print(f"  Erro ao mover '{nome_arquivo}': {e}")
            arquivos_ignorados += 1

    print(f"\nOrganização concluída!")
    print(f"  Arquivos organizados: {arquivos_organizados}")
    print(f"  Arquivos ignorados (diretórios ou erros): {arquivos_ignorados}")
    print("--------------------------------------------------")

if __name__ == "__main__":

    pasta_a_organizar = os.path.expanduser("~/Downloads") 

    organizar_pasta(pasta_a_organizar)
