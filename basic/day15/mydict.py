#Author:Cairo Li


class Config(dict):
    def __init__(self,defaults):
        print("gg")
        dict.__init__(self,defaults or {})


myconfig={'e':1,'ee':23}

cc=Config(myconfig)
cc['e']