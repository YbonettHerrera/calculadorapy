def mostrar_menu():
    print("\n" + "="*30)
    print("    CALCULADORA BÁSICA")
    print("="*30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Elevar al cubo")
    print("6. Salir")
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

def obtener_un_numero():
    """Obtiene un número del usuario"""
    try:
        num = float(input("Ingrese el número: "))
        return num
    except ValueError:
        print(" Error: Por favor ingresa números válidos")
        return None

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

def elevar_al_cubo(a):
    """Eleva un número al cubo (a la potencia 3)"""
    return a ** 3

def main():
    print("¡Bienvenido a la Calculadora! ")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (1-6): ")
            
            if opcion == "6":
                print("\n¡Gracias! ")
                break
            
            if opcion not in ["1", "2", "3", "4", "5"]:
                
                continue
            
            # Realizar operación
            if opcion == "5":
                # Para elevar al cubo solo se necesita un número
                num = obtener_un_numero()
                if num is None:
                    continue
                resultado = elevar_al_cubo(num)
                print(f"\n Resultado: {num}³ = {resultado}")
            else:
                # Para las demás operaciones se necesitan dos números
                num1, num2 = obtener_numeros()
                if num1 is None or num2 is None:
                    continue
                
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
                
                # Muesta el resultado
                print(f"\n Resultado: {num1} {operacion} {num2} = {resultado}")
            
            # Preguntar si quiere continuar con otra operación
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