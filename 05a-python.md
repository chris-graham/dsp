# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> - lists & tuples are both a sequence of values which can be any type. Both are indexed by integers. The major difference between the two is that lists are mutable and tuples are immutable.
- tuples will work as keys in dictionaries because only immutable elements can be used as dictionary keys (dictionary keys must be hashable). i.e. you couldn't use a tuple that contained a mutible object such as a list.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and Lists are both collections of objects and are both mutable. However, a set is unordered, unindexed and does not allow duplicate members; all of which are untrue for lists. Sets also support mathmatical operations like union, intersection, etc. Regarding performance, lists perform better when iterating, sets perform better when membership testing, so it depends on what you're doing as to which performs better. Lists are most likely the better alternative for general use unless you explicitly need the features of a set.
- Set Example:
```
test_set = set(['a', 'b', 'c'])
test_set.add('a')
'a' in test_set
True
print test_set
set(['a', 'c', 'b'])
```
- List Example:
```
test_list = ['a', 'b', 'c']
test_list.append('a')
'a' in test_list
True
print test_list
['a', 'b', 'c', 'a']
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a tool for building functions similar to 'def', however, lambda is an anonymous function and can only be used once. Lambda can only take a single expression, and that expression must return a value. Lambda functions aren't necessary but are convenient and produce cleaner code, especially when the parameter supplied requires a function.
```
addresses = [('161 Adelphi', 'Brooklyn', 'NY', 11205), ('119 Gates', 'Brooklyn', 'NY', 11238), ('228 W 71st', 'New York', 'NY', 10023), ('134 W 86th', 'New York', 'NY', 10024)]
sorted(addresses, key=lambda address: address[3])
[('228 W 71st', 'New York', 'NY', 10023), ('134 W 86th', 'New York', 'NY', 10024), ('161 Adelphi', 'Brooklyn', 'NY', 11205), ('119 Gates', 'Brooklyn', 'NY', 11238)]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a concise way to create lists instead of using a for loop. Functionally speaking, a list comprehension is comperable to a map & filter (both return list objects), however, list comprehensions are almost always preferred as they're the de-facto 'Pythonic' way to do iteration. If you already have a function defined, it might make more sense to use map & filter since maps accept a function as a parameter.
- List example
```
squares = [x**2 for x in range(10) if x**2 < 10]
print squares
[0, 1, 4, 9]
```
- Map & Filter equivalant
```
def square(x):
    return x**2

squares = map(square, range(10))
print squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

single_digit_squares = filter(lambda x: x < 10, squares)
print single_digit_squares
[0, 1, 4, 9]
```
- Set & Dictionary comprehensions
```
characters = {x for x in 'aabcccdefff' if x not in 'cde'}
print characters
set(['a', 'b', 'f'])

{x: x*5 for x in range(10)}
{0: 0, 1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





