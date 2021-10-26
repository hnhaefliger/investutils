def gordon_growth_model(next_dividends, dividend_growth_rate, rate_of_return):
    price = next_dividends / (rate_of_return - dividend_growth_rate)
    return price

def dividend_discount_model(expected_dividend_per_share, cost_of_capital_equity, dividend_growth_rate):
    price = expected_dividend_per_share / (cost_of_capital_equity - dividend_growth_rate)
    return price
