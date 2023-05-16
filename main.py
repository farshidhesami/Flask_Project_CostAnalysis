def calculate_discount(cost):
    if cost < 1000:
        return 0.10
    elif 1000 <= cost <= 2000:
        return 0.20
    else:
        return 0.3
    
    
    