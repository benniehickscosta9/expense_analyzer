"""
Main Application for Personal Expense Tracker
Provides a simple menu-driven interface
"""

from expense_tracker import ExpenseTracker
from expense_visualizer import ExpenseVisualizer

def main():
    tracker = ExpenseTracker()
    visualizer = ExpenseVisualizer(tracker)
    
    while True:
        print("\n" + "="*50)
        print("      PERSONAL EXPENSE TRACKER")
        print("="*50)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Show Expense Summary")
        print("4. View Category Pie Chart")
        print("5. View Category Bar Chart")
        print("6. View Monthly Trend")
        print("7. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            print("\n--- Add New Expense ---")
            try:
                amount = float(input("Enter amount: $"))
                category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
                description = input("Enter description (optional): ").strip()
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        
        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            tracker.show_summary()
        
        elif choice == '4':
            print("Generating Pie Chart...")
            visualizer.plot_category_pie_chart()
        
        elif choice == '5':
            print("Generating Bar Chart...")
            visualizer.plot_category_bar_chart()
        
        elif choice == '6':
            print("Generating Monthly Trend...")
            visualizer.plot_monthly_trend()
        
        elif choice == '7':
            print("Thank you for using Personal Expense Tracker!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-7.")

if __name__ == "__main__":
    main()