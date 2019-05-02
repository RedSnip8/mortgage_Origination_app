def mortage_calc (rate, term, principal):
    monthly_rate = (rate/100)/12
    if term > 30:
        month_term = term * -1
    else:
        month_term = term * -12
    
    return ((monthly_rate) * principal) / ( 1 - ((
        1 + (monthly_rate)) ** (month_term)
        )) 

print(mortage_calc(6.5, 30, 200_000))