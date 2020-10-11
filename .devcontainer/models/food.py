
class Food:

    def __init__(self, name, category, sub_category, recipe):
        self.name = name
        self.category = category
        self.sub_category = sub_category
        self.recipe = recipe
    
    def __str__(self):
        return f'"{self.name}" classified in {self.sub_category}, {self.category}'