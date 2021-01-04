class CQueue:

    def __init__(self):
        self.sa=[]
        self.sb=[]


    def appendTail(self, value: int) -> None:
        self.sa.append(value)


    def deleteHead(self) -> int:
        if(self.sb):
            return self.sb.pop()
        elif(self.sa):
            while(self.sa):
                self.sb.append(self.sa.pop())
        else:
            return -1
        return self.sb.pop()