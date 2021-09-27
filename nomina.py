class Nomina:
   
    def __init__(self,sueldo,he):
        self.__sueldo=sueldo
        self.__he=he
        self.__vhe=13000

    def descsalud(self):
        return self.__sueldo*0.04

    def descpension(self):
        return self.__sueldo*0.04

    def descuentoarl(self):
        return 5700    

    def calculohe(self):
        return self.__he*self.__vhe

    def total(self):
        return self.__sueldo-self.descuentonomina()

    def descuentonomina(self):
        return self.descsalud()+self.descpension()+self.descuentoarl()+self.calculohe()    


    def mostrar(self):
        print("*** Datos Empleados ***")
        print("Sueldo",self.__sueldo)
        print("Horas Extras",self.__he)
        print("******Descuentos Nomina***********")
        print("Pension: ",self.descpension())
        print("Salud ",self.descsalud())
        print("Arl ",self.descuentoarl())
        print("Total Descuento Nomina ",self.descuentonomina())
        print("Total ",self.total())
        
       
    