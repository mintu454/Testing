import tracemalloc
import pandas as pd
import simpy
import time
import big_o
import random

data = []
def car(env):
    global data
    while True:
        #print('Start parking at %d' % env.now) #time of parking
        parking_duration = 5                   #duration to park a car
        yield env.timeout(parking_duration)
        #print('Start driving at %d' % env.now) #time of driving
        trip_duration = 2                       #duration of trip
        yield env.timeout(trip_duration)
    
def simulate(n):
        env = simpy.Environment()
        env.process(car(env))
        env.run(until=n)
        
best,others=big_o.big_o(simulate,big_o.datagen.n_,n_repeats=20,min_n=1,max_n=10000)
print(best)        
