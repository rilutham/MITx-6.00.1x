total = 0

for i in range(1, 13):
    minipay = balance * monthlyPaymentRate
    balance = (balance - minipay) * (1 + annualInterestRate / 12.0)
    total += minipay
    print 'monthlyPaymentRate:', i
    print 'Minimum monthlyPaymentRately payment:', round(minipay, 2)
    print 'Remaining balance:', round(balance, 2)
    
print 'Total paid:', round(total, 2)
print 'Remaining balance:', round(balance, 2)