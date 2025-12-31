#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.nxtdevices import LightSensor
from pybricks.ev3devices import ColorSensor, Motor, GyroSensor
from pybricks.parameters import Port, Color, Button
from time import sleep

ev3 = EV3Brick()

global loop
global trajeto
global movimentoFinal
global chave
global retorno
movimentoFinal = False
loop = True
trajeto = True
# cordenadas abrindo uma lista
coordenadas = []
# Transcrever as portas de entrada --------------------------------------------------------
sensor_cor = ColorSensor(Port.S2)
sensor_luminosidade_esquerda = LightSensor(Port.S3)
sensor_luminosidade_direita = LightSensor(Port.S1)
giroscopio = GyroSensor(Port.S4)
motor_direita = Motor(Port.D)
motor_esquerda = Motor(Port.A)

#ev3.screen.load_image("Logo Gajac.png")
#ev3.speaker.beep(frequency=500, duration=100)

# desconsiderar essa função
def Confirmacao():
    global passe
    passe = False
    while not passe:
        if (len(ev3.buttons.pressed())>0):
            passe = True

def LeituraCoordenadas():

    
    # É necessário primeiro fazermos experimento na prática para ver como está cada conexão do robô.
    global loop
    global chave
    global sD
    global sE
    global fita
    fita = 40
    # ^| Qual variavel isso representa?
    loop = True
    chave = 0
    while (loop == True):
        # Se o botão estiver pressionado a leitura começará
        #- Botão pressionado e então começar o código?
        if (len(ev3.buttons.pressed())>0): 
            while (loop == True):
                motor_direita.run(80)
                motor_esquerda.run(80)
                sleep(1.65)
                motor_direita.run(0)
                motor_esquerda.run(0)
                coordenadas.append(sensor_cor.color())
                ev3.screen.print(coordenadas[chave], end='\n')
                if (coordenadas[chave] == Color.RED ):
                    loop = False
                if (coordenadas[chave] != Color.RED):
                    sleep(1)
                    motor_direita.run(0)
                    motor_esquerda.run(0)
                
                    chave += 1
    ev3.speaker.beep(frequency=500, duration=100)
    if loop == False:
        print(coordenadas)

def Alinhamento():
    global angulo
    global alinhou
    alinhou = False
    while not alinhou:
        sE = sensor_luminosidade_esquerda.reflection()
        sD = sensor_luminosidade_direita.reflection()
        fita = 40 # > 6 branco
                 # < 6 preto
        print('E: {}\t   D:{}'.format(sE,sD))

        if sE > fita and sD > fita: 
            motor_direita.run(50)
            motor_esquerda.run(50)

        elif sE < fita and sD > fita:
            motor_direita.run(30)
            motor_esquerda.run(-30)

        elif sD < fita and sE > fita:
            motor_direita.run(-30)
            motor_esquerda.run(30)

        elif sD < fita and sE < fita:
            motor_direita.brake()
            motor_esquerda.brake()
            alinhou = True
            angulo = giroscopio.angle()
    ev3.speaker.beep(frequency=500, duration=100)

def Movimento():
    global chave, movimentoFinal, localizacao
    linha = 2
    coluna = 1
    movimentoFinal = False
    chave = 0
    while movimentoFinal == True:

        while trajeto == True:
                
            if (chave < 1):
                if (coordenadas[chave] == Color.BLUE):
                    movimentoFrente()
                    somaLocalizacao += 3
                if (coordenadas[chave] == Color.YELLOW):
                    movimentoDireita()
                    bussola = "D"
                    somaLocalizacao += 2
                if (coordenadas[chave] == Color.GREEN):
                    movimentoEsquerda()
                    bussola = "E"
                    somaLocalizacao += 4
            else:
                if (coordenadas[chave] == Color.BLUE):
                    movimentoFrente()
                    if(bussola == "D"):
                        somaLocalizacao -= 1 
                    elif(bussola == "B"):
                        somaLocalizacao -= 3
                    elif(bussola == "E"):
                        somaLocalizacao += 1
                    elif (bussola == "N"):
                        somaLocalizacao += 3
                if (coordenadas[chave] == Color.YELLOW):
                    movimentoDireita()
                    if(bussola == "D"):
                        bussola = "B"
                        somaLocalizacao -= 2
                    elif(bussola == "B"):
                        bussola = "E"
                        somaLocalizacao -= 4
                    elif(bussola == "E"):
                        bussola = "N"
                        somaLocalizacao += 4 
                    elif (bussola == "N"):
                        bussola = "D"
                        somaLocalizacao += 2
                if (coordenadas[chave] == Color.GREEN):
                    movimentoEsquerda()
                    if(bussola == "D"):
                        bussola = "N"
                        somaLocalizacao += 2
                    elif(bussola == "B"):
                        bussola = "D"
                        somaLocalizacao -= 2
                    elif(bussola == "E"):
                        bussola = "B"
                        somaLocalizacao -= 4
                    elif (bussola == "N"):
                        bussola = "E"
                        somaLocalizacao += 4
                if (coordenadas[chave] == Color.RED):
                            parar()
                            movimentoFinal = True
                            chave -= 1
            chave += 1

def movimentoDireita():

    print("movimento direita")
    global retorno, vel, angulo_motor, angulo, contador, alinhou, retornoDivi, retornoDiviMain, loop
    loop = 1
    alinhou = False
    contador = int
    
    motor_esquerda.run(0)
    motor_direita.run(0)
    
    while (loop < 4):
        motor_direita.run_target(200, motor_direita.angle() - 20)
        motor_esquerda.run_target(200,motor_esquerda.angle() - 20)
        loop += 1
     
    giroscopio.reset_angle(0)
    
    while (abs(giroscopio.angle()) != 85):
        
        angulo = giroscopio.angle()
        
        if(angulo < 85):
            motor_esquerda.run(30)
            motor_direita.run(-30)
            
        if (angulo > 85):
            motor_esquerda.run(-30)
            motor_direita.run(30)

    motor_direita.run(0), motor_esquerda.run(0)
    
    alinhou = False
    
    while not alinhou:
        
        sE = sensor_luminosidade_esquerda.reflection()
        sD = sensor_luminosidade_direita.reflection()
        fita = 40 # > 30 branco
                  # < 30 preto
        

        if sE > fita and sD > fita: 
            motor_direita.run(100)
            motor_esquerda.run(100)

        elif sE < fita and sD > fita:
            motor_direita.run(30)
            motor_esquerda.run(-30)

        elif sD < fita and sE > fita:
            motor_direita.run(-30)
            motor_esquerda.run(30)

        elif sD < fita and sE < fita:
            motor_direita.run(0)
            motor_esquerda.run(0)
            alinhou = True
        
    motor_direita.run(100)
    motor_esquerda.run(100)
    sleep(2)
        
    alinhou = False
        
    while not alinhou:
        
        sE = sensor_luminosidade_esquerda.reflection()
        sD = sensor_luminosidade_direita.reflection()
        fita = 40 # > 30 branco
                  # < 30 preto
        

        if sE > fita and sD > fita: 
            motor_direita.run(100)
            motor_esquerda.run(100)

        elif sE < fita and sD > fita:
            motor_direita.run(30)
            motor_esquerda.run(-30)

        elif sD < fita and sE > fita:
            motor_direita.run(-30)
            motor_esquerda.run(30)

        elif sD < fita and sE < fita:
            motor_direita.run(0)
            motor_esquerda.run(0)
            alinhou = True
            
    motor_esquerda.run(0)
    motor_direita.run(0)
    print("FIM MOVIMENTO DIREITA")

def movimentoEsquerda():
    global retorno, vel, angulo_motor, angulo, contador, alinhou, retornoDivi, retornoDiviMain, loop
    loop = 0
    alinhou = False
    contador = int

    motor_esquerda.run(0)
    motor_direita.run(0)
    
    motor_esquerda.reset_angle(0)
    motor_direita.reset_angle(0)
    
    while (loop < 4):
        motor_direita.run_target(200, motor_direita.angle() - 20)
        motor_esquerda.run_target(200,motor_esquerda.angle() - 20)
        loop += 1
    
    giroscopio.reset_angle(0)
    
    while (abs(giroscopio.angle()) != 90):
        
        angulo = giroscopio.angle()
        
        if(giroscopio.angle() < 90):
            motor_esquerda.run(-30)
            motor_direita.run(30)
        if (giroscopio.angle() > 90):
            motor_esquerda.run(30)
            motor_direita.run(-30)

    motor_esquerda.run(0), motor_direita.run(0)
    
    while not alinhou:
        
        sE = sensor_luminosidade_esquerda.reflection()
        sD = sensor_luminosidade_direita.reflection()
        fita = 40 # > 30 branco
                  # < 30 preto
        

        if sE > fita and sD > fita: 
            motor_direita.run(100)
            motor_esquerda.run(100)

        elif sE < fita and sD > fita:
            motor_direita.run(30)
            motor_esquerda.run(-30)

        elif sD < fita and sE > fita:
            motor_direita.run(-30)
            motor_esquerda.run(30)

        elif sD < fita and sE < fita:
            motor_direita.run(0)
            motor_esquerda.run(0)
            alinhou = True
            
    motor_direita.run(100)
    motor_esquerda.run(100)
    sleep(2)
        
    alinhou = False
        
    while not alinhou:
        
        sE = sensor_luminosidade_esquerda.reflection()
        sD = sensor_luminosidade_direita.reflection()
        fita = 40 # > 30 branco
                  # < 30 preto
        

        if sE > fita and sD > fita: 
            motor_direita.run(100)
            motor_esquerda.run(100)

        elif sE < fita and sD > fita:
            motor_direita.run(30)
            motor_esquerda.run(-30)

        elif sD < fita and sE > fita:
            motor_direita.run(-30)
            motor_esquerda.run(30)

        elif sD < fita and sE < fita:
            motor_direita.run(0)
            motor_esquerda.run(0)
            alinhou = True
            
    motor_esquerda.run(0)
    motor_direita.run(0)

def movimentoFrente():
    global alinhou
    alinhou = False
    motor_direita.run(100)
    motor_esquerda.run(100)
    sleep(2)
    while not alinhou:
        
        print(sensor_luminosidade_direita.reflection()," - ", sensor_luminosidade_esquerda.reflection())
        sE = sensor_luminosidade_esquerda.reflection()
        sD = sensor_luminosidade_direita.reflection()
        fita = 40 # > 30 branco
                  # < 30 preto
        

        if sE > fita and sD > fita: 
            motor_direita.run(100)
            motor_esquerda.run(100)

        elif sE < fita and sD > fita:
            motor_direita.run(30)
            motor_esquerda.run(-30)

        elif sD < fita and sE > fita:
            motor_direita.run(-30)
            motor_esquerda.run(30)

        elif sD < fita and sE < fita:
            motor_direita.run(0)
            motor_esquerda.run(0)
            alinhou = True
    print("FIM MOVIMENTO FRENTE")

def movimentoInicial():
    global alinhou
    alinhou = False
    while not alinhou:
        
        sE = sensor_luminosidade_esquerda.reflection()
        sD = sensor_luminosidade_direita.reflection()
        fita = 40 # > 30 branco
                  # < 30 preto
        

        if sE > fita and sD > fita: 
            motor_direita.run(100)
            motor_esquerda.run(100)

        elif sE < fita and sD > fita:
            motor_direita.run(30)
            motor_esquerda.run(-30)

        elif sD < fita and sE > fita:
            motor_direita.run(-30)
            motor_esquerda.run(30)

        elif sD < fita and sE < fita:
            motor_direita.run(0)
            motor_esquerda.run(0)
            alinhou = True
            
    motor_direita.run(100)
    motor_esquerda.run(100)
    sleep(2)
    
    alinhou = False
    while not alinhou:
        
        sE = sensor_luminosidade_esquerda.reflection()
        sD = sensor_luminosidade_direita.reflection()
        fita = 40 # > 30 branco
                  # < 30 preto
        

        if sE > fita and sD > fita: 
            motor_direita.run(100)
            motor_esquerda.run(100)

        elif sE < fita and sD > fita:
            motor_direita.run(30)
            motor_esquerda.run(-30)

        elif sD < fita and sE > fita:
            motor_direita.run(-30)
            motor_esquerda.run(30)

        elif sD < fita and sE < fita:
            motor_direita.run(0)
            motor_esquerda.run(0)
            alinhou = True

def parar():
    global linha
    global coluna
    #ev3.screen.load_image()
    print("Trajeto Concluído!")
    ev3.screen.print("Linha: ", linha, " Coluna: ", coluna)
    trajeto = False
    #ev3.screen.clear()

#Definição de Botões

cima = Button.UP
baixo = Button.DOWN
esquerdo = Button.LEFT
direita = Button.RIGHT
centro = Button.CENTER

#Leitura

LeituraCoordenadas()
Confirmacao()
movimentoInicial()
Movimento()