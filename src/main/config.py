import yaml

class config_manager:
    
    def __init__(self):
        with open("project.yaml","r") as yamlFile:
            self.config = yaml.safe_load(yamlFile)

    def getConfig(self):
        return self.config
    
    def setConfig(self,newConfig):
        with open("project.yaml","w") as yamlFile:
            yaml.dump(newConfig, yamlFile, default_flow_style = False)