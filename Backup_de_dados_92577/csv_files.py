import os
import pandas as pd
import logging
import chardet
import csv

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def detectar_encoding(caminho, amostra_tamanho=1000):
    """
    Detecta o encoding de um arquivo utilizando uma amostra do mesmo.
    """
    with open(caminho, 'rb') as f:
        amostra = f.read(amostra_tamanho)
    return chardet.detect(amostra)['encoding']

def detectar_delimitador(caminho, encoding):
    """
    Detecta automaticamente o delimitador do arquivo CSV.
    """
    with open(caminho, 'r', encoding=encoding) as f:
        amostra = f.read(1024)
        sniffer = csv.Sniffer()
        if sniffer.has_header(amostra):
            return sniffer.sniff(amostra).delimiter
    return ';'  # Valor padrão caso não detecte

def analisar_arquivos(diretorio):
    """
    Analisa arquivos CSV no diretório fornecido.
    Gera um relatório sobre colunas, tipos de dados e possíveis erros de leitura.
    """
    relatorio = []
    arquivos = [f for f in os.listdir(diretorio) if f.endswith('.csv')]

    if not arquivos:
        logging.warning("Nenhum arquivo CSV encontrado no diretório.")
        return

    for arquivo in arquivos:
        caminho = os.path.join(diretorio, arquivo)
        logging.info(f"Analisando arquivo: {arquivo}")
        info = {"arquivo": arquivo}

        try:
            # Detectar encoding e delimitador
            encoding = detectar_encoding(caminho)
            delimitador = detectar_delimitador(caminho, encoding)
            logging.info(f"Encoding detectado: {encoding}, delimitador detectado: '{delimitador}'.")

            # Carregar arquivo para análise preliminar
            df = pd.read_csv(caminho, nrows=5, encoding=encoding, delimiter=delimitador)
            info["colunas"] = list(df.columns)
            info["tipos_dados"] = df.dtypes.astype(str).to_dict()
            info["status"] = "Lido com sucesso"
        except UnicodeDecodeError as e:
            info["status"] = f"Erro de codificação: {str(e)}"
        except pd.errors.ParserError as e:
            info["status"] = f"Erro de parsing: {str(e)}"
        except Exception as e:
            info["status"] = f"Erro inesperado: {str(e)}"

        relatorio.append(info)

    # Geração do relatório
    logging.info("\nRelatório de análise:")
    for item in relatorio:
        logging.info(f"\nArquivo: {item['arquivo']}")
        logging.info(f"Status: {item['status']}")
        if "colunas" in item:
            logging.info(f"Colunas detectadas: {', '.join(item['colunas'])}")
        if "tipos_dados" in item:
            logging.info(f"Tipos de dados: {item['tipos_dados']}")

    return relatorio

if __name__ == "__main__":
    # Diretório onde os arquivos CSV estão localizados (diretório atual)
    diretorio = os.getcwd()
    relatorio = analisar_arquivos(diretorio)
 