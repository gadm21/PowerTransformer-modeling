
import math 
from matplotlib import pyplot as plt 
from math import pi, sqrt 

class Transformer ():

    def __init__(self, material):
        
        self.option_materials = ['silicon iron', 'powdered iron']
        self.params = ['B_peak', 'k_c', 'alpha', 'beta', 'frequency', 'N1', 'N2', 'volume', 'lamination_thickness', 'R_eq']
        
        self.values = dict() 
        for param in self.params: self.values[param] = None 
        
        assert material in self.option_materials , 'material chosen is not available'
        self.material = material

        self.fill_params()

    def fill_params(self):
        self.values['frequency'] = 50
        self.values['N1'] = 10
        self.values['N2'] = 100
        self.values['volume'] = 0.3  
        self.values['lamination_thickness'] = 0.2

        if self.material == 'silicon iron':
            self.values['B_peak'] = 1.56 
            self.values['k_c'] = 3.388
            self.values['alpha'] = 1.7 
            self.values['beta'] = 1.9
            self.values['R_eq'] = 4.5
        elif self.material == 'powdered iron':
            self.values['B_peak'] = 1
            self.values['k_c'] = 1798 
            self.values['alpha'] = 1.02 
            self.values['beta'] = 1.89 
            self.values['R_eq'] = 11 
    
    def set_value(self, name, value):
        assert name in self.values, 'key doesnot exist in self.values'
        self.values[name] = value 
    
    def deg2rad(deg) : return (deg*pi) / 180 
    
    def get_open_circuit_test(self, voltage):
        p = voltage**2 / self.values['R_eq'] 
        i = math.sqrt(p/self.values['R_eq']) 
        return p, i

    def get_hysterisis_loss(self):
        for key, value in self.values.items():
            assert value, 'cannot calculate hysterisis loss because {} is not defined'.format(key) 
        return self.values['k_c'] * (self.values['frequency']**self.values['alpha']) * (self.values['B_peak']**self.values['beta']) * self.values['volume'] 

    def get_eddy_loss(self):
        for key, value in self.values.items():
            assert value, 'cannot calculate eddy loss because {} is not defined'.format(key) 
        return self.values['k_c'] * (self.values['B_peak']**2) * (self.values['frequency']**2) * (self.values['lamination_thickness']**2) * self.values['volume']

    def extract_range(self, v, points_num = 200):
        s, e = (float(c) for c in v.split('-'))
        step = (e-s) /points_num
        rangee = [i for i in np.arange(s, e, step)]
        return np.array(rangee)  

    def analyze_load(self, load) :
        if 'j' not in load :
            return float(load), 1
        
        if '-' in load : r, x = load.split('-') 
        else : r, x = load.split('+') 

        r = float(r) 
        x = float(x.split('j')[1]) 
        z = sqrt(r**2 + x**2)
        pf = r/z 
        return z, pf 


    def turns_ratio(self):
        return self.values['N1'] / self.values['N2'] 

    def solve(self, v1, load, pf):
        v2 = self.turns_ratio() * v1 
        l2 = v2/load 
        return v2 * l2 * pf  

    def get_efficiency(self, v1, load):
        if '-' in v1 : v1 = self.extract_range(v1, points_num=200)  
        i1 =    

        z, pf = self.analyze_load(load) 

        
        output_va = self.solve(v1, z, pf) 
        

if __name__ == "__main__":
    t = Transformer('silicon iron') 

    print(t.get_hysterisis_loss()) 
    print(t.get_eddy_loss()) 