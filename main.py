print("Hello! Today you will be finding out which type of community service you should try out! Answer the following questions below.")

OceanHeroWB = 0
OceanHero = 0
Recycling = 0
Gardening = 0
Donating = 0

validanswer1 = False
validanswer2 = False
validanswer3 = False
validanswer4 = False
validanswer5 = False

print("Where do you prefer working?")
      
print("1) Local/In my community")
print("2) Near oceans")
print("3) Outside/in gardens")
print("4) I'd prefer staying inside")
print("5) Anywhere works for me")

answer1 = int(input("Enter the location you prefer working at (enter the number): "))

if answer1 == 1 :
    Recycling += 1
    validanswer1 = True

if answer1 == 2 :
    OceanHero += 1
    validanswer1 = True

if answer1 == 3 :
    Gardening += 1
    validanswer1 = True

if answer1 == 4 :
    OceanHeroWB += 1
    validanswer1 = True

if answer1 == 5 :
    Donating += 1
    Recycling += 1
    OceanHero += 1
    Gardening += 1
    OceanHeroWB += 1
    validanswer1 = True
    
if validanswer1 == False:
    print("Invalid answer! Please restart code or this question won't be counted.")

print("Can you handle heavy work loads or lighter ones?")

print("1) Heavy")
print("2) Light")
print("3) Both")

answer2 = int(input("Enter your work amount (enter the number): "))

if answer2 == 1 :
    Donating += 0.5
    OceanHeroWB += 1
    validanswer2 = True

if answer2 == 2 :
    Gardening += 1
    OceanHero += 1
    Recycling += 1
    validanswer2 = True
    
if answer2 == 3 :
    Recycling += 1
    OceanHero += 1
    Gardening += 1
    OceanHeroWB += 1
    Donating += 1
    validanswer2 = True

if validanswer2 == False:
    print("Invalid answer! Please restart code or this question won't be counted.")

print("What are some fears you may have?")

print("1) Getting dirty")
print("2) Bugs, worms, spiders")
print("3) Drowning")
print("4) None")

answer3 = int(input("Enter your answer here (enter the number): "))

if answer3 == 1 :
    Gardening -= 1
    Donating -= 0.5
    OceanHero -= 0.5
    validanswer3 = True

if answer3 == 2 :
    Gardening -= 1
    validanswer3 = True

if answer3 == 3 :
    OceanHero -= 1
    validanswer3 = True

if answer3 == 4 :
    validanswer3 = True

if validanswer3 == False:
    print("Invalid answer! Please restart code or this question won't be counted.")


print("Any other fears?")

print("1) Getting dirty")
print("2) Bugs, worms, spiders")
print("3) Drowning")
print("4) None")

answer4 = int(input("Enter your answer here (enter the number): "))

if answer4 == 1 :
    Gardening -= 1
    Donating -= 0.5
    OceanHero -= 0.5
    validanswer4 = True

if answer4 == 2 :
    Gardening -= 1
    validanswer4 = True

if answer4 == 3 :
    OceanHero -= 1
    validanswer4 = True

if answer4 == 4:
    validanswer4 = True

if validanswer4 == False:
    print("Invalid answer! Please restart code or this question won't be counted.")

print("1) Recycling:", Recycling)
print("2) Collecting plastic in oceans:", OceanHero)
print("3) Gardening:", Gardening)
print("4) Donating:", Donating)
print("5) OceanHero web browser:", OceanHeroWB)

oneoption = False

if Recycling > max(OceanHero, Gardening, Donating, OceanHeroWB):
    print("You are most suited for doing some recycling! You can do this almost anywhere as recycling bins are everywhere to help reuse materials. Next time, make sure to try it out!")
    oneoption = True
    
if OceanHero > max(Recycling, Gardening, Donating, OceanHeroWB):
    print("You are most suited for collecting plastic bottles from the ocean! You can get more info at https://oceanhero.today")
    oneoption = True
    
if Gardening > max(Recycling, OceanHero, Donating, OceanHeroWB):
    print("You are most suited for gardening! You can find a nearby garden and start learning how to plant, water, and more.")
    oneoption = True
    
if Donating > max(Recycling, OceanHero, OceanHeroWB, Gardening):
    print("You are most suited for donating! You can start off by finding some old stuff that other people in need may find useful.")
    oneoption = True
    
if OceanHeroWB > max(Recycling, OceanHero, Donating, Gardening):
    print("OceanHero has a web broswer that collects plastic bottles from your searches. Download OceanHero at hhtps://oceanhero.today.")
    oneoption = True

if oneoption == False:
    answer5 = int(input("You have multiple community services you are suited for! Look above and choose one that you are most interested in (enter the number): "))
    if answer5 == 1 :
        print("You are most suited for doing some recycling! You can do this almost anywhere as recycling bins are everywhere to help reuse materials. Next time, make sure to try it out!")
        validanswer5 = True
    if answer5 == 2 :
        print("You are most suited for collecting plastic bottles from the ocean! You can get more info at  https://oceanhero.today")
        validanswer5 = True
    if answer5 == 3 :
        print("You are most suited for gardening! You can find a nearby garden and start learning how to plant, water, and more.")
        validanswer5 = True
    if answer5 == 4 :
        print("You are most suited for donating! You can start off by finding some old stuff that other people in need may find useful.")
        validanswer5 = True
    if answer5 == 5 :
        print("OceanHero has a web broswer that collects plastic bottles from your searches. Download OceanHero at hhtps://oceanhero.today.")
        validanswer5 = True
    if validanswer5 == False:
        print("Invalid answer! Please restart code or this question won't be counted.")
    
print("You can also try the other community services even if you didn't get them! If we can all help by doing even the smallest actions, we can help the world.")
print("(If you wanted to learn more about OceanHero and its web broswer the link is https://oceanhero.today)")
    
    
