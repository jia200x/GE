
class SMGR():
    def __init__(self, core):
        self.objs = []
        self.current_scenario = None
        self.scenarios = []
        self.core = None


    def add_scenario(self, scenario):
        self.scenarios.append(scenario)
        self.current_scenario = scenario

    def process(self):
        print "Processing!"
    def render(self):
        self.current_scenario.render(self.core)


