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
                    with open(f"{root}/README.md", "r+") as output_file:
                        # Executa o comando e redireciona a saída para o arquivo
                        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
                        current_content = output_file.read()
                        if current_content != result.stdout:
                            output_file.write(result.stdout)
                            print("README.md gerado com sucesso!")
                        else:
                            print("O conteúdo do README.md já está atualizado.")
                except subprocess.CalledProcessError as e:
                    print("Erro ao executar o comando terraform-docs:")
                    print(e.stderr)


if __name__ == "__main__":
    base_directory = os.path.abspath(os.path.dirname(__file__))
    run_terraform_docs(base_directory)