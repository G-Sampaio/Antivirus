import os 
verifica_Diretorio=(r'C:\Users\GuilhermeSampaio\OneDrive - BIOTROP SOLUÇÕES BIOLÓGICAS\Documentos\codes\AntiVirus Python\Vírus')


def verificar_Arquivo(verifica_Diretorio):
    malicioso_Encontrado = False
    for root,dirs,files in os.walk(verifica_Diretorio):
        for arquivo in files:
            if arquivo.endswith(('.bat','.exe')):
                caminho = os.path.join(root, arquivo)
                print(f"Arquivo Malícioso encontrado no Diretório {caminho}")
                virus_Encontrado = True
        
        if not virus_Encontrado:
            print("Nenhum arquivo malícioso encontrado :)")

try:
    verificar_Arquivo(verifica_Diretorio)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
