# comptage parallèle 

import threading
import time

def hello(n):
    for i in range(5):
        print(f"je suis le thread {n} et je vaut {i}")
    print("fin du thread", n)

th = []
for n in range(4):
    t = threading.Thread(target=hello, args=[n])
    t.start()
    th.append(t)

for t in th:
    t.join()

print("fin du programme")

