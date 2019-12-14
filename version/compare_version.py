def version(version1,version2):
#compare two different version strings 
#Assuming all chars in the inputted strings are valid characters i.e numbers and .
#Also assuming 1.0.1 === 1.0.1.0

  #split the chars into a list by the dot
  v1 = version1.split('.')
  v2 = version2.split('.')
  
  #compares the length of the inputs i.e if version1 = 1.0.1 and version2 = 1.0.1.2 it modifies version1 to 1.0.1.0
  if len(v1) != len(v2):
    for i in range(max(len(v1), len(v2))):
      if i > len(v1)-1:
        v1.append('0')
      if i > len(v2)-1:
        v2.append('0')
        
  # Gets if its equal, less than or greater than
  for i in range(len(v1)):
      if int(v1[i]) != int(v2[i]):
          ans =  int(v1[i]) -int(v2[i])
          if ans > 0:
            return version1 + ' is greater than ' + version2
          else :
            return version1 + ' is less than ' + version2

  return version1 + ' is equal to ' + version2




