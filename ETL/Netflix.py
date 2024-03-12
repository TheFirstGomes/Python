import pandas as pd
import os 
import glob

# caminho para ler os arquivos
folder_path = 'src\\data\\raw'

#listar todos os arquivos de excel
excel_files = glob.glob(os.path.join(folder_path,  '*.xlsx'))

if not excel_files:
    print("Nenhum arquivo compatível encontrado")
else:
    # DataFrame = tabela na memória para guardar os conteúdos dos arquivos
    dfs = []

    for excel_file in excel_files:
        try:
            # Ler o arquivo de excel
            df_temp = pd.read_excel(excel_file)
            # Pegar o nome do arquivo
            file_name = os.path.basename(excel_file)

            df_temp['filename'] = file_name

            # Coluna personalizada com o nome do País
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                df_temp['location'] = 'it'

            # Coluna personalizada com nome Campanha
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
            
            # Guardar os dados tratados dentro de um DataFrame
            dfs.append(df_temp)

            print(dfs)
        except Exception as ex:
            print(f"Erro ao ler o arquivo {excel_file}: {ex}")

if dfs:
    # Concatena todas as tabelas salvas no DFS em uma única tabela
    result = pd.concat(dfs, ignore_index=True)

    # Caminho de saída
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    # Configurou o motor de escrita
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    # Leva os dados do resultado a serem escritos no motor de excel configurado
    result.to_excel(writer, index=False)

    #Salvar o arquivo do Excel
    writer._save()
else: 
    print("Nenhum dado para ser salvo!")