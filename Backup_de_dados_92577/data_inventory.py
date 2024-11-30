import os
import pandas as pd

def listar_arquivos_e_colunas():
    # Obter o diretório onde o script está sendo executado
    pasta_atual = os.getcwd()
    print(f"Pasta atual: {pasta_atual}\n")

    # Extensões de arquivos suportados
    extensoes_suportadas = ['.csv', '.xlsx', '.xls']

    # Listar arquivos na pasta atual
    arquivos = [f for f in os.listdir(pasta_atual) if os.path.isfile(f)]

    for arquivo in arquivos:
        # Verificar se o arquivo tem uma extensão suportada
        _, extensao = os.path.splitext(arquivo)
        if extensao.lower() in extensoes_suportadas:
            print(f"Arquivo encontrado: {arquivo}")
            try:
                # Carregar o arquivo dependendo da extensão
                if extensao.lower() == '.csv':
                    df = pd.read_csv(arquivo)
                elif extensao.lower() in ['.xlsx', '.xls']:
                    df = pd.read_excel(arquivo)

                # Exibir colunas e tipos de dados
                print("Colunas e tipos de dados:")
                print(df.dtypes)
                print("\n" + "-"*50 + "\n")
            except Exception as e:
                print(f"Erro ao ler o arquivo {arquivo}: {e}\n")
        else:
            print(f"Arquivo ignorado (formato não suportado): {arquivo}\n")

if __name__ == "__main__":
    listar_arquivos_e_colunas()