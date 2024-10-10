
#1. **Reverse a String:**
   
def reverse_string(s):
    return s[::-1]

#2. **Count the Number of Vowels in a String:**

def count_vowels(s):
       vowels = "aeiouAEIOU"
       return sum(1 for char in s if char in vowels)

#3. **Check if a String is a Palindrome:**
  
def is_palindrome(s):
       return s == s[::-1]


#4. **Check if Two Strings are Anagrams:**

def are_anagrams(s1, s2):
       return sorted(s1) == sorted(s2)
 
#5. **Find All Occurrences of a Substring in Another String:**

def find_occurrences(main_str, sub_str):
       return [i for i in range(len(main_str)) if main_str.startswith(sub_str, i)]
 

#6. **String Compression Using Character Counts:**

def compress_string(s):
       compressed = []
       count = 1
       for i in range(1, len(s)):
           if s[i] == s[i-1]:
               count += 1
           else:
               compressed.append(s[i-1] + str(count))
               count = 1
       compressed.append(s[-1] + str(count))
       return ''.join(compressed)

#7. **Check if a String has All Unique Characters:**

def has_unique_chars(s):
       return len(s) == len(set(s))
 
#8. **Convert a String to Uppercase or Lowercase:**
 
def convert_case(s, to_upper=True):
       return s.upper() if to_upper else s.lower()
  

#9. **Count the Number of Words in a String:**

def count_words(s):
       return len(s.split())
  

#10. **Concatenate Two Strings Without Using `+` Operator:**

def concatenate_strings(s1, s2):
        return ''.join([s1, s2])
#11. **Remove All Occurrences of a Specific Element from a List:**

def remove_element(lst, element):
        return [x for x in lst if x != element]
 
#12. **Find the Second Largest Number in a List:**
 
def second_largest(lst):
        unique_sorted = sorted(set(lst), reverse=True)
        return unique_sorted[1] if len(unique_sorted) > 1 else None
  

#13. **Count Occurrences of Each Element in a List (Return Dictionary):**

def count_elements(lst):
        from collections import Counter
        return dict(Counter(lst))
 
#14. **Reverse a List In-Place:**

def reverse_list(lst):
        left, right = 0, len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
 
#15. **Merge Two Sorted Lists into a Single Sorted List:**
 
def merge_sorted_lists(lst1, lst2):
        return sorted(lst1 + lst2)
 

#16. **Find the Intersection of Two Lists:**

def list_intersection(lst1, lst2):
        return list(set(lst1) & set(lst2))
 

#17. **Remove Duplicates from a List While Preserving Order:**

def remove_duplicates(lst):
        seen = set()
        return [x for x in lst if not (x in seen or seen.add(x))]

def is_sorted(lst):
        return lst == sorted(lst) or lst == sorted(lst, reverse=True)

#19. **Find the Union of Two Lists Without Duplicates:**
def list_union(lst1, lst2):
        return list(set(lst1) | set(lst2))
#20. **Shuffle a List Randomly Without Built-In Functions:**
import random
def shuffle_list(lst):
        shuffled = lst[:]
        random.shuffle(shuffled)
        return shuffled

#21. **Find Common Elements in Two Tuples:**
def tuple_intersection(t1, t2):
        return tuple(set(t1) & set(t2))
#22. **Print Intersection of Two User-Entered Sets:**
def input_and_intersect_sets():
        set1 = set(map(int, input("Enter the first set of integers: ").split(',')))
        set2 = set(map(int, input("Enter the second set of integers: ").split(',')))
        print(set1 & set2)

#23. **Concatenate Two Tuples:**
def concatenate_tuples(t1, t2):
        return t1 + t2
#24. **Print Elements Present in First Set But Not in Second:**
def set_difference(s1, s2):
        return s1 - s2
#25. **Return a New Tuple with Elements from Specified Indices:**
def tuple_slice(t, start, end):
        return t[start:end]

#26. **Print Union of Two User-Entered Sets of Characters:**
def input_and_union_sets():
        set1 = set(input("Enter the first set of characters: ").split(','))
        set2 = set(input("Enter the second set of characters: ").split(','))
        print(set1 | set2)

#27. **Find Maximum and Minimum in a Tuple:**
def max_min_in_tuple(t):
        return max(t), min(t)

#28. **Print Union, Intersection, and Difference of Two Sets:**
def set_operations(s1, s2):
        print("Union:", s1 | s2)
        print("Intersection:", s1 & s2)
        print("Difference:", s1 - s2)
  

#29. **Count Occurrences of an Element in a Tuple:**
def count_element_in_tuple(t, element):
        return t.count(element)
 
#30. **Print Symmetric Difference of Two User-Entered Sets:**

def input_and_symmetric_difference_sets():
        set1 = set(input("Enter the first set of strings: ").split(','))
        set2 = set(input("Enter the second set of strings: ").split(','))
        print(set1 ^ set2)

#31. **Return Dictionary with Word Frequencies:**

def word_frequencies(words):
        return {word: words.count(word) for word in set(words)}
   

#32. **Merge Two Dictionaries (Add Values for Common Keys):**
def merge_dictionaries(d1, d2):
        merged = d1.copy()
        for key, value in d2.items():
            merged[key] = merged.get(key, 0) + value
        return merged
   

#33. **Access Value in a Nested Dictionary:**
def access_nested_dict(d, keys):
        for key in keys:
            d = d.get(key)
            if d is None:
                return None
        return d

#34. **Sort Dictionary by Values:**
def sort_dict_by_values(d, ascending=True):
        return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

#35. **Invert a Dictionary (Keys Become Values, Handle Duplicates):**
    
def invert_dict(d):
        inverted = {}
        for key, value in d.items():
            if value not in inverted:
                inverted[value] = [key]
            else:
                inverted[value].append(key)
        return inverted