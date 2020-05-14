

class Transformer ():

    def __init__(self, material):
        
        self.option_materials = ['silicon iron', 'powdered iron']
        self.params = ['B_peak', 'k_c', 'alpha', 'beta', 'frequency', 'N1', 'N2', 'volume', 'lamination_thickness']
        
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
        elif self.material == 'powdered iron':
            self.values['B_peak'] = 1
            self.values['k_c'] = 1798 
            self.values['alpha'] = 1.02 
            self.values['beta'] = 1.89 
    
    def set_value(self, name, value):
        assert name in self.values, 'key doesnot exist in self.values'
        self.values[name] = value 
     
    def get_hysterisis_loss(self):
        for key, value in self.values.items():
            assert value, 'cannot calculate hysterisis loss because {} is not defined'.format(key) 
        return self.values['k_c'] * (self.values['frequency']**self.values['alpha']) * (self.values['B_peak']**self.values['beta']) * self.values['volume'] 

    def get_eddy_loss(self):
        for key, value in self.values.items():
            assert value, 'cannot calculate eddy loss because {} is not defined'.format(key) 
        return self.values['k_c'] * (self.values['B_peak']**2) * (self.values['frequency']**2) * (self.values['lamination_thickness']**2) * self.values['volume']

t = Transformer('silicon iron') 

print(t.get_hysterisis_loss()) 
print(t.get_eddy_loss()) 