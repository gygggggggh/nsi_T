# compteur global partagé par les threads

import threading
cpt = 0
def incr():
    global cpt
    for i in range(10000):
        v = cpt
        cpt = v + 1

th = []
for n in range(4):
    t = threading.Thread(target=incr)
    t.start()
    th.append(t)

for t in th:
    t.join()

print(cpt)