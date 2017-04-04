# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:42:05 2017

@author: arthu
"""

# EP2_Arthur_e_Thomas

import sys,time,random
nv = 1
mon = [0]*5
mon[1] = 150 #vida
mon[2] = 50 #ataque
mon[3] = 20 #defesa
mon[4] = 150 #Vidafull
expfill = 30
exp = 0

            
thomasmon = [0]*5
thomasmon[1] = 50
thomasmon[2] = 40
thomasmon[3] = 10
thomasmon[0] = "Thomasmon"
thomasmon[4] = 50 #Vida full

pkm2 = [0]*10
pkm2[1] = 100
pkm2[2] = 20
pkm2[3] = 10
pkm2[0] = "Lalamon"
pkm2[4] = 50 #Vida full
pkm2[5] = "Rajada de água"
pkm2[6] = 20 + random.randint(1,20)
pkm2[7] = "Boma de água"
pkm2[8] = 90 + random.randint(5,50)
pkm2[9] = 0.3


typing_speed = 130 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
        
quick_speed = 1400        
def fast_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/quick_speed)

def battle():
    print("Batalha!! \n")
    a=1
    return a

def batalha(p1,p2):
    slow_type(("Batalha!!{} versus {}\n\n").format(p1[0],p2[0]))
    slow_type(("{} - Vida:{}/{} Ataque:{} Defesa:{}\n").format(p1[0],p1[1],p1[4],p1[2],p1[3]))
    slow_type(("{} - Vida:{}/{} Ataque:{} Defesa:{}\n\n").format(p2[0],p2[1],p2[4],p2[2],p2[3]))    
    p2[1] = p2[1] + p2[3]- p1[2]  #Vida do pokemon 2 - atk do 1
    p1[1] = p1[1] + p1[3]- p2[2]  #Vida do pokemon 1 - atk do 2
    slow_type("Resultado da batalha...\n")
    time.sleep(0.6)
    if p1[1] > p2[1]:
        slow_type("Você ganhou!\n")
        slow_type(("Seu Inspermon ainda tem {} de vida\n").format(p1[1]))
        a = 1
    else:
        slow_type("Você perdeu... Marcos Lisboa tem vergonha de você :(\n")
        a = 0
    return a
        
        


fast_type("""\  
              _____                                                 
              \_   \_ __  ___ _ __   ___ _ __ _ __ ___   ___  _ __  
               / /\/ '_ \/ __| '_ \ / _ \ '__| '_ ` _ \ / _ \| '_ \ 
            /\/ /_ | | | \__ \ |_) |  __/ |  | | | | | | (_) | | | |
            \____/ |_| |_|___/ .__/ \___|_|  |_| |_| |_|\___/|_| |_|
                             |_|                                                      
                  """)     
nummon = 0
opt_city = "\n Ir para a floresta(P) \n Ir ao FabLab(F) \n Dormir(D) \n"
slow_type("\n Bem vindo ao Inpermon!")
name = str(input(" Qual o seu nome? "))
if name == "k":
    typing_speed = 2500
        
        
slow_type(("OK! {}, você está na vila de Olimpia. Você pode passear livremente aqui! \n O que deseja fazer?".format(name)))
opt_jgl = "\n Andar(A) \n Voltar para a cidade(V) \n Dormir...aqui(D) \n"

while True:
    ans = str(input(opt_city))
    if ans == "P" or ans == "p":
        if nummon == 0:
            slow_type("Você não tem nenhum Inspermon! Não pode ir explorar ainda!")
        else:
            d = 8 #distance of steps to another city
            slow_type("Agora você está nas traiçoeiras matas selvagens da avenida Santo Amaro\n")
            time.sleep(0.5)
            slow_type(("Tome cuidado,{}").format(name))
            x = 0
            while x==0: #só pra n usar while true denovo
                cmd = str(input(opt_jgl))
                if cmd == "a" or cmd == "A":
                    d = d -1
                    slow_type(("Faltam {} passos para a próxima cidade \n").format(d))
                    if d == 0:
                        slow_type("Você chegou!")
                        sys.exit()
                    else:
                        r = random.random()
                        if r >= 0.4:
                            wpkm = random.randint(1,2) #which pokemon?
                            if wpkm == 1: adversario = thomasmon
                            if wpkm == 2: adversario = pkm2
                            bat = batalha(mon,adversario)
                            
                            if bat == 1:
                                thomasmon[1] = thomasmon[4]
                                exp = exp +10
                                fast_type(("Você ganhou {} de exp! Falta {} para o próximo nível!").format(10,expfill - exp))
                                if exp >= expfill:
                                    exp = 0
                                    expfill = expfill*1.5
                                    nv = nv + 1
                                    
                                    mon[1] = mon[1] + mon[1]*nv/2
                                    mon[2] = mon[2] + mon[2]*nv/3
                                    mon[3] = mon[3] + mon[3]*nv/2
                                    mon[4] = mon[4] + mon[4]*nv/2
                                    slow_type(("Você passou de nível! Agora {} está nível {}!").format(mon[0],nv))
                                    
                                
                            if bat == 0:
                                slow_type("Você perdeu o jogo!")
                                sys.exit()
                                
                if cmd == "V" or cmd == "v":
                    mon[1] = mon[4]
                    x = 1
                if cmd == "D" or cmd == "d":
                    print("Okay. Tchau")
                    sys.exit()
                    
            
            
    if ans == "F" or ans == "f":
        if nummon == 0:
            nomemon = name + "mon"
            slow_type("Parece que o professor tem algo para você! Oh, é um Inspermon!\n")
            slow_type(("Olá,{}! Vim te entregar esse Inspermon para você sair em sua jornada!\n").format(name))
            slow_type(("Você rebebeu um {}!\n").format(nomemon))
            
            mon[0] = nomemon
            time.sleep(1)
            slow_type(("{}, agora você é um mestre Inspermon!").format(name))
            fast_type(("Vá explorar!"))
            nummon = nummon + 1
        else:
            slow_type("Você ja passou por aqui!")
    if ans == "D" or ans == "d":
        print("Okay. Tchau!")
        break
sys.exit()
