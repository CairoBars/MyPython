#Author:Cairo Li
import threading
import time
class Singleton(object):#抽象单例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            print('cls:',cls)
            print('*args:',*args)
            print('**kwargs',**kwargs)
            orig=super(Singleton,cls)
            print(orig)
            cls._instance=orig.__new__(cls,*args,**kwargs)
        return cls._instance

class Bus(Singleton):
    lock=threading.RLock()
    def sendData(self,data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Singal Data...",data)
        self.lock.release()

#线程对象，为更加说明单例的含义,这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus=""
    name=""
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def run(self):
        self.my_bus=Bus()
        self.my_bus.sendData(self.name)

if __name__=="__main__":
    for i in range(3):
        print("Entity %d begin to run..."%i)
        my_entity=VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()


b=Bus()
c=Bus()

print(id(b))
print(id(c))