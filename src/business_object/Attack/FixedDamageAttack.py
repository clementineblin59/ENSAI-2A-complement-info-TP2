from business_object.Attack.Abstract_Attack import AbstractAttack

class FixedDamageAttack(AbstractAttack):
    def compute_damage(self,APkm,DPkm):
        return self._power