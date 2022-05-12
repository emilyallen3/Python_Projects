#Encapsulation Practice
#Emily Allen


class Protected:
    #This is a protected function
    def __init__(self):
        self._protectedVariable = 1
    #This is a private function
    def __init__(self):
        self.__privateVariable = 2

    def getPrivate(self):
        return self.__privateVariable

    def setPrivate(self,newPrivate):
        self.__privateVariable = newPrivate

#This object is protected
protectedObject = Protected()
protectedObject._protectedVariable = 3
print(protectedObject._protectedVariable)

#This object is private
privateObject = Protected()
privateObject.getPrivate()
privateObject.setPrivate(4)
privateObject.getPrivate()

X = protectedObject._protectedVariable
Y = privateObject.getPrivate()

print(X)
print(Y)

#This is a combination of a protected variable and a private variable
print(X+Y)



