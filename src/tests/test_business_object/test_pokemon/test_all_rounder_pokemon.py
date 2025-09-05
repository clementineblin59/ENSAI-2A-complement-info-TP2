from business_object.pokemon.all_rounder_pokemon import All_rounder_Pokemon
from business_object.statistic import Statistic


class TestAll_rounder:
    def test_get_coef_damage_type(self):
        # GIVEN
        Pikachu = All_rounder_Pokemon(stat_current=Statistic(sp_atk=100, sp_def=100))

        # WHEN
        multiplier = Pikachu.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])