
class Object:
    def __init__(self):
        #Should get id automatically
        self.id = 0
        self.x = 0
        self.y = 0
        self.xspeed = 0
        self.yspeed = 0
        self.sprite = 0

    #Register object in scenario
    def register(self, scenario):
        print "Registered object"
        scenario.add_obj(self)
    
    def render(self, dev):
       pass 
