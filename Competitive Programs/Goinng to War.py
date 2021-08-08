NCARDS = 52 #Number of cards
NSUITS = 4   #Number of suits

#defining values and suits
values = "23456789TJQKA"
suits = "cdhs"


MAXSTEPS = 500

def value(n):
  return values.index(values[n//NSUITS])

def war(deck1, deck2):
  inwar = False         
  war_queue = list()   
  steps = 0             
  
  while len(deck1) != 0 and len(deck2) != 0 and steps <= MAXSTEPS:
    steps += 1
    x = deck1.pop()
    y = deck2.pop()
    war_queue.extend([x, y])
    
    if inwar:
      inwar = False
    else:
      if value(x) > value(y):
        deck1.extend(war_queue)
        war_queue.clear()
      elif value(x) < value(y):
        deck2.extend(war_queue)
        war_queue.clear()
      else:
        inwar = True
  

  if len(deck1) != 0 and len(deck2) == 0:
    print("deck1 wins in", steps, "steps")
  elif len(deck1) == 0 and len(deck2) != 0:
    print("deck2 wins in", steps, "steps")
  else:
    print("Game tied after", steps)
  
        
def rank_card(value, suit):
  try:
    i = values.index(value) 
    j = suits.index(suit) 
    return i*NSUITS + j
    
  except ValueError:
    print(f"\nBad input\n value : {value}\n suit : {suit}")
    return


print("Enter how many times you want to run: ")
T = int(input())
  
while T != 0:
    T -= 1
    
    # Initalize  decks as queue
    decks = [[], []]
    
    for i in range(0, len(decks)):
      print("Deck", i+1, end=' ')
      temp_deck = input().strip().split()
      
      # Add ranks of card into deck
      for card in temp_deck:
        rank = rank_card(card[0], card[1])
        if rank != None:
          decks[i].append(rank)
        else:
          print("Re-enter values of deck", i+1)
          i -= 1
          break
    #getting result of both decks
    war(decks[0], decks[1])



"""
OUTPUT for different values:

@1st:
Enter how many times you want to run: 
1
Deck 1 4d Ks As 4h Jh 6h Jd Qs Qh 6s 6c 2c Kc 4s Ah 3h Qd 2h 7s 9s 3c 8h Kd 7h Th Td
Deck 2 8d 8c 9c 7c 5d 4c Js Qc 5s Ts Jc Ad 7d Kh Tc 3s 8s 2d 2s 5h 6d Ac 5c 9h 3d 9d
deck1 wins in 202 steps


@2nd:
Enter how many times you want to run: 
1
Deck 1 6d 9d 8c 4s Kc 7c 4d Tc Kd 3s 5h 2h Ks 5c 2s Qh 8d 7d 3d Ah Js Jd 4c Jh 6c Qc
Deck 2 9h Qd Qs 9s Ac 8h Td Jc 7s 2d 6s As 4h Ts 6h 2c Kh Th 7h 5s 9c 5d Ad 3h 8s 3c
deck1 wins in 170 steps

@3rd:
1
Deck 1 Ah As 4c 3s 7d Jc 5h 8s Qc Kh Td 3h 5c 9h 8c Qs 3d Ks 4d Kd 6c 6s 7h Qh 3c Jd
Deck 2 2h 8h 7s 2c 5d 7c 2d Tc Jh Ac 9s 9c 5s Qd 4s Js 6d Kc 2s Th 8d 9d 4h Ad 6h Ts
deck2 wins in 30 steps

@4th:
Enter how many times you want to run: 
2
Deck 1 9h Qd Qs 9s Ac 8h Td Jc 7s 2d 6s As 4h Ts 6h 2c Kh Th 7h 5s 9c 5d Ad 3h 8s 3c
Deck 2 2h 8h 7s 2c 5d 7c 2d Tc Jh Ac 9s 9c 5s Qd 4s Js 6d Kc 2s Th 8d 9d 4h Ad 6h Ts
deck1 wins in 204 steps
Deck 1 8d 8c 9c 7c 5d 4c Js Qc 5s Ts Jc Ad 7d Kh Tc 3s 8s 2d 2s 5h 6d Ac 5c 9h 3d 9d
Deck 2 2h 8h 7s 2c 5d 7c 2d Tc Jh Ac 9s 9c 5s Qd 4s Js 6d Kc 2s Th 8d 9d 4h Ad 6h Ts
deck1 wins in 226 steps

"""
