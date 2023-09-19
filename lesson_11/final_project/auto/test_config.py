import configparser

def test_config():
    config = configparser.ConfigParser()
    config.sections()

    config.read("final_project/test_config.ini") 
    print(config.sections())

    config.sections()
    sA = config["sectionA"]["prop"]
    print(sA)

    config.sections()
    prop = config["sectionA"].get("prop") #str
    prop_int = config["sectionA"].getint("prop_int") #int
    print(prop_int / 1)

    config.sections()
    prop = config["sectionC"].getboolean("prop_bool") #boolean
    print(prop)