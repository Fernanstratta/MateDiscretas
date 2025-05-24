def cifrado_cesar(texto: str, desplazamiento: int) -> str:
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():  # solo letras
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_codigo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo_codigo)
        else:
            resultado += caracter

    return resultado


def descifrar_cesar(texto: str, desplazamiento: int) -> str:
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():  # Solo letras
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_codigo = (ord(caracter) - base - desplazamiento) % 26 + base
            resultado += chr(nuevo_codigo)
        else:
            resultado += caracter

    return resultado


if __name__ == "__main__":
    try:
        print("¿Qué te gustaría hacer?")
        print("1. Cifrar texto")
        print("2. Descifrar texto")

        respuesta = None
        while respuesta not in [1, 2]:
            try:
                respuesta = int(input("Elige 1 o 2: "))
                if respuesta not in [1, 2]:
                    print("Por favor, ingresa 1 o 2.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

        while True:
            try:
                desplazamiento = int(input("Ingresa el desplazamiento: "))
                break
            except ValueError:
                print("Por favor, ingresa un número entero.")

        texto = input("Ingresa el texto: ")

        if respuesta == 1:
            print("Texto cifrado: " + cifrado_cesar(texto, desplazamiento))
        else:
            print("Texto descifrado: " + descifrar_cesar(texto, desplazamiento))

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
