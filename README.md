![Toolbox](.docs/img/toolbox.logo.png)

# Como usar o terraform-docs para documentar os módulos do Terraform

### Passo 1
Instale o [terraform-docs](https://terraform-docs.io/).

### Passo 2
Copie a pasta [.docs](./.docs) para dentro do módulo criado.

### Passo 3
Altere os arquivos **header.md** e **footer.md** na .docs que está dentro do módulo. Não alterar os que estão na raiz.

### Passo 4
Rode `terraform-docs -c .\.docs\.terraform-docs.yml . > README.md`.
    
    OBS.: Certifique-se de estar dentro da pasta do módulo.

# Pastas exemplos **module** e **resource**
A pastas [module](./module/) e [resource](./resource/) são um exemplos de um módulo para bucket do GCP e sua utilização.

# GitHub Actions - Documentation Workflow

O arquivo [documentation.yml](./.github/workflows/documentation.yml) é um workflow do GitHub Actions que automatiza a geração da documentação dos módulos do Terraform utilizando o `terraform-docs`. 

## Exemplo de `documentation.yml`

```yaml
name: Generate terraform docs # Nome do workflow

on:
  push: # Evento que aciona o workflow
    paths:
      - 'module/**' # Caminho do código fonte que aciona o workflow
    branches:
      - main # Branch que aciona o workflow
  pull_request: # Evento que aciona o workflow
    paths:
      - 'module/**' # Caminho do código fonte que aciona o workflow
  workflow_dispatch: # Permite que o workflow seja acionado manualmente

jobs:
  docs: # Nome do job
    runs-on: ubuntu-latest # Define o ambiente onde o job será executado (Ubuntu mais recente)
    permissions:
      contents: write # Permissão para escrever no conteúdo do repositório
      pull-requests: write # Permissão para escrever em pull requests
    steps:
    - uses: actions/checkout@v3 # Ação para fazer checkout do código fonte
      with:
        ref: ${{ github.event.pull_request.head.ref }} # Refere-se ao branch da pull request

    - name: Render terraform docs inside the README.md and push changes back to PR branch # Nome da etapa
      uses: terraform-docs/gh-actions@v1.3.0 # Ação para gerar documentação do Terraform
      with:
        working-dir: module/gcp-bucket # Diretório de trabalho onde o módulo Terraform está localizado
        output-file: README.md # Arquivo de saída onde a documentação será gerada
        config-file: .docs/.terraform-docs.yml # Arquivo de configuração do terraform-docs
        output-method: replace # Método de saída, substitui o conteúdo existente
        git-push: "true" # Habilita o push das mudanças de volta para o branch da PR
```

Este workflow é acionado em push ou pull request para a branch `main`, garantindo que a documentação esteja sempre atualizada.

Esse workflow está definido para rodar somente na pasta **module/gcp-bucket**. 

Para rodar em mais pastas deverá ser adicionado no `working-dir` as pastas, ex.: `working-dir: module/gcp-bucket,module/gcp-run`

# docs.py

Este script Python é usado para gerar documentação para módulos Terraform usando a ferramenta `terraform-docs`. Ele percorre os diretórios em busca de configurações específicas e gera arquivos `README.md` com a documentação.

## Requisitos

- Python 3.x
- `terraform-docs` instalado e disponível no PATH

Certifique-se de ter o `terraform-docs` instalado. Você pode instalá-lo seguindo as instruções na [documentação oficial](https://terraform-docs.io/user-guide/installation/).

## Uso

1. Navegue até o diretório onde o script `docs.py` está localizado.

2. Execute o script:
    ```sh
    python docs.py
    ```

3. O script irá percorrer os subdiretórios em busca de diretórios `.docs` e gerar arquivos `README.md` com a documentação do Terraform.
