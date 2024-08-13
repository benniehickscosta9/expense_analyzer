# Personal Expense Tracker

A simple Python tool to track, analyze, and visualize personal expenses.

## Features

- **Add Expenses**: Record expenses with amount, category, and description
- **View Expenses**: See all recorded expenses in a list format
- **Expense Summary**: Get total expenses broken down by category
- **Visualizations**: 
  - Pie chart showing expense distribution
  - Bar chart comparing categories
  - Monthly trend analysis (with sufficient data)

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

2. Follow the menu prompts:
   - **Option 1**: Add new expenses
   - **Option 2**: View all recorded expenses
   - **Option 3**: See expense summary by category
   - **Option 4**: Generate pie chart visualization
   - **Option 5**: Generate bar chart visualization
   - **Option 6**: View monthly trend (requires multiple entries)
   - **Option 7**: Exit the application

## Data Storage

- Expenses are automatically saved to `expenses.json`
- Data persists between sessions
- File is created automatically when you add your first expense

## Example Categories

- Food
- Transport
- Entertainment
- Utilities
- Shopping
- Healthcare
- Education

## Customization

You can easily modify the categories or add new visualization types by editing the respective Python files.

## Requirements

- Python 3.7+
- matplotlib
- pandas

The tool provides a simple, intuitive interface for personal finance tracking and visualization!