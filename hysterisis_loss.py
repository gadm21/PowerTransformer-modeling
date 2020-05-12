

class Transformer ():

    def __init__(self):

        self.permeability = 0 
        self.length = 0 
        self.area = 0 
        self.reluctance = 0 
        

        self.N1 = 0
        self.N2 = 0 

        self.flux = 0
        self.magnetomotive_force = 0 


class Signal ():

    def __init__(self, m, a, f):
        self.name = ''
        self.magnitude = m
        self.frequency = f
        self.angle = a