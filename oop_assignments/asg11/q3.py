def are_anagrams(s1, s2):
    # Anagrams have the same sorted characters
    return sorted(s1) == sorted(s2)

# Example usage:
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2)) 
