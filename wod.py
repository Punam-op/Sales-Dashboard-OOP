import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDashboard:

    # Constructor
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_excel(file_name)

    # Data show
    def show_data(self):
        print(self.df)
        print("\nColumns:")
        print(self.df.columns)

    # Product Wise Quantity
    def product_quantity(self):
        self.pro_quan = (
            self.df.groupby("Product")["Quantity"]
            .sum()
            .reset_index()
        )

    # Discount Wise Sales
    def discount_sales(self):
        self.sal_dis = (
            self.df.groupby("Discount")["Sales"]
            .sum()
            .reset_index()
        )

    # Product Wise Profit
    def product_profit(self):
        self.product_profit_df = (
            self.df.groupby("Product")["Profit"]
            .sum()
            .reset_index()
        )

    # Product Wise Sales
    def product_sales(self):
        self.product_sales_df = (
            self.df.groupby("Product")["Sales"]
            .sum()
            .reset_index()
        )

    # Create Dashboard
    def create_dashboard(self):

        # Calculations
        self.product_quantity()
        self.discount_sales()
        self.product_profit()
        self.product_sales()

        # Dashboard
        plt.figure(figsize=(12, 8))

        # -------------------------
        # 1st Graph
        # -------------------------
        plt.subplot(2, 2, 1)

        sns.barplot(
            data=self.pro_quan,
            x="Product",
            y="Quantity"
        )

        plt.title("Product Wise Quantity")
        plt.xticks(rotation=45)

        # -------------------------
        # 2nd Graph
        # -------------------------
        plt.subplot(2, 2, 2)

        sns.lineplot(
            data=self.sal_dis,
            x="Discount",
            y="Sales",
            marker="o"
        )

        plt.grid(axis="y")
        plt.title("Discount Wise Sales")
        plt.xticks(rotation=45)

        # -------------------------
        # 3rd Graph
        # -------------------------
        plt.subplot(2, 2, 3)

        plt.pie(
            self.product_profit_df["Profit"],
            labels=self.product_profit_df["Product"],
            autopct="%1.1f%%",
            startangle=90,
            explode=[0.05] * len(self.product_profit_df)
        )

        plt.title("Product Wise Profit Share")

        # -------------------------
        # 4th Graph
        # -------------------------
        plt.subplot(2, 2, 4)

        sns.barplot(
            data=self.product_profit_df,
            x="Product",
            y="Profit"
        )

        plt.title("Product Wise Profit")
        plt.xticks(rotation=45)

        # Dashboard show
        plt.tight_layout()
        plt.show()


# =================================
# Object Creation
# =================================

dashboard = SalesDashboard("Word.xlsx")

# Data dekhna
dashboard.show_data()

# Dashboard banana
dashboard.create_dashboard()