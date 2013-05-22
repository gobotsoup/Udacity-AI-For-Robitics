colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']
# dont move, move right, move down, move down, move right
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT
p = []
#measurements = ['green']
#motions = [[0,1]]
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        r=[]
        for j in range(len(p[i])):            
            hit = (Z == colors[i][j])
            r.append(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
        q.append(r)
        s=0
    for i in range(len(q)):
      s += sum(q[i])
    for i in range(len(q)):
    	for j in range(len(q[i])):
        	q[i][j] = q[i][j] / s
    
    return q
def move(p, U):
    q = []
    for i in range(len(p)):
        r = []
        for j in range(len(p[i])):
            s = p_move * p[(i-U[0]) % len(p)][(j-U[1]) % len(p[i])]
            s = s + (1-p_move) * p[i][j]            
            r.append(s)
        q.append(r)
    return q
    
for ar in colors:
    a = []
    p.append(a)
    initial = 1.0/(len(colors)*len(ar))
    for c in ar:
        a.append(initial)
for i in range(len(measurements)):
    p=move(p,motions[i])
    p=sense(p, measurements[i])    

#Your probability array must be printed 
#with the following code.
show(p)
