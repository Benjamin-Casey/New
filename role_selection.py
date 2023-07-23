import random

ROLES_FIVE_PLAYERS = [
	"King",
	"Knight",
	"Assassin",
	"Assassin",
	"Renegade"
]

ROLES_SIX_PLAYERS = [
	"King",
	"Knight",
	"Assassin",
	"Assassin",
	"Bandit",
	"Bandit"
]

ROLES_SEVEN_PLAYERS = [
	"King",
	"Knight",
	"Assassin",
	"Assassin",
	"Bandit",
	"Bandit",
	"Renegade"
]

SUBROLES = {
	"King" 		: [ "The King" ],
	"Knight" 	: [ "The Field Marshal", 
					"The Kingslayer", 
					"The Knight in Shining Armor", 
					"The Queen", 
					"The Rightful Heir" ],
	"Assassin" 	: [ "The Bear Trainer",
					"The Marksman",
					"The Priestess",
					"The Schemer",
					"The Thief"] ,
	"Renegade" 	: [ "The Champion",
					"The Cultist",
					"The Mimic",
					"The Sellsword",
					"The Straw Man" ],
	"Bandit" 	: [ "The Giant",
					"The Necromancer",
					"The Stalker",
					"The Wizard",
					"The Zealot"]
}


"""
Randomise the list
Assign each player a role
Assign each player other than the king a subrole
"""

def player_roles(players):
	p = players
	random.shuffle(p)
	random_plist = p

	p_roles = {}
	
	if len(random_plist) == 5:
		for i in range(0, 5):
			role = ROLES_FIVE_PLAYERS[i]
			if i == 0:
				p_roles[random_plist[i]] = (role, SUBROLES[role][0])
			elif i == 3:
				p_roles[random_plist[i]] = (role, SUBROLES[role][random.randint(0,4)])
				while p_roles[random_plist[i]] == p_roles[random_plist[i-1]]:
					print("re-rolling")
					p_roles[random_plist[i]] = (role, SUBROLES[role][random.randint(0,4)])

			else:
				p_roles[random_plist[i]] = (role, SUBROLES[role][random.randint(0,4)])

	elif len(random_plist) == 6:
		for i in range(0, 6):
			role = ROLES_SIX_PLAYERS[i]
			if i == 0:
				p_roles[random_plist[i]] = (role, SUBROLES[role][0])
			elif i == 3:
				p_roles[random_plist[i]] = (role, SUBROLES[role][random.randint(0,4)])
				while p_roles[random_plist[i]] == p_roles[random_plist[i-1]]:
					print("re-rolling")
					p_roles[random_plist[i]] = (role, SUBROLES[role][random.randint(0,4)])
			elif i == 5:
				p_roles[random_plist[i]] = (role, SUBROLES[role][random.randint(0,4)])
				while p_roles[random_plist[i]] == p_roles[random_plist[i-1]]:
					print("re-rolling")
					p_roles[random_plist[i]] = (role, SUBROLES[role][random.randint(0,4)])
			else:
				p_roles[random_plist[i]] = (role, SUBROLES[role][random.randint(0,4)])
	
	return p_roles

# p = ["Ben", "Riley", "Tom", "Aden", "Daniel", "Fletcher"]
p = ["Ben", "Riley", "Tom", "Aden", "Daniel"]

print(player_roles(p))
