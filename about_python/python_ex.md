# Python Exercises

1.  Given a string `name = "John Doe"`, check if it starts with the letter 'J'.
2.  Given two integers `a=7` and `b=3`, check if `a` is divisible by `b`.
3.  Given a float `x=-3.14`, check if it is positive or negative.
4.  Given a list `numbers=[1, 2, 3, 4, 5]`, find the sum of all elements in the list.
5.  Given a dictionary `person`, add a new key-value pair for the person's occupation.


## Solutions

1.  Given a string `name`, check if it starts with the letter 'J'.

```py
name = "John Doe"
if name[0] == "J":
    print("The name starts with the letter 'J'")
else:
    print("The name does not start with the letter 'J'")
```

2.  Given two integers `a` and `b`, check if `a` is divisible by `b`.


```py
a = 6
b = 3
if a % b == 0:
    print(f"{a} is divisible by {b}")
else:
    print(f"{a} is not divisible by {b}")
```

3.  Given a float `x`, check if it is positive or negative.

```py
x = -3.14
if x >= 0:
    print(f"{x} is positive")
else:
    print(f"{x} is negative")
```

4.  Given a list `numbers`, find the sum of all elements in the list.


```py
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(f"The sum of elements in the list is {sum}")
```

5.  Given a dictionary `person`, add a new key-value pair for the person's occupation.

```py
person = {"first_name": "John", "last_name": "Doe", "age": 30}
person["occupation"] = "Data Scientist"
print(person) # Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'occupation': 'Data Scientist'}
```