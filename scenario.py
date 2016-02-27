
class Scenario:
    def __init__(self):
        self.objects = []

    def add_obj(self, obj):
        self.objects.append(obj)

    def register(self, smgr):
        print "Registered scenario"
        smgr.add_scenario(self)
