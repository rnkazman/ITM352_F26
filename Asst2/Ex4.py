import pandas as pd
import ssl
import time


#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context


def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Numbner of rows: {len(df)}")
        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None



def display_initial_rows(data):
    """Ask the user how many initial rows to show and print them.

    Accepts a positive integer or 'all'. Invalid entries are reported and
    the user is re-prompted.
    """
    while True:
        response = input(
            f"\nHow many initial rows would you like to see? "
            f"(1-{len(data)}, or 'all'): "
        ).strip().lower()

        if response == "all":
            print(data)
            return

        try:
            num_rows = int(response)
        except ValueError:
            print(f"Invalid input '{response}'. Please enter a whole number or 'all'.")
            continue

        if num_rows < 1:
            print("Please enter a number greater than 0.")
            continue

        if num_rows > len(data):
            print(f"Only {len(data)} rows available; showing all of them.")
            continue

        print(data.head(num_rows))
        return


def show_employees_by_region(data):
    """Print the number of unique employees in each sales region."""
    counts = data.groupby("sales_region")["employee_id"].nunique()
    print("\nNumber of employees by region:")
    print(counts.to_string())


def get_user_selection(options, prompt, required=False, single=False):
    """Prompt for comma-separated option numbers and return the chosen options.

    Re-prompts on invalid input. An empty entry returns [] unless required.
    """
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f"Each number must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))
        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue
        return selected


def generate_custom_pivot_table(data):
    """Interactively build and display a pivot table."""
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "\nSelect rows (required):", required=True)

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (optional, Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print("No numeric columns available to aggregate.")
        return
    values = get_user_selection(value_options, "\nSelect value to aggregate:", required=True, single=True)

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "\nSelect aggregation function:", required=True, single=True)[0]

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func
        )
    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    print(pivot_table)


def show_average_sales_by_region(data):
    """Pivot average sales (quantity * unit_price) by region, with state and sale type sub-columns."""
    required = ["sales_region", "customer_state", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
    )
    print("\nAverage sales by region, by state and sale type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))


def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Average sales by region, by state and sale type", show_average_sales_by_region),
    ("Exit the program", exit_program),
)


def display_menu():
    """Show the menu and return a valid selection as an index into menu_options."""
    while True:
        print("\nSales Data Menu")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"  {number}. {description}")

        choice = input(f"Select an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")


def main():
    csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
    # csv_file = "junk.csv"  # Intentionally incorrect path to test error handling
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    try:
        while True:
            selection = display_menu()
            _, action = menu_options[selection]
            action(sales_data)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
