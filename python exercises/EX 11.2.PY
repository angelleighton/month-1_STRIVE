# Counting words line by line in blakepoems.txt.
text = open("blakepoems.txt", 'r')
d = dict() 

for line in text: 
    line = line.strip() 
    line = line.lower() 
    words = line.split(" ") 
  
    for word in words: 
        if word in d: 
            d[word] =+1
        else: 
            d[word] = 1
  
for key in list(d.keys()): 
    print(sorted(key, ":", d[key]))
    


# alphabetical order  sorted
# read line by line readline() / for line in