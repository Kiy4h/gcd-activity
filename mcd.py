import pygame, random
import util
import sonidos
from boton import Boton
from palanca import Palanca
from cube import Cube
from bomba import Bomba
from bombaE import BombaE
from explosion import Explosion
from helicopter import Helicopter
from pygame import *

def write_file(self, file_path):
    pass

def read_file(self, file_path):
    pass
def run():
    pygame.init()
    pygame.font.init()
    # recursos del juego
    screen = pygame.display.set_mode((799, 464), pygame.RESIZABLE)
    #screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    pygame.display.set_caption("MachineMCD")
    temporizador = pygame.time.Clock()
    power = 0
    maximo = 0
    gameOver= 0
    mcd1=1

    haybomba = False
    controlMaximo = True
    texto = pygame.font.Font('digital-7.ttf', 42)
    texto2 = pygame.font.Font('digital-7.ttf', 25)
    textobomba = pygame.font.Font('Crysta.ttf', 26)
    # fondo de pantalla
    fondo = util.cargar_imagen('escenario.png', optimizar=True)
    decoracion = util.cargar_imagen('decoracion.png')
    final = util.cargar_imagen('Final.png')

    bomba = Bomba(-20,-20)
    bombaE = BombaE(100,100)
    # grupos
    sprites = pygame.sprite.OrderedUpdates()
    explo = pygame.sprite.Group()
    control = pygame.sprite.Group()
    cube1 = pygame.sprite.Group()
    cube2 = pygame.sprite.Group()
    helicopter = pygame.sprite.Group()
    Bomasprites = pygame.sprite.Group()
    botonA = Boton(500,435,'a')
    botonB = Boton(600,435,'s')
    palanca = Palanca(208,387)
    helicoptero= Helicopter(105,95)
    control.add([botonA,botonB, palanca])
    helicopter.add([helicoptero])
    sprites.add([cube1,cube2,helicopter])

    salir = False
    def divisoresPropios(n):
       lista = []
       for i in range(1,(n/2)+1):
           if (n%i)==0:
               lista.append(i)
       lista.append(n)
       return lista

    def mcd(a,b):
        a,b = max(abs(a),abs(b)),min(abs(a),abs(b));
        while b>0:
            a,b = b,a%b
        return a

    def draw_cubes():
        posY1=350
        posX1=60
        posY2=350
        posX2=410
        n=0
        j=0
        for i in range(numcubes1):        
            if j < 11:
                j= j+1
                posX1=posX1+25
                cube1.add(Cube(posX1, posY1))            
            else:
                j=1
                posX1=60 + 25
                posY1=posY1-25
                cube1.add(Cube(posX1, posY1))          
        for m in range(numcubes2):        
            if n < 11:
                n= n+1
                posX2=posX2+25
                cube2.add(Cube(posX2, posY2))
            else:
                n=1
                posX2=410 + 25
                posY2=posY2-25
                cube2.add(Cube(posX2, posY2))


    numero1=random.randint(0, 70);
    numero2=random.randint(1, 70);

    numcubes1= numero1
    numcubes2= numero2
    #numcubes1=4
    #numcubes2=12
    mcd1= mcd(numero1, numero2)
    div1=[]
    div2=[]
    div1=divisoresPropios(numero1)    
    div2=divisoresPropios(numero2)
    Text_Divisores1 = ""
    Text_Divisores2 = ""
    for divisor1 in div1:
        Text_Divisores1 += str(divisor1)+" "
    for divisor2 in div2:
        Text_Divisores2 += str(divisor2)+" "
            
            
    draw_cubes()
    bombanumero = textobomba.render("00",1,(176,0,0))
    while not salir:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                salir = True
            elif e.type == pygame.KEYDOWN:
                if e.unicode == 'a' or e.unicode == 'A':
                    if haybomba == False:       
                        power = maximo
                        controlMaximo = False
                        bomba = Bomba(helicoptero.rect.x+45, helicoptero.rect.y+20)  
                        sprites.add(bomba)
                        haybomba = True
        #    elif e.type == pygame.JOYBUTTONUP:

        if controlMaximo == True:
            teclasSelect = pygame.key.get_pressed()
            if teclasSelect[K_DOWN]and maximo>0:
                maximo= maximo-1
                bombanumero = textobomba.render( str(maximo),1,(176,0,0))
                #text = font.render( str(maximo),1,WHITE)    
            elif teclasSelect[K_UP] and maximo<99:
                maximo=maximo+1
                bombanumero = textobomba.render( str(maximo),1,(176,0,0))

        if numcubes1==0 and numcubes2==0:

            gameOver = 2
    #    if (numcubes1>0 or numcubes2>0)and power == 0 and haybomba == True:

    #    if (numcubes1>0 or numcubes2>0):
     

      #      gameOver = 1

        if power> 0:         
            bomba_en_colision2 = pygame.sprite.spritecollide(bomba, cube2, False)
            bomba_en_colision1 = pygame.sprite.spritecollide(bomba, cube1, False)        

            if (bomba_en_colision1):
                if (numcubes2>0 and numcubes1<power) or (numcubes2>0 and numcubes1==0):
                    gameOver = 1
                    bomba.kill()
            if (bomba_en_colision2):
                if (numcubes1>0 and numcubes2<power) or (numcubes1>0 and numcubes2==0)  :            
                    gameOver = 1
                    bomba.kill()

                #haybomba = False
            

            if bomba_en_colision1 and numcubes1>=power:
                power -=1
                numcubes1-= 1
                
                bomba_en_colision1[0].kill()
                cube1.remove(bomba_en_colision1[0])
                sprites.add(Explosion(bomba_en_colision1[0]))
                sonidos.reproducir_sonido('boom')
            

            if bomba_en_colision2 and numcubes2>=power:
                power -=1
                numcubes2-= 1
                bomba_en_colision2[0].kill()
                cube2.remove(bomba_en_colision2[0])
                sprites.add(Explosion(bomba_en_colision2[0]))
                sonidos.reproducir_sonido('boom')
            
        elif power==0:
            bomba.kill()
            haybomba = False



        cubos1 = texto.render( str( len(cube1.sprites()) ),1,(255,215,0)) 
        cubos2 = texto.render( str( len(cube2.sprites()) ),1,(255,215,0)) 
          
        game1 = ["Ganaste!! ","el poder de mayor destruccion es","Casi lo logras!!","Lo sentimos!!","Divisores del ", ":"] 
        gameMCD = texto2.render( str( mcd1),1,(255,255,255)) 
        num1 = texto2.render( str( numero1),1,(255,255,255))       
        num2 = texto2.render( str( numero2 ),1,(255,255,255))       
        
        sprites.update()
        screen.blit(fondo, (0, 0))
        cube1.draw(screen)
        cube2.draw(screen)       
        sprites.draw(screen)
        helicopter.draw(screen)
        Bomasprites.draw(screen)
        screen.blit(decoracion, (0, 0))
        screen.blit(cubos1, (347, 98))
        screen.blit(cubos2, (417, 98)) 
        screen.blit(bombanumero, (387, 55))

        if gameOver!= 0:
            screen.blit(final, (0, 0))
                
            if gameOver == 2 and maximo == mcd1 :
                textIm1 = texto.render(game1[0],1,(255,255,255))
                textIm2 = texto2.render(game1[1],1,(255,255,255))
            if gameOver == 2 and maximo != mcd1 :
                textIm1 = texto.render(game1[2],1,(255,255,255))
                textIm2 = texto2.render(game1[1],1,(255,255,255))
            if gameOver == 1:
                textIm1 = texto.render(game1[3],1,(255,255,255))
                textIm2 = texto2.render(game1[1],1,(255,255,255))
            textIm3 = texto2.render(game1[4],1,(255,255,255))
           # mcd2 = texto2.render(mcd1,1,(255,255,255))
            screen.blit(textIm1,(150,110))            
            screen.blit(textIm2,(150,145))
            screen.blit(gameMCD, (520, 145))
            #screen.blit(mcd2, (520, 145))
            screen.blit(textIm3, (170, 185))
            screen.blit(num1, (320, 185))
            screen.blit(texto2.render(Text_Divisores1,1,(255,255,255)),(175, 210))
            screen.blit(textIm3, (170, 250))
            screen.blit(num2, (320, 250))
            screen.blit(texto2.render(Text_Divisores2,1,(255,255,255)),(175, 275))
            
        control.draw(screen)
        control.update()
        pygame.display.flip()
        temporizador.tick(60)
        
if __name__ == '__main__':
    run()        
