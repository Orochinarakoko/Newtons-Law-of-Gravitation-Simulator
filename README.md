# Newtons-Law-of-Gravitation-Simulator
An N-body simulator of how randomly distributed particles will interact with each other under the force of gravity.

# How it works
1) User defines parameters, and VPython is used to render the bodies in random places in the specified area. All bodies start at rest.
2) The script loops through every body, and then loops again through every other body and calculates the displacement vector between the 2 bodies.
4) The magnitude of the displacement vector is calculated, and using a proportionality relationship derived from Newton's Law of Gravititation ( F = -1/distance^3 * displacement vector)
