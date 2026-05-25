# print("hello world!") 
# print("Iam learning python") 
# print("AI is the queen!") 

# checking request package

# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)

# variables

# user_name = "Alice"
# user_age = 25
# name = "Dave"

# calc
# total = 100 -10
# print(total)

# power = 100 * 2
# print(power)

# string = " holla mammi"

# long_string = """
# Man on a edge
# Crying for his life for
# Me on the bed
# """


# first_name = "John"

# last_name = "Watson"

# full_name = first_name + " " +  last_name

# long_dash = "-" * 20

# print(full_name)
# print(long_dash)

# len(full_name)


# is_true = True

# dynamic text

# name = "Dave"

# string = f"my friend name is {name}"

# print(string)

# name = "Dave"

# name = name.lower()

# print(name)

# if statement

# temp = 36

# if temp > 35:
#     print("its very hot!")
# elif temp > 25:
#     print("its hot!")
# else:
#     print("its cold!")

# has_ticket = True
# age = 15

# if has_ticket:
#     if age >= 18:
#         print("enjoy the movie!")
#     else:
#         print("cannot enter!")
# else:
#     print("Please purchase a ticket")


# for i in range(3, 10, 3):
#     print(i)

# list

# age = 25

# has_card = False

# my_list = ["Alan", 26, age, True, has_card]

# my_list[0] = "John"
# my_list.append("Jack")
# my_list.remove("Jack")
# my_list.insert(1, "Jane")

# name = my_list[0]

# print(my_list)

# dictionary

# person = {
#     "name": "john",
#     "age": 20,
#     "city": "Brazil"
# }

# person["city"]

# person["name"] = "Monk"
# person["card"] = True

# person

# person["name"]

# person.keys()
# person.values()
# person.items()

# tuples and slice

# empty = ()

# point = (1, 2)

# colors = ("red", "green", "blue")

# colors[0:1]

# sets 

# empty_set = set()

# numbers = {1,2, 3, 4, 5, 6}
# colors = set(["Blue", "green", "yellow", "red"])

# # list to set
# scores = [3, 5, 2, 3, 9, 7, 5]

# unique_scores = set(scores)

# print(unique_scores)

# func

# def greet():
#     print("hello!!")
#     print("hello again!!")
    

# greet()
# greet()
# greet()

# def check_weather():
#     temp = 45

#     if temp >= 35:
#         print("Hot as hell!")
#     else:
#         print("Nice weather!")

# check_weather()

# def greet(f_name="John", l_name="Doe"):
#    print(f"Hi, {f_name} {l_name}")

# greet(f_name="Mike", l_name="Tyson")
# greet()

# example

# def calculate_total(price, tax, discount):
#    tax = price * tax
#    f_price = price + tax - discount
#    print(f"Total: ${f_price}")

# calculate_total(10, 0.5, 10)

# global variables


# def calculate_total(price):
#     # variables
#     tax_rate = 0.2
#     discount = 10

#     # calc
#     tax = price * tax_rate
#     f_price = price + tax - discount

#     # print
#     print(f"Total: ${f_price}")

# calculate_total(10)


#  Return

# def add_print(a, b):
#     print(a + b)

# add_print(10, 5)

# def return_add(a, b):
#     return(a + b)

# result = return_add(10, 5)

# result + 10

#  Return muultiple values

# def simple_function():
#     numbers = [1, 2, 3, 4, 5, 6]
#     f_n = numbers[0]
#     l_n = numbers[-1]
#     return f_n, l_n

# f_n,l_n = simple_function()

# print(f_n, l_n)

# import

# import math

# root = math.sqrt(6)

# from math import sqrt, pi

# sqrt(8)

# print(pi * 4)

# import random

# number = random.randint(1, 20)
# choice = random.choice(["banana", "apple", "orange", "watermelon"])

# number
# choice

# import datetime

# today = datetime.date.today()

# today


# import os

# current_dir = os.getcwd()

# current_dir

# import pandas as pd


# import requests

# coordinates for paris
# latitude = 48.85
# longitude = 2.35

# # api parameters
# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# # request
# response = requests.get(url)
# data = response.json()

# # return
# temp = data["current"]["temperature_2m"]

#  combine func with it 

# def get_weather(latitude, longitude):
#     response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
#     data = response.json()
#     return data["current"]["temperature_2m"]

# # coordinate of different countries

# paris_temp = get_weather(48.85, 2.35)
# london_temp = get_weather(51.50, -0.12)
# tokyo_temp = get_weather(35.68, 139.69)

# # print
# print(f"Paris : {paris_temp} C")
# print(f"london : {london_temp} C")
# print(f"tokyo : {tokyo_temp} C")

# working with data

#  classes

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

# class Cat:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# jerry = Dog("Harry", "mustif")

# jerry.breed

#  real world example

# classa nd its attributes

# class APIConfig:
#     def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
#         self.api_key = api_key
#         self.model = model
#         self.max_tokens = max_tokens
#         self.base_url = "https://api.openai.com/v1"

# # Create different configurations/ instances/ objects
# # Using the required parameters
# dev_config = APIConfig("sk-dev-key", max_tokens=50)

# # Using all named arguments (clearest)
# prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# # Check the configuration
# print(dev_config.model)       
# print(prod_config.model)       
# print(prod_config.max_tokens)  


# Mehods / behaviours

# class DataValidator:
#     def __init__(self):
#         self.errors = []
    
#     def validate_email(self, email):
#         if "@" not in email:
#             self.errors.append(f"Invalid email: {email}")
#             return False
#         return True
    
#     def validate_age(self, age):
#         if age < 0 or age > 150:
#             self.errors.append(f"Invalid age: {age}")
#             return False
#         return True
    
#     def get_errors(self):
#         return self.errors

# # Use the validator
# validator = DataValidator()

# # Notice: we don't pass self, just the email
# validator.validate_email(email="bad-email")
# validator.validate_age(age=200)

# # Or using positional arguments
# validator.validate_email("another-bad-email")
# validator.validate_age(150)

# print(validator.get_errors())

# inheritance


# Parent class - general animal
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         return f"{self.name} is eating"
    
#     def sleep(self):
#         return f"{self.name} is sleeping"

# # Child class - specific animal
# class Dog(Animal):
#     def bark(self):
#         return f"{self.name} says woof!"

# # Create a dog - using positional argument
# my_dog = Dog("Buddy")
# # Or with named argument
# my_dog2 = Dog(name="Max")

# # Dog can do animal things (inherited)
# print(my_dog.eat())    # Buddy is eating
# print(my_dog.sleep())  # Buddy is sleeping

# # Dog can also do dog things
# print(my_dog.bark())   # Buddy says woof!

#  example with inheritance with sub methods

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_pet = True

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Pass name to parent's __init__
#         self.breed = breed      # Dog-specific attribute
    
#     def describe(self):
#         return f"{self.name} is a {self.breed}"

# # Create dogs with breeds - positional arguments
# golden = Dog("Buddy", "Golden Retriever")

# # Or with named arguments (clearer)
# poodle = Dog(name="Max", breed="Poodle")

# print(golden.describe())  # Buddy is a Golden Retriever
# print(golden.is_pet)      # True (inherited from Animal)