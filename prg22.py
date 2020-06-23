def doormatPattern(rows, columns): 

    width = columns 

      

    # Print the pattern having a top triangle 

    for i in range (0, int (rows / 2)): 

        pattern = ".|." * ((2 * i) + 1) 

        print (pattern.center (width, '-')) 

      

    # Print GeeksforGeeks in the center 

    print ("WELCOME".center (width, '-')) 

      

    # Print the pattern having  

    # an inverted triangle 

    i = int (rows / 2) 

    while i > 0: 

        pattern = ".|." * ((2 * i) - 1) 

        print (pattern.center (width, '-')) 

        i = i-1

    return
    
str1=input()
lst=str1.split()
rows=int(lst[0])
columns=int(lst[1])
if 5<rows<101 and 15<columns<303 and rows*3==columns:
	doormatPattern(rows, columns) 