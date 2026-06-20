restart = "S"

while restart == "S":
    print("\n1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Celsius")
    print("6 - Kelvin para Fahrenheit")

    option = input("\nEscolha uma opção: ")

    if option not in ("1", "2", "3", "4", "5", "6"):
        print("\nOpção inválida.")
        continue
    else:
        while True:
            try:
                value = float(input("\nDigite a temperatura: "))
                break

            except ValueError:
                print("\nValor inválido.")

    if option == "1":
        result = value * 9 / 5 + 32
    elif option == "2":
        result = value + 273.15
    elif option == "3":
        result = (value - 32) * 5 / 9
    elif option == "4":
        result = (value - 32) * 5 / 9 + 273.15
    elif option == "5":
        result = value - 273.15
    elif option == "6":
        result = (value - 273.15) * 9 / 5 + 32

    if option == "1":
        print(f"\n{round(value, 2):g} °C equivalem a {round(result, 2):g} °F")
    elif option == "2":
        print(f"\n{round(value, 2):g} °C equivalem a {round(result, 2):g} K")
    elif option == "3":
        print(f"\n{round(value, 2):g} °F equivalem a {round(result, 2):g} °C")
    elif option == "4":
        print(f"\n{round(value, 2):g} °F equivalem a {round(result, 2):g} K")
    elif option == "5":
        print(f"\n{round(value, 2):g} K equivalem a {round(result, 2):g} °C")
    elif option == "6":
        print(f"\n{round(value, 2):g} K equivalem a {round(result, 2):g} °F")

    restart = input("\nDeseja realizar outra conversão? (S/N) ").title()

    while True:
        if restart not in ("S", "N"):
            print("\nResposta inválida.")
            restart = input("\nDeseja realizar outra conversão? (S/N) ").title()
        else:
            break