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

class Sviluppatore(Persona):
    def __init__(self,nome,cognome,anno,residenza,posizione,pagaAnnua):
        super().__init__(nome,cognome,anno,residenza)
        self.posizione = posizione
        self.pagaAnnua = pagaAnnua

    def ProfiloPersonale(self):
        return (f"{self.posizione} {self.pagaAnnua}")

    def __str__(self):
        
        return (f"{self.posizione} {self.nome} {self.cognome}")


per = Persona("Manuel","della Gala",1980,"Cerveteri")
print(per.ProfiloPersonale())
print(per.__str__())

svi = Sviluppatore("Manuel","della Gala",1980,"Cerveteri","FullStack",20000)
print(svi.ProfiloPersonale())
print(svi.__str__())
