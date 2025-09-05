from business_object.Attack.FixedDamageAttack import FixedDamageAttack
from business_object.pokemon.all_rounder_pokemon import All_rounder_Pokemon
from business_object.statistic import Statistic

class TestFixedDamageAttack:
    def test_fixedattack(self):
        # GIVEN

        Pikachu = All_rounder_Pokemon(stat_current=Statistic(sp_atk=100, sp_def=100))
        Roudoudou = All_rounder_Pokemon(stat_current=Statistic(sp_atk=100, sp_def=100))
        Eclair = FixedDamageAttack(power = 100, name = "Eclair")

        # WHEN
        damage = Eclair.compute_damage(Pikachu, Roudoudou)

        # THEN
        assert damage == 100


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])