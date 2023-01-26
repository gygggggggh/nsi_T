
class File:
    def __init__(self):
        self.file = []
        
    def __str__(self):
        txt = ""
        for i in self.file:
            txt += str(i) + " <- "
        return txt
    
    def est_vide(self):
        return self.file == []
    
    def enfiler(self, x):
        self.file.append(x)

    def defiler(self):
        if self.est_vide():
            raise MemoryError("File vide")
        return self.file.pop(0)
    
attente = File()
attente.enfiler("Jean")
attente.enfiler("Pierre")
print(attente)
attente.defiler()
print(attente)


