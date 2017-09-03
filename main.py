"""
april 15th 2017
program will read and plot .csv data from acceleration app I have on my phone
programmer: william (willpiam)
kids we gunna use sub routines this time
"""
#import needed liberys
import pygame#used for ploting graph


#setup variables
fileName = "roboDrop.csv"
length = sum(1 for line in open(fileName))
wholeList = [length]
timeList = []#holds a list of all the times
xList = []
yList = []
zList = []
width = 1000
height = 500
white  = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
grey = (211,211,211)
mult = 10
tmult = 500
add = 10
thick = 3

def main():
    print "main is go"
    pygame.init()
    wholeFile()
    easySplit()
    ploter()
    
            

def wholeFile():#function creates list of all data and gets ride of two unnessary lines
    print "oldFash is go"#debugging 
    doc  = open(fileName,"r")#opens data file
    for i in range (length):
        wholeList.append(str(doc.readline()))#adds lines from file to the list. Each list entry is formated as time,x,y,x
    for i in range (0,length):#was length -1
        wholeList[i] = wholeList[i+1]
    for i in range (0, length):
        wholeList[i] = wholeList[i+1]
    doc.close()#closes data file
        



def easySplit():#easy split has proven to be not so easy... I'm going to keep working on it though 
    print "easySplit is go"
    listLengths()
    for i in range (0, length):
        current = wholeList[i]
        current = current[:-2]#gets rid of a symbol that may be messing tings up
        timeList[i], xList[i], yList[i], zList[i] = current.split(',')
  
    
def listLengths():#this function will grow the lists with .append. because apperently I can't just create a file with a length to start
    for i in range (length):
        timeList.append("")
        xList.append("")
        yList.append("")
        zList.append("")

def ploter():#uses pygame to plot data
    print "plotter is go"
    graph = pygame.display.set_mode((width, height))#creates window
    graph.fill(white)#makes background white
    grid(graph)#function puts grid on graph
    pygame.display.update()#puts stuff on the screen (updates graph)
    for i in range(0, length):#here we create and draw lines from points 
        time = float(timeList[i])#var time is pulled from the time list
        time = time*tmult#time is multiplyed because otherwise it would be to small and wouldn't loog good on the screen
        if (i < length-1):#here we create the second points in the lines
            nextTime = float(timeList[i+1])
            nextTime = nextTime*tmult
            nextx = float(xList[i+1])
            nextx = nextx+add
            nextx = nextx*mult
            nexty = float(yList[i+1])
            nexty = nexty+add+add
            nexty = nexty*mult
            nextz = float(zList[i+1])
            nextz = nextz+add+add+add
            nextz = nextz*mult
        x = float(xList[i])
        x = x+add
        x = x*mult
        y = float(yList[i])
        y = y+add+add
        y = y*mult
        z = float(zList[i])
        z = z+add+add+add
        z = z*mult
        pygame.draw.lines(graph, black, False, [(time,x),(nextTime,nextx)], thick)
        pygame.draw.lines(graph, blue, False, [(time,y),(nextTime,nexty)], thick)
        pygame.draw.lines(graph, green, False, [(time,z),(nextTime,nextz)], thick)
        pygame.display.update()   
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()#ends the program.. still gives me an error but im not worried about it for now as its the last thing to heppen befor the program closes
            

def grid(graph):#draws grid on graph
    interval = timeList[1]
    interval = float(interval)
    for i in range (length):
        interval = timeList[i]
        interval = float(interval)
        interval = interval*tmult
        pygame.draw.lines(graph, grey, False, [(interval,0),(interval,width)], 1)
        
main()
