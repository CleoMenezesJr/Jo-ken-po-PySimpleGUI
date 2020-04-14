import PySimpleGUI as sg
from random import randint
sg.theme('BlueMono')

cont = 0
placar_jogador = 0
placar_computador = 0

nome =sg.popup_get_text('Por favor, digite teu nome', 'Jo-Ken-Po!')
#Mensagens
msg0 = (f'{nome} Ganhou!!!')
msg1 = ('Computador Ganhou!!')
msg2 = ('Empate!!')
#dicionarios
dl = {'size':(10,0), 'font':('Serif Bold', 20)}
de = {'size':(2,0), 'font':('Serif Bold', 20), 'background_color':'Light Blue'}


layout = [
	[sg.Text(nome, **dl), sg.InputText(placar_jogador, key='placar_jogador', **de, justification='right'), sg.Text('X', **dl, justification='center'), sg.InputText(placar_computador, key='placar_computador', **de, justification='left'), sg.Text('Computador', **dl)],
	[sg.Button(key='0', image_filename='Images/pedra.png'), sg.Button(key = '1', image_filename='Images/papel.png'), sg.Button(key = '2', image_filename='Images/tesoura.png')],
	[sg.Text('Rodada', **dl), sg.InputText(cont, key= 'cont', **de, justification='center')]
]
janela = sg.Window('Jo-Ken-Po!', layout)


##############

while True:
	# Computador
	computador_jogada = randint(0, 2)
	computador = ['Pedra', 'Papel', 'Tesoura']


	#jogo
	event, values = janela.read()
	#jogador joga pedra
	if event in '0':
		if computador_jogada == 0 and event == '0':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg2)
		elif computador_jogada == 1 and event == '0':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg1)
			placar_computador += 1
		elif computador_jogada == 2 and event == '0':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg0)
			placar_jogador += 1

	#jogador joga pedra
	if event in '1':
		if computador_jogada == 0 and event == '1':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg0)
			placar_jogador += 1
		elif computador_jogada == 1 and event == '1':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg2)
		elif computador_jogada == 2 and event == '1':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg1)
			placar_computador += 1

	#jogador joga tesoura
	if event in '2':
		if computador_jogada == 0 and event == '2':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg1)
			placar_computador += 1
		elif computador_jogada == 1 and event == '2':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg0)
			placar_jogador += 1
		elif computador_jogada == 2 and event == '2':
			sg.popup(f'O Computador jogou {computador[computador_jogada]}', msg2)


	cont += 1
	janela['cont'].Update(cont)
	janela['placar_computador'].Update(placar_computador)

	janela['placar_jogador'].Update(placar_jogador)
	if event in(None, 'Cancel', ):
		break
janela.close()