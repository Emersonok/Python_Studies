def palindrome(s):
  if s == s[::-1]:
    return True
  return False

print(palindrome("madam"))


def palindrome_python(s):
  original_string = s
  reversed_string = reverse(s)
  if original_string == reversed_string:
    return True
  else:
    return False

def reverse(data):
  data = list(data)# making sure all data is a list, converting all data into lists
  start = 0 #starting point
  end = len(data)-1 # ending point
  while end > start: #keep swapping as far as end values are ahead 
   data[start], data[end] = data[end], data[start] #switching positions of start and end
   start = start + 1 #always put, loop steps
   end = end -1 #always put, loop steps

  return ''.join(data) #transform list of letters into string

print(palindrome_python('madam'))
print(palindrome_python("racecar"))
print(palindrome_python("car"))


