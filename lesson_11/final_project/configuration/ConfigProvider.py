import configparser

global_config = configparser.ConfigParser()
print("обратились к файловой системе")
global_config.read("final_project/test_config.ini") 
        

class ConfigProvider:
    def __init__(self) -> None:
        self.config = global_config       
        
    #Можно делать общие методы
    def get(self, sections:str, prop: str):
       return self.config[sections].get(prop)
    
    def getint(self, sections:str, prop: str):
       return self.config[sections].getint(prop)
    
    #Можно делать специфичные методы
    def get_ui_url(self):
       return self.config["ui"].get("base_url")