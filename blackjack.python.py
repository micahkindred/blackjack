from random import randint
def blackjack():
  tot=500
  winOrLose=0
  answer="Yes"
  
  while tot>0 and (answer=="Yes" or answer=="yes"):
    bet=input("How much money would you like to bet?")
    cards=list()
    cards.append(randint(1,13))
    cards.append(randint(1,13))
    dcards=list()
    dcards.append(randint(1,13))
    dcards.append(randint(1,13))
    cv=list()
    dv=list()
  
    cv.append(0)
    cv.append(0)
    dv.append(0)
    dv.append(0)

    if cards[0]==1:
      print("Your first card is an ace")
      cv[0]=int(input("Would you like the ace to be worth 1 or 11?"))
    elif cards[0]==11:
      print("Your first card is a jack")
      cv[0]=10
    elif cards[0]==12:
      print("Your first card is a queen")
      cv[0]=10
    elif cards[0]==13:
      print("Your first card is a king")
      cv[0]=10
    else:
      print("Your first card is a "+str(cards[0]))
      cv[0]=int(cards[1])
      
    if cards[1]==1:
      print("Your second card is an ace")
      cv[1]=int(input("Would you like the ace to be worth 1 or 11?"))
    elif cards[1]==11:
      print("Your second card is a jack")
      cv[1]=10
    elif cards[1]==12:
      print("Your second card is a queen")
      cv[1]=10
    elif cards[1]==13:
      print("Your second card is a king")
      cv[1]=10
    else:
      print("Your second card is a "+str(cards[1]))
      cv[1]=int(cards[1])

    if dcards[0]==1:
      dv[0]=11
      print("The dealer's first card is an ace")
    elif dcards[0]==11:
      dv[0]=10
      print("The dealer's first card is a jack")
    elif dcards[0]==12:
      dv[0]=10
      print("The dealer's first card is a queen")
    elif dcards[0]==13:
      dv[0]=10
      print("The dealer's first card is a king")
    else:
      dv[0]=int(dcards[0])
      print("The dealer's first card is a "+str(cv[0]))
    
    if dcards[1]==1:
      dv[1]=11
    elif dcards[1]==11:
      dv[1]=10
    elif dcards[1]==12:
      dv[1]=10
    elif dcards[1]==13:
      dv[1]=10
    else:
      dv[1]=int(dcards[1])
    
    ind=2
    s=sum(cards)

    ans="hit"
    while ans=="hit" and s<=21:
      ans=input("Would you like to hit or stay?")
      if ans=="hit":
        cards.append(randint(1,13))
        cv.append(0)
        if cards[ind]==1:
          print("Your new card is an ace")
          cv[ind]=int(input("Would you like the ace to be worth 1 or 11?"))
        elif cards[ind]==11:
          print("Your new card is a jack")
          cv[ind]=10
        elif cards[ind]==12:
          print("Your new card is a queen")
          cv[ind]=10
        elif cards[ind]==13:
          print("Your new card is a king")
          cv[ind]=10
        else:
          print("Your new card is a "+str(cards[ind]))
          cv[ind]=int(cards[ind])
          ind+=1
      s=sum(cards)
      
      
    s=sum(cards)
    ds=sum(dcards)
    
    if s>21:
      print("You lose, you went over")
      tot=tot-bet
    elif s<21 and s>ds:
      print("YOU WIN")
      tot=tot+bet
    elif s<21 and s<ds:
      print("You lose, dealer wins")
      tot=tot-bet
    elif s<21 and ds>21:
      print("You win, dealer went over")
      tot=tot+bet
    elif s==21:
      print("YOU WIN!!!!!!!!!!!!!!")
      tot=tot+bet
    elif s==ds:
      print("you tied")
    answer=input("Would you like to play again?")
  print "Game over. You finished with",tot,"dollars"
    


blackjack()