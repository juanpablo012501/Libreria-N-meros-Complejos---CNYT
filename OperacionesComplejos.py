import math

def sumCom(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def prodCom(c1, c2):
    return (c1[0]*c2[0] - c1[1]*c2[1], c1[0]*c2[1] + c1[1]*c2[0])

def sustCom(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def modCom(c):
    return math.sqrt((c[0]**2) + (c[1]**2))

def divCom(c1, c2):
    mod = (modCom(c2))**2
    return ((c1[0]*c2[0] + c1[1]*c2[1])/mod , (c2[0]*c1[1] - c1[0]*c2[1])/mod)

def conjCom(c):
    return (c[0], -1*c[1])

def convCartPol(c):
    if c[0] == 0 and c[1] == 0:
        return (0,0)
    elif c[0] == 0 and c[1] > 0:
        return (modCom(c), math.pi/2)
    elif c[0] == 0 and c[1] < 0:
        return (modCom(c), (3*math.pi)/2)
    elif c[1] == 0 and c[0] > 0:
        return (modCom(c), 0)
    elif c[1] == 0 and c[0] < 0:
        return (modCom(c), math.pi)
    return (modCom(c), math.atan(c[1]/c[0]))

def convPolCart(rho):
    return (rho[0]*math.cos(rho[1]), rho[0]*math.sin(rho[1]))

def faseCom(c):
    rho = convCartPol(c)
    fase = rho[1]
    while fase > 2*math.pi:
        fase = fase - 2*math.pi
    return fase