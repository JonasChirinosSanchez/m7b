def parse_student(x):
    student = {}

    student["id"] = int(x[0:8])

    student["name"] = x[8:-4]

    student["birthdate"] = x[4:-2] + "/" + x[-2:]

    return student

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
