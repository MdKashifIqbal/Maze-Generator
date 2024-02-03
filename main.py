from colorama import init
from termcolor import colored
from colorama import just_fix_windows_console
just_fix_windows_console()
import random
#generating the initial maze of n*n size
def mazegenerator(n):
    mazematrix=[]
    for row in range(n):
        currRow=[]
        for col in range(n):
            currRow.append("o")
        mazematrix.append(currRow)
    
    #adding 25% random walls
    qn=(n*n)//4
    dic={}
    countwalls=0
    while countwalls<qn:
        rand1=random.randint(0,n-1)
        rand2=random.randint(0,n-1)
        if (rand1,rand2) not in dic:
            dic[(rand1,rand2)]=0
            mazematrix[rand1][rand2]="▓"
            countwalls+=1
    
    #definining start and end
    mazematrix[0][0]="S"
    mazematrix[n-1][n-1]="E"
    return mazematrix


#displaying the maze

def displaymaze(mazematrix):
    n=len(mazematrix)
    for row in range(n):
        for col in range(n):
            if mazematrix[row][col]=="o":
                print(colored("|o|","blue","on_black"),end="")
            elif mazematrix[row][col]=="▓":
                print(colored("|▓|","red","on_black"),end="")
            elif mazematrix[row][col]=="S":
                print(colored("|S|","green","on_black"),end="")
            elif mazematrix[row][col]=="◍":
                print(colored("|◍|","green","on_black"),end="")
            else:
                print(colored("|E|","green","on_black"),end="")
        print()


#displaymaze(mazegenerator(5))

#finding path
def findPath(mazematrix,pos,path,visited,shortest_path):
    row,col=pos
    n=len(mazematrix)

    #if the pos is out of bounds or is a wall
    if row<0 or row>n-1 or col<0 or col>n-1 or mazematrix[row][col]=="▓" or (row,col) in visited:
        return False
    
    if (row,col) in visited:
        path.pop()
        return False
    visited[(row,col)]=1
    path.append([row,col])

    #return path if we reach end
    if row==n-1 and col==n-1:
        if shortest_path==[] or len(path)<len(shortest_path):
            shortest_path[:]=path.copy()

    #if any of the direction found path 
    findPath(mazematrix,[row-1,col],path,visited,shortest_path)
    findPath(mazematrix,[row+1,col],path,visited,shortest_path)
    findPath(mazematrix,[row,col-1],path,visited,shortest_path)
    findPath(mazematrix,[row,col+1],path,visited,shortest_path)
    
    path.pop()
    return False



#displaying the path
def displaypath(mazematrix,shortestPath):
    if not shortestPath:
        print("no path found")
        return
    n=len(mazematrix)
    for i in range(len(shortestPath)):
        if shortestPath[i]==[0,0] or shortestPath[i]==[n-1,n-1]:
            continue
        row,col=shortestPath[i]
        mazematrix[row][col]= "◍"
    displaymaze(mazematrix)



def main():
    n=int(input("What size matrix you want? type a number"))

    maze=mazegenerator(n)
    mazematrix=path=mazegenerator(n)
    print("This is your maze")
    displaymaze(maze)
    while True:
        userChoice=int(input("1.Show Path? 2.Intialize another maze 3.Exit"))
        if userChoice==3:
            print("Exited, You chose to exit")
            break
        elif userChoice==2:
            maze=mazegenerator(n)
            print("Your new maze")
            displaymaze(maze)
        elif userChoice==1:
            shortestPath=[]
            findPath(mazematrix,[0,0],[],{},shortestPath)
            displaypath(mazematrix,shortestPath)
        else:
            print("Wrong input, choose : 1.Show Path? 2.Intialize another maze 3.Exit")
main()



    

    