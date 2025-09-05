from business_object.pokemon.attacker_pokemon import Attacker_Pokemon
from business_object.statistic import Statistic

class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        Pikachu = Attacker_Pokemon(stat_current=Statistic(attack=100, speed=100))

        # WHEN
        multiplier = Pikachu.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])