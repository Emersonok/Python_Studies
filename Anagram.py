def anagram(str1, str2): #create a function with two vars to  
                         #represent both strings to be compared

    if len(str1) != len(str2): # anagrams must have the same length
                               #They're not anagrams if len are different
        return False
    
    str1 = sorted(str1)     #sort both anagrams so you can compare the values 1 by 1
    str2 = sorted(str2)
    print(str1, str2)

    for x in range(len(str1)): #loop thru one value 
        if str1[x] == str2[x]: #compare it with the other value
            return True
        else:
            return False

s1 = ["s", "e", "t"]
s2 = ["t", "e", "s", "t"]
print(anagram(s1, s2))



