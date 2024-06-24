
def month_to_season(month):
    if month in [12,1,2]:
        return "winter"
    elif month in [3,4,5]:
        return "spring"
    elif month in [6,7,8]:
        return "summer"
    elif month in [9,10,11]:
        return "outumn"
    else:
        return "incorrect month"
print(month_to_season(9))
print(month_to_season(5))
print(month_to_season(20))