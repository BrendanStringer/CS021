#Brendan L. Stringer
#CS021
#Assignment2.1
#The purpose of this is to calculate the earning after some stock transactions 

#List all the variables
NumShares=float(2000)
PaidShare=float(40)
SoldShare=float(42.75)
PercentCommission=float(0.03)

#Calculate how much Joe paid for the stock 
AmtPaid = NumShares * PaidShare

#Calculate commission paid to the broker upon purchase of the stock
PurchaseCommission = AmtPaid * PercentCommission

#Calculate how much the stock was sold for 
AmtSold = SoldShare * NumShares

#Calculate commission paid to the broker upon the sale of the stock 
SaleCommission = AmtSold * PercentCommission

#Calculate profits 
Profit = AmtSold - AmtPaid - PurchaseCommission - SaleCommission

#Print values
print('Joe paid: $', format(AmtPaid,'10.2f'))
print('Purchase Commission: $', format(PurchaseCommission,'10.2f'))
print('Joe sold the stock for: $', format(AmtSold,'10.2f'))
print('Sale Commision: $', format(SaleCommission,'10.2f'))
print("Joe's profit: $", format(Profit,'10.2f'))


