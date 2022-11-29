import pygame,random,time
from pygame.locals import *

pygame.init()
tempo = pygame.time.Clock()

texto_inicio_fonte = pygame.font.SysFont('Arial', 80)
placar_fonte= pygame.font.SysFont("Arial", 28)

tela_inicial = pygame.display.set_mode((500, 530), 0, 32)           # Janela
pygame.display.set_caption("DOC")                            # Titulo da janela
tela_icone = pygame.image.load('assets/logo2.png')                       # Imagem do icone do jogo
pygame.display.set_icon(tela_icone)

tela_de_fundo = pygame.image.load('assets/DOC.png')                     # Imagem de fundo
tela_jogo = pygame.image.load('assets/Fundo.png')

# Cores
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
AZUL = (50, 190, 255)
BRANCO = (255, 255, 255)

verde = pygame.draw.polygon(tela_inicial, VERDE, ((81, 317), (230, 317), (230, 159)))
amarelo = pygame.draw.polygon(tela_inicial, AMARELO, ((409, 315), (263, 315), (263, 168)))
vermelha = pygame.draw.polygon(tela_inicial, VERMELHO, ((80, 345), (230, 346), (230, 495)))
azul = pygame.draw.polygon(tela_inicial, AZUL, ((411, 345), (265, 347), (263, 495)))



texto_comeco = texto_inicio_fonte.render('Jogar', True, (255, 255, 255))   # Texto do botao começar

def choose_color():
    verde_light = {'cor': VERDE, 'posicao': ((81, 317), (230, 317), (230, 169))}
    amarelo_light = {'cor': AMARELO, 'posicao': ((409, 315), (263, 315), (263, 168))}
    azul_light = {'cor': AZUL, 'posicao': ((411, 345), (264, 346), (263, 495))}
    vermelho_light = {'cor': VERMELHO, 'posicao': ((80, 345), (230, 346), (230, 495))}

    colors = [verde_light, amarelo_light, vermelho_light, azul_light]
    return random.choice(colors)


def blinkColors(list_colors):
    # Desenhando o score

    text_placar = placar_fonte.render("{0}".format(pontos), True, (255, 255, 0))
    text_rect = text_placar.get_rect()

    text_rect.midtop = (250,  0)

    tela_inicial.blit(text_placar, text_rect)

    for color in list_colors:
        
        pygame.draw.polygon(tela_inicial, color['cor'], color['posicao'])
        pygame.display.update()
        time.sleep(0.3)                                         # Tempo para mostrar a proxima cor

        tela_inicial.blit(tela_jogo, (0, 30))
        pygame.display.update()
        time.sleep(0.3)
        

game = False
seq_colors = []
pontos = 0

# Aguarda a resposta do jogador e retorna a resposta
def Resposta(qnt_color):
    user_guess = []

    while 1 <= qnt_color:
        for ocorrencia in pygame.event.get():
            if ocorrencia.type == pygame.QUIT:
                quit()
            if ocorrencia.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if verde.collidepoint(mouse):
                    
                    user_guess.append(VERDE)
                    qnt_color -= 1
                elif amarelo.collidepoint(mouse):
                    
                    user_guess.append(AMARELO)
                    qnt_color -= 1
                elif vermelha.collidepoint(mouse):
                   
                    user_guess.append(VERMELHO)
                    qnt_color -= 1
                elif azul.collidepoint(mouse):
                    
                    user_guess.append(AZUL)
                    qnt_color -= 1
                
    return user_guess


def check_Resposta(resp_player, lista_seq):
    seq_colors = []
    for cor in lista_seq:
        seq_colors.append(cor['cor'])

    if resp_player == seq_colors:
        return True
    else:
        return False

while not game:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        if evento.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if btn_play.collidepoint(mouse):
                game = True

    tela_inicial.blit(tela_de_fundo, (0, 30))
    
    btn_play = pygame.draw.rect(tela_inicial, (0, 0, 0), (115, 370, 270, 100))  # Desenha botao
    tela_inicial.blit(texto_comeco, (172, 365))
    pygame.display.update()
    tempo.tick(27)

tela_inicial.blit(tela_jogo, (0, 30))
pygame.display.update()

game = True
while game:
    time.sleep(1)
    tela_inicial.fill((0,0,0))
    tela_inicial.blit(tela_jogo, (0, 30))
    
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game= False

    seq_colors.append(choose_color())              # Escolhe uma cor e adiciona a lista de sequencia
    blinkColors(seq_colors)
    # Desenhando o score

    text_placar = placar_fonte.render("{0}".format(pontos), True, (255, 255, 0))
    text_rect = text_placar.get_rect()

    text_rect.midtop = (250,  0)

    tela_inicial.blit(text_placar, text_rect)
    pygame.display.update()    


    

    resposta_jogador = Resposta(len(seq_colors))    # Aguarda a resposta do jogador

    if check_Resposta(resposta_jogador, seq_colors):
        pontos = pontos + 1
       
        
        
    else:
        game=False
    
    
    
    


       

    

    
