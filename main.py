from doubly_circular_linked_list import DoublyCircularLinkedList


while True:
    title = "Menu principal"
    print(title + "\n" + len(title) * '-')
    print("1. Juego eliminacion de numeros primos")
    print("2. Juego eliminacion de multiplos")
    print("3. Salir del programa")

    main_menu = input("Ingrese una opcion: ")

    if main_menu == "1":
        while True:
            title_game1 = "'Eliminacion de numeros primos'"
            print(title_game1 + "\n" + len(title_game1) * '-')
            print("1. Creacion de la lista")
            print("2. Identificacion de numeros primos")
            print("3. Turno de los jugadores")
            print("4. Finalizacion del juego")
            print("5. Volver al menu principal")

            game1_menu = input("Ingrese una opcion: ")

            if game1_menu == "1":
                initial_number = int(input("Ingrese el número inicial: "))
                upper_limit = int(input("Ingrese el límite superior: "))
                circular_list = DoublyCircularLinkedList(initial_number, upper_limit)
                print("Lista creada.")

            elif game1_menu == "2":
                circular_list.identify_primes()
                print("Números primos identificados.")

            elif game1_menu == "3":
                player = input("Ingrese el nombre del jugador: ")
                circular_list.take_turn(player)
                if circular_list.game_over():
                    print(f"{player} ha ganado.")
                    break

            elif game1_menu == "4":
                if game_over(circular_list):
                    print("El juego ya ha finalizado.")
                else:
                    print("Finalizando el juego...")
                    break

            elif game1_menu == "5":
                break

            else:
                print("Ingrese una opcion valida")


    elif main_menu == "2":
        while True:
            title_game2 = "'Eliminacion de multiplos'"
            print(title_game2 + "\n" + len(title_game2) * '-')
            print("1. Creacion de la lista")
            print("2. Eleccion del numero base")
            print("3. Turno de los jugadores")
            print("4. Identificacion de multiplos")
            print("5. Finalizacion del juego")
            print("6. Volver al menu principal")

            game2_menu = input("Ingrese una opcion: ")

            if game2_menu == "1":
                pass

            elif game2_menu == "2":
                pass

            elif game2_menu == "3":
                pass

            elif game2_menu == "4":
                pass

            elif game2_menu == "5":
                pass

            elif game2_menu == "6":
                break

            else:
                print("Ingrese una opcion valida")

    elif main_menu == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Ingrese una opcion valida ")