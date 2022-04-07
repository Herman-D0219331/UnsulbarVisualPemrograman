#Class
class Petugas:
    
    jumlah_petugas = 0 #Variable
    
    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim
        Petugas.jumlah_petugas += 2
        
Asmawi = Petugas("Asamawi","D0219312")
Herman= Petugas("Herman","D0219331")

print(Petugas.jumlah_petugas)