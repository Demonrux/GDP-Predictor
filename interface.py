from logic import predict_gdp, data_file, show_plot


def console_interface():
    min_year = data_file['Year'].min()
    max_year = data_file['Year'].max()
    available_countries = data_file['Country Code'].unique()

    print("Available country codes:")
    print(available_countries)

    while True:
        country = input("\nEnter country code ('quit' to exit): ").strip().upper()

        if country.lower() == 'quit':
            print("Exiting the program...")
            break

        if country not in available_countries:
            print(f"Error! Country '{country}' not found in the data.")
            continue

        try:
            year = int(input(f"Enter year({min_year}-{max_year}): "))
        except ValueError:
            print("Error: Incorrect year.")
            continue

        if year < min_year or year > max_year:
            print(f"Error: Year {year} goes beyond data boundaries ({min_year}-{max_year})")
            continue

        try:
            prediction = predict_gdp(country, year)
            print(f"\nPrediction for  {country} in {year} year:")
            print(f"{prediction:,.2f}")

            real_data = data_file[(data_file['Country Code'] == country) & (data_file['Year'] == year)]
            if not real_data.empty:
                real_value = real_data['Value'].iloc[0]
                print(f"Real value: {real_value:,.2f} $")
                error_percent = abs(prediction - real_value) / real_value * 100
                print(f"Prediction error: {error_percent:.2f}%")
                show_plot()

        except Exception as error:
            print(f"Error: {error}")