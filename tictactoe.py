import random

#loserNumber will be 1 is player loses and 2 is AI loses. loserNumber will be 0 if its a tie
#gameEnd will be true when there is a three in a row. If the board fills up, win will also be true


loserNumber = 0
winCounterAI = 0
winCounterPL = 0
gameCount = 0
board = [['-','-','-'],['-','-','-'],['-','-','-']]
print("Tic-Tac-Toe vs a Computer")



def printBoard():
	for r in range (len(board)):
		print("  ", end="")
		for c in range(len(board[0])):	
			print(board[r][c],end="")
			if(c != 2):
				print("  |  ", end="")
		print()
		if(r!=2):
			print("------------------", end="")
		print()



def userInputx():
	print("Enter where you'd like to place your x. Enter the row and column index like: 00, 12, 21")
	A = input()
	A= str(A)
	X = int(A[0])
	Y = int(A[1])
	board[X][Y] = 'x'
	printBoard()



def userInputo():
	print("Enter where you'd like to place your o. Enter the row and column index like: 00, 12, 21")
	A = input()
	A= str(A)
	X = int(A[0])
	Y = int(A[1])
	board[X][Y] = 'o'
	printBoard()



def checkWin():
	global loserNumber
	global firstTurn
	global winCounterAI
	global winCounterPL
	global board
	
	bruh = "Its a tie!"
	heh = "Player wins!"
	heh2 = "AI wins!"
	count = 0

	#if its a tie:

	for r in range(len(board)):
		for c in range(len(board[r])):
			if(board[r][c] == '-'):
				continue
			else:
				count = count + 1
	if(count == 9):
		loserNumber = 0
		print(bruh)
		count = 0
		return 1
	else:
		count = 0
	

	#if the player using o wins:

	if(board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterAI+=1
			loserNumber = 1
			print(heh2)
			return 2
		elif(firstTurn==2):
			winCounterPL+=1
			loserNumber =2
			print(heh)
			return 2

	

	if(board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterAI+=1
			loserNumber = 1
			print(heh2)
			return 2
		elif(firstTurn==2):
			winCounterPL+=1
			loserNumber =2
			print(heh)
			return 2

	
	if(board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterAI+=1
			loserNumber = 1
			print(heh2)
			return 2
		elif(firstTurn==2):
			winCounterPL+=1
			loserNumber =2
			print(heh)
			return 2


	if(board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterAI+=1
			loserNumber = 1
			print(heh2)
			return 2
		elif(firstTurn==2):
			winCounterPL+=1
			loserNumber =2
			print(heh)
			return 2



	if(board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterAI+=1
			loserNumber = 1
			print(heh2)
			return 2
		elif(firstTurn==2):
			winCounterPL+=1
			loserNumber =2
			print(heh)
			return 2


	if(board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterAI+=1
			loserNumber = 1
			print(heh2)
			return 2
		elif(firstTurn==2):
			winCounterPL+=1
			loserNumber =2
			print(heh)
			return 2



	if(board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterAI+=1
			loserNumber = 1
			print(heh2)
			return 2
		elif(firstTurn==2):
			winCounterPL+=1
			loserNumber =2
			print(heh)
			return 2

	if(board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterAI+=1
			loserNumber = 1
			print(heh2)
			return 2
		elif(firstTurn==2):
			winCounterPL+=1
			loserNumber =2
			print(heh)
			return 2



	#if the player using x wins:

	if(board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterPL+=1
			loserNumber = 2
			print(heh)
			return 2
		elif(firstTurn==2):
			winCounterAI+=1
			loserNumber =1
			print(heh2)
			return 2
	


	if(board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterPL+=1
			loserNumber = 2
			print(heh)
			return 2
		elif(firstTurn==2):
			winCounterAI+=1
			loserNumber =1
			print(heh2)
			return 2
	

	if(board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterPL+=1
			loserNumber = 2
			print(heh)
			return 2
		elif(firstTurn==2):
			winCounterAI+=1
			loserNumber =1
			print(heh2)
			return 2

	
	if(board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterPL+=1
			loserNumber = 2
			print(heh)
			return 2
		elif(firstTurn==2):
			winCounterAI+=1
			loserNumber =1
			print(heh2)
			return 2

	if(board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterPL+=1
			loserNumber = 2
			print(heh)
			return 2
		elif(firstTurn==2):
			winCounterAI+=1
			loserNumber =1
			print(heh2)
			return 2

	
	if(board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterPL+=1
			loserNumber = 2
			print(heh)
			return 2
		elif(firstTurn==2):
			winCounterAI+=1
			loserNumber =1
			print(heh2)
			return 2


	if(board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterPL+=1
			loserNumber = 2
			print(heh)
			return 2
		elif(firstTurn==2):
			winCounterAI+=1
			loserNumber =1
			print(heh2)
			return 2



	if(board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x'):
		board = [['-','-','-'],['-','-','-'],['-','-','-']]
		if(firstTurn == 1):
			winCounterPL+=1
			loserNumber = 2
			print(heh)
			return 2
		elif(firstTurn==2):
			winCounterAI+=1
			loserNumber =1
			print(heh2)
			return 2

	return 0




def firstTurnFunc():
	global firstTurn
	global loserNumber
	global board

	print("New Game!")
	board = [['-','-','-'],['-','-','-'],['-','-','-']]
	printBoard()
	list1 = [1,2]
	firstTurn = random.choice(list1)
	
	if (loserNumber == 1 or loserNumber == 2):
		firstTurn = loserNumber


	if loserNumber == 1:	
		userInputx()
		return


	
	elif loserNumber ==2:
		board[1][1] = 'x'
		return

	if firstTurn == 1:
		userInputx()
		return

	elif firstTurn ==2:
		board[1][1] = 'x'
		return





def checkCornersForAIo():
	if(board[0][0] == 'x'):	
		if(board[2][0] == '-'):
			board[2][0] = 'o'
			return False
		elif(board[0][2] == '-'):
			board[0][2] = 'o'
			return False
		
	
	
	if(board[0][2] == 'x'):	
		if(board[0][0] == '-'):
			board[0][0] = 'o'
			return False
		elif(board[2][2] == '-'):
			board[2][2] = 'o'
			return False
		

	if(board[2][0] == 'x'):	
		if(board[2][2] == '-'):
			board[2][2] = 'o'
			return False
		elif(board[0][0] == '-'):
			board[0][0] = 'o'
			return False
		

	if(board[2][2] == 'x'):	
		if(board[2][0] == '-'):
			board[2][0] = 'o'
			return False
		elif(board[0][2] == '-'):
			board[0][2] = 'o'
			return False
		



	if(board[0][0] == 'o'):	
		if(board[2][0] == '-'):
			board[2][0] = 'o'
			return False
		elif(board[0][2] == '-'):
			board[0][2] = 'o'
			return False
			
	
	if(board[0][2] == 'o'):	
		if(board[0][0] == '-'):
			board[o][0] = 'o'
			return False
		elif(board[2][2] == '-'):
			board[2][2] = 'o'
			return False
		

	if(board[2][0] == 'o'):	
		if(board[2][2] == '-'):
			board[2][2] = 'o'
			return False
		elif(board[0][0] == '-'):
			board[0][0] = 'o'
			return False
		

	if(board[2][2] == 'o'):	
		if(board[2][0] == '-'):
			board[2][0] = 'o'
			return False
		elif(board[0][2] == '-'):
			board[0][2] = 'o'
			return False
		
	return True
	



def checkCornersForAIx():
	if(board[0][0] == 'o'):	
		if(board[2][0] == '-'):
			board[2][0] = 'x'
			return False
		elif(board[0][2] == '-'):
			board[0][2] = 'x'
			return False
			
	
	if(board[0][2] == 'o'):	
		if(board[0][0] == '-'):
			board[0][0] = 'x'
			return False
		elif(board[2][2] == '-'):
			board[2][2] = 'x'
			return False
		

	if(board[2][0] == 'o'):	
		if(board[2][2] == '-'):
			board[2][2] = 'x'
			return False
		elif(board[0][0] == '-'):
			board[0][0] = 'x'
			return False
		

	if(board[2][2] == 'o'):	
		if(board[2][0] == '-'):
			board[2][0] = 'x'
			return False
		elif(board[0][2] == '-'):
			board[0][2] = 'x'
			return False
		



	if(board[0][0] == 'x'):	
		if(board[2][0] == '-'):
			board[2][0] = 'x'
			return False
		elif(board[0][2] == '-'):
			board[0][2] = 'x'
			return False
			
	
	if(board[0][2] == 'x'):	
		if(board[0][0] == '-'):
			board[0][0] = 'x'
			return False
		elif(board[2][2] == '-'):
			board[2][2] = 'x'
			return False
		

	if(board[2][0] == 'x'):	
		if(board[2][2] == '-'):
			board[2][2] = 'x'
			return False
		elif(board[0][0] == '-'):
			board[0][0] = 'x'
			return False
		

	if(board[2][2] == 'x'):	
		if(board[2][0] == '-'):
			board[2][0] = 'x'
			return False
		elif(board[0][2] == '-'):
			board[0][2] = 'x'
			return False
		
	return True








def checkDPadForAIo():
	if(board[0][1] == 'x'):	
		if(board[1][0] == '-'):
			board[1][0] = 'o'
			return False
		elif(board[1][2] == '-'):
			board[1][2] = 'o'
			return False
			
	
	if(board[1][0] == 'x'):	
		if(board[0][1] == '-'):
			board[0][1] = 'o'
			return False
		elif(board[2][1] == '-'):
			board[2][1] = 'o'
			return False
		
	if(board[2][1] == 'x'):	
		if(board[1][0] == '-'):
			board[1][0] = 'o'
			return False
		elif(board[1][2] == '-'):
			board[1][2] = 'o'
			return False
		
	if(board[1][2] == 'x'):	
		if(board[0][1] == '-'):
			board[0][1] = 'o'
			return False
		elif(board[2][1] == '-'):
			board[2][1] = 'o'
			return False
		



	
	if(board[0][1] == 'o'):	
		if(board[1][0] == '-'):
			board[1][0] = 'o'
			return False
		elif(board[1][2] == '-'):
			board[1][2] = 'o'
			return False
			
	
	if(board[1][0] == 'o'):	
		if(board[0][1] == '-'):
			board[0][1] = 'o'
			return False
		elif(board[2][1] == '-'):
			board[2][1] = 'o'
			return False
		

	if(board[2][1] == 'o'):	
		if(board[1][0] == '-'):
			board[1][0] = 'o'
			return False
		elif(board[1][2] == '-'):
			board[1][2] = 'o'
			return False
		

	if(board[1][2] == 'o'):	
		if(board[0][1] == '-'):
			board[0][1] = 'o'
			return False
		elif(board[2][1] == '-'):
			board[2][1] = 'o'
			return False
		

	return True

	
	


def checkDPadForAIx():
	if(board[0][1] == 'o'):	
		if(board[1][0] == '-'):
			board[1][0] = 'x'
			return False
		elif(board[1][2] == '-'):
			board[1][2] = 'x'
			return False
			
	
	if(board[1][0] == 'o'):	
		if(board[0][1] == '-'):
			board[0][1] = 'x'
			return False
		elif(board[2][1] == '-'):
			board[2][1] = 'x'
			return False
		

	if(board[2][1] == 'o'):	
		if(board[1][0] == '-'):
			board[1][0] = 'x'
			return False
		elif(board[1][2] == '-'):
			board[1][2] = 'x'
			return False
		

	if(board[1][2] == 'o'):	
		if(board[0][1] == '-'):
			board[0][1] = 'x'
			return False
		elif(board[2][1] == '-'):
			board[2][1] = 'x'
			return False
		



	if(board[0][1] == 'x'):	
		if(board[1][0] == '-'):
			board[1][0] = 'x'
			return False
		elif(board[1][2] == '-'):
			board[1][2] = 'x'
			return False
			
	
	if(board[1][0] == 'x'):	
		if(board[0][1] == '-'):
			board[0][1] = 'x'
			return False
		elif(board[2][1] == '-'):
			board[2][1] = 'x'
			return False
		
	if(board[2][1] == 'x'):	
		if(board[1][0] == '-'):
			board[1][0] = 'x'
			return False
		elif(board[1][2] == '-'):
			board[1][2] = 'x'
			return False
		

	if(board[1][2] == 'x'):	
		if(board[0][1] == '-'):
			board[0][1] = 'x'
			return False
		elif(board[2][1] == '-'):
			board[2][1] = 'x'
			return False
		

	return True










while( winCounterPL !=3 or winCounterAI != 3):  

	if(winCounterPL == 3 or winCounterAI == 3):
		if(winCounterPL == 3):	
			print("Player won the match :0")
			exit()
		else:
			print("Easy mode AI won lol")
			exit()

	
		



	#start the game!!!!
	firstTurnFunc()





	#now do the next turns 


	#AI is on o (second)
	#player is on x (first)
	if firstTurn==1:	
		if (board[1][1] == 'x'):
			board[0][0]='o'
			printBoard()
			
			#turn 2
			userInputx()

			checkCornersForAIo()
			printBoard()
		


			#turn 3
			userInputx()
			if (checkWin() == 1 or checkWin()==2):
				continue
			

			#DO IT LIKE THIS FOR REST OF WHILE LOOP
			#checkCornersForAIo()
			if(checkCornersForAIo()):
				printBoard()
				checkDPadForAIo()
				printBoard()
			else:
				printBoard()
			if (checkWin() == 1 or checkWin()==2):
				continue




			#turn 4
			userInputx()
			if (checkWin() == 1 or checkWin()==2):
				continue

			
			#checkCornersForAIo()
			if(checkCornersForAIo()):
				printBoard()
				checkDPadForAIo()
				printBoard()
			else:
				printBoard()

			if (checkWin() == 1 or checkWin()==2):
				continue
			
			#turn 5
			userInputx()
			if (checkWin() == 1 or checkWin()==2):
				continue




			#checkCornersForAIo()
			if(checkCornersForAIo()):
				printBoard()
				checkDPadForAIo()
				printBoard()
			else:
				printBoard()

			if (checkWin() == 1 or checkWin()==2):
				continue



		
		else:
			board[1][1] = 'o'
			printBoard()
		
			#turn 2
			
			userInputx()
			
			#checkCornersForAIo()
			if(checkCornersForAIo()):
				printBoard()
				checkDPadForAIo()
				printBoard()
			else:
				printBoard()


		

			#turn 3
			userInputx()		
			if (checkWin() == 1 or checkWin()==2):
				continue


			#checkCornersForAIo()
			if(checkCornersForAIo()):
				printBoard()
				checkDPadForAIo()
				printBoard()
			else:
				printBoard()

			if (checkWin() == 1 or checkWin()==2):
				continue
		
		


			#turn 4
			userInputx()
			if (checkWin() == 1 or checkWin()==2):
				continue



			#checkCornersForAIo()
			if(checkCornersForAIo()):
				printBoard()
				checkDPadForAIo()
				printBoard()
			else:
				printBoard()

			if (checkWin() == 1 or checkWin()==2):
				continue


			
			#turn 5
			userInputx()
			if (checkWin() == 1 or checkWin()==2):
				continue



			#checkCornersForAIo()
			if(checkCornersForAIo()):
				printBoard()
				checkDPadForAIo()
				printBoard()
			else:
				printBoard()

			
			if (checkWin() == 1 or checkWin()==2):
				continue
	
		


	
	
	#AI is on x (first)
	#player is on o (second)
	if firstTurn ==2:
		printBoard()
		userInputo()
		
		#turn 2
		#checkCornersForAIx()
		if(checkCornersForAIx()):
			printBoard()
			checkDPadForAIx()
			printBoard()
		else:
			printBoard()


		
		userInputo()


		#turn 3
		#checkCornersForAIx()
		if(checkCornersForAIx()):
			printBoard()
			checkDPadForAIx()
			printBoard()
		else:
			printBoard()
		
		
		if (checkWin() == 1 or checkWin()==2):
			continue



		userInputo()
	
		if (checkWin() == 1 or checkWin()==2):
			continue

		
		#turn 4
		#checkCornersForAIx()
		if(checkCornersForAIx()):
			printBoard()
			checkDPadForAIx()
			printBoard()
		else:
			printBoard()

		
		if (checkWin() == 1 or checkWin()==2):
			continue


		userInputo()
		
		
		if (checkWin() == 1 or checkWin()==2):
			continue	


		#turn 5
		#checkCornersForAIx()
		if(checkCornersForAIx()):
			printBoard()
			checkDPadForAIx()
			printBoard()
		else:
			printBoard()

		
		if (checkWin() == 1 or checkWin()==2):
			continue


		userInputo()
		
		if (checkWin() == 1 or checkWin()==2):
			continue
		






exit()




















