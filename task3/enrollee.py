class Enrollee:
    def __init__(self,name,russian,math,physics):
        self._name=name
        self._russian=russian
        self._math=math
        self._physics=physics

    @property
    def full_name(self):
        return self._name

    @property
    def russian(self):
        return self._russian

    @property
    def math(self):
        return self._math

    @property
    def physics(self):
        return self._physics
    def score_sum(self):
        return self.physics+self.math+self.russian
    def print_info(self):
        print("Полное имя:",self._name,",", "Русский:",self._russian,
              ",","Математика:",self._math,",","Физика:",self._physics,",","Сумма баллов",self.score_sum())
