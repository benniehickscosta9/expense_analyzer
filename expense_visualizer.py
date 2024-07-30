"""
Expense Visualization Module
Creates charts and graphs for expense analysis
"""

import matplotlib.pyplot as plt
import pandas as pd
from expense_tracker import ExpenseTracker

class ExpenseVisualizer:
    def __init__(self, tracker):
        self.tracker = tracker
    
    def plot_category_pie_chart(self):
        """Create a pie chart of expenses by category"""
        summary = self.tracker.get_summary()
        if not summary:
            print("No data to visualize.")
            return
        
        categories = list(summary.keys())
        amounts = list(summary.values())
        
        plt.figure(figsize=(10, 8))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title('Expense Distribution by Category')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    
    def plot_category_bar_chart(self):
        """Create a bar chart of expenses by category"""
        summary = self.tracker.get_summary()
        if not summary:
            print("No data to visualize.")
            return
        
        categories = list(summary.keys())
        amounts = list(summary.values())
        
        plt.figure(figsize=(12, 6))
        bars = plt.bar(categories, amounts, color='skyblue', edgecolor='black')
        plt.title('Expenses by Category')
        plt.xlabel('Categories')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        
        # Add value labels on bars
        for bar, amount in zip(bars, amounts):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    f'${amount:.2f}', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
    
    def plot_monthly_trend(self):
        """Plot monthly expense trend (if enough data exists)"""
        if len(self.tracker.expenses) < 2:
            print("Not enough data for trend analysis.")
            return
        
        # Convert to DataFrame for easier date handling
        df = pd.DataFrame(self.tracker.expenses)
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M')
        
        monthly_expenses = df.groupby('month')['amount'].sum()
        
        plt.figure(figsize=(12, 6))
        monthly_expenses.plot(kind='line', marker='o', linewidth=2, markersize=8)
        plt.title('Monthly Expense Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Expenses ($)')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()