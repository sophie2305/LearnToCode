# Regex themed Kata

## Problem 1 (7 kyu) 

Link to Kata --> [Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e)

### Overview

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata `y` isn't considered a vowel.

## Problem 2 (6 kyu)

Link to Kata --> [Convert string to camel case](https://www.codewars.com/kata/517abf86da9663f1d2000003)

### Overview

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The **first word** within the output should be capitalized **only if the original word was capitalized** (known as Upper Camel Case, also often referred to as Pascal case).

Examples
```
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
```

# Problem 3 (5 kyu)

Link to Kata --> [Extract the domain name from a URL](https://www.codewars.com/kata/514a024011ea4fb54200004b)

### Overview

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

```
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```

# Bonus Problem (5 kyu)

Link to Kata --> [Regex Password Validation](https://www.codewars.com/kata/52e1476c8147a7547a000811)

### Overview

You need to write regex that will validate a password to make sure it meets the following criteria:

* At least six characters long
* contains a lowercase letter
* contains an uppercase letter
* contains a number

Valid passwords will only be alphanumeric characters.