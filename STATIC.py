SCORES = {
    'cha': {'name': 'Charisma', 'score': 'cha'},
    'con': {'name': 'Constitution', 'score': 'con'},
    'dex': {'name': 'Dexterity', 'score': 'dex'},
    'int': {'name': 'Intelligence', 'score': 'int'},
    'str': {'name': 'Strength', 'score': 'str'},
    'wis': {'name': 'Wisdom', 'score': 'wis'}
}


SKILLS = {
    'arco': {'name': 'Acrobatics', 'score': 'dex'},
    'anih': {'name': 'Animal Handling', 'score': 'wis'},
    'cana': {'name': 'Arcana', 'score': 'int'},
    'athl': {'name': 'Athletics', 'score': 'str'},
    'decp': {'name': 'Deception', 'score': 'cha'},
    'hist': {'name': 'History', 'score': 'int'},
    'insi': {'name': 'Insight', 'score': 'wis'},
    'inti': {'name': 'Intimidation', 'score': 'cha'},
    'inve': {'name': 'Investigation', 'score': 'int'},
    'medi': {'name': 'Medicine', 'score': 'wis'},
    'nat': {'name': 'Nature', 'score': 'int'},
    'prcp': {'name': 'Perception', 'score': 'wis'},
    'perf': {'name': 'Performance', 'score': 'cha'},
    'pers': {'name': 'Persuasion', 'score': 'cha'},
    'reli': {'name': 'Religion', 'score': 'int'},
    'sloh': {'name': 'Sleight of Hand', 'score': 'dex'},
    'stea': {'name': 'Stealth', 'score': 'dex'},
    'surv': {'name': 'Survival', 'score': 'wis'}
}


ALIGNMENTS = {
    'CE': {'abrv': 'CE', 'name': 'Chaotic Evil'},
    'CG': {'abrv': 'CG', 'name': 'Chaotic Good'},
    'CN': {'abrv': 'CN', 'name': 'Chaotic Neutral'},
    'LE': {'abrv': 'LE', 'name': 'Lawful Evil'},
    'LG': {'abrv': 'LG', 'name': 'Lawful Good'},
    'LN': {'abrv': 'LN', 'name': 'Lawful Neutral'},
    'NE': {'abrv': 'NE', 'name': 'Neutral Evil'},
    'NG': {'abrv': 'NG', 'name': 'Neutral Good'},
    'TN': {'abrv': 'TN', 'name': 'True Neutral'}
}

CLASSES = {
    'brb': {'abrv': 'brb', 'name': 'Barbarian', 'saves':['str','con']},
    'bar': {'abrv': 'bar', 'name': 'Bard', 'saves':['dex','cha']},
    'clc': {'abrv': 'clc', 'name': 'Cleric', 'saves':['wis','cha']},
    'dri': {'abrv': 'dri', 'name': 'Druid', 'saves':['int','wis']},
    'fgt': {'abrv': 'fgt', 'name': 'Figher', 'saves':['str','con']},
    'mnk': {'abrv': 'mnk', 'name': 'Monk', 'saves':['str','dex']},
    'pdn': {'abrv': 'pdn', 'name': 'Paladin', 'saves':['wis','cha']},
    'rgr': {'abrv': 'rgr', 'name': 'Ranger', 'saves':['str','dex']},
    'rog': {'abrv': 'rog', 'name': 'Rogue', 'saves':['dex','int']},
    'sor': {'abrv': 'sor', 'name': 'Sorcerer', 'saves':['con','cha']},
    'lok': {'abrv': 'lok', 'name': 'Warlock', 'saves':['wis','cha']},
    'wiz': {'abrv': 'wiz', 'name': 'Wizard', 'saves':['int','wis']}
}
