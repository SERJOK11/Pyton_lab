def find_common_participants(first_group, second_group, separator=','):
    participants_first = set(first_group.split(separator))
    participants_second = set(second_group.split(separator))

    common_participants = list(participants_first.intersection(participants_second))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print(participants)
