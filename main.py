def displayChoice(currentSelection, selectionChoiceDict):
    print("{}:".format(currentSelection['title']))
    choices = selectionChoiceDict['names']
    print("\n\t".join("{} - {}".format(n,v) for n,v in enumerate(choices)))

def QueryChoices(PC, selection):
    choices = db.query('select * from choice where selectionID=?', selection)
    filtered = list()
    for choice in choices:
        if choice.restrictions in PC.traits:
            continue
        else:
            filtered.append(choice)
    return filtered

def QuerySelections(selections):
    retrieved = list()
    for selection in selections:
        retrieved += db.query('select * from selection where selectionID=?',selection)
    return retrieved

def fillPC(PC):
    stack = list(SEL_BG,SEL_CLASS,SEL_RACE)
    while len(stack):
        curSel = stack.pop()
        selChoices = QueryChoices(PC,curSel)
        displayChoice(curSel,selChoices)
        choice = input("> ")
        choice = selChoices[choice]
        if 'subSelections' in choice.attribs:
            stack.extend(QuerySelections(choice.subSelections))
        PC.setChoice(choice)

        return PC
