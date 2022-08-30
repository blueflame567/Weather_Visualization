from math import sqrt, cos, sin, atan2, acos

def toSpherical(x, y, z):
    r = sqrt(x*x+y*y+z*z)
    theta = acos(z/r)
    phi = atan2(y,x)
    return(r, theta, phi)

def toCartesian(r, theta, phi):
    x = r*cos(phi)*sin(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(theta)
    return(x, y, z)
