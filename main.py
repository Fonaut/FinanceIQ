
"""FinanceIQ: beginner financial analysis project."""


def calculate_profit_margin(revenue, net_income):
    """Return net profit margin as a percentage."""
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")

    return (net_income / revenue) * 100


def calculate_roa(net_income, average_assets):
    """Return return on assets as a percentage."""
    if average_assets <= 0:
        raise ValueError("Average assets must be greater than zero.")

    return (net_income / average_assets) * 100


def calculate_roe(net_income, average_equity):
    """Return return on equity as a percentage."""
    if average_equity <= 0:
        raise ValueError("Average equity must be greater than zero.")

    return (net_income / average_equity) * 100


def main():
    company = "Example Company"
    revenue = 100000
    net_income = 15000
    average_assets = 250000
    average_equity = 120000

    margin = calculate_profit_margin(revenue, net_income)
    roa = calculate_roa(net_income, average_assets)
    roe = calculate_roe(net_income, average_equity)

    print(f"Company: {company}")
    print(f"Revenue: ${revenue:,.2f}")
    print(f"Net income: ${net_income:,.2f}")
    print(f"Net profit margin: {margin:.2f}%")
    print(f"Return on Assets: {roa:.2f}%")
    print(f"Return on Equity: {roe:.2f}%")


if __name__ == "__main__":
    main()