class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name

    def set_calories(self, calories):
        if isinstance(calories, (int, float)):
            self.calories = calories


    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories


    def is_healthy(self):
        return self.calories < 200

    @staticmethod
    def is_delicious():
        return True


class JellyBean(Dessert):
    def __init__(self, name, calories, flavor):
        super().__init__(name, calories)
        self.flavor = flavor


    def set_flavor(self, flavor):
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor


    def is_delicious(self):
        return self.flavor != "black licorice"


jb = JellyBean("JellyBean", 150, "black licorice")

print("вид сладости:", jb.get_name(), "\n",
      "сладость:", jb.get_flavor(), "\n",
      "калорийность:", jb.get_calories(), "\n",
      "полезно?:", jb.is_healthy(), "\n",
      "не 'black licorice':", jb.is_delicious())
