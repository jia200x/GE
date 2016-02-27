
class Scenario:
    def __init__(self):
        self.objects = []

    def add_obj(self, obj):
        self.objects.append(obj)

    def register(self, smgr):
        print "Registered scenario"
        smgr.add_scenario(self)

    def render(self, core):
        print "Rendering inside scenario"
        self.render_objs(core)

    def render_objs(self, core):
        print "Rendering visible objects!"
        for o in self.objects:
            o.render(core)
        pass
        #for each visible object, render.
