class Allergies:

    def __init__(self, score):
        self.score = score & 255
        self.allergies = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8, 
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }

    def allergic_to(self, item):
        return bool(self.score & self.allergies[item])

    @property
    def lst(self):
        return [i for i, k in self.allergies.items() if self.score & k]

"""
0001 = 1
0010 = 2
0011 = 3
0100 = 4
0101 = 5
0110 = 6
0111 = 7
1000 = 8

for each existing allergy:
    - Check if the score has the allergy

"""