from swap_meet.item import Item
#wave 5
class Decor(Item):
    def __init__(self, category="Decor", condition=0.0):
        super().__init__(category)
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."
    
    
    def condition_description(self):
        return super().condition_description()