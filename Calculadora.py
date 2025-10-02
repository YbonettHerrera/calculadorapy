def mostrar_menu():
    print("\n" + "="*30)
    print("    CALCULADORA BÁSICA")
    print("="*30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("-"*30)

def obtener_numeros():
    """Se obtienen dos números del usuario"""
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        return num1, num2
    except ValueError:
        print(" Error: Por favor ingresa números válidos")
        return None, None

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return " Error: No se puede dividir por cero"
    return a / b

def main():
    print("¡Bienvenido a la Calculadora! ")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (1-5): ")
            
            if opcion == "5":
                print("\n¡Gracias por usar esta calculadora! ")
                break
            
            if opcion not in ["1", "2", "3", "4"]:
                print(" Opción no válida. Por favor selecciona 1-5.")
                continue
            
            # Obtener números para realizar la operaración
            num1, num2 = obtener_numeros()
            if num1 is None or num2 is None:
                continue
            
            # Realiza la operación
            if opcion == "1":
                resultado = sumar(num1, num2)
                operacion = "+"
            elif opcion == "2":
                resultado = restar(num1, num2)
                operacion = "-"
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                operacion = "×"
            elif opcion == "4":
                resultado = dividir(num1, num2)
                operacion = "÷"
            
            # Muestra el resultado
            print(f"\n Resultado: {num1} {operacion} {num2} = {resultado}")
            
            # Pregunta si quiere continuar con otra operación
            continuar = input("\n¿Quieres hacer otra operación? (s/n): ").lower()
            if continuar != 's' and continuar != 'si':
                print("\n¡Gracias! ")
                break
                
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! ")
            break
        except Exception as e:
            print(f" Error inesperado: {e}")

if __name__ == "__main__":
    main()