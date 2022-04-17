from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        _pokemon_name_list = [pokemon.name for pokemon in self.pokemon]
        if pokemon_name in _pokemon_name_list:
            self.pokemon.pop(_pokemon_name_list.index(pokemon_name))
            return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        _trainer_info = [f"Pokemon Trainer {self.name}",
                         f"Pokemon count {len(self.pokemon)}"]
        _pokemon_info = [f"- {pokemon.pokemon_details()}" for pokemon in self.pokemon]
        return '\n'.join(_trainer_info + _pokemon_info)


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
