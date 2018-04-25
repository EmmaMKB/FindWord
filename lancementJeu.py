from lettre import *
import pygame,sys
from pygame.locals import *
pygame.init()
from couleurs import Couleurs
from random import choice
from variablejoueurs import lettresjoueurs1,lettresjoueurs2
from boutonscommandes import *
from time import *
#from tkinter import *
def deroulementjeu():


    global fenetre
    BLEU = (0,0,0)
    JAUNE = (255,255,255)
    ROUGE = (255,0,0)
    #pygame.mixer.music.load("breathe.mp3")
    #pygame.mixer.music.queue("ThisLife.mp3")
    dictionnaire = open("dico.txt","r")
    dictionnaire=dictionnaire.read()
    dictionnaire = dictionnaire.split("\n")
    fenetre = pygame.display.set_mode((1366,768),RESIZABLE)
    '''fenetre.fill(choice(Couleurs))
    debut = True
    toura3 = pygame.image.load("3tours.png")
    toura5 = pygame.image.load("5tours.png")
    toura7 = pygame.image.load("7tours.png")
    fenetre.blit(toura3,(554,100))
    fenetre.blit(toura5, (554, 250))
    fenetre.blit(toura7, (554, 400))
    while debut:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                (x,y)=event.pos
                if x>=554 and x<=554+260:
                    if y>=100 and y<= 172:
                        coupmax = 3
                        debut = False
                        break
                    else:
                        if y>=250 and y<=322:
                            coupmax = 5
                            debut = False
                            break
                        else:
                            if y>=400 and y<=472:
                                coupmax = 7
                                debut = False
                                break'''
    coupmax = 3
    fenetre.fill(choice(Couleurs))
    victoire = pygame.image.load("fireworks.png")
    nouveau = pygame.image.load("nouvellepartie.png")
    aide = pygame.image.load("scores.png")
    pygame.display.set_caption('FindWord')
    Fond = pygame.image.load("fond.png")
    bloque = pygame.image.load("bloque.png")
    espace = pygame.image.load("espaceecrit.png")
    boutonvalider = pygame.image.load("valider.png")
    boutonrelancer = pygame.image.load("relance.png")
    ecrit1 = pygame.image.load("capture1.png")
    ecrit2 = pygame.image.load("capture2.png")
    logo = pygame.image.load("launch.png")
    coup1_img = pygame.image.load("coupjoueur1.png")
    coup2_img = pygame.image.load("coupjoueur2.png")
    fenetre.fill(choice(Couleurs))
    fenetre.blit(nouveau, (420,600))
    fenetre.blit(boutonvalider, (550, 500))
    fenetre.blit(boutonrelancer, (350, 500))
    fenetre.blit(Fond,(0,0))
    fenetre.blit(lancejoueur1,(870,30))
    fenetre.blit(lancejoueur2,(870,70))
    fenetre.blit(espace,(250,196))
    fenetre.blit(logo,(10,600))
    fenetre.blit(aide,(1100,10))
    coup1,coup2=0,0
    x,y = 0,20
    tour1 = True
    tour2 = True
    posx,posy = 210,200
    posx2,posy2 = 210,200
    boolltre1,boolltre2,boolltre3,boolltre4,boolltre5,boolltre6,boolltre7,boolltre8=1,1,1,1,1,1,1,1
    boolltre12,boolltre22,boolltre32,boolltre42,boolltre52,boolltre62,boolltre72,boolltre82=1,1,1,1,1,1,1,1
    motjoueur1 = ""
    pointtour1 = 0
    motjoueur2 = ""
    pointtour2 = 0
    joueur2jeu = 0
    finpartie = False
    police = pygame.font.Font('imagine_font.ttf',26)
    police2 = pygame.font.Font('Roboto-Condensed.ttf',14)
    #pygame.mixer.music.play()
    while True:
        a = True
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                (x,y) = event.pos
                a = x
                b = y
                if a>=420 and a<=540:
                    if b>=600 and b<=637:
                        deroulementjeu()
                if a<=970 and a>=870:
                    if b>=30 and b<=60:
                        if tour1:
                            tour1 = False
                            fenetre.blit(lancejoueur2,(870,70))
                            fenetre.blit(tourjoueur1,(870,30))
                            if joueur2jeu > 0:
                                fenetre.blit(texteaafficher,(500,10))
                                fenetre.blit(Fond,(0,0))
                                fenetre.blit(texteaafficher,(450,10))
                                fenetre.blit(lancejoueur1,(870,30))
                                fenetre.blit(lancejoueur2,(870,70))
                                fenetre.blit(espace,(250,196))
                            tourdujoueur1()
                            fenetre.blit(espace,(250,196))
                            posx2 = 210
                            posy2 = 200
                            motjoueur2 = ""
                            break
                    if a<=970 and a>=870:
                        if b>=70 and b<=100:
                            if not tour1:
                                fenetre.blit(tourjoueur2,(870,70))
                                tourdujoueur2()
                (x,y) = event.pos
                c = x
                d = y
                c2 = x
                d2 = y
                ####$$$$$$$$$$$$$$$$$$$$$$$4 CONDITIONS POUR LES LETTRES DU JOUEUR1
                if tour1 == False and finpartie==False:
                    
                    if (c>=0 and c<=40) and (d>=80 and d<=120):
                        if boolltre1 == 1:
                            posx += 40
                            lettre1.afficher(fenetre,posx,posy)
                            fenetre.blit(bloque,(0,80))
                            boolltre1 = 0
                            motjoueur1 += lettre1.lettreeq()
                            pointtour1 += lettre1.retournervaleur()
                    if (c>=0 and c<=40) and (d>=120 and d<=160):
                        if boolltre2 == 1:
                            posx += 40
                            lettre2.afficher(fenetre,posx,posy)
                            fenetre.blit(bloque,(0,120))
                            boolltre2 = 0
                            motjoueur1 += lettre2.lettreeq()
                            pointtour1 += lettre2.retournervaleur()
                    if (c>=0 and c<=40) and (d>=160 and d<=200):
                        if boolltre3 == 1:
                            posx += 40
                            lettre3.afficher(fenetre,posx,posy)
                            fenetre.blit(bloque,(0,160))
                            boolltre3 = 0
                            motjoueur1 += lettre3.lettreeq()
                            pointtour1 += lettre3.retournervaleur()
                    if (c>=0 and c<=40) and (d>=200 and d<=240):
                        if boolltre4 == 1:
                            posx += 40
                            lettre4.afficher(fenetre,posx,posy)
                            fenetre.blit(bloque,(0,200))
                            boolltre4 = 0
                            motjoueur1 += lettre4.lettreeq()
                            pointtour1 += lettre4.retournervaleur()
                    if (c>=0 and c<=40) and (d>=240 and d<=280):
                        if boolltre5 == 1:
                            posx += 40
                            lettre5.afficher(fenetre,posx,posy)
                            fenetre.blit(bloque,(0,240))
                            boolltre5 = 0
                            motjoueur1 += lettre5.lettreeq()
                            pointtour1 += lettre5.retournervaleur()
                    if (c>=0 and c<=40) and (d>=280 and d<=320):
                        if boolltre6 == 1:
                            posx += 40
                            lettre6.afficher(fenetre,posx,posy)
                            fenetre.blit(bloque,(0,280))
                            boolltre6 = 0
                            motjoueur1 += lettre6.lettreeq()
                            pointtour1 += lettre6.retournervaleur()
                    if (c>=0 and c<=40) and (d>=320 and d<=360):
                        if boolltre7 == 1:
                            posx += 40
                            lettre7.afficher(fenetre,posx,posy)
                            fenetre.blit(bloque,(0,320))
                            boolltre7 = 0
                            motjoueur1 += lettre7.lettreeq()
                            pointtour1 += lettre7.retournervaleur()
                    if (c>=0 and c<=40) and (d>=360 and d<=400):
                        if boolltre8 == 1:
                            posx += 40
                            lettre8.afficher(fenetre,posx,posy)
                            fenetre.blit(bloque,(0,360))
                            boolltre8 = 0
                            motjoueur1 += lettre8.lettreeq()
                            pointtour1 += lettre8.retournervaleur()
                    #conditions de relance de jeu
                    if (c>=350 and c<=350+160) and (d>=500 and d<=540):
                        fenetre.blit(espace, (250, 196))
                        motjoueur1=""
                        boolltre1, boolltre2, boolltre3, boolltre4, boolltre5, boolltre6, boolltre7, boolltre8 = 1, 1, 1, 1, 1, 1, 1, 1
                        posx,posy=210,200
                        tourdujoueur1()
                    if (c>=550 and c<=550+160) and (d>=500 and d<=540):
                        fenetre.blit(lancejoueur1, (870, 30))
                        fenetre.blit(tourjoueur2, (870, 70))
                        fenetre.blit(espace, (250, 196))
                        fenetre.blit(ecrit1, (0, 0))
                        if motjoueur1 in dictionnaire:
                            texteaafficher = police.render('{} {} points'.format(motjoueur1, pointtour1), True, BLEU)
                        else:
                            pointtour1 = 0
                            texteaafficher = police.render('Mot invalide {} point'.format(pointtour1), True, BLEU)
                        fenetre.blit(texteaafficher, (10, 10))
                        fenetre.blit(tourjoueur2, (870, 70))
                        motjoueur1 = ""
                        tour1 = True
                        tour2 = False
                        boolltre1, boolltre2, boolltre3, boolltre4, boolltre5, boolltre6, boolltre7, boolltre8 = 1, 1, 1, 1, 1, 1, 1, 1
                        coup1 += 1
                        texteaafficher = police2.render("COUPS : {} / {}".format(coup1,coupmax),True,ROUGE)
                        fenetre.blit(coup1_img,(0,439))
                        fenetre.blit(texteaafficher,(10,445))
                        posx,posy=210,200
            ######CONDITIONS POUR LE JOUEUR 2
                elif tour1 == True and finpartie==False:
                    
                    if (c2>=750 and c2<=790) and (d2>=80 and d2<=120):
                        if boolltre12 == 1:
                            posx2 += 40
                            lettre1_2.afficher(fenetre,posx2,posy2)
                            fenetre.blit(bloque,(750,80))
                            boolltre12 = 0
                            motjoueur2 += lettre1_2.lettreeq()
                            pointtour2 += lettre1_2.retournervaleur()
                    if (c2>=750 and c2<=790) and (d2>=120 and d2<=160):
                        if boolltre22 == 1:
                            posx2 += 40
                            lettre2_2.afficher(fenetre,posx2,posy2)
                            fenetre.blit(bloque,(750,120))
                            boolltre22 = 0
                            motjoueur2 += lettre2_2.lettreeq()
                            pointtour2 += lettre2_2.retournervaleur()
                    if (c2>=750 and c2<=790) and (d2>=160 and d2<=200):
                        if boolltre32 == 1:
                            posx2 += 40
                            lettre3_2.afficher(fenetre,posx2,posy2)
                            fenetre.blit(bloque,(750,160))
                            boolltre32 = 0
                            motjoueur2 += lettre3_2.lettreeq()
                            pointtour2 += lettre3_2.retournervaleur()
                    if (c2>=750 and c2<=790) and (d2>=200 and d2<=240):
                        if boolltre42 == 1:
                            posx2 += 40
                            lettre4_2.afficher(fenetre,posx2,posy2)
                            fenetre.blit(bloque,(750,200))
                            boolltre42 = 0
                            motjoueur2 += lettre4_2.lettreeq()
                            pointtour2 += lettre4_2.retournervaleur()
                    if (c2>=750 and c2<=790) and (d2>=240 and d2<=280):
                        if boolltre52 == 1:
                            posx2 += 40
                            lettre5_2.afficher(fenetre,posx2,posy2)
                            fenetre.blit(bloque,(750,240))
                            boolltre52 = 0
                            motjoueur2 += lettre5_2.lettreeq()
                            pointtour2 += lettre5_2.retournervaleur()
                    if (c2>=750 and c2<=790) and (d2>=280 and d2<=320):
                        if boolltre62 == 1:
                            posx2 += 40
                            lettre6_2.afficher(fenetre,posx2,posy2)
                            fenetre.blit(bloque,(750,280))
                            boolltre62 = 0
                            motjoueur2 += lettre6_2.lettreeq()
                            pointtour2 += lettre6_2.retournervaleur()
                    if (c2>=750 and c2<=790) and (d2>=320 and d2<=360):
                        if boolltre72 == 1:
                            posx2 += 40
                            lettre7_2.afficher(fenetre,posx2,posy2)
                            fenetre.blit(bloque,(750,320))
                            boolltre72 = 0
                            motjoueur2 += lettre7_2.lettreeq()
                            pointtour2 += lettre7_2.retournervaleur()
                    if (c2>=750 and c2<=790) and (d2>=360 and d2<=400):
                        if boolltre82 == 1:
                            posx2 += 40
                            lettre8_2.afficher(fenetre,posx2,posy2)
                            fenetre.blit(bloque,(750,360))
                            boolltre82 = 0
                            motjoueur2 += lettre8_2.lettreeq()
                            pointtour2 += lettre8_2.retournervaleur()
                    if (c2>=350 and c2<=350+160) and (d2>=500 and d2<=540) and tour2==False:
                        fenetre.blit(espace,(250,196))
                        motjoueur2 = ""
                        boolltre12, boolltre22, boolltre32, boolltre42, boolltre52, boolltre62, boolltre72, boolltre82 = 1, 1, 1, 1, 1, 1, 1, 1
                        posx2, posy2 = 210, 200
                        tourdujoueur2()
                    if (c2>=550 and c2<=550+160) and (d2>=500 and d2<=540):
                        fenetre.blit(tourjoueur1, (870, 30))
                        fenetre.blit(lancejoueur2, (870, 70))
                        fenetre.blit(espace, (250, 196))
                        fenetre.blit(ecrit2, (420, 0))
                        if motjoueur2 in dictionnaire:
                            texteaafficher = police.render('{} {} points'.format(motjoueur2, pointtour2), True, BLEU)
                        else:
                            pointtour2 = 0
                            texteaafficher = police.render('mot invalide {} point'.format(pointtour2), True, BLEU)
                        fenetre.blit(texteaafficher, (420, 10))
                        motjoueur2 = ""
                        tour1 = False
                        tour2 = True
                        boolltre12, boolltre22, boolltre32, boolltre42, boolltre52, boolltre62, boolltre72, boolltre82 = 1, 1, 1, 1, 1, 1, 1, 1
                        coup2 += 1
                        texteaafficher = police2.render("COUPS : {} / {}".format(coup2, coupmax), True, ROUGE)
                        fenetre.blit(coup2_img, (383, 439))
                        fenetre.blit(texteaafficher, (700, 445))
                        print(texteaafficher)
                        posx2, posy2 = 210, 200
                    if coup2 == coupmax:
                        sleep(0.5)
                        finpartie = True
                        if pointtour1 > pointtour2:
                            texteaafficher = police.render("Joueur 1 Vainqueur avec {} points".format(pointtour1),True,BLEU)
                            fenetre.blit(texteaafficher,(120,280))
                            fenetre.blit(victoire,(360,320))
                        elif pointtour2 > pointtour1:
                            texteaafficher = police.render("Joueur 2 Vainqueur avec {} points".format(pointtour2),True,BLEU)
                            fenetre.blit(texteaafficher, (120, 280))
                            fenetre.blit(victoire, (360, 320))
                        else:
                            texteaafficher = police.render("Egalite de {} points".format(pointtour2),True,ROUGE)
                            fenetre.blit(texteaafficher, (250, 300))

        pygame.display.update()
def tourdujoueur1():
    listelettre = open("lettres.txt","r")
    listelettre = listelettre.read()
    listelettre = listelettre.split("\n")
    ###creation de 8 lettres pour le joueur1
    a = []
    for i in range(8):
        a += [choice(listelettre)]
    global lettre1 
    lettre1 = lettre(a[0])
    global lettre2 
    lettre2 = lettre(a[1])
    global lettre3
    lettre3 = lettre(a[2])
    global lettre4 
    lettre4 = lettre(a[3])
    global lettre5 
    lettre5 = lettre(a[4])
    global lettre6 
    lettre6 = lettre(a[5])
    global lettre7
    lettre7 = lettre(a[6])
    global lettre8 
    lettre8 = lettre(a[7])
    tout = [lettre1,lettre2,lettre3,lettre4,
            lettre5,lettre6,lettre7,lettre8]
    x,y=0,80
    for variable in tout:
        global fenetre
        sleep(0.02)
        variable.afficher(fenetre,x,y)
        x+=0
        y+=40

def tourdujoueur2():
    listelettre = open("lettres.txt","r")
    listelettre = listelettre.read()
    listelettre = listelettre.split("\n")
    ###creation de 8 lettres pour le joueur1
    a = []
    for i in range(8):
        a += [choice(listelettre)]
    global lettre1_2 
    lettre1_2 = lettre(a[0])
    global lettre2_2 
    lettre2_2 = lettre(a[1])
    global lettre3_2
    lettre3_2 = lettre(a[2])
    global lettre4_2
    lettre4_2 = lettre(a[3])
    global lettre5_2
    lettre5_2 = lettre(a[4])
    global lettre6_2
    lettre6_2 = lettre(a[5])
    global lettre7_2
    lettre7_2 = lettre(a[6])
    global lettre8_2
    lettre8_2 = lettre(a[7])
    tout = [lettre1_2,lettre2_2,lettre3_2,lettre4_2,
            lettre5_2,lettre6_2,lettre7_2,lettre8_2]
    x,y=750,80
    for variable in tout:
        global fenetre
        sleep(0.02)
        variable.afficher(fenetre,x,y)
        x+=0
        y+=40
deroulementjeu()
