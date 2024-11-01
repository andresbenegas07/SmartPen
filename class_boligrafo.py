class Boligrafo:
    def __init__(self, grosor_punta, color):
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantidad_tinta = 80
    
    def escribir(self, texto):
        no_alcanza_tinta = "No alcanza la tinta"
        if self.grosor_punta == "Fino":
            if self.cantidad_tinta >= len(texto):
                self.cantidad_tinta -= len(texto)
                print(texto)
            else:
                if self.cantidad_tinta >= len(texto):
                    self.cantidad_tinta -= (texto * 2)
                    print(texto)
        else:
            return no_alcanza_tinta

    def recargar(self, ingreso_tinta):
        self.cantidad_tinta += ingreso_tinta 
        if self.cantidad_tinta > self.capacidad_tinta_maxima:
            sobrante = self.cantidad_tinta - self.capacidad_tinta_maxima
            self.capacidad_tinta_maxima = 100
            print(f"Se recargó la lapicera y sobró {sobrante}")
        else:
            print("Lapicera recargada")             

    
    def mostrar_cantidad_maxima_de_tinta(self):
        return self.capacidad_tinta_maxima
    
    def mostrar_grosor_punta(self):   
        return self.grosor_punta
    
    def mostrar_color(self):    
        return self.color

    def mostrar_cantidad_de_tinta(self):    
        return self.cantidad_tinta