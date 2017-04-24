# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:42:05 2017

@author: arthu
"""

# EP2_Arthur_e_Thomas
import json
import sys,time,random
nv = 1
expfill = 20
exp = 0
nvevo1 = 5
nvevo2 = 10


class pokemon(object):
    def __init__(self,nome,vida,vidat,atk1,atk2,defesa,nome_atk1,nome_atk2,nv):
        self.nome = nome
        self.vida = vida
        self.vidat = vidat
        self.atk1 = atk1
        self.atk2 = atk2
        self.defesa = defesa
        self.nome_atk1 = nome_atk1
        self.nome_atk2 = nome_atk2
        self.nv = nv



mon = [] #Lista de pokemons totais

mon.append(pokemon("Thomasmon",100,100,30,55,20,"Bola de fogo","Lança-fogo",1))
mon.append(pokemon("Dilmon",130,130,40,60,10,"Golpe fatal","Cortar",1))
mon.append(pokemon("Arielmon",80,80,30,20,10,"Cortar","fogo",1))
mon.append(pokemon("Omakamon",130,130,30,40,18,"Chute","Lança de fogo",1))
mon.append(pokemon("Lalamon",100,100,20,50,12,"Golpe furioso","Ataque do ganso",1))


typing_speed = 230
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

insperdex_list = []

def batalha1(p1,p2):
    if p2 not in insperdex_list:
        insperdex_list.append(p2)
    slow_type(("Batalha!!{} versus {}\n\n").format(p1.nome,p2.nome))
    time.sleep(0.2)
    slow_type(("{} - Vida:{}/{} Defesa:{} Level:{} \n").format(p1.nome,p1.vida,p1.vidat,p1.defesa,p1.nv))
    slow_type(("{} - Vida:{}/{} Defesa:{} Level:{} \n\n").format(p2.nome,p2.vida,p2.vidat,p2.defesa,p2.nv))
    x = 0
    time.sleep(0.5)
    opc_bat = (" {}(A)\n {}(B)\n Fugir(F)\n ").format(p1.nome_atk1,p1.nome_atk2)
    while x == 0:
        batresp = input(opc_bat)
        if batresp == "a" or batresp == "A":
            atkdoplayer = p1.atk1 + random.randint(1,10)*p1.nv #Elemento supresa
            slow_type(("Você usou {} ").format(p1.nome_atk1))
        if batresp == "b" or batresp == "B":
            atkdoplayer = p1.atk2 + random.randint(1,10)*p1.nv
            slow_type(("Você usou {} ").format(p1.nome_atk2))
        if batresp == "f" or batresp == "F":
            fugir = random.randint(1,10)
            if fugir >=6:
                time.sleep(0.1)
                slow_type("Você conseguiu fugir!\n")
                a = 1
                x = 1
                return a
            else:
                time.sleep(0.1)
                slow_type("Você não conseguiu fugir!\n")
                atkdoplayer = 0
                time.sleep(0.3)

        atk = atkdoplayer - p2.defesa
        if atk < 0:
            atk = 0
            slow_type("Seu ataque não foi muito efetivo\n")
        p2.vida = p2.vida - atk #Vida do pokemon 2 - atk do 1
        fast_type(("Você deu {} de dano. {} ainda tem {} de vida!\n").format(atk,p2.nome,p2.vida))

        time.sleep(0.3)
        enemy_atk_choice = random.randint(1,2)
        if enemy_atk_choice == 1:
            ATQ = p2.atk1 + p2.nv*random.randint(1,10)
            NOME = p2.nome_atk1
        else:
            ATQ = p2.atk2 + p2.nv*random.randint(1,10)
            NOME = p2.nome_atk2
        atk = ATQ- p1.defesa


        if p2.vida > 0:
            slow_type(("{} usou {}!".format(p2.nome,NOME)))
            if atk < 0:
                atk = 0
                slow_type(("Não foi efetivo!\n"))
            p1.vida = p1.vida - atk  #Vida do pokemon 1 - atk do 2
            slow_type(("{} deu {} de dano! Você ainda tem {} de vida!\n").format(p2.nome,atk,p1.vida))
        if p1.vida <= 0:
            slow_type("Resultado da batalha...\n")
            time.sleep(0.4)
            slow_type("Você perdeu... Marcos Lisboa tem vergonha de você :(\n")
            a = 0
            x=1

        if p2.vida <= 0:
            slow_type("Resultado da batalha...\n")
            time.sleep(0.4)
            slow_type("Você ganhou!\n")
            slow_type(("Seu Inspermon ainda tem {} de vida\n").format(p1.vida))
            a = 1
            x=1
            p2.vida = p2.vidat
            time.sleep(0.4)

    return a

def levelup(obj):
    obj.atk1 = obj.atk1 + obj.atk1//5
    obj.atk2 =obj.atk2 + obj.atk2//5
    obj.defesa =obj.defesa + obj.defesa//5
    obj.vida =obj.vida + obj.vida//5
    obj.vidat =obj.vidat + obj.vidat//5
    obj.nv = obj.nv + 1

startmon = pokemon(" ",1000,0,0,0,0," "," ",1)

fast_type("""
 ______
/\__  _\ .
\/_/\ \/     ___     ____  _____      __   _ __    ___ ___     ___     ___
   \ \ \   /' _ `\  /',__\/\ '__`\  /'__`\/\`'__\/' __` __`\  / __`\ /' _ `\ .
    \_\ \__/\ \/\ \/\__, `\ \ \L\ \/\  __/\ \ \/ /\ \/\ \/\ \/\ \L\ \/\ \/\ \ .
    /\_____\ \_\ \_\/\____/\ \ ,__/\ \____\  \_\ \ \_\ \_\ \_\ \____/\ \_\ \_\ .
    \/_____/\/_/\/_/\/___/  \ \ \/  \/____/ \/_/  \/_/\/_/\/_/\/___/  \/_/\/_/
                             \ \_\ .
                              \/_/
                  """)

primeirapergunta =input("Novo jogo(N) ou Carregar jogo(C)?")
if primeirapergunta == "C" or primeirapergunta == "c":
    with open("save.json") as archivein:
        listsave = json.load(archivein)
        startmon.nome = listsave[0]
        startmon.vida = listsave[1]
        startmon.vidat=listsave[2]
        startmon.atk1=listsave[3]
        startmon.atk2=listsave[4]
        startmon.defesa=listsave[5]
        startmon.nome_atk1=listsave[6]
        startmon.nome_atk2=listsave[7]
        startmon.nv=listsave[8]
        name = listsave[9]
        city_count = listsave[10]
        
        nummon = 1
        slow_type(("\n Bem vindo de volta,{}\n").format(name))
        time.sleep(0.5)

if primeirapergunta == "N" or primeirapergunta == "n":
    city_count = 1
    nummon = 0

    slow_type("\n Bem vindo ao Inpermon! Qual o seu nome?")
    name = input(" ")
    if name == "god": #Pra testes, usar o nome "god" faz o jogo ficar mais rapido e sme necessidade de passar pelo fablab
        def slow_type(a):
            print(a)
        nummon = 1 #numero de pokemons
        nomemon = name + "mon"
        startmon = pokemon(nomemon,400,400,80,100,25,"ATK1","ATK2",9)


slow_type(("OK! {}, você está na cidade {}. Você pode passear livremente aqui! \n O que deseja fazer?".format(name,city_count)))
opt_jgl = "\n Andar(A) \n Voltar para a cidade(V) \n Abrir Insperdex(I) \n Dormir...aqui(D) \n Salvar o jogo \n "
print("\n Dicas: Passe no Fablab antes de ir à floresta para pegar seu Inspermon! Ele evolui pela primeira vez no nível 5 e depois no nível 10")
while True:
    ans = str(input("O que deseja fazer?\n Ir para a floresta(P)\n Ir para o Fablab(F)\n Dormir(D) \n Salvar(S) \n "))
    if ans == "F" or ans == "f":
        if nummon == 0: #Se vc tem zero pokemons, vc fala cm o professor
            nomemon = name + "mon"
            slow_type("Parece que o professor tem algo para você! Oh, é um Inspermon!\n")
            slow_type(("Olá,{}! Vim te entregar esse Inspermon para você sair em sua jornada!\n").format(name))
            slow_type(("Você rebebeu um {}!\n").format(nomemon))
            startmon = pokemon(nomemon,100,100,60,70,25,"Lança de fogo","Chute",1)
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
            d = 8 #distance of steps to another city
            slow_type("Agora você está nas traiçoeiras matas selvagens da avenida Santo Amaro\n")
            time.sleep(0.5)
            slow_type(("Tome cuidado,{}").format(name))
            x = 0
            while x==0: #só pra n usar while true denovo
                cmd = str(input(opt_jgl))
                if cmd == "i" or cmd == "I":
                    slow_type(("Abrindo Insperdex!\n"))
                    time.sleep(0.5)
                    if not insperdex_list:
                        print("Você ainda não enfrentou nenhum Inspermon!")
                    else:
                        for j in range(len(mon)):
                            if j < len(insperdex_list):
                                print(("|{}|\n").format(insperdex_list[j].nome))
                            else:
                                print("|???|\n")

                if cmd == "a" or cmd == "A":
                    d = d -1
                    slow_type(("Faltam {} passos para a cidade {} \n").format(d,city_count+1))
                    if d == 0:
                        city_count = city_count +1
                        slow_type("Você chegou!\n")
                        slow_type(("Agora você está na cidade {}").format(city_count))
                        d = 8
                        startmon.vida = startmon.vidat
                        for i in range(len(mon)):
                            levelup(mon[i])

                    else:
                        r = random.random()
                        if r >= 0.4:
                            adver = random.choice(mon)
                            bat = batalha1(startmon,adver)
                            if bat == 1:

                                exp = exp + 10*adver.nv
                                fast_type(("Você ganhou {} de exp! Falta {} para o próximo nível!\n").format(10*adver.nv,expfill - exp))
                                if exp >= expfill:
                                    exp = 0
                                    expfill = expfill*1.5
                                    levelup(startmon)
                                    slow_type(("Você passou de nível! Agora {} está nível {}!").format(startmon.nome,startmon.nv))
                                    if startmon.nv == 5:
                                        time.sleep(0.2)
                                        slow_type(("Seu {} está evoluindo..").format(startmon.nome))
                                        time.sleep(0.5)
                                        nome_antigo = startmon.nome
                                        startmon.nome ="Super " + nome_antigo
                                        startmon.atk1 =startmon.atk1 + startmon.atk1//5
                                        startmon.atk2 =startmon.atk2 + startmon.atk2//5
                                        slow_type(("Agora você tem um {}!").format(startmon.nome))
                                    if startmon.nv == 10:
                                        time.sleep(0.2)
                                        slow_type(("Seu {} está evoluindo..").format(startmon.nome))
                                        time.sleep(0.5)
                                        nome_antigo = startmon.nome
                                        startmon.nome ="Mega " + nome_antigo
                                        startmon.atk1 =startmon.atk1+ startmon.atk1//5
                                        startmon.atk2 =startmon.atk2 + startmon.atk2//5
                                        slow_type(("Agora você tem um {}!").format(startmon.nome))

                            if bat == 0:
                                slow_type("\n Você perdeu o jogo!")
                                sys.exit() #Fecha o sistema

                if cmd == "V" or cmd == "v":
                    startmon.vida = startmon.vidat #Recupera a vida do pokemon
                    x = 1
                if cmd == "D" or cmd == "d":
                    print("Okay. Tchau")
                    sys.exit() #Fecha o sistema
                if cmd == "S" or cmd == "s":
                    listsave = [startmon.nome,startmon.vida,startmon.vidat,startmon.atk1,startmon.atk2,startmon.defesa,startmon.nome_atk1,startmon.nome_atk2,startmon.nv,name,city_count]
                    with open("save.json","w") as archive:
                            json.dump(listsave,archive)
                            time.sleep(0.5)
                            slow_type("Jogo salvo!")

    if ans == "D" or ans == "d":
        print("Okay. Tchau!")
        break
    if ans == "S" or ans == "s":
         listsave = [startmon.nome,startmon.vida,startmon.vidat,startmon.atk1,startmon.atk2,startmon.defesa,startmon.nome_atk1,startmon.nome_atk2,startmon.nv,name,city_count]
         with open("save.json","w") as archive:
             json.dump(listsave,archive)
             time.sleep(0.5)
             slow_type("Jogo salvo!")
sys.exit()
