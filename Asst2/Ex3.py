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


def main():
    csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
    # csv_file = "junk.csv"  # Intentionally incorrect path to test error handling
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    # describe the dataframe field data types
    print("\nData types of the dataframe fields:")
    print(sales_data.dtypes)

    try:
        while True:
            display_initial_rows(sales_data)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
