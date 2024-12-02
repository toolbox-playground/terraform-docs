![Toolbox](.docs/img/toolbox.logo.png)

# Como usar o terraform-docs para documentar os módulos do Terraform

### Passo 1
Instale o [terraform-docs](https://terraform-docs.io/) e o [Python](https://www.python.org/downloads/)

### Passo 2
Copie a pasta [.docs](./.docs) para dentro do módulo criado.

### Passo 3
Altere os arquivos **header.md** e **footer.md** na .docs que está dentro do módulo. Não alterar os que estão na raiz.

### Passo 4
Execute o terraform-docs dentro do módulo. Dentro da pasta do módulo execute

  No Windows
  ```sh
  terraform-docs -c .\.docs\.terraform.docs.yaml . > README.md
  ```

  No Linux
  ```sh
  terraform-docs -c .docs/.terraform-docs.yml . > README.md
  ```

# docs.py
Script em Python para percorrer os subdiretórios em busca de diretórios `.docs` e gerar arquivos `README.md` com a documentação do Terraform usando o terraform-docs

```python
import os
import subprocess

def run_terraform_docs(directory):
    for root, dirs, files in os.walk(directory):
        if '.docs' in dirs:
            if root != directory:
                try:
                    # Comando a ser executado
                    command = ["terraform-docs", "-c", f"{root}/.docs/.terraform-docs.yml", f"{root}"]
                    print(f"Executando terraform-docs no {root}")
                    with open(f"{root}/README.md", "w") as output_file:
                        # Executa o comando e redireciona a saída para o arquivo
                        subprocess.run(command, stdout=output_file, stderr=subprocess.PIPE, text=True, check=True)
                        print("README.md gerado com sucesso!")
                except subprocess.CalledProcessError as e:
                    print("Erro ao executar o comando terraform-docs:")
                    print(e.stderr)


if __name__ == "__main__":
    base_directory = os.path.abspath(os.path.dirname(__file__))
    run_terraform_docs(base_directory)
```

## Uso
1. Navegue até o diretório onde o script `docs.py` está localizado.

2. Execute o script:
    ```sh
    python docs.py
    ```

3. O script irá percorrer os subdiretórios em busca de diretórios `.docs` e gerar arquivos `README.md` com a documentação do Terraform usando o terraform-docs

# Pastas exemplos **module** e **resource**
A pastas [module](./module/) e [resource](./resource/) são um exemplos de um módulo para bucket do GCP e sua utilização.

# GitHub Actions - Documentation Workflow

O arquivo [documentation.yml](./.github/workflows/documentation.yml) é um workflow do GitHub Actions que automatiza a geração da documentação dos módulos do Terraform utilizando o `terraform-docs`. 

## Exemplo de `documentation.yml`

```yaml
# Nome do workflow
name: Generate terraform docs

# Evento que aciona o workflow
on:
  push:
    # Caminho do código fonte que aciona o workflow
    paths:
      - 'module/**'
    # Branch que aciona o workflow
    branches:
      - main
  pull_request:
    # Caminho do código fonte que aciona o workflow
    paths:
      - 'module/**'
  # Permite que o workflow seja acionado manualmente
  workflow_dispatch:

jobs:
  python:
    # Define o sistema operacional do runner
    runs-on: ubuntu-latest
    permissions:
      # Permissão para escrever no conteúdo do repositório
      contents: write
      # Permissão para escrever em pull requests
      pull-requests: write
    steps:
      # Ação para fazer checkout do código fonte
      - uses: actions/checkout@v3
        with:
          # Refere-se ao branch da pull request
          ref: ${{ github.event.pull_request.head.ref }}

      # Configura o Python
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          # Define a versão do Python
          python-version: '3.12'

      # Instala o terraform-docs
      - name: Install terraform-docs
        run: |
          # Baixa o arquivo compactado
          curl -sSLo ./terraform-docs.tar.gz https://terraform-docs.io/dl/v0.19.0/terraform-docs-v0.19.0-$(uname)-amd64.tar.gz
          # Cria um diretório
          mkdir terraform-docs
          # Descompacta o arquivo baixado
          tar -xzf terraform-docs.tar.gz -C terraform-docs
          # Torna o arquivo executável
          chmod +x terraform-docs/terraform-docs
          # Move o arquivo para o diretório binário
          mv terraform-docs/terraform-docs /usr/local/bin/terraform-docs
          # Remove o arquivo compactado
          rm terraform-docs.tar.gz
          # Remove o diretório
          rm -rf terraform-docs

      # Executa o script docs.py
      - name: Run docs.py
        run: python docs.py

      # Comita e envia as mudanças
      - name: Commit & Push changes
        uses: actions-js/push@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

Este workflow é acionado em push ou pull request para a branch `main`, garantindo que a documentação esteja sempre atualizada.