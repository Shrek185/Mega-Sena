"""
Evitar repetição de números em um mesmo jogo: Atualmente, o código garante que não haverá repetição de números dentro de um mesmo jogo. Isso é importante para evitar que um jogo contenha números duplicados, o que reduziria drasticamente as chances de acerto.

Utilizar números menos frequentes: Em vez de gerar números aleatórios uniformemente entre 1 e 60, você pode considerar utilizar uma distribuição que favoreça números menos frequentes. Isso pode aumentar as chances de ter um jogo único, o que, em teoria, reduziria a chance de dividir o prêmio em caso de acerto.

Considerar números frequentemente sorteados: Por outro lado, também é válido considerar números que são frequentemente sorteados. Embora isso não garanta um prêmio maior em caso de acerto, pode aumentar as chances de ganhar junto com outros jogadores, resultando em prêmios mais altos.

Análise histórica dos resultados: Realizar uma análise dos resultados anteriores da Mega Sena pode fornecer insights sobre padrões de números frequentemente sorteados, números menos sorteados e combinações de números que aparecem juntos com mais frequência. Isso pode ajudar na seleção dos números para os palpites.

Simulação e otimização: É possível usar técnicas de simulação e otimização para gerar palpites de forma mais inteligente, levando em consideração as informações históricas e as estratégias mencionadas anteriormente.

Combinações inteligentes: Em vez de gerar os palpites de forma completamente aleatória, você pode considerar gerar combinações inteligentes baseadas em padrões observados nos resultados anteriores. Por exemplo, escolher números que formam sequências, combinações de números primos, ou outras características que podem aumentar ligeiramente as chances de acerto.
"""
# Importa a função 'sample' do módulo 'random' para gerar amostras aleatórias e a função 'sleep' do módulo 'time' para introduzir atrasos.
from random import sample
from time import sleep

# Função para gerar um palpite para um jogo da Mega Sena.
def gerar_palpite():
    # Utiliza a função sample para selecionar 6 números únicos entre 1 e 60 e os retorna ordenados.
    return sorted(sample(range(1, 61), 6))

# Função para imprimir os jogos na tela.
def imprimir_jogos(jogos):
    # Imprime uma linha decorativa indicando que os jogos estão sendo sorteados.
    print('-=' * 3, f' SORTEANDO {len(jogos)} JOGOS ', '-=' * 3)
    # Itera sobre os jogos e os imprime na tela, aguardando 1 segundo entre cada jogo.
    for i, jogo in enumerate(jogos):
        print(f'Jogo {i + 1}: {jogo}')
        sleep(1)
    # Imprime uma mensagem de boa sorte após a exibição dos jogos.
    print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

# Função principal que controla o fluxo do programa.
def main():
    # Imprime cabeçalho para o jogo da Mega Sena.
    print('_' * 30)
    print('       JOGA NA MEGA SENA      ')
    print('-' * 30)
    # Pergunta ao usuário quantos jogos ele deseja sortear.
    quant = int(input('Quantos jogos você quer que eu sorteie? '))
    
    # Gera uma lista de jogos usando list comprehension e a função 'gerar_palpite()'.
    jogos = [gerar_palpite() for _ in range(quant)]
    # Chama a função 'imprimir_jogos()' para exibir os jogos sorteados na tela.
    imprimir_jogos(jogos)

# Condição que verifica se este arquivo está sendo executado diretamente.
if __name__ == "__main__":
    # Chama a função principal 'main()' para iniciar o programa.
    main()
