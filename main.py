from vpython import *
import random

L = 4e10
xaxis = curve(color=color.gray(0.5), radius=3e8)
xaxis.append(vec(0,0,0))
xaxis.append(vec(L,0,0))
yaxis = curve(color=color.gray(0.5), radius=3e8)
yaxis.append(vec(0,0,0))
yaxis.append(vec(0,L,0))
zaxis = curve(color=color.gray(0.5), radius=3e8)
zaxis.append(vec(0,0,0))
zaxis.append(vec(0,0,L))


scene.caption = """In GlowScript programs:
Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
scene.forward = vector(0,0.3,-1)

G = 6.7e-11 # Newton gravitational constant

b1=sphere(pos=vector(4.1e11,0,0),radius=1e9,color=color.blue,make_trail=True,interval=10,retain=50)
b2=sphere(pos=vector(0,4.3e11,0),radius=1e9,color=color.yellow,make_trail=True,interval=10,retain=50)
b3=sphere(pos=vector(0,-5e11,0),radius=1e9,color=color.red,make_trail=True,interval=10,retain=50)

b1.mass=2e29
b2.mass=2e29
b3.mass=4e29


b1.p=vector(random.randint(0,100),1e3,random.randint(0,100))*b1.mass
b2.p=vector(random.randint(0,100),random.randint(0,100),1e3)*b2.mass
b3.p=vector(0,0,0)-b1.p-b2.p

dt=1e5

hitflag=0
while hitflag==0:
    rate(400)
    r12 = b1.pos - b2.pos   #2+1-
    r23 = b2.pos - b3.pos
    r31 = b3.pos - b1.pos   

    F12 = G * b1.mass * b2.mass * norm(r12) / mag2(r12)
    F23 = G * b2.mass * b3.mass * norm(r23) / mag2(r23)
    F31 = G * b3.mass * b1.mass * norm(r31) / mag2(r31)
    
    b1.p = b1.p - F12*dt + F31*dt
    b2.p = b2.p - F23*dt + F12*dt
    b3.p = b3.p - F31*dt + F23*dt

    b1.pos = b1.pos + (b1.p/b1.mass) * dt
    b2.pos = b2.pos + (b2.p/b2.mass) * dt
    b3.pos = b3.pos + (b3.p/b3.mass) * dt

    if mag(b1.pos-b2.pos)<5e9:
        hitflag=1
    if mag(b2.pos-b3.pos)<5e9:
        hitflag=1
    if mag(b1.pos-b3.pos)<5e9:
        hitflag=1

