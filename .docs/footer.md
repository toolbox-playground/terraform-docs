## Uso

Escreva como utlizar o módulo.

### Passo 1

No seu main.tf, adicione o seguinte código:
```hcl

provider "google" {
  project     = "id-do-projeto-gcp"
  region      = "us-central1"
  
}

module "bucket" {
  source = "../module/gcp-bucket"
  name = "terraform-docs"
}


```

Nota:
- **source** é o caminho para o módulo no repositório Git. Certifique-se de substituir pelo caminho correto do seu módulo.
- **nome_do_modulo** é o nome do módulo. Você pode usar qualquer nome que desejar.
- **bucket_name** é o nome do bucket no Google Cloud Storage
- **bucket_location** é a localização do bucket no Google Cloud Storage
- **project_id** é o ID do projeto no Google Cloud Platform
- **storage_class** é a classe de armazenamento do bucket no Google Cloud Storage

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