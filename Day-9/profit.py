def calculate_profit_loss(N, stock_info, M, stock_prices, time):
    realized_pl = 0
    unrealized_pl = 0

    for i in range(N):
        quantity_bought, time_of_purchase, time_of_sell = stock_info[i]
        if time_of_sell <= time:
            realized_pl += quantity_bought * (stock_prices[i][time_of_sell - 1] - stock_prices[i][time_of_purchase - 1])
        else:
            unrealized_pl += quantity_bought * (stock_prices[i][-1] - stock_prices[i][time_of_purchase - 1])

    return realized_pl, unrealized_pl

# Reading input
N = int(input())
stock_info = []
for _ in range(N):
    stock_info.append(list(map(int, input().split())))

M = int(input())
stock_prices = []
for _ in range(N):
    stock_prices.append(list(map(int, input().split())))

time = int(input())

# Calculating P/L
realized_pl, unrealized_pl = calculate_profit_loss(N, stock_info, M, stock_prices, time)

# Printing output
print(realized_pl)
print(unrealized_pl)
