from openpyxl import load_workbook
from pathlib import Path

def salvar_dados_excel(data, os_num, servico, valor):
    caminho_arquivo = Path(__file__).parent / "MIMO.xlsx"  # corrigido

    print(f"📄 Usando caminho: {caminho_arquivo}")  # Diagnóstico opcional

    wb = load_workbook(caminho_arquivo)
    ws = wb.active

    linha = 2
    while ws[f"A{linha}"].value:
        linha += 1

    ws[f"A{linha}"] = data
    ws[f"C{linha}"] = os_num
    ws[f"D{linha}"] = servico
    ws[f"E{linha}"] = valor

    wb.save(caminho_arquivo)
    print(f"✅ Dados salvos com sucesso na linha {linha}")