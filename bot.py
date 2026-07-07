#permite usar cores nos textos
from colorama import init, Fore, Style
init()

#permite criar pequenas pausas na conversa
import time

#dicionário vazio pra guardar as respostas da pessoa ao longo da conversa
answers = {}

#Moldura de boas vindas com um efeito de "digitação" pausada
print('╔' + '═' * 48 + '╗')
print('║' + '   Welcome to a chat with Táta! 🤖'.center(48) + '║')
print('╚' + '═' * 48 + '╗')
time.sleep(1)

#Faz uma pequena introdução para dizer que só consegue se comunicar em inglês
print(f'Hi! I am {Fore.BLUE}Táta{Style.RESET_ALL}, and i can only speak English!')
time.sleep(1)
print('Please answer in English too. 😊')
print('=' * 40)

#permite que a pessoa escreva apenas letras no nome dela e também permite nomes compostos com espaços
#nomes com acentos também funcionam por conta do python 3
while True:
    name_input = input(f'Hello my name is {Fore.BLUE}Táta😊 {Style.RESET_ALL}What is your name? ')
    if name_input.replace(' ', '').isalpha():
        break
    else:
        print(f'{Fore.RED}Please use only letters in your name!{Style.RESET_ALL}')

answers['name'] = name_input #guarda o nome no dicionário

print('=' * 40)

print(f'What a beautiful name! Nice to meet you, {name_input}!')

print('=' * 40)
#identifica a idade, não permite idades negativas e nem idades escritas em formato de string
while True:
    age_input = input(f'I have {Fore.BLUE}13{Style.RESET_ALL} years old what about you? ')
    try:
        age = int(age_input)
        if age < 0:
            print(f'{Fore.RED}Age cannot be negative!{Style.RESET_ALL}')
            continue
        break
    except ValueError:
        print(f'{Fore.RED}Sorry, but that is not a valid age!{Style.RESET_ALL}')

answers['age'] = age #guarda a idade no dicionário

print('=' * 40)
#verifica a diferença de idades e faz uma resposta para cada número da diferença de idade
bot_age = 13
age_difference = age - bot_age

if age_difference > 20:
    print(f'Wow, you are {age_difference} years older than me?! You must know SO much about the world!')
elif age_difference > 0:
    print(f'Yay, you are {age_difference} years older than me! I still have a lot to learn!')
elif age_difference == 0:
    print(f'No way, we are the same age?! Best friends already!')
else:
    print(f'What?! You are younger than me? That is so cool, i feel lika a wise old bot now')

print('=' * 40)
#O bot reconhece as cores e responde de acordo com as cores que ele conhece
#Se a pessoa digitar uma cor em inglês o bot não responderá
portuguese_colors = ['azul', 'vermelho', 'verde', 'amarelo', 'roxo', 'preto', 'branco', 'rosa']

while True: #faz voltar para a pergunta se a pessoa escrever alguma cor em português
    color = input('What is your favorite color? ')
    color = color.lower() #faz com que todas as respostas fiquem em caixa baixa, para bater com as cores do bot

    if color in portuguese_colors:
        print(f'{Fore.RED}Oops! Remember, i only understand English. Try again in English{Style.RESET_ALL}')
        continue
    break

answers['favorite color'] = color #guarda a cor no dicionário

print('=' * 40)
if color == 'blue':
    print(f'{Fore.BLUE}Ooooh {color.capitalize()}! Just like the sky and the ocean, so calming!{Style.RESET_ALL}')
elif color == 'red':
    print(f'{Fore.RED}{color.capitalize()}! The color of the hearts, so full of energy!{Style.RESET_ALL}')
elif color == 'green':
    print(f'{Fore.GREEN}Hurrah! {color.capitalize()} Is amazing, just like the nature!{Style.RESET_ALL}')
elif color == 'yellow':
    print(f'{Fore.YELLOW}{color.capitalize()}?! That is such a happy, sunny color{Style.RESET_ALL}')
elif color == 'purple':
    print(f'{Fore.MAGENTA}Yeap! {color.capitalize()}, so royal and mysterious!{Style.RESET_ALL}')
elif color == 'black':
    print(f'{Fore.BLACK}Uuh {color.capitalize()} is so sleek and mysterious!{Style.RESET_ALL}')
elif color == 'white':
    print(f'{Fore.WHITE}Wow {color.capitalize()}? Pure and elegant!{Style.RESET_ALL}')
elif color == 'pink':
    print(f'{Fore.LIGHTMAGENTA_EX}I love {color.capitalize()}! So sweet and cheerful!{Style.RESET_ALL}')
else:
    print(f'Wow {color.capitalize()}! I have never heard anyone pick that before!')

#resumo final com tudo que foi guardado no dicionário
print('=' * 40)
print('╔' + '═' * 48 + '╗')
print('║' + '        It was an honor to meet you! 📋'.center(48) + '║')
print('╚' + '═' * 48 + '╝')

for key, value in answers.items():
    print(f'{Fore.CYAN}{key.capitalize()}{Style.RESET_ALL}: {value}')