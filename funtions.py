
import csv

def load_file(file_name: str) -> dict:
    heroes = {}

    with open(file_name, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for datos in reader:
            llave = datos["id"]

            heroes[llave] = {
                "name": datos["name"],
                "gender": datos["gender"],
                "eye_color": datos["eye_color"],
                "race": datos["race"],
                "hair_color": datos["hair_color"],
                "height": datos["height"],
                "publisher": datos["publisher"],
                "skin_color": datos["skin_color"],
                "alignment": datos["alignment"],
                "weight": datos["weight"],
            }

    return heroes
