
import random
import math


koordinat = [[25, 230], [95, 260], [300, 465], [410, 250], [145, 665], [480, 415], [420, 555], [560, 365], [415, 635], [595, 360], [520, 585], [660, 180], [575, 665], [605, 625], [725, 370], [700, 500], [685, 595], [700, 580], [685, 610], [555, 815], [720, 635], [510, 875], [770, 610], [830, 485], [760, 650], [475, 960], [795, 645], [830, 610], [835, 625], [525, 1000], [845, 680], [975, 580], [875, 920], [650, 1130], [580, 1175], [1170, 65], [1215, 245], [1250, 400], [1220, 580], [1320, 315], [1340, 725], [1150, 1160], [1465, 200], [1530, 5], [1605, 620], [1740, 245]]

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def alldistance(coordinates):
    dis = 0
    for i in range(len(coordinates)-1):
        dis += distance(coordinates[i],coordinates[i+1])
    return dis

def generatePop(koordinat,n):
    pop = []
    for i in range(n):
        pop.append(random.sample(koordinat,len(koordinat)))
    return pop

def crossover(x,y):
    r = random.randint(0,len(x)-2)
    x = x[0:r]
    for i in y:
        if i not in x:
            x.append(i)
    return x

def calcFit(gen):
    return 1/alldistance(gen)


def roulette(pop):
    roulette = []
    new_pop = []
    total_fit = 0
    for i in pop:
        total_fit += calcFit(i)       
    for i in pop:
        for j in range(round(calcFit(i)*100/total_fit)):
            roulette.append(i)    
    loop = 0        
    while len(new_pop)!=len(pop)+5 and loop<1000:
        temp = crossover(random.sample(roulette,1)[0],random.sample(roulette,1)[0])
        if temp not in new_pop:
            new_pop.append(temp)
        loop+=1    
            
    return new_pop,total_fit
            
def mutations(childs):
    rate = [1]*1 + [0]*99
    for i in childs:
        mutate = random.sample(rate,1)[0]
        if mutate==1:
            index = random.randint(0,len(childs)-1)
            childs[index] = random.sample(childs[index],len(childs[0]))
    return childs            

def findBest(pop):
    shortest = alldistance(pop[0])
    shortest_path = []
    for i in pop:
        if alldistance(i)<shortest:
            shortest_path = i
            shortest = alldistance(i)
            
    return shortest_path,shortest


def solve(koordinat):
    pop = generatePop(koordinat,10)
    NC=0
    NCMax = 500
    shortest = alldistance(pop[0])
    shortest_path = []
    while NC<NCMax: 
        try:
            newgen,total_fit = roulette(pop)
            pop = mutations(newgen)
            #print(total_fit)
            temp = findBest(pop)
            if temp[1]<shortest:
                shortest = temp[1]
                shortest_path = temp[0]
            if total_fit<10e-05:
                pop = generatePop(koordinat,10) 
                print("difergen")
        except Exception as e:
            print(e)
            pop = generatePop(koordinat,10)
            pass
        NC+=1
    return shortest_path,shortest     
    
    

x, y = solve(koordinat)
