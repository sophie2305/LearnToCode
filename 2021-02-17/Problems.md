# Regex themed Kata

## Problem 1 (7 kyu) 

Link to Kata --> [Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e)

### Overview

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata `y` isn't considered a vowel.

## Problem 2 (7 kyu)

Link to Kata --> [Regex validate PIN code](https://www.codewars.com/kata/55f8a9c06c018a0d6e000132)

### Overview

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples
```
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
```

## Problem 3 (6 kyu)

Link to Kata --> [Convert string to camel case](https://www.codewars.com/kata/517abf86da9663f1d2000003)

### Overview

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The **first word** within the output should be capitalized **only if the original word was capitalized** (known as Upper Camel Case, also often referred to as Pascal case).

Examples
```
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
```

## Bonus Problem (5 kyu)

Link to Kata --> [Regex Password Validation](https://www.codewars.com/kata/52e1476c8147a7547a000811)

### Overview

You need to write regex that will validate a password to make sure it meets the following criteria:

* At least six characters long
* contains a lowercase letter
* contains an uppercase letter
* contains a number

Valid passwords will only be alphanumeric characters.
