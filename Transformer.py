

class Transformer ():

    def __init__(self, material):
        
        self.B_peak = None 
        self.k_c = None 
        self.alpha = None 
        self.beta = None 

        self.values = dict() 
        self.values['frequency'] = None 
        self.values['N1'] = None 
        self.values['N2'] = None 
        self.values['volume'] = None 
        
        self.option_materials = ['silicon iron', 'powdered iron']
        assert material in self.option_materials , 'material chosen is not available'
        self.material = material

        self.fill_params()

    def fill_params(self):
        
        if self.material == 'silicon iron':
            self.B_peak = 1.56 
            self.k_c = 3.388
            self.alpha = 1.7 
            self.beta = 1.9
        elif self.material == 'powdered iron':
            self.B_peak = 1
            self.k_c = 1798 
            self.alpha = 1.02 
            self.beta = 1.89 
    
    def set_value(self, name, value):

        assert name in self.values, 'key doesnot exist in self.values'
        self.values[name] = value 
     
    def get_hysterisis_loss(self):
        for key, value in self.values.items():
            assert value, 'cannot calculate hysterisis loss because {} is not defined'.format(key) 
        return self.k_c * (self.values['frequency']**self.alpha) * (self.B_peak**self.beta) * self.values['volume'] 



t = Transformer('silicon iron') 

t.set_value('frequency', 50) 
t.set_value('N1', 10) 
t.set_value('N2', 100) 
t.set_value('volume', 0.3) 

print(t.get_hysterisis_loss()) 