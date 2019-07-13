from time import sleep
import datetime

class Clock(object):
    def __init__(self,hour = 0, minute = 0 ,second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    def show(self):
        return  '%02d:%02d:%02d' %(self.hour, self.minute, self.second)

ISOTIMEFORMAT = '%H:%M:%S'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime)
H,M,S = theTime.split(':')
clock = Clock(int(H),int(M),int(S))
while True:
    print(clock.show())
    sleep(1)
    clock.run()
