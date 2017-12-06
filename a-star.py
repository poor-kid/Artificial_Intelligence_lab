import sys
def check_explored(start,explored):
    for i in explored:
        if i[0] == start[0] and i[1] == start[1]:
            return 1
    return 0
def find_heu(listt,start):
    for i in listt:
        if i[0] == start[0] and i[1] == start[1]:
            #print i[4]
            return i[4]
    return sys.maxint
def move_up(s,pack,g1,g2,listt,explored,goal,count):
    start = []
    for i in range (0,2):
        start.append(s[i])
    start.append(s[0])
    start.append(s[1])
    """if start[0]-1 >=0:
        start[0] = start[0]-1
        if pack[start[0]][start[1]] == '-' or pack[start[0]][start[1]] == '.':
            if (check_explored(start,explored) == 0):
                listt.append(start)
                explored.append(start)"""
    if start[0]-1 >=0:
        start[0] = start[0]-1
        if pack[start[0]][start[1]] == '-' or pack[start[0]][start[1]] == '.':
            if (check_explored(start,explored) == 0):
             h = s[5]+1+abs(start[0]-goal[0])+abs(start[1]-goal[1])
             #print find_heu(listt,start)
             if(find_heu(listt,start) > h):
                 start.append(h)
                 start.append(s[5]+1)
                 listt.append(start)
                 
    return
def move_down(s,pack,g1,g2,listt,explored,goal,count):
    start = []
    for i in range (0,2):
        start.append(s[i])
    start.append(s[0])
    start.append(s[1])
    if start[0]+1 <=g1:
        start[0] = start[0]+1
        if pack[start[0]][start[1]] == '-' or pack[start[0]][start[1]] == '.':
            if (check_explored(start,explored)==0):
                h = s[5]+1+abs(start[0]-goal[0])+abs(start[1]-goal[1])
                print find_heu(listt,start)
                if(find_heu(listt,start) > h):
                    start.append(h)
                    start.append(s[5]+1)
                    listt.append(start)
    return
def move_left(s,pack,g1,g2,listt,explored,goal,count):
    start = []
    for i in range (0,2):
        start.append(s[i])
    start.append(s[0])
    start.append(s[1])
    if start[1]-1 >=0:
        start[1] = start[1]-1
        if pack[start[0]][start[1]] == '-' or pack[start[0]][start[1]] == '.':
            if (check_explored(start,explored)==0):
                h = s[5]+1+abs(start[0]-goal[0])+abs(start[1]-goal[1])
                print find_heu(listt,start)
                if(find_heu(listt,start) > h):
                    start.append(h)
                    start.append(s[5]+1)
                    listt.append(start)
    return
def move_right(s,pack,g1,g2,listt,explored,goal,count):
    start = []
    for i in range (0,2):
        start.append(s[i])
    start.append(s[0])
    start.append(s[1])
    if start[1]+1 <=g2:
        start[1] = start[1]+1
        if pack[start[0]][start[1]] == '-' or pack[start[0]][start[1]] == '.':
            if (check_explored(start,explored)==0):
                h = s[5]+1+abs(start[0]-goal[0])+abs(start[1]-goal[1])
                print find_heu(listt,start)
                if(find_heu(listt,start) > h):
                    start.append(h)
                    start.append(s[5]+1)
                    listt.append(start)
    return
def printing(start,explored,goal):
    ll =[]
    lll = []
    lll.append(start[0])
    lll.append(start[1])
    ll.append(goal)
    x = start[2]
    y = start[3]
    """ll =[]
    lll = []
    lll.append(x)
    lll.append(y)
    ll.append(lll)"""
    count =0 
    while x!= -1 and y!= -1:
        for i in range(len(explored)-1):
            if explored[i][0] == x and explored[i][1] == y:
                lll = []
                lll.append(x)
                lll.append(y)
                ll.append(lll)
                count = count+1
                x = explored[i][2]
                y = explored[i][3]
                break
   
    ll.reverse()
    print count
    #print ll
    for i in range(0,len(ll)-1):
    #for i in ll:
        print ll[i][0]," ",ll[i][1]
    #print goal[0]," ",goal[1]

def a_star(pack,goal,g1,g2,listt,explored,count):
    while listt:
        start = listt.pop()
        count = count+1
        print start
        explored.append(start)
        if(start[0] == goal[0] and start[1] == goal[1]):
            print "sucess"
            print count
            printing(start,explored,goal)
            return
        else:
            move_down(start,pack,g1,g2,listt,explored,goal,count)
            move_right(start,pack,g1,g2,listt,explored,goal,count)
            move_left(start,pack,g1,g2,listt,explored,goal,count)
            move_up(start,pack,g1,g2,listt,explored,goal,count)

def main():
    p1,p2 = (raw_input().split(" "))
    p1 = int (p1)
    p2 = (int)(p2)
    f1,f2 = raw_input().split(" ")
    g1,g2 = raw_input().split(" ")
    g1 = (int)(g1)
    g2  =(int)(g2)
    f1 = (int)(f1)
    f2  = (int)(f2)
    pack = []
    listt = []
    for i in xrange (0,g1):
        pack.append((raw_input().strip()))
    l = []
    l.append(p1)
    l.append(p2)
    l.append(-1)
    l.append(-1)
    l.append(0)
    l.append(0)
    listt.append(l)
    goal = [f1,f2]
    explored = []
    explored.append(l)
    count =0
    a_star(pack,goal,g1,g2,listt,explored,count)
    
main()
