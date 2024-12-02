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