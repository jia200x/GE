
class SMGR():
    def __init__(self):
        self.objs = []
        self.current_scenario = None
        self.scenarios = []

    def render_objs(self, dev):
        pass
        #for each visible object, render.

    def add_scenario(self, scenario):
        self.scenarios.append(scenario)
        self.current_scenario = scenario


