import pygame,random,time

pygame.init()
tempo = pygame.time.Clock()

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


def choose_color():
    verde_light = {'cor': VERDE, 'posicao': ((81, 317), (230, 317), (230, 169))}
    amarelo_light = {'cor': AMARELO, 'posicao': ((409, 315), (263, 315), (263, 168))}
    azul_light = {'cor': AZUL, 'posicao': ((411, 345), (264, 346), (263, 495))}
    vermelho_light = {'cor': VERMELHO, 'posicao': ((80, 345), (230, 346), (230, 495))}

    colors = [verde_light, amarelo_light, vermelho_light, azul_light]
    return random.choice(colors)


def blinkColors(list_colors):
    for color in list_colors:
        
        pygame.draw.polygon(tela_inicial, color['cor'], color['posicao'])
        pygame.display.update()
        time.sleep(0.3)                                         # Tempo para mostrar a proxima cor

        tela_inicial.blit(tela_jogo, (0, 30))
        pygame.display.update()
        time.sleep(0.3) 

game = False
seq_colors = [] 

tela_inicial.blit(tela_jogo, (0, 30))
pygame.display.update()

game = True
while game:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game= False

    seq_colors.append(choose_color())              # Escolhe uma cor e adiciona a lista de sequencia
    blinkColors(seq_colors)        

    
    
    pygame.display.update()


       

    

    
