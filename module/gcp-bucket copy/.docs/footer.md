## Uso

Este módulo foi criado para criação de buckets no GCP. Abaixo segue como utilizá-lo.

### Passo 1

No seu main.tf, adicione o seguinte código:
```hcl

provider "google" {
  project     = "id-do-projeto-gcp"
  region      = "us-central1"
  
}

module "nome_do_modulo" {
  source = "../module/gcp-bucket"
  name = "terraform-docs"
}


```

Nota:
- **project** é o ID do projeto no Google Cloud Platform. Certifique-se de substituir pelo ID correto do seu projeto.
- **region** é a região onde o bucket será criado. Certifique-se de substituir pela região correta.
- **nome_do_modulo** é o nome do módulo. Você pode usar qualquer nome que desejar.
- **source** é o caminho para o módulo no repositório local. Certifique-se de substituir pelo caminho correto do seu módulo.
- **name** é o nome do bucket no Google Cloud Storage

### Passo 2

Verifique suas configurações usando o seguinte comando:

```bash
terraform init
terraform plan
```

### Passo 3

Aplique as mudanças

```bash
terraform apply
```