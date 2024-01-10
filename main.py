from math import *
from tkinter import *
from time import *
from random import *
myWindow = Tk()
s = Canvas(myWindow, width=800, height=600, background = "#a1c2f7")
s.pack()

##Due
##By Diba Darooneh

#Background
#Sky
skycolour=['#17c1ff','#21c4ff','#26c5ff','#29c6ff','#30c8ff','#36c9ff','#3dcbff','#42ccff','#45cdff','#4dcfff','#4fd0ff','#54d1ff','#59d2ff','#5ed3ff','#63d4ff','#69d6ff','#6ed7ff','#73d8ff','#78d9ff','#7ddaff','#85dcff','#8cdeff','#94e0ff','#9ee3ff','#a3e5ff','#a8e6ff','#b0e8ff','#b5e9ff','#b8eaff','#bdebff']
for i in range (30):
	s.create_rectangle(0,0+i*20,800,20+i*20, fill=skycolour[i], outline='')

#Cloud
r=[-1,4,2,6]
for i in range (4):
	x=100*r[i]
	y=100*sin(r[i]/2.3)
	s.create_oval(x,y,x+60,y+60, fill="white", outline="")
	s.create_oval(x+30,y+70,x+125,y-20,fill="white", outline="")
	s.create_oval(x+100,y,x+160,y+60,fill="white", outline="")

#Trees
s.create_polygon(0,550,90,550,40,450,65,350,0,350 ,fill="#8a4f19", smooth=True)
s.create_rectangle(0,350,40,550, fill="#8a4f19", outline='')
s.create_polygon(800,550,710,550,760,450,735,350,800,350 ,fill="#8a4f19", smooth=True)
s.create_rectangle(800,350,760,550, fill="#8a4f19", outline='')

colour=[]
r1 = 120
r2 = 120
for i in range (3000):
	x1=randint(-200,200)
	y=randint(180,420)
	x2=randint(600,1000)
	size=randint(10,30)
	centerx1=x1+size/2
	centery=y+size/2
	centerx2=x2+size/2
	distance1=sqrt((0-centerx1)**2+(300-centery)**2)
	distance2=sqrt((800-centerx2)**2+(300-centery)**2)	
	colour.append(choice(["#106916", '#2bab33','#56f056', '#1f521f']))	
	if distance1<=r1:
		s.create_oval(x1,y,x1+size,y+size,fill=colour[i], outline="")
	if distance2<=r2:
		s.create_oval(x2,y,x2+size,y+size,fill=colour[i], outline="")


#Grass
s.create_polygon(-100,600,50,500,200,525,700,500,775,525,900,575, smooth=True, fill='#71cf42')
s.create_rectangle(0,550,800,600, fill="#71cf42", outline="")
for i in range (10):
	x=randint(0,800)
	y=randint(525,600)
	s.create_polygon(x-6,y+5,x-4,y+2,x-2,y+5,x,y,x+2,y+4,x+4,y+2,x+6,y+5, fill="#106916")

#Prep
#Lists
kitex=[]
kitey=[]
kites=[]
speedx=[1,2,3,]
speedy=[1,2,3]
kiteline1=[]
kiteline2=[]
kitestring=[]
ys=[]
xs=[]
spaces=[]
heads=[]
bodies=[]
xkites=[]
ykites=[]
xppls=[]
yppls=[]
kitetail=[]
birds=[]
birdx=[]
birdy=[]
colour=["#fa7c07", "#239918","#faf207"]
colour2=["#f75e6d", "#429de3", "#9b42e3"]
colour3=["#f5f373","black", "#402a04"]

#Values
for i in range (3):
	kitex.append(randint(300,650))
	kitey.append(randint(150,350))
	kites.append(0)
	xkites.append(0)
	ykites.append(0)
	kiteline1.append(0)
	kiteline2.append(0)
	kitetail.append(0)
	kitestring.append(0)
	space=randint(30,50)
	spaces.append(space)
	y=randint(525,545)
	ys.append(y)
	x=390+i*space
	xs.append(x)
	heads.append(0)
	bodies.append(0)
	xppls.append(0)
	yppls.append(0)
	birds.append(0)
	birdx.append(0)
	birdy.append(0)
	
#Animation
t = 0
while True:

	#Kite
	for i in range (3):
		xkites[i] = kitex[i]+30*sin(0.01*t*speedx[i])
		ykites[i] = kitey[i]-30*sin(2*0.01*t*speedy[i])
		kites[i]=s.create_polygon(xkites[i]-50,ykites[i]+5,xkites[i],ykites[i]-20,xkites[i]+50,ykites[i]+5,xkites[i],ykites[i]+30, fill=colour[i]) 
		kiteline1[i]=s.create_line(xkites[i]-50,ykites[i]+5,xkites[i]+50,ykites[i]+5,)
		kiteline2[i]=s.create_line(xkites[i],ykites[i]-20,xkites[i],ykites[i]+30,)
		kitetail[i]=s.create_line(xkites[i]+40,ykites[i],xkites[i]+50,ykites[i]-10,xkites[i]+60,ykites[i],xkites[i]+70,ykites[i]+5,xkites[i]+80,ykites[i],xkites[i]+100,ykites[i]-10,xkites[i]+110,ykites[i],xkites[i]+120,ykites[i]+5,xkites[i]+130,ykites[i],xkites[i]+140,ykites[i]-10, smooth=True, width=3, fill=colour[i])

	#People
		xppls[i] = xs[i]+30*cos(0.01*t*speedx[i]*0.3)
		yppls[i] = ys[i]
		heads[i]=s.create_polygon(xppls[i],yppls[i]+5,xppls[i]+15,yppls[i]+5,xppls[i]+15,yppls[i]+50,xppls[i],yppls[i]+50, smooth=True, fill=colour2[i])
		bodies[i]=s.create_oval(xppls[i],yppls[i],xppls[i]+15,yppls[i]+15, fill=colour3[i], outline='')

	#String
		kitestring[i]=s.create_line(xkites[i],ykites[i], xkites[i]+space, ykites[i]+space*2, xppls[i]+15,yppls[i]+25, fill="white", smooth=True)

	for i in range (4):
	
		s.update()
		sleep(0.004)
	for i in range(3):
		s.delete( kites[i], kiteline1[i],kiteline2[i], heads[i], bodies[i], kitestring[i], kitetail[i])
	t+=1






