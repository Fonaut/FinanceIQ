
import matplotlib.pyplot as plt
from financial_data import financial_data


def create_financial_chart():
    # Get the years from our financial dataset
    years = list(financial_data.keys())

    # Get revenue for each year
    revenues = [
        data["revenue"]
        for data in financial_data.values()
    ]

    # Get net income for each year
    net_incomes = [
        data["net_income"]
        for data in financial_data.values()
    ]

    # Create the chart
    plt.figure(figsize=(10, 6))

    # Plot revenue
    plt.plot(
        years,
        revenues,
        marker="o",
        linewidth=2,
        label="Revenue"
    )

    # Plot net income
    plt.plot(
        years,
        net_incomes,
        marker="s",
        linewidth=2,
        label="Net Income"
    )

    # Add chart title and labels
    plt.title("FinanceIQ: Revenue vs Net Income")
    plt.xlabel("Year")
    plt.ylabel("Amount ($)")

    # Display whole years on the x-axis
    plt.xticks(years)

    # Add legend and grid
    plt.legend()
    plt.grid(True)

    # Adjust spacing
    plt.tight_layout()

    # Save the chart
    plt.savefig("financial_comparison.png")

    # Display the chart
    plt.show()


if __name__ == "__main__":
    create_financial_chart()
