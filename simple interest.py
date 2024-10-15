P=int(input("p:")) #principal amount
T=int(input("T:")) #Time the money invested or borrowed for particular years
R=int(input("R:")) #rate of interest per annum
Simple_Interest= (P*T*R)/(100)   #simple interest
Total_Amount=P+Simple_Interest             #Total interest
print("Simple Interest:",Simple_Interest)
print("Total Amount:",Total_Amount)