class baju:
   def __init__(self, inputnama_baju, inputmerek): 
       self.nama_baju = inputnama_baju
       self.merek = inputmerek
baju1 = baju("kemeja", "vans")
baju2 = baju("kaos", "Distro")

print(baju1.__dict__)