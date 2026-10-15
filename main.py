"""FinanceIQ: beginner financial analysis project."""


def calculate_profit_margin(revenue, net_income):
    """Return net profit margin as a percentage."""
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")
    return (net_income / revenue) * 100


def main():
    company = "Example Company"
    revenue = 100000
    net_income = 15000
    margin = calculate_profit_margin(revenue, net_income)
    print(f"Company: {company}")
    print(f"Revenue: ${revenue:,.2f}")
    print(f"Net income: ${net_income:,.2f}")
    print(f"Net profit margin: {margin:.2f}%")


if __name__ == "__main__":
    main()
