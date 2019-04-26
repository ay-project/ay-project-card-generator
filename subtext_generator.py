#!/usr/bin/python3


def generate(abilities):
    subtext = ""
    battlecries=[]
    if "taunt" in abilities:
        subtext += "Taunt "

    if "battlecry" in abilities:
        subtext += "Battlecry: "
        battlecries = abilities['battlecry']

    for battlecry in battlecries:
        if battlecry["type"] == "charge":
            subtext += "Charge "
        elif battlecry["type"] == "heal":
            subtext += generate_healing(battlecry) 
        elif battlecry["type"] == "draw":
            subtext += generate_draw(battlecry) 
        elif battlecry["type"] == "dmg":
            subtext += generate_damage(battlecry) 
        elif battlecry["type"] == "bonus":
            subtext += generate_activated_bonus(battlecry) 
        
    if "bonus" in abilities:
        subtext += "Bonus: "
        subtext += generate_passive_bonus(abilities['bonus'])


    return subtext


def generate_healing(ability):
    subtext = "Heals"

    if "target" in ability:
        subtext += " {} for ".format(handle_target(ability['target']))
    else:
        subtext += " target for"
    
    subtext += " {} HP.".format(ability['potency'])
    return subtext

def generate_damage(ability):
    subtext = "Deals"

    subtext += " {} dammge to".format(ability['potency'])

    if "target" in ability:
        subtext += " {}".format(handle_target(ability['target']))
    else:
        subtext += " target."
    
    return subtext

def generate_draw(ability):
    subtext = ""
    subtext += "{} draws".format(handle_target(ability['target']))
    subtext += " {} cards.".format(ability['potency'])
    return subtext

def generate_attribute_bonus(bonus):
    subtext = ""
    if int(bonus['potency']) > 0:
        subtext += "Increases "
    elif int(bonus['potency']) < 0:
        subtext += "Decreases "

    if bonus['type'] == 'atk':
        subtext += "attack "
    elif bonus['type'] == 'hp':
        subtext += "HP "
    
    if "target" in bonus:
        subtext += "of {} ".format(handle_target(bonus['target']))
    else:
        subtext += "of target "
    
    subtext += "by {}.".format(bonus['potency'])

    return subtext

def generate_activated_bonus(ability):
    subtext = ""
    for bonus in ability['bonus']:
        subtext += generate_passive_bonus(bonus)
        if bonus != ability['bonus'][-1]:
            subtext += " and "

    if "target" in ability:
        subtext += "of {}.".format(handle_target(ability['target']))
    else:
        subtext += "of target."

    return subtext



def handle_target(target):
    return "something"