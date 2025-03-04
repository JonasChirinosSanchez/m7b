def parse_student(input):
    list_input = list(input)

    id_input = list_input[0:8]

    name_input = list_input[8:-4]

    birthday_input = list_input[-4:]

    dict_input = {"id": "".join(id_input),
                  "name":"".join(name_input),
                  "birthday":"".join(birthday_input[0:2]) + "/" + "".join(birthday_input[2:])}
    return dict_input


def count_items(it):
    it_counts = {}

    for item in it:
        if item not in it_counts:
            it_counts[item] = it.count(item)

    return it_counts


def list_fighters(data):
    names = set()

    for key in data:
        names.add(key)
        names.update(data[key].get("loss"))
        names.update(data[key].get("win"))

    new_list = list(names)
    new_list.sort()

    return new_list

battle_data = {
    "Trisharp": {
        "loss": ["Togehug", "Psygoose"],
        "win": ["Pikaju", "Bulbizard"],
    },
    "Infernchimp": {
        "loss": ["Togehug", "Pikaju"],
        "win": ["Bulbizard", "Tehog"],
    },
    "Tehog": {
        "loss": ["Togehug", "Charasaur"],
        "win": ["Bulbizard", "Pikaju"]
    },
    "Psygoose": {
        "loss": ["Togehug", "Pikaju"],
        "win": ["Bulbizard", "Infernchimp"]
    },
}


print(list_fighters(battle_data))
