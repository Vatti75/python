from collections import Counter



def non_repeated(Name):
    non_repeated_char=[]

    for char in Name:
        if Name.count(char)==1:
            non_repeated_char.append(char)

    return non_repeated_char

def count_occurrences(Name):
    string_count={}

    for char in Name:
        if char in string_count:
            string_count[char]+=1
        else:
            string_count[char]=1
    
    return string_count

def Calculate_total(Name):
    total_char=0

    for char in Name:
        total_char+=1
    
    return total_char

def Max_value(size):
    array=[]

    print("Enter the elements of the array:")
    for _ in range(size):
        array.append(int(input()))

    counter=Counter(array)
    max_value=max(counter.keys())

    return max_value







