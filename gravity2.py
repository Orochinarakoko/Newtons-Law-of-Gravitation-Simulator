from vpython import *


num_bodies = int(input("How many bodies >>> "))

area = float(input("Side length of the cubic area in which bodies will be generated >>> "))

dt = float(input("Time step >>> "))

steps = int(input("How many steps >>> ")) 



bodies = []



t = 0

for i in range(num_bodies):
    body = sphere(pos = vector(random()*area,random()*area,random()*area),make_trail = True,retain = 50 , pps = 5)
    bodies.append(body)


    
for i in bodies:
    i.mass = (4/3)*pi

    i.v = vector(0,0,0)

    i.collided = 0

    
COM = sphere(radius = 3 , pos = vector(50,50,50), color = color.magenta)




                                      
while t < steps:

    mnet = vector(0,0,0)
    
    for body1 in bodies:
        
        Anet = vector(0,0,0)

        mnet += body1.pos
        
        for body2 in bodies:
            if body1 == body2:
                continue
            else:
                displacement = body1.pos - body2.pos
                distance = mag(displacement)

                if distance < 2:
                    
                    norm_vect = body1.pos - body2.pos

                    norm_vect = norm_vect / mag(norm_vect)

                    perp_comp1 = dot(body1.v , norm_vect) * norm_vect

                    perp_comp2 = dot(body2.v,norm_vect)*norm_vect

                    par_comp1 = body1.v - perp_comp1
                    par_comp2 = body2.v - perp_comp2

                    body1.v = par_comp1 + perp_comp2

                    body2.v = par_comp2 + perp_comp1

                    body1.pos += 0.1*norm_vect
                    body2.pos -= 0.1*norm_vect
             


                    
                else:

                    Anet = Anet - 4/3*pi*((distance)**-3)*displacement




        body1.pos = body1.pos + (body1.v*dt + 0.5*Anet*dt**2) # use s = ut + 1/2at^2 to update position vector
    
        body1.v = body1.v + Anet*dt # use v = u + at to update velocity vector


    COM.pos = mnet / num_bodies 
    t = t + dt

