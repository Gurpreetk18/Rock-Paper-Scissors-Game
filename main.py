rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
number=int(input("Enter 0 for rock 1 for paper 2 for scissor\n"))
a=[rock,paper,scissors]
print("You chose"+a[number])
choice=random.randint(0,2)
print("Computer chose"+a[choice])
print(choice)
print(number)
if choice==number:
  print("it's a draw")
elif a[choice]==rock and a[number]==scissors:
  print("You lose")
elif a[number]==rock and a[choice]==scissors:
  print("You win")
elif choice>number:
  print("You lose")
else:
  print("You win")