mortgage_interest_rates = {
    1: 0.0595,
    2: 0.059,
    3: 0.056,
    5: 0.0529,
    10: 0.06
}

amortization_period_years = {
    1: 5,
    2: 10,
    3: 15,
    4: 20,
    5: 25
}

client_name = input("Client's Name: ")
address = input("Address: ")
purchase_price = float(input("Purchase Price: $"))

if purchase_price <= 500000:
    min_down_payment = 5
elif purchase_price <= 1000000:
    min_down_payment = (0.05*500000) + (0.10*(purchase_price - 500000))
else:
    min_down_payment = 20


min_downpayment_percent = round(min_down_payment / purchase_price * 100, 3)
print(f"Min Down Payment percent is: {min_downpayment_percent}%")

down_payment_percentage = float(
    input("Enter Down Payment Percentage(5 ,10 ,15 ,20): "))

if down_payment_percentage < min_downpayment_percent:
    print("error please enter a valid Down Payment Percentage")
else:
    down_payment_percentage == down_payment_percentage

Down_payment_ammount = (purchase_price * down_payment_percentage / 100)

if down_payment_percentage >= 5 and down_payment_percentage < 10:
    insurance_rate = 4
elif down_payment_percentage >= 10 and down_payment_percentage < 15:
    insurance_rate = 3.1
elif down_payment_percentage >= 15 and down_payment_percentage < 20:
    insurance_rate = 2.8
else:
    insurance_rate = 0

insurance_cost = round(
    (purchase_price - Down_payment_ammount) * insurance_rate / 100, 2)

principal_amount = purchase_price - Down_payment_ammount + insurance_cost

mortgage_term = int(input("Enter Mortgage Term (1, 2, 3, 5, 10 years): "))

amortization_period = int(
    input("Enter Amortization Period (5, 10, 15, 20 ,25 years): "))

# n is the number of monthly payments
n = amortization_period * 12

if mortgage_term == 1:
    a = 0.0595
elif mortgage_term == 2:
    a = 0.059
elif mortgage_term == 3:
    a = 0.056
elif mortgage_term == 5:
    a = 0.0529
elif mortgage_term == 10:
    a = 0.06


EMR = ((1 + a/2)**(2/12)) - 1

M = principal_amount * (EMR * (1 + EMR)**n) / ((1 + EMR)**n - 1)


print(EMR)
print(M)
# print(Monthly_payment)
# print(n)


# amortization_period = int(input("Amortization Period (5, 10, 15, 20 ,25 years): "))


# if purchase_price <= 500000:
#     min_down_payment = 5
# elif purchase_price <= 1000000:
#     min_down_payment = (0.05*500000) + (0.10*(purchase_price - 500000))
# else:
#     min_down_payment = 20


# down_payment_amount = int(round(purchase_price * down_payment_percentage / 100, 2))


# insurance_rate = 0

# if 5 <= down_payment_percentage < 10:
#     insurance_rate = 4
# elif 10 <= down_payment_percentage < 15:
#     insurance_rate = 3.1
# elif 15 <= down_payment_percentage < 20:
#     insurance_rate = 2.8
# else:
#     20 <= down_payment_percentage < 20
#     insurance_rate = 0
# insurance_cost = round((purchase_price - down_payment_amount) * insurance_rate / 100, 2)


# mortgage_interest_rates = {
#     1: 0.0595,
#     2: 0.059,
#     3: 0.056,
#     5: 0.0529,
#     10: 0.06
# }


# annual_interest_rate = 0

# if mortgage_term == 1:
#     annual_interest_rate = mortgage_interest_rates[1]

# elif mortgage_term == 2:
#     annual_interest_rate = mortgage_interest_rates[2]

# elif mortgage_term == 3:
#     annual_interest_rate = mortgage_interest_rates[3]

# elif mortgage_term == 5:
#     annual_interest_rate = mortgage_interest_rates[5]

# elif mortgage_term == 10:
#     annual_interest_rate = mortgage_interest_rates[10]

# amortization_period_years = {
#     1: 5,
#     2: 10,
#     3: 15,
#     4: 20,
#     5: 25
# }


# effective_monthly_rate = 0

# if amortization_period_years == 1:
#     effective_monthly_rate = round(((1 + mortgage_term/2 )^2 )^1/12 - 1,  2)

# elif amortization_period_years == 2:
#     effective_monthly_rate = round(((1 + mortgage_term/2 )^2 )^1/12 - 1,  2)

# elif amortization_period_years == 3:
#     effective_monthly_rate = round(((1 + mortgage_term/2 )^2 )^1/12 - 1, 2)

# elif amortization_period_years == 4:
#     effective_monthly_rate = round(((1 + mortgage_term/2 )^2 )^1/12 - 1,  2)

# elif amortization_period_years == 5:
#     effective_monthly_rate = round(((1 + mortgage_term/2 )^2 )^1/12 - 1,  2)

# print(f"The minimum down payment is: % {min_down_payment}")
# print(f"The down payment amount is: $ {down_payment_amount}")
# print(f"The mortgage insurance price is: $ {insurance_cost}")
# print(f"The total morgage amount is: $ {purchase_price - down_payment_amount + insurance_cost}")
