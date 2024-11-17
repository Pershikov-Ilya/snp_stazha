def rps_game_winner(array=None):
    if array is None:
        array = [[], []]
    if array is None or len(array) != 2:
        raise ValueError("WrongNumberOfPlayersError")

    choices = {"P", "S", "R"}

    p1_name, p1_choice = array[0]
    p2_name, p2_choice = array[1]

    if (p1_choice not in choices) or (p2_choice not in choices):
        raise ValueError("NoSuchStrategyError")

    r = {
        "R": "S",
        "S": "P",
        "P": "R"
    }

    if p1_choice == p2_choice:
        print("choice:", p1_choice)
        return f"player1 {p1_choice}"
    elif r[p1_choice] == p2_choice:
        print("choice:", p1_choice)
        return f"{p1_name} {p1_choice}"
    elif r[p2_choice] == p1_choice:
        print("choice:", p2_choice)
        return f"{p2_name} {p2_choice}"


print(rps_game_winner([["player1", "P"], ["player2", "S"]]))
print(rps_game_winner([["player1", "P"], ["player2", "P"]]))