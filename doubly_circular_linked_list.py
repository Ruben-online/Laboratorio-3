from node import Node
from math import isqrt


class DoublyCircularLinkedList:

    def __init__(self, initial, limit):
        self.head = Node(initial)
        current = self.head
        for num in range(initial + 1, limit + 1):
            new_node = Node(num)
            new_node.prev = current
            current.next = new_node
            current = new_node
        current.next = self.head
        self.head.prev = current

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    def identify_primes(self, circular_list):
        current = circular_list.head
        while True:
            if self.is_prime(current.value):
                current.is_prime = True
            else:
                current.is_prime = False
            current = current.next
            if current == circular_list.head:
                break

    def take_turn(self, player, circular_list):
        current = circular_list.head
        while True:
            if current.is_prime:
                current.is_prime = False
                break
            current = current.next
            if current == circular_list.head:
                break

    def game_over(self, circular_list):
        current = circular_list.head
        while True:
            if current.is_prime:
                return False
            current = current.next
            if current == circular_list.head:
                break
        return True

    def play(self):
        initial_number = int(input("Ingrese el número inicial: "))
        upper_limit = int(input("Ingrese el límite superior: "))

        circular_list = DoublyCircularLinkedList(initial_number, upper_limit)
        self.identify_primes(circular_list)

        player1 = "Jugador 1"
        player2 = "Jugador 2"

        while not self.game_over(circular_list):
            self.take_turn(player1, circular_list)
            if self.game_over(circular_list):
                break  # Salir del bucle si el jugador 1 ha ganado
            self.take_turn(player2, circular_list)

        print(f"{player1} es el ganador.")
