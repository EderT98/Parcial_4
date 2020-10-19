class MyClass:
    def __init__(self, nro_identificacion, nombre_art, precio, pais, tipo_art, stock):
        self.nro_identificacion = nro_identificacion
        self.nombre_art = nombre_art
        self.precio = precio
        self.pais = pais
        self.tipo_art = tipo_art
        self.stock = stock


def to_string(obj):
    cd = 'Numero de articulo: {:<10}'.format(obj.nro_identificacion)
    cd += 'Nombre de articulo: {:<20}'.format(obj.nombre_art)
    cd += 'Precio: ${:<8}'.format(obj.precio)
    cd += 'Pais {:<2}'.format(obj.pais)
    cd += 'Tipo articulo: {:<2}'.format(obj.tipo_art)
    cd += 'Stock: {:<2}'.format(obj.stock)
    return cd
