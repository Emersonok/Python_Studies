def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1 = sorted(str1)
    str2 = sorted(str2)
    print(str1, str2)

    for x in range(len(str1)):
        if str1[x] == str2[x]:
            return True
        else:
            return False

s1 = ["s", "e", "t"]
s2 = ["t", "e", "s", "t"]
print(anagram(s1, s2))



