"""
Expense Visualization Module
Creates charts and graphs for expense analysis
"""

import matplotlib.pyplot as plt
import seaborn as sns

class ExpenseVisualizer:
    def __init__(self, expense_tracker):
        self.tracker = expense_tracker
    
    def plot_category_pie_chart(self):
        """Create a pie chart of expenses by category"""
        categories = self.tracker.get_expenses_by_category()
        
        if not categories:
            print("No expenses to visualize.")
            return
        
        plt.figure(figsize=(10, 8))
        plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=90)
        plt.title('Expenses by Category')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    
    def plot_category_bar_chart(self):
        """Create a bar chart of expenses by category"""
        categories = self.tracker.get_expenses_by_category()
        
        if not categories:
            print("No expenses to visualize.")
            return
        
        plt.figure(figsize=(12, 6))
        categories_sorted = dict(sorted(categories.items(), key=lambda x: x[1], reverse=True))
        
        plt.bar(categories_sorted.keys(), categories_sorted.values())
        plt.title('Expenses by Category')
        plt.xlabel('Categories')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_monthly_trend(self):
        """Plot monthly expense trend (simplified)"""
        expenses = self.tracker.expenses
        
        if not expenses:
            print("No expenses to visualize.")
            return
        
        # Group by month (simplified - using first 7 characters of date)
        monthly_expenses = {}
        for expense in expenses:
            month = expense['date'][:7]  # YYYY-MM
            if month not in monthly_expenses:
                monthly_expenses[month] = 0
            monthly_expenses[month] += expense['amount']
        
        plt.figure(figsize=(12, 6))
        months_sorted = sorted(monthly_expenses.keys())
        amounts = [monthly_expenses[month] for month in months_sorted]
        
        plt.plot(months_sorted, amounts, marker='o', linewidth=2, markersize=8)
        plt.title('Monthly Expense Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Expenses ($)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()