# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator Designed by Emeka Joseph!")
print("\nYou will get your love score by checking on the number of times the letters in the word TRUE occurs and then check for the number of times the letters in the word LOVE occurs and then get an output for the love score.")
name1 = input("\nWhat is your name? \n")
name2 = input("\nWhat is your crush or partner's name? \n")

love = list('love')
true = list('true')

print(love)

print(true)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = list((name1+name2).lower())
print(names)

print("*********************")
print("The number of time L O V E occured in your combined names.")
print("*********************")


for x in love:
  # if x in names:
  print(f"{x} occurs {names.count(x)}")

total_love_count = sum(names.count(s) for s in love)

print(f"Total = {total_love_count}")
  

print("*********************")
print("The number of time T R U E occured in your combined names.")
print("*********************")   

for y in true:
  # if y in names:
    print(f"{y} occurs {names.count(y)}")
  
total_true_count = sum(names.count(y) for y in true)
print(f"Total = {total_true_count}")

love_score = str(total_true_count)+str(total_love_count)

print(f"Love Score = {love_score}")

score = int(love_score)

if score < 10 or score > 90:
  print(f"Your score is {score}%, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}%, you are alright together.")
else:
  print(f"Your score is {score}%.")

print("\nThis is just a game. Don't take it serious and loss your soulmate.\U0001F605\U0001F605\U0001F605\U0001F605 ")