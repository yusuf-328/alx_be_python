"""Algorithm
1. prompt the user to enter their weather condition
2. provide clothing recommendations
3. provide a statement that handles unexpected input
"""
user_weather = input("What's the weather like today? (sunny/rainy/cold): ")

if user_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I dont have recommendations for this weather.")