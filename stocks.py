# Brian Mohabeer
# CS175L-02
# Stocks
Commission_Rate = float(input("Please enter commission rate: "))
Num_Shares = float(input("Please enter number of shares: "))
Purchase_Price = float(input("Please enter the purchase price: "))
Selling_Price = float(input("Please enter the selling price: "))
amountPaidForStock = Num_Shares*Purchase_Price
purchaseCommission = Commission_Rate*amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = Num_Shares*Selling_Price
sellingCommission = Commission_Rate*stockSoldFor
totalRecieved = stockSoldFor - sellingCommission
profitOrLoss = totalRecieved - totalPaid

print(f'Amount paid for stock: ${amountPaidForStock:,.2f}')
print(f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print(f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print(f'Commission paid on the sale: ${sellingCommission:,.2f}')
print(f'Profit (or loss if negative): ${profitOrLoss:,.2f}')
