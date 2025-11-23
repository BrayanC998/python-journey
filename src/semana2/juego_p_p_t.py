def rps(player1, player2):
    # Empate
    if player1 == player2:
        return "Draw!"

    # Casos donde gana Player 1
    if (
        (player1 == "piedra" and player2 == "tijeras")
        or (player1 == "tijeras" and player2 == "papel")
        or (player1 == "papel" and player2 == "piedra")
    ):
        return "Player 1 won!"

    # Si no es empate ni gana el jugador 1 → gana el jugador 2
    return "Player 2 won!"
