class timer:
    def __init__(self,name='none' ,beg = 100.0,end= 0.0 ,rate = 5.0)
        self.name = name
        self.begAt = beg# start condition of the timer
        self.timer = beg # timer
        self.endAt = end # end condition of the timer
        self.rate = rate # rate of change of timer
    def update(self):
        self.timer -= self.rate
        self.checkEnd()
    def checkEnd(self):
        if self.timer<- self.endAt:
            self.timer = self.endAt
    def beginTimer(self,name='none' ,beg = 100.0,end= 0.0 ,rate = 5.0):
        self.name = name
        self.begAt = beg# start condition of the timer
        self.timer = beg # timer
        self.endAt = end # end condition of the timer
        self.rate = rate # rate of change of timer
    def setEnd(self,end):
        self.endAt = end
    def begAt(self,end):
        self.endAt = end
