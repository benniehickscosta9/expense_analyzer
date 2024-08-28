# Personal Expense Tracker

A simple Python tool to analyze and visualize personal expenses.

## Installation

1. Ensure you have Python 3.7+ installed
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the menu options:
   - **Add Expense**: Record new expenses with amount, category, and optional description
   - **View Summary**: See total expenses and breakdown by category
   - **Show Category Pie Chart**: Visualize expense distribution as pie chart
   - **Show Category Bar Chart**: View expenses by category as bar chart
   - **Show Monthly Trend**: See expense trends over time
   - **Exit**: Close the application

## Features

- **Data Persistence**: Expenses are automatically saved to `expenses.json`
- **Category Analysis**: Group and analyze expenses by category
- **Visualizations**: Multiple chart types for better insights
- **Simple Interface**: Easy-to-use text-based menu
- **Trend Analysis**: View monthly spending patterns

## File Structure

- `expense_tracker.py` - Core expense management functionality
- `expense_visualizer.py` - Chart and graph creation
- `main.py` - Main application interface
- `expenses.json` - Data storage (created automatically)
- `requirements.txt` - Required Python packages

## Example Usage

```
=== PERSONAL EXPENSE TRACKER ===
1. Add Expense
2. View Summary
3. Show Category Pie Chart
4. Show Category Bar Chart
5. Show Monthly Trend
6. Exit

Enter your choice (1-6): 1
Enter amount: $25.50
Enter category (e.g., Food, Transport, Entertainment): Food
Enter description (optional): Lunch at restaurant
Expense added: $25.5 for Food
```

The tool will help you track and understand your spending patterns through both numerical summaries and visual charts!