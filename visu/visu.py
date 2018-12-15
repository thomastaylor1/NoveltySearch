#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:42:37 2018

@author: 3414621
"""
from numpy import *

def layoutSVG(filenameMaze, svgString):
    cpt = 0
    linesMaze = [line.rstrip('\n').split() for line in open(filenameMaze)]
    for line in linesMaze:
        if (cpt == 1):
            svgString += "<circle cx=\""+ line[0] +"\" cy=\""+ line[1]+"\" r=\"5\" stroke=\"black\" fill=\"white\" />"
            #print("coordonnées du robot")
        if (cpt == 3):
            svgString += "<circle cx=\""+ line[0] +"\" cy=\""+ line[1]+"\" r=\"3\" stroke=\"black\" fill=\"white\"/>"
            #print("goal")
        if (cpt > 3):
            svgString += "<line x1=\""+line[0]+"\" y1=\""+line[1]+"\" x2=\""+line[2]+"\" y2=\""+line[3]+"\" \
            style=\"stroke:rgb(0,0,0);stroke-width:2\" />"
        cpt += 1
    return svgString
    
def layoutSVGNoEnd(filenameMaze, svgString):
    cpt = 0
    linesMaze = [line.rstrip('\n').split() for line in open(filenameMaze)]
    for line in linesMaze:
        if (cpt == 1):
            svgString += "<circle cx=\""+ line[0] +"\" cy=\""+ line[1]+"\" r=\"5\" stroke=\"black\" fill=\"white\" />"
            #print("coordonnées du robot")
        if (cpt > 3):
            svgString += "<line x1=\""+line[0]+"\" y1=\""+line[1]+"\" x2=\""+line[2]+"\" y2=\""+line[3]+"\" \
            style=\"stroke:rgb(0,0,0);stroke-width:2\" />"
        cpt += 1
    return svgString

def goalSVG(svgString):
    cpt = 0
    linesMaze = [line.rstrip('\n').split() for line in open(filenameMaze)]
    for line in linesMaze:
        if (cpt == 3):
                svgString += "<circle cx=\""+ line[0] +"\" cy=\""+ line[1]+"\" r=\"3\" stroke=\"black\" fill=\"white\"/>"
                #print("goal")
        cpt += 1
    return svgString
    
def pointsSVG(filenameDat, svgString):
    lines = [line.rstrip('\n').split() for line in open(filenameDat)]
    x = [line[1] for line in lines]
    y = [line[2] for line in lines]
    solved = [line[3] for line in lines]
    for i in range(len(x)):
        color = "black"
        if solved[i] == "1":
            color = "red"
        svgString += "<circle cx=\""+ x[i] +"\" cy=\""+ y[i] +"\" r=\"0.3\" stroke=\""+color+"\" fill=\""+color+"\"/>"
    return svgString

def writeSVG(filenameSVG, svgString):
    fileSVG = open(filenameSVG, 'w')
    fileSVG.write(svgString)
    fileSVG.close()
    
def svgHeader(dimx, dimy):
    svgString = "<html><body><svg width=\""+str(dimx)+"\" height=\""+str(dimy)+"\">"
    svgString += "<rect width=\"100%\" height=\"100%\" fill=\"white\"/>"
    return svgString

def svgCloser(svgString):
    svgString += "</svg></body></html>"
    return svgString
    
if __name__ == "__main__":
    name = "hard_maze"
    drawPoints = True
    filenameMaze = name + ".txt"
    #filenameDat = filenameMaze + "record.dat"
    filenameDat = "record.dat"
    filenameSVG = name + ".svg"
    if name == "medium_maze": 
        svgString = svgHeader(300, 150)
    if name == "hard_maze": 
        svgString = svgHeader(210, 210) #dimensions
    svgString = goalSVG(svgString)
    if(drawPoints) :
        svgString = pointsSVG(filenameDat, svgString) #points
    svgString = layoutSVGNoEnd(filenameMaze, svgString) #labyrinthe après les points pour bien voir le pt de départ
    svgString = svgCloser(svgString) #fin du balisage
    writeSVG(filenameSVG, svgString) #écriture du fichier
    
    
        
    
