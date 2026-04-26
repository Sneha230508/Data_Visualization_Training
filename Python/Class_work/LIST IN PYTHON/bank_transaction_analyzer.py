# 7. Bank Transaction Analyzer

transactions = [10000, -5000, 20000, -7000, 15000]

balance = sum(transactions)

withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals)

big_deposits = len([t for t in transactions if t > 10000])

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", big_deposits)
#output
"""Total Balance: 33000
Largest withdrawal: -7000
Deposits> 10000:2"""