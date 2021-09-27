class Camisa:
    __talla=""
    __precio=0
    __color=""
    __marca=""
    '''
    constructor de la Clase Camisa
    '''
    def __init__(self,talla,precio,color,marca):
        self.__talla=talla
        self.__precio=precio
        self.__color=color
        self.__marca=marca

    '''
    Metodo Mostrar
    '''
    def mostrar(self):
        print("Datos de Camisa")
        print("Talla ",self.__talla)
        print("Precio",self.__precio)
        print("Color",self.__color)
        print("Marca",self.__marca)

