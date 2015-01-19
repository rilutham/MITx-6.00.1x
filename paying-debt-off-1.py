fixed = 10
 
while True:
    remain = balance
    for i in range(1, 13):
        remain = (remain - fixed) * (1 + annualInterestRate / 12.0)
    if remain > 0:
        fixed += 10
    else:
        break
    
print 'Lowest Payment:', fixed