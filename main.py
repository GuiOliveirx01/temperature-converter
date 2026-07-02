units = {
    "1": ("°C", "°F"),
    "2": ("°C", "K"),
    "3": ("°F", "°C"),
    "4": ("°F", "K"),
    "5": ("K", "°C"),
    "6": ("K", "°F")
}

restart = "S"

while restart == "S":
    print("\n1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Celsius")
    print("6 - Kelvin para Fahrenheit")

    option = input("\nEscolha uma opção: ")

    if option not in units:
        print("\nOpção inválida.")
        continue
    else:
        while True:
            try:
                value = float(input("\nDigite a temperatura: "))
                break

            except ValueError:
                print("\nValor inválido.")

    source, target = units[option]

    formulas = {
        "1": value * 9 / 5 + 32,
        "2": value + 273.15,
        "3": (value - 32) * 5 / 9,
        "4": (value - 32) * 5 / 9 + 273.15,
        "5": value - 273.15,
        "6": (value - 273.15) * 9 / 5 + 32
    }

    result = formulas[option]

    print(f"\n{round(value, 2):g}{source} equivalem a {round(result, 2):g}{target}")

    restart = input("\nDeseja realizar outra conversão? (S/N) ").title()

    while True:
        if restart not in ("S", "N"):
            print("\nResposta inválida.")
            restart = input("\nDeseja realizar outra conversão? (S/N) ").title()
        else:
            break