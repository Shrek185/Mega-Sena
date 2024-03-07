import tkinter as tk
from random import sample
from time import sleep

# Função para gerar um palpite para um jogo da Mega Sena.
def gerar_palpite():
    # Utiliza a função sample para selecionar 6 números únicos entre 1 e 60 e os retorna ordenados.
    return sorted(sample(range(1, 61), 6))

# Função para imprimir os jogos na GUI.
def imprimir_jogos_gui(jogos):
    # Limpa o conteúdo anterior na caixa de texto
    text_output.delete(1.0, tk.END)
    # Adiciona os jogos na caixa de texto
    text_output.insert(tk.END, '-=' * 3 + f' SORTEANDO {len(jogos)} JOGOS ' + '-=' * 3 + '\n\n')
    for i, jogo in enumerate(jogos):
        text_output.insert(tk.END, f'Jogo {i + 1}: {jogo}\n')
        text_output.update()
        sleep(1)
    text_output.insert(tk.END, '\n' + '-=' * 5 + '< BOA SORTE! >' + '-=' * 5 + '\n')

# Função principal que controla o fluxo do programa.
def sortear_jogos():
    # Pega a quantidade de jogos do campo de entrada
    quant = int(entry_quant.get())
    
    # Gera uma lista de jogos usando list comprehension e a função 'gerar_palpite()'.
    jogos = [gerar_palpite() for _ in range(quant)]
    # Chama a função 'imprimir_jogos()' para exibir os jogos sorteados na tela.
    imprimir_jogos_gui(jogos)

# Criar janela principal
root = tk.Tk()
root.title("Sorteio da Mega Sena")

# Label e campo de entrada para a quantidade de jogos
label_quant = tk.Label(root, text="Quantidade de Jogos:")
label_quant.grid(row=0, column=0, padx=5, pady=5)
entry_quant = tk.Entry(root)
entry_quant.grid(row=0, column=1, padx=5, pady=5)

# Botão para sortear jogos
button_sortear = tk.Button(root, text="Sortear", command=sortear_jogos)
button_sortear.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Caixa de texto para exibir os jogos sorteados
text_output = tk.Text(root, width=40, height=10)
text_output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Iniciar loop da interface gráfica
root.mainloop()
