
import math


class Attributes:

    def abilitymod(self, abilityscore):
        self.modifier = math.trunc((abilityscore / 2) - 5)
        return self.modifier


toon = Attributes()
testabilities = {
    'Strength': 15,
    'Dexterity': 11,
    'Constitution': 12,
    'Intelligence': 13,
    'Wisdom': 14,
    'Charisma': 18,
}
toonMods = []
for abilities in testabilities.values():
    toonMods.append(toon.abilitymod(abilities))

print("Ability = \tScore \t(Modifier)")
print('STR \t= \t', testabilities['Strength'], "\t  (", toonMods[0], ")")
print('DEX \t= \t', testabilities['Dexterity'], "\t  (", toonMods[1], ")")
print('CON \t= \t', testabilities['Constitution'], "\t  (", toonMods[2], ")")
print('INT \t= \t', testabilities['Intelligence'], "\t  (", toonMods[3], ")")
print('WIS \t= \t', testabilities['Wisdom'], "\t  (", toonMods[4], ")")
print('CON \t= \t', testabilities['Charisma'], "\t  (", toonMods[5], ")")
