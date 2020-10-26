class Mercador():

    def __init__(self, cajas):
        self.cajas = []
        for _ in range(cajas):
            self.cajas.append(Caja())

    def avanzarTiempo(self, tiempo):
    
    def llegarCliente(self, cliente_id):
        for caja in self.cajas:


class Caja():

    def __init__(self):
        self.clientes = []
    
    def clienteCaja(self, cliente_id):
        if cliente_id in self.clientes:
            return cliente_id 
