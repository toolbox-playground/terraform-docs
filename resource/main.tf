provider "google" {
  project     = "id-do-projeto-gcp"
  region      = "us-central1"
  
}

module "bucket" {
  source = "../module/gcp-bucket"
  name = "terraform-docs"
}