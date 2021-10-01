import copy
#Imaginary Numbers
class imaginaryNumbers:
    pass


nu = imaginaryNumbers()
nu.real = 10
nu.im = 20

nu1 = copy.deepcopy(nu)

print(nu1.real, nu1.im)


#Time Class

class Time:
    pass
def printTime(t):
    print(str(t.hours)+":"+str(t.minutes)+":"+str(t.seconds))
time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30


def increment(time, seconds):
    time.seconds = time.seconds + seconds
    while time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1
    while time.minutes >= 60:
        time.minutes = time.minutes - 60
        time.hours = time.hours + 1

printTime(time)
increment(time,31)
printTime(time)


def convertToSeconds(t):
    minutes = t.hours * 60 + t.minutes
    seconds = minutes * 60 + t.seconds
    return seconds

def makeTime(seconds):
    time = Time()
    time.hours = seconds // 3600
    time.minutes = (seconds%3600) // 60
    time.seconds = seconds%60
    return time


def IncrementUsingSeconds(time, inc):
    t = convertToSeconds(time) + inc
    r = makeTime(t)
    return r

ttts = IncrementUsingSeconds(time,40)
printTime(ttts)