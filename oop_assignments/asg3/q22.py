def manual_len(s):
    count = 0
    for char in s:
        count += 1
    return count

def print_max_length_string_manual(s1, s2):
    len_s1 = manual_len(s1)
    len_s2 = manual_len(s2)
    
    if len_s1 > len_s2:
        print(s1)
    elif len_s2 > len_s1:
        print(s2)
    else:
        print(s1)
        print(s2)


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print_max_length_string_manual(string1, string2)
