import random
user_choice=int(input("enter your choice where 0-rock,1-paper,2-scissor:"))
comp_choice=random.randint(0,2)
print(f"computer choosed{comp_choice}")
if user_choice==comp_choice:
  print("its a tie")
elif (user_choice==0 and comp_choice==1)or(user_choice==1 and comp_choice==2)or(user_choice==2 and comp_choice==1):
  print("you loose!")
else:
  print("you win!")