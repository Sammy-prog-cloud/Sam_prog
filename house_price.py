price = 1000000
good_credit = True
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment : ${down_payment}")

high_income = True
good_credit = True
eligible = 1000000
if high_income and good_credit:
    print(f"Eligible for loan: ${eligible}")