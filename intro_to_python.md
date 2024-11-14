# Homework
*2024-11-14*
## Boolean
The statement below would print a Boolean value, which one?
```python
print(10 > 9)
#True
```
The statement below would print a Boolean value, which one?
```python
print(10 == 9)
#False
```
The statement below would print a Boolean value, which one?
```python
print(10 < 9)
#False
```
The statement below would print a Boolean value, which one?
```python
print(bool("abc"))
#True
```
The statement below would print a Boolean value, which one?
```python
print(bool(0))
#False
```

## If Else
Print "Hello World" if a is greater than b.
```python
a = 50
b = 10
if a > b:
  print("Hello World")
```
Print "Hello World" if a is not equal to b.
```python
a = 50
b = 10
if a != b:
  print("Hello World")
```
Print "Yes" if a is equal to b, otherwise print "No".
```python
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
```
Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
```python
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
```
Print "Hello" if a is equal to b, and c is equal to d.
```python
if a == b and c == d:
  print("Hello")
```
Print "Hello" if a is equal to b, or if c is equal to d.
```python
if a == b or c == d:
  print("Hello")
```
Complete the code block, print "YES" if 5 is larger than 2.
Hint: remember the indentation.
```python
if 5 > 2:
  print("YES")
```
Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
```python
a = 2
b = 5
print("YES") if a == b else print("NO")
```
---
*2024-11-12*
## Python Slicing Exercises
 Slice the word until first "a". (Tosc)
```python
wrd="Toscana"
ans_1=wrd[:-3]
print(ans_1)
#Tosc
```
Slice the word so that you get "cana".
```python
wrd="Toscana"
ans_1=wrd[3:]
print(ans_1)
#cana
```
## Python Dictionary Exercises
### Dictionaries
Select the correct function to print the number of key/value pairs in the dictionary:
```python
x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))
```
### Access Dictionaries
Use the get method to print the value of the "model" key of the car dictionary.
```python
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
```
### Change Dictionaries
Change the "year" value from 1964 to 2020.
```python
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
```
### Add Dictionary Items
Add the key/value pair "color" : "red" to the car dictionary.
```python
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
```
Insert the missing part to add an item to the dictionary.
```python
x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color'='green'})
```
### Remove Dictionary Items
Use the pop method to remove "model" from the car dictionary.
```python
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
```
Use the clear method to empty the car dictionary.
```python
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
```
Insert a correct syntax for removing the 'color' item of the dictionary:
```python
myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar("color")
```

---
*2024-11-10*
## Exercise 1: print() function
```python
print("hello world")
#hello world
```
Assign hello world to variable.
```python
my_text = "hello world"
print(my_text)
#hello world
```

## Exercise 2: Variables
Assign a number to the variable: glass_of_water.
```python
glass_of_water = 3
print ("I drank", glass_of_water ,"glasses of water today.")
#I drank 3 glasses of water today.
```
Fill the print function so it prints glass_of_water
```python
glass_of_water=glass_of_water + 1
print(glass_of_water)
#4
```

## Exercise 3: Data Types
Assign an integer to the variable, then print it.
```python
men_stepped_on_the_moon=12
print(men_stepped_on_the_moon)
#12
```
Type a couple of words or a short sentence for your variable, then print it.
```python
my_reason_for_coding="program evil nanorobot army for world domination :)"
print(my_reason_for_coding)
#program evil nanorobot army for world domination :)
```
Assign a float with 2 decimals to the variable below.
```python
global_mean_sea_level_2018=21
global_mean_sea_level_2018=21.36
print(global_mean_sea_level_2018)
#21.36
```

## Exercise 9: Strings
Assign the string below to the variable in the exercise.
"It's always darkest before dawn."
```python
str="It's always darkest before dawn."
print(str)
#It's always darkest before dawn.
```
By using first, second and last characters of the string, create a new string.
```python
ans_1=str[0]+str[1]+str[-1]
ans_1
#'It.'
```
Replace the (.) with (!)
```python
str = str.replace(".","!")
str
#"It's always darkest before dawn!"
```

## Exercise 10: len() function
Using len() function find out how many items are in the list.
```python
lst=[11, 10, 12, 101, 99, 1000, 999]
answer_1=len(lst)
print(answer_1)
#7
```
Find out the length of the string given below.
```python
msg="be yourself, everyone else is taken."
msg_length=len(msg)
print(msg_length)
#36
```
How many keys are there in the dictionary?
```python
dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5, "Barcelona":5,"Liverpool": 5}
ans_1=len(dict)
print(ans_1)
#5
```

## Exercise 11: .sort() method
Sort the list in ascending order with .sort() method.
```python
lst=[11, 100, 1000, 999]
lst.sort()
print(lst)
#[11, 100, 999, 1000]
```
This time sort the countries in alphabetic order.
```python
lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
lst.sort()
print(lst)
#['Belize', 'Canada', 'India', 'Japan', 'Kazakhstan', 'Taiwan', 'Ukraine']
```
Now sort the list in descending order with .sort() method.
```python
lst=[11, 100, 101, 999, 1001]
lst.sort(reverse = True)
print(lst)
#[1001, 999, 101, 100, 11]
```

## Exercise 12: .pop() method
Pop the last item of the list below.
```python
lst=[11, 10, 99, 1000, 999]
popped_item = lst.pop(-1)
print(popped_item)
#999
print(lst)
#[11, 10, 99, 1000]
```
Remove "broccoli" from the list using .pop and .index methods.
```python
lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
lst.index("broccoli")
#4
item=lst.pop(4)
print(lst, item)
#['milk', 'banana', 'eggs', 'bread', 'lemons'] broccoli
```
Save Italy's GDP in a separate variable and remove it from the dictionary.
```python
GDP_2018={"US": 21,"China": 16,"Japan": 5,"Germany": 4,"India": 3,"France": 3,"UK": 3,"Italy": 2}
italy_gdp=GDP_2018.pop("Italy")
print(GDP_2018)
#{'US': 21, 'China': 16, 'Japan': 5, 'Germany': 4, 'India': 3, 'France': 3, 'UK': 3}
print(italy_gdp, "trillion USD")
#2 trillion USD
```