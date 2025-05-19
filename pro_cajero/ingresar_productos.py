""" funcion para ingresar los productos, calcularlos y almacenarlos """

def enter_products():
    buying_data={}
    enter_details = True
    while enter_details:
        details = input("Presione 'A' para agregar un producto o 'Q' para salir.").upper()
        if details == "A":
            cantidad = int(input("Ingrese cantidad: "))
            producto = input("Ingrese producto: ")
            buying_data.update({producto:cantidad})
        elif details ==  "Q":
            enter_details = False
        else:
            print("Por favor seleccione la opción correcta.")
    return buying_data

def get_price(producto,cantidad):
        productos_data = {
        'Leche': 2,
        'Whisky': 40,
        'Yerba': 2,
        'Huevos': 1,
        'Laser': 25,
        'Sillon': 120,
        'Bicicleta': 200,
        'Guitarra': 750,
        'Espia': 2000,
        'Cocina': 600,
        'Heladera': 500
    }
        subtotal = productos_data[producto] * cantidad
        print(subtotal)
        
enter_products()

      
    
   