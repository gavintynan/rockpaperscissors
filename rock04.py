#By: Gavin Tynan

lowerList = 0
upperList = 2
listRPS = ["Rock","Paper","Scissors"]
round = 3
z = 0
rndCnt = 1
aWins = 0
bWins = 0
ties = 0
aGameWins = 0
bGameWins = 0
gameTies = 0

import random

print "*"*44
print
print "*                                          *"
print
print "*     Welcome to Rock, Paper, Scissors     *"
print
print "*                                          *"
print
print "*"*44

while rndCnt == 1:
	singleAWins = 0
	singleBWins = 0
	z = 0
	print "1) Play Rock, Paper, Scissors"
	print "2) Quit"
	rndCnt = input("Please enter a choice --> ")
	print
	if rndCnt == 1:
		round = input("Please enter a number of rounds -->")
		while z < round:
			z = z + 1
			indexA = random.randint(lowerList,upperList)
			indexB = random.randint(lowerList,upperList)
			studentA = listRPS[indexA]
			studentB = listRPS[indexB]
			print "Round " + str(z) + ": Student A throws " + str(studentA)
			print "Round " + str(z) + ": Student B throws " + str(studentB)
			if studentA == "Rock":
				if studentB == "Rock":
					print "The round is a tie"
					ties = ties + 1
				if studentB == "Paper":
					print "Student B wins the round"
					singleBWins = singleBWins + 1
					bWins = bWins + 1
				if studentB == "Scissors":
					print "Student A wins the round"
					singleAWins = singleAWins + 1
					aWins = aWins + 1
			if studentA == "Paper":
				if studentB == "Paper":
					print "The round is a tie"
					ties = ties + 1
				if studentB == "Rock":
					print "Student A wins the round"
					singleAWins = singleAWins + 1
					aWins = aWins + 1
				if studentB == "Scissors":
					print "Student B wins the round"
					singleBWins = singleBWins + 1
					bWins = bWins + 1
			if studentA == "Scissors":
				if studentB == "Scissors":
					print "The round is a tie"
					ties = ties + 1
				if studentB == "Rock":
					print "Student B wins the round"
					singleBWins = singleBWins + 1
					bWins = bWins + 1
				if studentB == "Paper":
					print "Student A wins the round"
					singleAWins = singleAWins + 1
					aWins = aWins + 1
			print
		if singleAWins > singleBWins:
			aGameWins = aGameWins + 1
		if singleBWins > singleAWins:
			bGameWins = bGameWins + 1
		if singleAWins == singleBWins:
			gameTies = gameTies + 1
print
print "	     	ROUND STATS			GAME STATS"
print "player   	 W	L	T	||	W	L	T"
print "-"*65
print "StudentA         " + str(aWins) + "      " + str(bWins) + "       " + str(ties) + \
"               " + str(aGameWins) + "       " + str(bGameWins) + "        " + str(gameTies)
print "StudentB         " + str(bWins) + "      " + str(aWins) + "       " + str(ties) + \
"               " + str(bGameWins) + "       " + str(aGameWins) + "        " + str(gameTies)	
