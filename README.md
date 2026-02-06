# Newtons-Law-of-Gravitation-Simulator
An N-body simulator of how randomly distributed particles will interact with each other under the force of gravity.

# How it works
1) User defines parameters, and VPython is used to render the bodies in random places in the specified area. All bodies start at rest.
2) The script loops through every body, and then loops again through every other body and calculates the displacement vector between the 2 bodies.
3) If the magnitude of the displacement vector is less than 2 (ie the bodies have collided), then vector mechanics are used to decompose the velocities of both bodies in to parallel and perpendicular components, and they swap perpendicular components
4) If not, then magnitude of the displacement vector is calculated, and using a proportionality relationship derived from Newton's Law of Gravititation ( F = -1/distance^3 * displacement vector), we determine a force vector
5) This is repeated for every body, and the resultant force vector is calculated by summing all individual force vectors.
6) This is then used to calculate the acceleration of the body, and an euler integration method is used to approximate the position and velocity vectors of the body
7) This is then repeated for every body, and the time step increases by 1.
8) A centre of mass ( purple ball ) is also calculated in every time step.
