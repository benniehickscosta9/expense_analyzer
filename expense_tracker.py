"""
Simple Personal Expense Tracker
A tool to analyze and visualize personal expenses
"""

import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

class ExpenseTracker:
    def __init__(self, data_file="expenses.json"):
        self.data_file = data_file
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=2)
    
    def add_expense(self, amount, category, description=""):
        """Add a new expense"""
        expense = {
            'id': len(self.expenses) + 1,
            'amount': float(amount),
            'category': category,
            'description': description,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Expense added: ${amount} for {category}")
    
    def get_total_expenses(self):
        """Calculate total expenses"""
        return sum(expense['amount'] for expense in self.expenses)
    
    def get_expenses_by_category(self):
        """Group expenses by category"""
        categories = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in categories:
                categories[category] = 0
            categories[category] += expense['amount']
        return categories
    
    def get_recent_expenses(self, days=7):
        """Get expenses from the last N days"""
        cutoff_date = datetime.now() - timedelta(days=days)
        recent = []
        for expense in self.expenses:
            expense_date = datetime.strptime(expense['date'], "%Y-%m-%d %H:%M:%S")
            if expense_date >= cutoff_date:
                recent.append(expense)
        return recent
    
    def show_summary(self):
        """Display expense summary"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        total = self.get_total_expenses()
        categories = self.get_expenses_by_category()
        
        print("\n=== EXPENSE SUMMARY ===")
        print(f"Total Expenses: ${total:.2f}")
        print(f"Number of Expenses: {len(self.expenses)}")
        print("\nBy Category:")
        for category, amount in categories.items():
            percentage = (amount / total) * 100
            print(f"  {category}: ${amount:.2f} ({percentage:.1f}%)")