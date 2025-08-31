# Patrón Singleton - Contador Global
# Archivo: singleton_contador.py

class ContadorGlobal:
    _instancia = None
    _inicializado = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ContadorGlobal, cls).__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not ContadorGlobal._inicializado:
            self.valor = 0
            ContadorGlobal._inicializado = True
    
    def incrementar(self):
        self.valor += 1
        return self.valor
    
    def decrementar(self):
        self.valor -= 1
        return self.valor
    
    def obtener_valor(self):
        return self.valor
    
    def resetear(self):
        self.valor = 0
        return self.valor
    
    def __str__(self):
        return f"Contador: {self.valor}"

# Función de demostración
def main():
    print("=== Demostración Patrón Singleton ===")
    
    # Crear primera instancia
    contador1 = ContadorGlobal()
    print(f"Contador1 inicial: {contador1}")
    
    # Incrementar desde contador1
    contador1.incrementar()
    contador1.incrementar()
    contador1.incrementar()
    print(f"Después de 3 incrementos: {contador1}")
    
    # Crear segunda "instancia" (en realidad es la misma)
    contador2 = ContadorGlobal()
    print(f"Contador2 (misma instancia): {contador2}")
    
    # Verificar que son la misma instancia
    print(f"¿Son la misma instancia? {contador1 is contador2}")
    
    # Modificar desde contador2
    contador2.decrementar()
    print(f"Después de decrementar desde contador2: {contador1}")
    
    # Demostrar que el cambio se refleja en ambas referencias
    print(f"Valor en contador1: {contador1.obtener_valor()}")
    print(f"Valor en contador2: {contador2.obtener_valor()}")
    
    # Resetear contador
    contador1.resetear()
    print(f"Después de resetear: {contador2}")

if __name__ == "__main__":
    main()