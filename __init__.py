from flask import (
    Flask,
    render_template_string,
    render_template,
    request,
    url_for,
    send_from_directory)
from math import floor, ceil
import json
import jinja2 as j2
import STATIC


class Skill(object):
    def __init__(self, skill, ability, PC):
        self.name = skill
        self.ability = ability
        self.proficiency = PC.skillProfs
        self.expertise = PC.expertises
        self.__calc(PC)

    def __calc(self, PC):
        if self.name in PC.skillProfs:
            scale = 1
            if self.name in PC.expertises:
                scale = 2
        else:
            scale = 0
        self.value = PC.stats[self.ability].mod() + (PC.profBonus() * scale)

    def update(self, PC):
        self.__calc(PC)


class Stat(object):
    __types = ('str', 'dex', 'con', 'int', 'wis', 'cha')
    __Proper = dict(zip(
        __types, 'Strength,Dexterity,Constitution,Intelligence,Wisdom,Charisma'.split(',')))

    def __init__(self, statType, value):
        if statType in self.__types:
            self.type = statType
            self.value = value

    def mod(self):
        return floor((self.value - 10) / 2)

    def __str__(self):
        return """{type}: {value} ({mod})""".format(
            type=self.__Proper[self.type],
            value=self.value,
            mod="+{}".format(self.mod) if self.mod > 0 else "{}".format(self.mod))

    def proper(self):
        return self.__Proper[self.type]

    def __repr__(self):
        return self.__str__()


class Character(object):
    _stats = ('str', 'dex', 'con', 'int', 'wis', 'cha')
    _skills = (
        ('Acrobatics', 'dex'),
        ('Animal Handling', 'wis'),
        ('Arcana', 'int'),
        ('Athletics', 'str'),
        ('Deception', 'cha'),
        ('History', 'int'),
        ('Insight', 'wis'),
        ('Intimidation', 'cha'),
        ('Investigation', 'int'),
        ('Medicine', 'wis'),
        ('Nature', 'int'),
        ('Perception', 'wis'),
        ('Performance', 'cha'),
        ('Persuasion', 'cha'),
        ('Religion', 'int'),
        ('Sleight of Hand', 'dex'),
        ('Stealth', 'dex'),
        ('Survival', 'wis'))

    def __init__(self):
        self.stats = dict(
            zip(self._stats, (Stat(stat, 0) for stat in self._stats)))
        self.skills = dict()

    def profBonus(self):
        return ceil(self.level / 4) + 1


app = Flask(__name__)


@app.route('/')
@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route("/characterSheet", methods=['POST'])
def characterSheet():
    PC = Character()
    PC.XP = 0
    PC.level = 1
    PC.name = request.form['pcName']
    PC.align = request.form['pcAlign']
    PC.deity = request.form['pcDeity']

    PC.skillProfs = dict(
        (skill, 1) for skill, _ in PC._skills if skill in (
            'Athletics', 'History', 'Perception', 'Persuasion'))
    PC.expertises = dict()

    PC.stats = dict((stat, Stat(stat, int(
        request.form['pc' + stat.capitalize()]))) for stat in PC._stats)

    PC.skills = dict()
    for skill, ability in PC._skills:
        PC.skills[skill] = Skill(skill, ability, PC)
    

    PC.race = {"name": 'Human', "size": "Medium"}
    PC.background = {'name': "Noble"}
    PC.sex = 'Female'
    PC.hair = 'Purple'
    PC.eye = 'Blue'
    PC.height = '''5'7"'''
    PC.weight = "150 lbs."
    PC.characterClass = {
        "name": 'Fighter 1',
        "hitdie": 'd10',
        "spellcastingAbility": "int"
    }
    PC.health = {
        'max': '12'
    }
    PC.attacks = [
        {"name": "Greataxe",
         "atk": "+5",
         "dmg": "1d12+3",
         "type": "S",
         "shortRange": "*",
         "longRange": "*"},
        {"name": "Javelin",
         "atk": "+5",
         "dmg": "1d6+3",
         "type": "P",
         "shortRange": "30",
         "longRange": "120"},
        {"name": "Dagger",
         "atk": "+5",
         "dmg": "1d4+3",
         "type": "Pf",
         "shortRange": "20",
         "longRange": "60"},
        {"name": "Sling",
         "atk": "-1",
         "dmg": "1d4-1",
         "type": "B",
         "shortRange": "30",
         "longRange": "120"},
    ]
    PC.AC = {
        "total": 17,
        "armor": 16,
        "shield": 0,
        "dex": 0,
        "class": 1
    }
    PC.spellDC = 8 + PC.profBonus() + \
        PC.stats[PC.characterClass['spellcastingAbility']].mod()
    PC.languages = "Common, Draconic, Dwarvish"
    PC.proficiencies = "All armor, shields, simple weapons, martial weapons, playing cards"
    PC.specAttacks = [
        "", "", "", "", ""
    ]
    PC.specDefenses = [
        "", "", "", ""
    ]
    PC.features = [
        {"lvl": "1",
         "name": "Second Wind",
         "effect": "You can use a bonus action to regain 1d10+{} HP".format(1),
         "time": "short rest"},
        {"lvl": "1",
         "name": "Fighting Style",
         "effect": "(Defense) - While wearing armor, you gain a +1 bonus to AC",
         "time": "-"
         }
    ]
    if len(PC.features) < 13:
        PC.features.extend("" for _ in range(12 - len(PC.features)))

    return render_template('characterSheet.html', PC=PC)


if __name__ == "__main__":
    app.run('127.0.0.1', '8000')
