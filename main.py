"""
Main Application for Personal Expense Tracker
"""

from expense_tracker import ExpenseTracker
from expense_visualizer import ExpenseVisualizer

def main():
    tracker = ExpenseTracker()
    visualizer = ExpenseVisualizer(tracker)
    
    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Show Category Pie Chart")
        print("4. Show Category Bar Chart")
        print("5. Show Monthly Trend")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Enter amount: $"))
                category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
                description = input("Enter description (optional): ").strip()
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == '2':
            tracker.show_summary()
        
        elif choice == '3':
            visualizer.plot_category_pie_chart()
        
        elif choice == '4':
            visualizer.plot_category_bar_chart()
        
        elif choice == '5':
            visualizer.plot_monthly_trend()
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()