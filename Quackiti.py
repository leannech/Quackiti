##QUACKITI##

#shower rate retrieval
def shower_rate():
    know_rate = input("ayo! do you happen to know what your shower flow rate is? Y or N? ")

    if know_rate == 'Y' or know_rate == 'y':
        user_rate= float(input("that's rad dude! what is it? dont forget we only take Liter/Min: "))
    else:
        print("all good dude! just take a large container and turn your shower for one min then measure how much water it's in there!")
        user_rate = yourmom()
    return (user_rate)

#determine shower rate
def yourmom():
    import time
    print("Start filling up a litre bucket while also timing how long it takes")
    print()

    for i in range(0, 11):
        print(i)
        time.sleep(0.1)
        
    print()

#to stop while loop
    x = 0
    
    while x == 0:
        answer = input("Has the bucket been filled yet? Press Y for YES and N for NO: ")

        if answer == "N" or answer == "n":
            for i in range(0, 11):
                print(i)
                time.sleep(0.1)   
            print()

        elif answer == "Y" or answer == 'y':
            time = float(input("Please enter the amount of time (in minutes) it took for the litre bucket to fill up: "))
            flow_rate = 1/time
            print("Your flow rate is " , round(flow_rate, 2))
            return flow_rate
            #to stop while loop
            x = 1

#record time in shower
def mymom():
    import time
    overall_time = []
    while True:
        start = input("Press the 'Enter' key when you turn on the shower")
        begin = time.time()
        endtimer = input("Press the 'Enter' key when you turn off the shower")
        end = time.time()
        shower_time = int(end - begin)
        overall_time.append(shower_time)
        total_mins = sum(overall_time)/60

        while True:
            ask = input("Have you finished showering? Y or N: ")
            if ask == "Y" or ask == "y":
                print("You have showered for",round(total_mins,2),"minutes.")
                return(total_mins)
                break
            elif ask == "N" or ask == "n":
                break
            else:
                print("Invalid.")




##QUOTE

def mynuts(shower_water):
    import time
    #shower_water = 7000
    walnut = shower_water/18.9
    print("Ah yes. Nuts.")
    time.sleep(2)
    print("Woah dude, not the nuts you're thinking about.")
    time.sleep(2)
    print("Get your mind out of the gutter.")
    time.sleep(3)
    print("Anyway, before your thoughts rudely interupted,")
    time.sleep(2)
    print("Gosh.")
    time.sleep(1)
    print("Please never think of that again.")
    time.sleep(2)
    print("Anyway, nuts.")
    time.sleep(2)
    print("WALnuts.")
    time.sleep(3)
    print("(I still can't believe you thought about the other kind of nuts)")
    time.sleep(2)
    print("With the water you used during your shower, you could've made ", round(walnut, 2), " walnuts.")
    time.sleep(2)
    print("Wow. ", round(walnut, 2), " big nuts.")
    time.sleep(2)
    print("Literally. They fit like more than half of my palm.")
    time.sleep(2)
    print("No other nut can do that.")
    time.sleep(2.5)
    print("Wait...")
    time.sleep(1.5)
    print("No.")
    time.sleep(1.5)
    print("Alright, it's time for me to go.")
    time.sleep(2)
    print("Go do whatever you want with some nuts.")
    time.sleep(4)
    print("...and with whichever nut you'd like 😉 .")
def put_it_in_rice(shower_water):
    import time
    #shower_water = 7000
    rice = shower_water/2500
    print("Rice.")
    time.sleep(1)
    print("A great grain.")
    time.sleep(1)
    print("Very yum.")
    time.sleep(1)
    print("A nice delectable.")
    time.sleep(1)
    print("If you want to call 'rice' a delectable.")
    time.sleep(2)
    print("It honestly is just rice.")
    time.sleep(2)
    print("Would you actually consider 'rice' being a 'delectable'?")
    time.sleep(2.5)
    print("Don't answer that.")
    time.sleep(1)
    print("Answer this: ")
    time.sleep(1)
    print("How much of the water used in the shower could've been used to make some rough rice in a rice field?")
    time.sleep(4)
    print("Answer it.")
    time.sleep(2)
    print("Okay, fine. I'll answer it.")
    time.sleep(2)
    print("You could've used the water to make ", rice, "  kilograms of rough rice in a rice field.")
    time.sleep(3)
    print("I really hope you're not rough right now.")
    time.sleep(3)
    print("I mean, you did just shower. So...")
    time.sleep(2)
    print("To be fair, I wouldn't judge.")
    time.sleep(1)
    print("Being rough right out of the shower can't be such a bad thing, can it?")
    time.sleep(3.5)
    print("ANYWAY- enough shower talk.")
    time.sleep(2.5)
    print("Get 'smooth' or... something.")
    time.sleep(4)
    print("...why are shower's kinda...")
def AverageAmerican(shower_water):
    import time
    #shower_water = 65.1
    math = shower_water - 65.1
    if math > 0:
        print("Congrats. You managed to waste ", round(math,2), " litres of more water than the average American.")
        time.sleep(2)
        print("When you're above average in using water that could've been used elsewhere.")
        time.sleep(1.5)
        print("Lmao.")
    elif math < 0:
        print("Congrats. You managed to waste less water than the average American.")
        time.sleep(2)
        print("When you're under average in using water that could've been used elsewhere. Congrats. Again.")
        time.sleep(1.5)
        print("Lmao.")
    else:
        print("You somehow managed to shower exactly the same as an average american.")
        time.sleep(2)
        print("I'm actually impressed, the actual precision someone needs to have to do that-")
        time.sleep(2.5)
        print("...or you ARE the Average American..")
def washing_machine_go_brr(shower_water):
    import time
    #shower_water = 7000
    laundry = shower_water/76
    print("Laundry.")
    time.sleep(2)
    print("Go do yours.")
    time.sleep(2)
    print("With how long you've showered for, you could've done ", round(laundry, 2), " loads of laundry.")
    time.sleep(1.5)
    print("Stop procrastinating your laundry, bud.")
def avocado(shower_water):
    import time
    #shower_water = 7000
    avocado = shower_water/227
    print("So about that worldwide avocado shortage")
    time.sleep(2)
    print("With the water you just used in the shower, while harnessing your inner-farmer, you could've grown ", round(avocado), " avocados.")
    time.sleep(2)
    print("Tell that to the people smuggling avocados right now.")
    time.sleep(2)
    print("Actually don't.")
    time.sleep(1.5)
    print("They might want to smuggle you.")
def tshirt(shower_water):
    import time
    #shower_water = 65.1
    shirt = shower_water/1514
    print("You know how many cotton shirts could've been made during your shower?")
    time.sleep(2)
    print("Well do you?")
    time.sleep(2)
    print("I thought so. So listen up:")
    time.sleep(2)
    print("You could've made ", round(shirt, 2), " cotton shirts with all the water you showered with.")
    time.sleep(3)
    print("Stop reading this topless, go throw on at least one of the ", round(shirt, 2) , " cotton shirts you could've made.")
def apple_bottom_jeans(shower_water):
    import time
    #shower_water = 65.1
    jeans = shower_water/6814
    print("So buddy, with your lovely shower, you could have actually created ", round(jeans, 2), " apple bottom jeans.")
    time.sleep(5)
    print("You're probably going to throw on a pair of jeans after this shower, aren't you?")
    time.sleep(3)
    print("Disrespectful.")

#get quote
def functions(total_water):
    import random
    list_of_functions = [apple_bottom_jeans, tshirt, avocado, washing_machine_go_brr, AverageAmerican, put_it_in_rice, mynuts]

    i = random.randint(0,6)
    list_of_functions[i](total_water)

#yeet a graph 
def save_stats(totalWaterList, date):

    import numpy as np
    import matplotlib.pyplot as plt
      
    fig = plt.figure(figsize = (10, 5))
     
    # creating the bar plot
    plt.bar(date, totalWaterList, color ='blue',
            width = 0.4)
     
    plt.xlabel("DATE")
    plt.ylabel("WATER CONSUMED (liters)")
    plt.title("SHOWER WOTah STATS")
    plt.show()



#MAIN
import time
#just some example
totalWaterList = [9.3, 10.8, 15.2, 7.5]
date = ['2022-01-19','2022-01-20','2022-01-21','2022-01-22']

#get todays date
from datetime import datetime
retrieveDate = datetime.today().strftime('%Y-%m-%d')
date.append(retrieveDate)

print("\n-------WELCOME TO QUACKITI--------\n")

shower_rate = shower_rate()
print("\nSo... about that shower.... are you going to start showering soon? ")
shower_time = mymom() #ursula's timer function

total_water = shower_rate*shower_time #calculate total water

totalWaterList.append(total_water)

time.sleep(2)
print("\nCalibrating...")
time.sleep(5)

print("\n"*49)

print("\nHope you had a good shower! Here is the long awaited Judgement Quote...\n")
time.sleep(4) 
functions(total_water)
time.sleep(5)
print("\n"*49)


print("\nYeah... \nokokokokok..... \nHere is your long awaited stats too")

time.sleep(2)
print("\nCalibrating...")
time.sleep(4)
save_stats(totalWaterList, date)

    
