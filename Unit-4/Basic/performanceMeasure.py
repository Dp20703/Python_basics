#using time module:
import time

#starting time:
start=time.time()

#program body starts
for i in range(5):
    print(i)

#sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

#program body ends

#end time:
end=time.time()

#total time taken
print("Runtime of the program is:" + str(end-start))


# ...........................................................................#

#using time module:
import timeit

setup_code="from math import factorial"
statement="""for i in range (5):
                factorial(i)
"""

print('Execution time is:'+str(timeit.timeit(setup=setup_code,stmt=statement,number=10000000)))
