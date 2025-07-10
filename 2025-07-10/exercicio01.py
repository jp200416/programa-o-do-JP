import sys

if __name__ == "__main__":
    csv_file = 'cotacao_dolar.csv'
    processed_data = []

    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            header = file.readline() 

            for line in file:
                row = line.strip().split(';')
                
                if len(row) == 3: 
                    try:
                        buy_value = float(row[0].replace(',', '.'))
                        sell_value = float(row[1].replace(',', '.'))
                        cotation_date_str = row[2] 
                        processed_data.append([buy_value, sell_value, cotation_date_str])
                    except ValueError as ve:
                        print(f"Skipping row due to data conversion error: {row} - {ve}")
                else:
                    print(f"Skipping malformed row: {row}")
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    if processed_data:
        print("Processed Dolar Cotation Data:")
        for item in processed_data:
            print(item)
    else:
        print("No data was processed or the file could not be read.")