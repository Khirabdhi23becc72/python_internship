def print_max_length_string(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    
    if len1 > len2:
        print("String with maximum length:", s1)
    elif len2 > len1:
        print("String with maximum length:", s2)
    else:
        print("Both strings have the same length:")
        print(s1)
        print(s2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print_max_length_string(string1, string2)
