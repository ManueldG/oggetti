class Persona:
    def __init__(self, nome,cognome,anno,residenza):
        self.nome = nome
        self.cognome = cognome
        self.anno = anno
        self.residenza = residenza
    
    def ProfiloPersonale(self):
        return (f"{self.nome} {self.cognome} {self.anno} {self.residenza}")

    def __str__(self):
        return (f"{self.nome} {self.cognome}")


per = Persona("Manuel","della Gala",1980,"Cerveteri")
print(per.ProfiloPersonale())
print(per.__str__())