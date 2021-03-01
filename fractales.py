from turtle import *
  
  
speed('fastest')   
rt(-90) 
angle = 45
shape("turtle")

  
# function to plot a Y 
def fractal(size, nivel):    
  
    if nivel > 0: 
        colormode(255) 
          
        # aqui vamos cambiando el color del arbol
        pencolor(0, 255//nivel, 0) 
          
        # avanzamos hacia delante el size
        fd(size) 
  
        #nos movemos a la derecha
        rt(angle) 
  
        #recursivo a la decha
        fractal(0.7 * size, nivel-1) 
          
        pencolor(0, 255//nivel, 0) 
        
        #giramos a la izquiera (estabamos en la dcha, por lo que izda 2 veces el angulo)
        lt( 2 * angle ) 
  
        #llamada recursiva al arbol
        fractal(0.7 * size, nivel-1) 
          
        pencolor(0, 255//nivel, 0) 
        #rotamos a la decha angle quedandonos en el centro de nuevo
        rt(angle) 
        #volvemos atras el size
        fd(-size) 
           
          
fractal(100, 15) 


def fractal_branch(size):
    distance=30
    angle   = 30
    anglechange=30
    left(90)
    F="F"
    F_2="F[-F]F[+F][F]"
    pos_list = []
    ang_list = []
    up()
    ht()
    goto(0,-250)

# reshow the turtle
    down()
    for i in range(size):
        F= F.replace("F",F_2)
    print (F)
    if size > 0: 
        colormode(255)
        i=0
        for letter in F:
            pencolor(0, i%255, 0)
            if letter=='F':
                forward(distance)
            elif letter=='+':
                left(angle)
                angle=angle-anglechange
            elif letter=='-':
                right(angle)
                angle=angle+anglechange
            elif letter=='[':
                pos_list.append(pos())
                ang_list.append(angle)
            elif letter==']':
                up()
                goto(pos_list.pop())
                down()
                ang_aux = ang_list.pop()
                if angle > ang_aux:
                    left(abs(angle-ang_aux))
                    angle = ang_aux
                else:
                    right(abs(angle-ang_aux))
                    angle = ang_aux
                    
            i=i+1
fractal_branch(4)
def fractal_koch(size,distance):
    angle   = 60
    anglechange=60
   # left(90)
    F="F++F++F"
    F_2="F-F++F-F"
    pos_list = []
    ang_list = []
    up()
    goto(-100,100)
    right(90)
# reshow the turtle
    down()
    for i in range(size):
        F= F.replace("F",F_2)
    print (F)
    colormode(255)
    i=0
    for letter in F:
        pencolor(0, i%255, 0)
        if letter=='F':
            forward(distance)
        elif letter=='+':
            right(angle)
           # angle=angle-anglechange
        elif letter=='-':
            left(angle)
           # angle=angle+anglechange
        i=i+1

distance=1
fractal_koch(6,distance)
down()