from Abstract_Pokemon import AbstractPokemon

class All_rounder_Pokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
       
        multiplier = 1 + (self.sp_atk_current + self.sp_def_current ) / 200

        return multiplier