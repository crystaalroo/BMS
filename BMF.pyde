from collections import deque
contador_obstaculos=0
arr=[0]*400
porc_libre=400
porc=0
pos_shiba=[0,0]
pos_medalla=[0,0]
pos_start=[0,0]
entrenar=False
world=[[0]*20 for i in range(0,20)]
iter=1
dibujar=True
entre=[[0,0]]
num_e=0
visualizar=False
recorrido=0
buscar=False
empezar=False
personaje=0
imprimir=False

class deportista:
    def __init__(self,image_name):
        self.world=[[0]*20 for i in range(0,20)]
        self.pond=[[sys.maxsize/2.0]*20 for i in range(0,20)]
        self.recorrido=[[0,0]]
        self.imagen=loadImage(image_name)
        self.valores=[0.0]*4
        self.maximo=0
        self.minimo=0
        
    def imprimir(self,x,y):
        image(self.imagen,x*50,y*50,50,50)
        
    def set_world(self,x,y,n):
        self.world[x][y]=n
        
    def get_world(self,x,y):
        return self.world[x][y]

    def set_valores(self,v1,v2,v3,v4):
        self.valores[0]=v1
        self.valores[1]=v2
        self.valores[2]=v3
        self.valores[3]=v4
    
    def get_valores(self,pos):
        return self.valores[pos]
    
    def entrenar(self,x0,y0,x1,y1):
        x=x0
        y=y0
        auxiliar=[[x,y]]
        q=deque([x,y])
        ponderacion=self.world[x][y]
        visitado=[[0]*20 for i in range(0,20)]
        visitado[x][y]=1
        while True:
            if x==x1 and y==y1: break
            vr=[0]*8
            while True:
                ran=int(random(80))%8
                vr[ran]=1
                if ran==1 and x>0 and y>0 and self.world[x-1][y-1]!=5 and visitado[x-1][y-1]==0:
                    x-=1
                    y-=1
                    break
                if ran==2 and x>0 and self.world[x-1][y]!=5 and visitado[x-1][y]==0:
                    x-=1
                    break
                if ran==3 and x>0 and y<19 and self.world[x-1][y+1]!=5 and visitado[x-1][y+1]==0:
                    x-=1
                    y+=1
                    break
                if ran==4 and y>0 and self.world[x][y-1]!=5 and visitado[x][y-1]==0:
                    y-=1
                    break
                if ran==5 and y<19 and self.world[x][y+1]!=5 and visitado[x][y+1]==0:
                    y+=1
                    break
                if ran==6 and x<19 and y>0 and self.world[x+1][y-1]!=5 and visitado[x+1][y-1]==0:
                    x+=1
                    y-=1
                    break
                if ran==7 and x<19 and self.world[x+1][y]!=5 and visitado[x+1][y]==0:
                    x+=1
                    break
                if ran==8 and x<19 and y<19 and self.world[x+1][y+1]!=5 and visitado[x+1][y+1]==0:
                    x+=1
                    y+=1
                    break
                contador=0
                for i in range(0,8):
                    if vr[i]==1:
                        contador+=1
                if contador==8:
                    q.pop()
                    if len(q)==0: return
                    x=q[-1][0]
                    y=q[-1][1]
                    break
            visitado[x][y]=1
            auxiliar.append([x,y])
            ponderacion+=self.world[x][y]
            if [x,y]!=q[-1]: q.append([x,y])
        ajuste=ponderacion-(self.maximo+self.minimo)/2.0
        maximo=max(self.maximo,ponderacion)
        if self.minimo==0: minimo=ponderacion
        minimo=min(self.minimo,ponderacion)
        for i in auxiliar:
            self.pond[i[0]][i[1]]+=ajuste
        print(self.pond)
        return auxiliar
    
    def busqueda(self,x,y,xf,yf):
        ruta=[[x,y]]
        vis=[[0]*20 for i in range(0,20)]
        x_min=0
        y_min=0
        vis[x][y]=1
        while True:
            if x==xf and y==yf: break   
            minimo=sys.maxsize 
            if  x>0 and y>0 and vis[x-1][y-1]==0 and self.world[x-1][y-1]!=5:
                if self.pond[x-1][y-1]<minimo:
                    x_min=x-1
                    y_min=y-1
                    minimo=self.pond[x_min][y_min]            
                    
                    
            if  x>0 and vis[x-1][y]==0 and self.world[x-1][y]!=5:
                if self.pond[x-1][y]<minimo:
                    x_min=x-1
                    y_min=y
                    minimo=self.pond[x_min][y_min]    
                    
            if  x>0 and y<19 and vis[x-1][y+1]==0 and self.world[x-1][y+1]!=5:
                if self.pond[x-1][y+1]<minimo:
                    x_min=x-1
                    y_min=y+1
                    minimo=self.pond[x_min][y_min]    
                    
            if  y>0 and vis[x][y-1]==0 and self.world[x][y-1]!=5:
                if self.pond[x][y-1]<minimo:
                    y_min=y-1
                    x_min=x
                    minimo=self.pond[x_min][y_min]    
            
            if  y<19 and vis[x][y+1]==0 and self.world[x][y+1]!=5:
                if self.pond[x][y+1]<minimo:
                    y_min=y+1
                    x_min=x
                    minimo=self.pond[x_min][y_min]    
                    
            if  x<19 and y>0 and vis[x+1][y-1]==0 and self.world[x+1][y-1]!=5:
                if self.pond[x+1][y-1]<minimo:
                    x_min=x+1
                    y_min=y-1
                    minimo=self.pond[x_min][y_min]    
                    
            if  x<19 and y<19 and vis[x+1][y+1]==0 and self.world[x+1][y+1]!=5:
                if self.pond[x+1][y+1]<minimo:
                    x_min=x+1
                    y_min=y+1
                    minimo=self.pond[x_min][y_min]    
                    
            if  x<19 and vis[x+1][y]==0 and self.world[x+1][y]!=5:
                if self.pond[x+1][y-1]<minimo:
                    x_min=x+1
                    y_min=y
                    minimo=self.pond[x_min][y_min]    
            ruta.append([x_min,y_min])
            print([x_min,y_min])
            x=x_min
            y=y_min
            if vis[x][y]==0:break
            vis[x][y]=1
        return ruta
        

            
        
        
def setup():
    global bolt,phelps,super,contador_obstaculos
    bolt=deportista('bolt.png')
    phelps=deportista('phelps.png')
    super=deportista('super.png')
    bolt.set_valores(2.5,.3,1.5,1)
    phelps.set_valores(1.5,1,2.5,.3)
    super.set_valores(3,2.5,1,.3)
    cuadros=50
    size(1401,1500)
    fill(130,80,210)
    stroke(130,80,210)
    rect(0,0,1000,1500) #CANVAS
    fill(255,255,255)
    rect(1001,0,400,1500)#JUEGO
    stroke(255,255,255)
    for i in range(0,21): #LINEEEAS!
        line(cuadros*i,0,cuadros*i,1000)
        line(0,cuadros*i,1000,cuadros*i)
    fill(10,80,230)
    titulo()

    contador_obstaculos=1
    dibujarPorcentajes()
    
def draw():
    global bolt,phelps,super,entrenar,pos_shiba,pos_medalla,dibujar,entre,iter,num_e,visualizar,contador_obstaculos,buscar,recorrido,empezar,personaje,imprimir,pos_start
    if not empezar and imprimir:
        if personaje==2:
            if iter!=len(entre):
                redibujar(entre[iter-1][0],entre[iter-1][1])
                super.imprimir(entre[iter][0],entre[iter][1])
                iter+=1
                delay(5)
            else:
                redibujar(entre[iter-1][0],entre[iter-1][1])
                iter=0
                personaje=0
                imprimir=False
        if personaje==1:
            if iter!=len(entre):
                redibujar(entre[iter-1][0],entre[iter-1][1])
                phelps.imprimir(entre[iter][0],entre[iter][1])
                iter+=1
                delay(1)
            else:
                redibujar(entre[iter-1][0],entre[iter-1][1])
                iter=0
                personaje=2
        if personaje==0:
            if iter!=len(entre):
                redibujar(entre[iter-1][0],entre[iter-1][1])
                bolt.imprimir(entre[iter][0],entre[iter][1])
                iter+=1
                delay(5)
            else:
                redibujar(entre[iter-1][0],entre[iter-1][1])
                iter=0
                personaje=1
                
    if empezar and not imprimir:
        if personaje==0:
            print("aqui")
            entre=bolt.busqueda(pos_start[0],pos_start[1],pos_medalla[0],pos_medalla[1])
            print("hello")
            empezar=False
            imprimir=True
        if personaje==1:
            entre=phelps.busqueda(pos_start[0],pos_start[1],pos_medalla[0],pos_medalla[1])
            empezar=False
            imprimir=True
        if personaje==2:
            entre=super.busqueda(pos_start[0],pos_start[1],pos_medalla[0],pos_medalla[1])
            empezar=False
            imprimir=True
            personaje=0
     
    if entrenar and dibujar:
        if num_e==30:
            contador_obstaculos=8
            entrenar=False
            num_e=31
            buscar=True
        if num_e>19 and num_e<30:
            super.imprimir(1250/50,500/50)
            entre=super.entrenar(pos_shiba[0],pos_shiba[1],pos_medalla[0],pos_medalla[1])
            dibujar=False
        if num_e>9 and num_e<20:
            phelps.imprimir(1250/50,500/50)
            entre=phelps.entrenar(pos_shiba[0],pos_shiba[1],pos_medalla[0],pos_medalla[1])
            dibujar=False

        if num_e<10:
            bolt.imprimir(1250/50,500/50)
            entre=bolt.entrenar(pos_shiba[0],pos_shiba[1],pos_medalla[0],pos_medalla[1])
            dibujar=False
            
    if entrenar and dibujar==False:
        if num_e>19 and num_e<30:
            if iter!=len(entre):
                redibujar(entre[iter-1][0],entre[iter-1][1])
                if visualizar: super.imprimir(entre[iter][0],entre[iter][1])
                iter+=1
                delay(1)
            else:
                redibujar(entre[iter-1][0],entre[iter-1][1])
                dibujar=True
                num_e+=1
                iter=0
                entre=[[0,0]]
        if num_e>9 and num_e<20:
            if iter!=len(entre):
                redibujar(entre[iter-1][0],entre[iter-1][1])
                if visualizar: phelps.imprimir(entre[iter][0],entre[iter][1])
                iter+=1
                delay(1)
            else:
                redibujar(entre[iter-1][0],entre[iter-1][1])
                dibujar=True
                num_e+=1
                iter=0
                entre=[[0,0]]
        if num_e<10:
            if iter!=len(entre):
                redibujar(entre[iter-1][0],entre[iter-1][1])
                if visualizar: bolt.imprimir(entre[iter][0],entre[iter][1])
                iter+=1
                delay(1)
            else:
                redibujar(entre[iter-1][0],entre[iter-1][1])
                dibujar=True
                num_e+=1
                iter=0
                entre=[[0,0]]

    
def titulo():
    f=createFont("AmericanTypewriter",20)
    textFont(f)
    text("BUSQUEDA EN EL ",1020,50)
    text("MUNDO FANTASIA",1020,80)
    
def dibujarPorcentajes(): #PORCENTAJE BARRA
    cuadros_titulo()
    fill(255,255,255)
    stroke(255,255,255)
    rect(1120,250,300,100)#Margenes
    fill(0,0,0)
    text("20%",1150,350)
    text("80%",1330,350)
    rect(1150,250,5,50)#Margenes
    rect(1330,250,5,50)
    rect(1155,275,175,5) #Linea central
   # BOTON OK
    stroke(0,0,0)
    fill(255,255,255)
    rect(1220,350,50,30,10)
    fill(32,32,0)
    text("OK",1230,370)
    
def cuadros_titulo():
    global contador_obstaculos
    f=createFont("AmericanTypewriter",20)
    textFont(f)
    fill(255,255,255)
    stroke(255,255,255)
    rect(1010,250,100,100)
    fill(0,0,0)
    stroke(0,0,0)
    if contador_obstaculos==1: text("Obstaculos",1020,260)
    if contador_obstaculos==2: text("Agua",1020,260)
    if contador_obstaculos==3: text("Montaña",1020,260)
    if contador_obstaculos==4: text("Barranco",1020,260)

def mousePressed():
    global contador_obstaculos,arr,bolt,pos_medalla,porc,entrenar,pos_shiba,world,visualizar,buscar,empezar,pos_start
    if buscar and mouseX>=0 and mouseX<=1000 and mouseY>=0 and mouseY<=1000:
        x=int(mouseX/50)
        y=int(mouseY/50)
        if bolt.get_world(x,y)!=5:
            start_image=loadImage("start.png")
            start_image.resize(50,50)
            world[x][y]=6
            image(start_image,x*50,y*50)
            pos_start=[x,y]
        buscar=False
        empezar=True

    if mouseX>=1250 and mouseX<=1270 and mouseY>=380 and mouseY<=400 and contador_obstaculos==7:
            visualizar=not visualizar
            entrenamientos()
    if mouseX>=0 and mouseX<=1000 and mouseY>=0 and mouseY<=1000 and contador_obstaculos==6:
        x=int(mouseX/50)
        y=int(mouseY/50)
        if bolt.get_world(x,y)!=5:
            medalla=loadImage("medalla.png")
            medalla.resize(50,50)
            world[x][y]=-1
            image(medalla,x*50,y*50)
            contador_obstaculos=7
            pos_medalla=[x,y]
            entrenar=True
            visualizar=True
            entrenamientos()
            cuadros_titulo()
            
    if mouseX>=0 and mouseX<=1000 and mouseY>=0 and mouseY<=1000 and contador_obstaculos==5:
        x=int(mouseX/50)
        y=int(mouseY/50)
        if bolt.get_world(x,y)!=5:
            shiba=loadImage("shiba.png")
            shiba.resize(50,50)
            world[x][y]=0
            image(shiba,x*50,y*50)
            contador_obstaculos=6
            pos_shiba=[x,y]
        
    if mouseX>=1220 and mouseX<=1270 and mouseY>=350 and mouseY<=380 and contador_obstaculos<5:
        if contador_obstaculos==4:
            contador_obstaculos=5
            dibujar_lla()
        if contador_obstaculos==3:
            contador_obstaculos=4
            dibujar_mon()
        if contador_obstaculos==2:
            contador_obstaculos=3
            dibujar_agua()
        if contador_obstaculos==1:
            contador_obstaculos=2
            dibujar_obstaculos()

def mouseReleased():
    global porc,contador_obstaculos
    if mouseX>=1150 and mouseX<=1330 and mouseY>=250 and mouseY<=300 and contador_obstaculos<5:
        dibujarPorcentajes()
        x=mouseX
        porc=(x-1150)*60/180
        porc=int(porc)+20
        fill(200,20,20)
        rect(x,250,5,50)
        text(str(porc)+"%",x,330)

            
def dibujar_obstaculos():
    global bolt,phelps,super,porc,arr,porc_libre,world
    cuadros_titulo()
    image_bomb=loadImage("bomb.png")
    stroke(255,255,255)
    fill(255,255,255)
    rect(1001,150,400,300)
    can_por=porc*4
    for _ in range (0,can_por):
        randomSeed(0)
        while True:
            k=int(random(400))
            if arr[k]==0:
                y=int(k/20)
                arr[k]=5
                x=k%20
                bolt.set_world(x,y,5)
                phelps.set_world(x,y,5)
                super.set_world(x,y,5)
                world[x][y]=5
                image(image_bomb,50*x,50*y,50,50)
                break
    porc_libre-=can_por
    print(porc_libre)
    dibujarPorcentajes()

    
def dibujar_lla():
    global bolt,phelps,super,porc,arr,porc_libre,world
    cuadros_titulo()
    image_lla=loadImage("lla.png")
    stroke(255,255,255)
    fill(255,255,255)
    rect(1001,150,400,300)
    can_por=porc*porc_libre
    can_por/=100
    for _ in range (0,can_por):
        randomSeed(0)
        while True:
            k=int(random(400))
            if arr[k]==0:
                y=int(k/20)
                arr[k]=5
                x=k%20
                bolt.set_world(x,y,bolt.get_valores(2))
                phelps.set_world(x,y,phelps.get_valores(2))
                super.set_world(x,y,super.get_valores(2))
                world[x][y]=4
                image(image_lla,50*x,50*y,50,50)
                
                break
    porc_libre-=can_por
    rellenar()


def dibujar_mon():
    global bolt,phelps,super,porc,arr,porc_libre,world
    cuadros_titulo()
    image_mon=loadImage("mon.png")
    stroke(255,255,255)
    fill(255,255,255)
    rect(1001,150,400,300)
    can_por=porc*porc_libre
    can_por/=100
    print(can_por)
    for _ in range (0,can_por):
        randomSeed(0)
        while True:
            k=int(random(400))
            if arr[k]==0:
                y=int(k/20)
                arr[k]=5
                x=k%20
                bolt.set_world(x,y,bolt.get_valores(0))
                phelps.set_world(x,y,phelps.get_valores(0))
                super.set_world(x,y,super.get_valores(0))
                world[x][y]=3
                image(image_mon,50*x,50*y,50,50)
                break
    porc_libre-=can_por
    
    dibujarPorcentajes()
    
def dibujar_agua():
    global bolt,phelps,super,porc,arr,porc_libre,world
    cuadros_titulo()
    image_agua=loadImage('agua.png')
    stroke(255,255,255)
    fill(255,255,255)
    rect(1001,150,400,300)
    can_por=porc*porc_libre
    can_por/=100
    print(can_por)
    for _ in range (0,can_por):
        randomSeed(0)
        while True:
            k=int(random(400))
            if arr[k]==0:
                y=int(k/20)
                arr[k]=5
                x=k%20
                bolt.set_world(x,y,bolt.get_valores(3))
                phelps.set_world(x,y,phelps.get_valores(3))
                super.set_world(x,y,super.get_valores(3))
                world[x][y]=2
                image(image_agua,50*x,50*y,50,50)
                break
    porc_libre-=can_por
    dibujarPorcentajes()

    
def rellenar():
    global arr,phelps,bolt,super,world
    y=0
    for k in range(0,400):
        if arr[k]==0:
            y=int(k/20)
            x=k%20
            bolt.set_world(x,y,bolt.get_valores(1))
            super.set_world(x,y,super.get_valores(1))
            phelps.set_world(x,y,phelps.get_valores(1))
            world[x][y]=1

            
def cuadros_titulo():
    global contador_obstaculos
    f=createFont("AmericanTypewriter",20)
    textFont(f)
    fill(255,255,255)
    stroke(255,255,255)
    rect(1010,250,100,100)
    fill(0,0,0)
    stroke(0,0,0)
    if contador_obstaculos==1: text("Obstaculos",1020,260)
    if contador_obstaculos==2: text("Agua",1020,260)
    if contador_obstaculos==3: text("Montaña",1020,260)
    if contador_obstaculos==4: text("Barranco",1020,260)
    if contador_obstaculos==7: 
        text("Ver entrenamiento",1020,400)
        text("Entrenamiento: ",1020,550)
        
    

def redibujar(x,y):
    global world
    fill(130,80,210)
    stroke(130,80,210)
    rect(x*50+1,y*50+1,48,48)
    if world[x][y]==6:
        image_start=loadImage("start.png")
        image(image_start,50*x,50*y,50,50)
    if world[x][y]==5:
        image_bomb=loadImage("bomb.png")
        image(image_bomb,50*x,50*y,50,50)
    if world[x][y]==2:
        image_agua=loadImage('agua.png')
        image(image_agua,50*x,50*y,50,50)
    if world[x][y]==3:
        image_mon=loadImage("mon.png")
        image(image_mon,50*x,50*y,50,50)
    if world[x][y]==4:
        image_lla=loadImage("lla.png")
        image(image_lla,50*x,50*y,50,50)
    if world[x][y]==0:
        image_shiba=loadImage("shiba.png")
        image(image_shiba,50*x,50*y,50,50)
    if world[x][y]==-1:
        image_medalla=loadImage("medalla.png")
        image(image_medalla,50*x,50*y,50,50)
        
def entrenamientos():
    global visualizar
    fill(255,255,255)
    stroke(0,0,0)
    rect(1250,380,20,20)
    fill(0,0,0)
    if visualizar:
        stroke(0,0,0)
        ellipse(1260,390,5,5)



    
    
