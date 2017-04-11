# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:42:05 2017

@author: arthu
"""

# EP2_Arthur_e_Thomas

import sys,time,random
nv = 1

expfill = 30
exp = 0
    
class pokemon(object):
    def __init__(self,nome,vida,vidat,atk1,atk2,defesa,nome_atk1,nome_atk2):
        self.nome = nome
        self.vida = vida
        self.vidat = vidat
        self.atk1 = atk1
        self.atk2 = atk2
        self.defesa = defesa
        self.nome_atk1 = nome_atk1
        self.nome_atk2 = nome_atk2

mon = []
       
mon.append(pokemon("Thomasmon",100,100,30,55,20,"Bola de fogo","Lança-fogo"))
mon.append(pokemon("Dilmon",130,130,40,60,10,"Golpe fatal","Cortar"))
mon.append(pokemon("Arielmon",80,80,30,20,10,"Cortar","fogo"))
mon.append(pokemon("Omakamon",130,130,30,40,18,"Chute","Lança de fogo"))
mon.append(pokemon("Lalamon",100,100,20,50,12,"Golpe furioso","Ataque do ganso"))


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



def batalha1(p1,p2):
    slow_type(("Batalha!!{} versus {}\n\n").format(p1.nome,p2.nome))
    slow_type(("{} - Vida:{}/{} Defesa:{}\n").format(p1.nome,p1.vida,p1.vidat,p1.atk1,p1.defesa))
    slow_type(("{} - Vida:{}/{} Defesa:{}\n\n").format(p2.nome,p2.vida,p2.vidat,p2.atk1,p2.defesa))    
    x = 0
    opc_bat = (" {}(A)\n {}(B)\n Fugir(F)\n ").format(p1.nome_atk1,p1.nome_atk2)
    while x == 0:
        batresp = str(input(opc_bat))
        if batresp == "a" or batresp == "A":
            atkdoplayer = p1.atk1
            slow_type(("Você usou {}").format(p1.nome_atk1))
        if batresp == "b" or batresp == "B":
            atkdoplayer = p1.atk2
            slow_type(("Você usou {}").format(p1.nome_atk2))
        if batresp == "f" or batresp == "F":
            fugir = random.randint(1,10)
            if fugir >=6:
                slow_type("Você conseguiu fugir!\n")
                a = 1
                x = 1
                return a
            else:
                slow_type("Você não conseguiu fugir!\n")
                atkdoplayer = 0
                time.sleep(0.3)
        
        atk = atkdoplayer - p2.defesa
        if atk < 0:
            atk = 0
            fast_type("Seu ataque não foi muito efetivo\n")
        p2.vida = p2.vida - atk #Vida do pokemon 2 - atk do 1
        fast_type(("Você deu {} de dano. {} ainda tem {} de vida!\n").format(atk,p2.nome,p2.vida))
        
        time.sleep(0.3)
        enemy_atk_choice = random.randint(1,2)  
        if enemy_atk_choice == 1:
            ATQ = p2.atk1
            NOME = p2.nome_atk1
        else:
            ATQ = p2.atk2
            NOME = p2.nome_atk2
        atk = ATQ- p1.defesa
        
        print(("{} usou {}!".format(p2.nome,NOME)))
        if atk < 0:
            atk = 0
            fast_type(("Não foi efetivo!\n"))
        p1.vida = p1.vida - atk  #Vida do pokemon 1 - atk do 2
        fast_type(("{} deu {} de dano! Você ainda tem {} de vida!\n").format(p2.nome,atk,p1.vida))
        if p1.vida <= 0:
            slow_type("Resultado da batalha...\n")
            slow_type("Você perdeu... Marcos Lisboa tem vergonha de você :(\n")
            a = 0
            x=1
       
        if p2.vida <= 0:
            slow_type("Você ganhou!\n")
            slow_type(("Seu Inspermon ainda tem {} de vida\n").format(p1.vida))
            a = 1
            x=1
            p2.vida = p2.vidat
        
    return a

def levelup(obj):
    obj.atk1 = obj.atk1*1.2
    obj.atk2 = obj.atk2*1.2
    obj.defesa = obj.defesa*1.2
    obj.vida = obj.vida*1.2
    obj.vidat = obj.vidat*1.2


print("""\  
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


if name == "k": #Pra testes, usar o nome "k" faz o jogo ficar mais rapido e sme necessidade de passar pelo fablab
    def slow_type(a):
        print(a)
    nummon = 1 #numero de pokemons
    nomemon = name + "mon"
    startmon = pokemon(nomemon,100,100,60,70,25,"Lança de fogo","Chute")
        
        
slow_type(("OK! {}, você está na vila de Olimpia. Você pode passear livremente aqui! \n O que deseja fazer?".format(name)))
opt_jgl = "\n Andar(A) \n Voltar para a cidade(V) \n Dormir...aqui(D) \n"

while True:
    ans = str(input(opt_city))
    if ans == "F" or ans == "f":
        if nummon == 0: #Se vc tem zero pokemons, vc fala cm o professor
            nomemon = name + "mon"
            slow_type("Parece que o professor tem algo para você! Oh, é um Inspermon!\n")
            slow_type(("Olá,{}! Vim te entregar esse Inspermon para você sair em sua jornada!\n").format(name))
            slow_type(("Você rebebeu um {}!\n").format(nomemon))
            
            startmon = pokemon(nomemon,100,100,60,70,25,"Lança de fogo","Chute")
            time.sleep(1)
            slow_type(("{}, agora você é um mestre Inspermon!").format(name))
            fast_type(("Vá explorar!"))
            nummon = nummon + 1
        else:
            slow_type("Parece que você já passou por aqui")
    if ans == "P" or ans == "p":
        if nummon == 0:
            slow_type("Você não tem nenhum Inspermon! Não pode ir explorar ainda!")
        if nummon == 1:
            d = 200 #distance of steps to another city
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
                            adver = random.choice(mon)
                            bat = batalha1(startmon,adver)
                            
                            if bat == 1:
                                
                                exp = exp +10
                                fast_type(("Você ganhou {} de exp! Falta {} para o próximo nível!\n").format(10,expfill - exp))
                                if exp >= expfill:
                                    exp = 0
                                    expfill = expfill*1.5
                                    levelup(startmon)
                                    slow_type(("Você passou de nível! Agora {} está nível {}!").format(startmon.nome,nv))
                                    
                            if bat == 0:
                                slow_type("\n Você perdeu o jogo!")  
                                sys.exit() #Fecha o sistema
                                
                if cmd == "V" or cmd == "v":
                    startmon.vida = startmon.vidat #Recupera a vida do pokemon
                    x = 1
                if cmd == "D" or cmd == "d":
                    print("Okay. Tchau")
                    sys.exit() #Fecha o sistema
    if ans == "D" or ans == "d":
        print("Okay. Tchau!")
        break
sys.exit()
