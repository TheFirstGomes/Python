# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.lower() == "sim"
    afinidade_animais = afinidade_animais.lower() == "sim"

    # Desenvolva a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
        return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    elif intensidade >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100:
        return "A afinidade elemental do feiticeiro é com o elemento Água!"
    else:
        return "A afinidade elemental do feiticeiro é com o elemento Ar!"

# Entrada do usuário
intensidade_feitico = int(input("Intensidade do feitiço (de 1 a 10): "))
while intensidade_feitico < 1 or intensidade_feitico > 10:
    print("Intensidade do feitiço deve estar entre 1 e 10.")
    intensidade_feitico = int(input("Intensidade do feitiço (de 1 a 10): "))

componente_raro_feitico = input("Componente raro (sim ou não): ").lower()
while componente_raro_feitico not in ['sim', 'não']:
    print("Por favor, responda com 'sim' ou 'não'.")
    componente_raro_feitico = input("Componente raro (sim ou não): ").lower()

fase_lunar_feitico = input("Fase lunar (cheia ou crescente): ").lower()
while fase_lunar_feitico not in ['cheia', 'crescente', 'minguante']:
    print("Por favor, escolha entre 'cheia', 'crescente' ou 'minguante'.")
    fase_lunar_feitico = input("Fase lunar (cheia, crescente ou minguante): ").lower()

idade_feiticeiro = int(input("Idade do feiticeiro (em anos): "))

afinidade_animais_feiticeiro = input("Afinidade com animais mágicos (sim ou não): ").lower()
while afinidade_animais_feiticeiro not in ['sim', 'não']:
    print("Por favor, responda com 'sim' ou 'não'.")
    afinidade_animais_feiticeiro = input("Afinidade com animais mágicos (sim ou não): ").lower()


# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão
print(resultado)