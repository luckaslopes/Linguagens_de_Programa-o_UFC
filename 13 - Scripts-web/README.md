# Automatizador de Organização de Downloads

## Visão Geral do Projeto

Este projeto apresenta um **script Python** simples e prático, projetado para **automatizar a organização de arquivos** em uma pasta, como a sua pasta de `Downloads`. Ele classifica os arquivos movendo-os para subpastas específicas (`Documentos`, `Imagens`, `Videos`, etc.) com base em suas extensões.

A ideia é transformar uma pasta desorganizada em um ambiente mais limpo e fácil de navegar, economizando tempo e esforço que seriam gastos na organização manual.

---

## O Problema: Pasta de Downloads Desorganizada

É comum que a pasta de `Downloads` se torne um depósito para todo tipo de arquivo: PDFs de documentos, imagens, instaladores de programas, planilhas, arquivos compactados e muito mais. Essa mistura dificulta encontrar o que você precisa e manter o sistema organizado.

Nosso script resolve isso automaticamente, categorizando e movendo esses arquivos para seus respectivos lugares.

---

## Como a Solução Funciona

O script `organizador_downloads.py` faz o seguinte:

1.  **Define Mapeamentos**: Possui um dicionário que mapeia extensões de arquivo comuns (ex: `.pdf`, `.jpg`, `.zip`) para nomes de categorias (ex: `Documentos`, `Imagens`, `Compactados`). Arquivos com extensões não mapeadas vão para uma pasta "Outros".
2.  **Lê a Pasta**: Percorre todos os itens na pasta de origem especificada.
3.  **Identifica o Tipo**: Para cada arquivo, extrai sua extensão.
4.  **Cria Subpastas**: Se a subpasta da categoria (ex: `Documentos/`) ainda não existir, ela é criada automaticamente dentro da pasta de origem.
5.  **Move o Arquivo**: O arquivo é então movido para a subpasta correspondente à sua categoria.
6.  **Relata o Processo**: Imprime no console quais arquivos foram movidos e para onde, além de um resumo final.

---

## Estrutura do Repositório

* `README.md`: Este arquivo.
* `organizador_downloads.py`: O script Python principal que executa a organização.

---

## Como Executar o Script

Siga os passos abaixo para usar o organizador de downloads no seu computador:

1.  **Copie o Código**:
    * Pegue o conteúdo completo do arquivo `organizador_downloads.py` (que foi fornecido na conversa) e **salve-o** em um arquivo chamado `organizador_downloads.py` no seu computador.
    * (Opcional, mas recomendado) Copie o conteúdo deste `README.md` e salve-o como `README.md` na mesma pasta.

2.  **Ajuste o Caminho da Pasta (MUITO IMPORTANTE!)**:
    * Abra o arquivo `organizador_downloads.py` em um editor de texto.
    * Localize a linha que define `pasta_a_organizar` (ela estará dentro do bloco `if __name__ == "__main__":`).
    * **Mude o caminho padrão (`os.path.expanduser("~/Downloads")`)** para o **caminho exato da pasta que você deseja organizar**.
        * **Exemplo para Windows**: `pasta_a_organizar = r"C:\Users\SeuUsuario\Downloads"` (substitua `SeuUsuario` pelo seu nome de usuário). O `r` antes da string é crucial para lidar corretamente com as barras invertidas.
        * **Exemplo para Linux/macOS**: `pasta_a_organizar = os.path.expanduser("~/Downloads")` (esta é a forma padrão de acessar a pasta de Downloads do usuário).
    * **Recomendação de Segurança**: Para testar o script com segurança, **crie uma pasta temporária** (ex: `C:\Users\SeuUsuario\Desktop\MeusTestesDeDownload`), coloque alguns arquivos variados nela, e **aponte `pasta_a_organizar` para esta pasta de teste** antes de rodar o script pela primeira vez. Assim, você entende como ele funciona sem mexer diretamente nos seus downloads reais.

3.  **Execute o Script**:
    * Abra o **Terminal** (Linux/macOS) ou **Prompt de Comando/PowerShell** (Windows).
    * Navegue até o diretório onde você salvou o arquivo `organizador_downloads.py` usando o comando `cd`. Por exemplo:
        ```bash
        cd C:\Caminho\Para\Sua\Pasta
        ```
    * Execute o script com o Python:
        ```bash
        python organizador_downloads.py
        ```

Você verá as mensagens de progresso no terminal, indicando quais arquivos estão sendo movidos e para onde.

---

## Conceitos Chave

* **Automação de Tarefas**: Um exemplo prático de como scripts podem eliminar a necessidade de tarefas manuais e repetitivas.
* **Manipulação de Sistema de Arquivos**: Uso dos módulos `os` e `shutil` do Python para interagir com arquivos e diretórios (listar, criar, mover).
* **Mapeamento e Classificação**: Utilização de um dicionário (`defaultdict`) para categorizar arquivos com base em suas extensões.
* **Robustez Básica**: Inclui tratamento de erros para caminhos inválidos e problemas ao mover arquivos.

---

Sinta-se à vontade para modificar o script, adicionar novas categorias de arquivo ou ajustar os caminhos conforme sua necessidade!