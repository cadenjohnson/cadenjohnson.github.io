# script used to analyze powerball drawing numbers
# Caden Johnson

import csv
import requests
import matplotlib.pyplot as plt


# display results in a graph
def display_graph(array1, array2):
    figure, axis = plt.subplots(2,1)

    #numbers
    x=[]
    y=[]
    for g in array1:
        x.append(g[0])
        y.append(g[1])
    axis[0].bar(x,y, width=0.4, color='g')
    axis[0].set_title('Distribution of Numbers')

    #pball
    x=[]
    y=[]
    for g in array2:
        x.append(g[0])
        y.append(g[1])
    axis[1].bar(x,y, width=0.4, color='g')
    axis[1].set_title('Distribution of Powerball numbers')

    plt.tight_layout()
    plt.show()


# sort via the quantity of occurances
def sortSecond(val):
        return val[1]


# sort the data
def sort_data(array):
        return sorted(array, key=sortSecond, reverse=True)


# analyze the powerball data
def analyze(timeline):
    numbers = []
    ro, co = 90,2
    ro2, co = 90,2
    for i in range(ro):
        c = []
        for i in range(co):
            c.append(0)
        numbers.append(c)

    balls=[]
    for i in range(ro2):
        c = []
        for i in range(co):
            c.append(0)
        balls.append(c)

    # open file and add numbers to correct arrays
    with open('NCELPowerball.csv') as File:
        plots=csv.reader(File, delimiter=',')
        row_num=0
        limit = 0
        for row in plots:
            if row_num == 0:
                row_num = row_num+1
                continue
            limit = limit + 1
            if limit > int(timeline):
                break
            x=0
            for col in row:
                x=x+1
                if x!=1 and x!=8 and x!=9:
                    num=int(col)
                    if x==7:
                        balls[num][0] = num
                        balls[num][1] = int(balls[num][1])+1
                    else:
                        numbers[num][0] = num
                        numbers[num][1] = int(numbers[num][1])+1

    #init final arrays
    final_array1=[]
    final_array2=[]

    # filter out empty arrays
    for j in numbers:
        if j[0]!=0:
            final_array1.append(j)

    for r in balls:
        if r[0]!=0:
            final_array2.append(r)
            
    sorted_num = sort_data(final_array1)
    sorted_pball = sort_data(final_array2)
    winners = []
    winnerp = []

    print(final_array1)
    
    for n in range(5):
        winners.append(sorted_num[n][0])
    winnerp.append(sorted_pball[0][0])

    return winners, winnerp, final_array1, final_array2
                       


response = requests.get('https://nclottery.com/powerball-download')
open("NCELPowerball.csv", "wb").write(response.content)
timeline = input('How many drawings would you like to analyze? -->')

try:
    timeline = int(timeline)
except:
    print("not valid timeline")
    
if timeline < 1:
    print("not valid timeline")
else:
    numbers, pball, array1, array2 = analyze(timeline)
    print('based on data...')
    print('winning numbers:   ', numbers)
    print('winning powerball: ', pball)
    display_graph(array1, array2)







        
