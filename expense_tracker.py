"""
Simple Personal Expense Tracker
A tool to analyze and visualize personal expenses
"""

import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

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
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': float(amount),
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Expense added: ${amount} for {category}")
    
    def view_expenses(self):
        """Display all expenses"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print("\n--- All Expenses ---")
        for expense in self.expenses:
            print(f"ID: {expense['id']} | Date: {expense['date']} | "
                  f"Amount: ${expense['amount']} | Category: {expense['category']} | "
                  f"Description: {expense['description']}")
    
    def get_summary(self):
        """Get expense summary by category"""
        if not self.expenses:
            return {}
        
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            summary[category] = summary.get(category, 0) + amount
        
        return summary
    
    def show_summary(self):
        """Display expense summary"""
        summary = self.get_summary()
        if not summary:
            print("No expenses to summarize.")
            return
        
        print("\n--- Expense Summary ---")
        total = 0
        for category, amount in summary.items():
            print(f"{category}: ${amount:.2f}")
            total += amount
        
        print(f"\nTotal Expenses: ${total:.2f}")
        return summary