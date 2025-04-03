import pyautogui
import pandas as pd
import time
import pyperclip

pyautogui.PAUSE = 1.5

def salvar_csv(nome_arquivo, dados):
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False)
    print(f"Arquivo CSV '{nome_arquivo}' criado com sucesso!")
    
def ler_csv(nome_arquivo):
    return pd.read_csv(nome_arquivo)

def executar_tarefas(lista_tarefas):
    resultados = []
    resultado_calculo = ""
    for _, tarefa in lista_tarefas.iterrows():
        inicio = time.time()  
        
        try:
            if tarefa["Tipo"] == "tecla":
                pyautogui.press(tarefa["Execução"])
            elif tarefa["Tipo"] == "texto":
                pyautogui.write(tarefa["Execução"])
            elif tarefa["Tipo"] == "hotkey":
                keys = tarefa["Execução"].split("+")
                pyautogui.hotkey(*keys)
                if "ctrl+c" in tarefa["Execução"]:
                    time.sleep(1)  
                    resultado_calculo = pyperclip.paste()
            elif tarefa["Tipo"] == "espera":
                time.sleep(int(tarefa["Execução"]))
            status = "Sucesso"
        except Exception as e:
            status = f"Erro: {str(e)}"
        
        fim = time.time()  
        tempo_execucao = fim - inicio  

        resultados.append({
            "Tarefa": tarefa["Tarefa"],
            "Status": status,
            "Tempo de Execução (s)": round(tempo_execucao, 4)
        })
    
    return resultados, resultado_calculo

tarefas = [
    {"Tarefa": "Abrir menu Iniciar", "Tipo": "tecla", "Execução": "win"},
    {"Tarefa": "Digitar calculadora", "Tipo": "texto", "Execução": "calculadora"},
    {"Tarefa": "Pressionar enter", "Tipo": "tecla", "Execução": "enter"},
    {"Tarefa": "Esperar", "Tipo": "espera", "Execução": "2"},
    {"Tarefa": "Digitar cálculo", "Tipo": "texto", "Execução": "23*4"},
    {"Tarefa": "Pressionar enter", "Tipo": "tecla", "Execução": "enter"},
    {"Tarefa": "Selecionar o resultado", "Tipo": "hotkey", "Execução": "ctrl+a"},
    {"Tarefa": "Copiar o resultado", "Tipo": "hotkey", "Execução": "ctrl+c"},
    {"Tarefa": "Fechar a calculadora", "Tipo": "hotkey", "Execução": "alt+f4"}
]

salvar_csv("tarefas.csv", tarefas)

df_lido = ler_csv("tarefas.csv")

resultados, resultado_calculo = executar_tarefas(df_lido)

df_resultados = pd.DataFrame(resultados)

# Salvar relatório em Excel
df_resultados.to_excel("relatorio_tarefas.xlsx", index=False)

print(f"Resultado do cálculo: {resultado_calculo}")    
print("Relatórios gerados com sucesso!")
