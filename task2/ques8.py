

str1 = input("Hi.\nPlease enter a string with number:  ")

dig_no = 0
alpha_num = 0
for i in str1:
   if i.isdigit():
       dig_no += 1
   else:
       alpha_num +=1



print("No of Digits: ", dig_no , "\nNo of Alphabets: " , alpha_num)
