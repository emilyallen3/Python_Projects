#Abstrsaction Practice
#Emily Allen
#Python Version 3.10.4

from abc import ABC, abstractmethod
#This is the parent class and it contains one regular and one abstract method
class music(ABC):
    def getArtist(self, artist):
        print("The song's artist is", artist)
    @abstractmethod
    def singer(self, artist):
        pass

#This is the child class that defines the implementation of it's parent's abstract method
class musicGroup(music):
    def singer(self, artist):
        print("{} has a female singer.".format(artist))

#This is an object of the child class
obj = musicGroup()

#The child class object is using a parent class method
obj.getArtist('Paramore')

#The child class object is using the parent class abstract method that was defined in the child class
obj.singer('Paramore')