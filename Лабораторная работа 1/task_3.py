list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_player = int(len(list_players) // 2)

team_one = list_players[:middle_player]
team_two = list_players[middle_player:]

print(team_one)
print(team_two)