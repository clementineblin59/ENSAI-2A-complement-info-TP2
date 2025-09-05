from business_object.pokemon.Abstract_Pokemon import AbstractPokemon

class Defender_Pokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
       
        multiplier = 1 + (self.attack_current + self.defense_current) / 200

        return multiplier