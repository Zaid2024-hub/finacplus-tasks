def min_units(value, units):
    dp = [float('inf')] * (value + 1)
    dp[0] = 0

    for i in range(1, value + 1):
        for unit in units:
            if i - unit >= 0:
                dp[i] = min(dp[i], dp[i - unit] + 1)
    return dp[value]

def average_units(units):
    total_units = 0
    for amount in range(1, 100):  # From 1 to 99
        total_units += min_units(amount, units)
    avg = total_units / 99
    return round(avg, 2)

if __name__ == "__main__":
    unit_set = [1, 2, 5, 10, 20, 50]
    print("Units:", unit_set)
    print("Average unit usage for 1-99:", average_units(unit_set))
