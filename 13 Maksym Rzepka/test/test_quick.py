import random
from timeit import timeit

listpos = [i for i in range(500)]
listposodw = [500 - i for i in range(1001)]
listrow = 500*[1]
listlos = random.sample(range(0, 500), 500)

t1_quick = timeit("sort.quicksort(listpos)", number=1000, globals=globals())/1000
t1_bubble = timeit("sort.bubblesort(listpos)", number=1000, globals=globals())/1000
t2_quick = timeit("sort.quicksort(listposodw)", number=1000, globals=globals())/1000
t2_bubble = timeit("sort.bubblesort(listposodw)", number=1000, globals=globals())/1000
t3_quick = timeit("sort.quicksort(listrow)", number=1000, globals=globals())/1000
t3_bubble = timeit("sort.bubblesort(listrow)", number=1000, globals=globals())/1000
t4_quick = timeit("sort.quicksort(listlos)", number=1000, globals=globals())/1000
t4_bubble = timeit("sort.bubblesort(listlos)", number=1000, globals=globals())/1000
print("t1_quick: ", t1_quick)
print("t1_bubble: ", t1_bubble)
print("t2_quick: ", t2_quick)
print("t2_bubble: ", t2_bubble)
print("t3_quick", t3_quick)
print("t3_bubble", t3_bubble)
print("t4_quick", t4_quick)
print("t4_bubble", t4_bubble)

