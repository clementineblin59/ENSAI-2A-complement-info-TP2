from Abstract_Pokemon import AbstractPokemon

class Attacker_Pokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
       
        multiplier = 1 + (self.speed_current + self.attack_current) / 200

        return multiplier