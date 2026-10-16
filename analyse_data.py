
from financial_data import financial_data
from main import calculate_profit_margin



def analyze_company():
    previous_revenue = None

    for year, data in financial_data.items():
        revenue = data["revenue"]
        net_income = data["net_income"]

        margin = calculate_profit_margin(
            revenue, net_income
        )

        print(f"Year: {year}")
        print(f"Revenue: ${revenue:,.2f}")
        print(f"Net Income: ${net_income:,.2f}")
        print(f"Profit Margin: {margin:.2f}%")

        if previous_revenue is not None:
            growth = calculate_growth(
                revenue, previous_revenue
            )
            print(f"Revenue Growth: {growth:.2f}%")
        else:
            print("Revenue Growth: N/A")

        previous_revenue = revenue

        print("------------------------")


def calculate_growth(current, previous):
    if previous == 0:
        raise ValueError("Previous value cannot be zero.")

    return ((current - previous) / previous) * 100
if __name__ == "__main__":
    analyze_company()
