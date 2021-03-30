from vpython import *

scene = canvas(title='Sistem Tata Surya',
               width=1200, height=550,
               center=vector(0,0,0), background=color.black)
e_graph = gcurve(color=color.white)
# scene.camera.pos = vec(0,0,30)

#Set radius planet
RADIUS_MATAHARI = 2
RADIUS_MERKURIUS = 0.08
RADIUS_VENUS = 0.21
RADIUS_BUMI = 0.25
RADIUS_MARS = 0.2
RADIUS_JUPITER = 0.9
RADIUS_SATURNUS = 0.8
RADIUS_URANUS = 0.7
RADIUS_NEPTUNUS = 0.6

#Jarak planet berdasarkan Titius-Bode x 10
JARAK_MATAHARI = 0
JARAK_MERKURIUS = 3.9 
JARAK_VENUS = 7.2
JARAK_BUMI = 10
JARAK_MARS = 15.2
JARAK_JUPITER = 52
JARAK_SATURNUS = 95.4 
JARAK_URANUS = 191.8 
JARAK_NEPTUNUS = 300.6 

#Set massa planet (mass x 1/1x10^24)
MASSA_MATAHARI = 2e3
MASSA_MERKURIUS = 0.33 
MASSA_VENUS = 4.87
MASSA_BUMI = 5.972 
MASSA_BULAN = 0.073
MASSA_MARS = 0.642
MASSA_JUPITER = 1898
MASSA_SATURNUS = 568
MASSA_URANUS = 86.8
MASSA_NEPTUNUS = 102

#KONDISI 1
# Kecepatan planet (kecepatan asli)
# KECEPATAN_MATAHARI = 0
# KECEPATAN_MERKURIUS = 47.4 #km/s
# KECEPATAN_VENUS = 35
# KECEPATAN_BUMI = 29.8
# KECEPATAN_BULAN = 2 #1.022 km/s
# KECEPATAN_MARS = 24.1
# KECEPATAN_JUPITER = 13.1
# KECEPATAN_SATURNUS = 9.7
# KECEPATAN_URANUS = 6.8
# KECEPATAN_NEPTUNUS = 5.4

#KONDISI 2
# Kecepatan planet (1/2 keccepatan asli)
# KECEPATAN_MATAHARI = 0
# KECEPATAN_MERKURIUS = 23.7 
# KECEPATAN_VENUS = 17.5
# KECEPATAN_BUMI = 14.9
# KECEPATAN_BULAN = 2
# KECEPATAN_MARS = 12.05 
# KECEPATAN_JUPITER = 6.55
# KECEPATAN_SATURNUS = 4.85
# KECEPATAN_URANUS = 3.4
# KECEPATAN_NEPTUNUS = 2.7


#KONDISI 3
#Kecepatan planet (kecepatan mars diubah)
KECEPATAN_MATAHARI = 0
KECEPATAN_MERKURIUS = 23.7 #km/s
KECEPATAN_VENUS = 17.5
KECEPATAN_BUMI = 14.9
KECEPATAN_BULAN = 2
KECEPATAN_MARS = 23 
KECEPATAN_JUPITER = 6.55
KECEPATAN_SATURNUS = 4.85
KECEPATAN_URANUS = 3.4
KECEPATAN_NEPTUNUS = 2.7

MOMENTUM_MATAHARI = 0
MOMENTUM_MERKURIUS = KECEPATAN_MERKURIUS*MASSA_MERKURIUS #km/s
MOMENTUM_VENUS = KECEPATAN_VENUS*MASSA_VENUS
MOMENTUM_BUMI = KECEPATAN_BUMI*MASSA_BUMI
MOMENTUM_BULAN = KECEPATAN_BULAN*MASSA_BULAN
MOMENTUM_MARS = KECEPATAN_MARS*MASSA_MERKURIUS
MOMENTUM_JUPITER = KECEPATAN_JUPITER*MASSA_JUPITER
MOMENTUM_SATURNUS = KECEPATAN_SATURNUS*MASSA_SATURNUS
MOMENTUM_URANUS = KECEPATAN_URANUS*MASSA_URANUS
MOMENTUM_NEPTUNUS = KECEPATAN_NEPTUNUS*MASSA_NEPTUNUS


def interaksi_gravitasi(objek1,objek2):
    
    #Menentukan interaksi matahari dengan plaet
    G = 1 
    r_vec = objek1.pos-objek2.pos
    r_mag = mag(r_vec)

    r_hat = r_vec/r_mag
    gaya_mag = G*objek1.massa*objek2.massa/r_mag**2
    gaya_vec = -gaya_mag*r_hat
    
    return gaya_vec
    


#Membuat objek matahari dan planet
MATAHARI = sphere(pos=vec(JARAK_MATAHARI,0,0), 
                  radius= RADIUS_MATAHARI, 
                  massa=MASSA_MATAHARI, 
                  momentum=vec(0,0,0), 
                  emmisive=True, 
                  texture="http://i.imgur.com/yoEzbtg.jpg")

sunlight = local_light(pos=vec(0,0,0), color=color.white)
sunlight2 = local_light(pos=vec(0,0,0), color=color.white)


MERKURIUS = sphere(pos=vec(JARAK_MERKURIUS,0,0), 
                   radius= RADIUS_MERKURIUS, 
                   massa=MASSA_MERKURIUS, 
                   momentum=vec(0,0,MOMENTUM_MERKURIUS),
                   make_trail = True,
                   trail_radius = 0.05,
                   emmisive=True, 
                   texture=textures.granite)

VENUS = sphere(pos=vec(JARAK_VENUS,0,0), 
               radius= RADIUS_VENUS, 
               massa=MASSA_VENUS, 
               momentum=vec(0,0,MOMENTUM_VENUS),
               make_trail = True,
               trail_radius = 0.05,
               emmisive=True, 
               texture=textures.gravel)

BUMI = sphere(pos=vec(JARAK_BUMI,0,0), 
              radius= RADIUS_BUMI,
              massa=MASSA_BUMI, 
              momentum=vec(0,0,MOMENTUM_BUMI),
              make_trail=True,
              trail_radius = 0.05,
              emmisive=True, 
              texture=textures.earth)


MARS = sphere(pos=vec(JARAK_MARS,0,0), 
              radius= RADIUS_MARS,
              massa=MASSA_MARS, 
              momentum=vec(0,0,MOMENTUM_MARS),
              make_trail = True,
              trail_radius = 0.05,
              emmisive=True, 
              texture=textures.wood_old)

JUPITER = sphere(pos=vec(JARAK_JUPITER,0,0), 
                 radius= RADIUS_JUPITER, 
                 massa=MASSA_JUPITER, 
                 momentum=vec(0,0,MOMENTUM_JUPITER),
                 make_trail = True,
                 trail_radius = 0.05,
                 emmisive=True, 
                 texture=textures.rough)

SATURNUS = sphere(pos=vec(JARAK_SATURNUS,0,0), 
                  radius= RADIUS_SATURNUS, 
                  massa=MASSA_SATURNUS, 
                  momentum=vec(0,0,MOMENTUM_SATURNUS),
                  make_trail = True,
                  trail_radius = 0.05,
                  emmisive=True, 
                  texture=textures.stucco)

URANUS = sphere(pos=vec(JARAK_URANUS,0,0), 
                radius= RADIUS_URANUS,
                massa=MASSA_URANUS, 
                momentum=vec(0,0, MOMENTUM_URANUS),
                make_trail = True,
                trail_radius = 0.05,
                emmisive=True, 
                color=color.blue)

NEPTUNUS = sphere(pos=vec(JARAK_NEPTUNUS,0,0), 
                  radius= RADIUS_NEPTUNUS, 
                  massa=MASSA_NEPTUNUS, 
                  momentum=vec(0,0,MOMENTUM_NEPTUNUS),
                  make_trail = True,
                  trail_radius = 0.05,
                  emmisive=True, 
                  color=color.cyan)

planets = [MERKURIUS, VENUS, BUMI, MARS, JUPITER, SATURNUS, URANUS, NEPTUNUS]
rotasi = [59, -243, 1, 1, 0.375, 0.417, 0.708, -0.667]

dt = 0.0001
t = 0
while (True):
    rate(1e70)
    
    for planet in planets:
      planet.gaya = interaksi_gravitasi(planet, MATAHARI)
      planet.momentum = planet.momentum + planet.gaya * dt
      planet.pos = planet.pos + planet.momentum/planet.massa*dt

      #Rotasi planet
      MATAHARI.rotate(angle=radians(360/22*dt), axis=vec(0,1,0))
      MERKURIUS.rotate(angle=radians(360/rotasi[0]*dt), axis=vec(0,1,0))
      VENUS.rotate(angle=radians(360/rotasi[1]*dt), axis=vec(0,1,0))
      BUMI.rotate(angle=radians(360/rotasi[2]*dt), axis=vec(0,1,0))
      MARS.rotate(angle=radians(360/rotasi[3]*dt), axis=vec(0,1,0))
      JUPITER.rotate(angle=radians(360/rotasi[4]*dt), axis=vec(0,1,0))
      SATURNUS.rotate(angle=radians(360/rotasi[5]*dt), axis=vec(0,1,0))
      URANUS.rotate(angle=radians(360/rotasi[6]*dt), axis=vec(0,1,0))
      NEPTUNUS.rotate(angle=radians(360/rotasi[7]*dt), axis=vec(0,1,0))
      
    # Update waktu
    t = t + dt
