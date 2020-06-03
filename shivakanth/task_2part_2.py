import tracemalloc
import pandas as pd
import simpy
import time
import random

data = []
def car(env, i):
    global data
    while True:
        #print('Start parking at %d' % env.now) #time of parking
        data.append([i, 'Park', env.now])
        parking_duration = 5                   #duration to park a car
        yield env.timeout(parking_duration)
        #print('Start driving at %d' % env.now) #time of driving
        data.append([i, 'drive', env.now])
        trip_duration = 2                       #duration of trip
        yield env.timeout(trip_duration)

        
times =[]        
mem_traces = []
for i in range(10, 1000, 10):
    tracemalloc.start()
    print("Running", i)
    
    start_time = time.time()
    env = simpy.Environment()
    env.process(car(env, i))
    mem_traces.append(tracemalloc.get_traced_memory())
    env.run(until=i)

    tracemalloc.stop()
    t1 = time.time()

    diff = t1 - start_time
    times.append(diff)
    
dataframe = pd.DataFrame(data, columns = ['loop', 'action', 'time'])
dataframe.to_csv("park_drive.csv")
