import logic


def console_interface():
    print("Model training...")
    logic.train_model()
    min_year = logic.data_file['Year'].min()
    max_year = logic.data_file['Year'].max()
    available_countries = logic.data_file['Country Code'].unique()

    print("Available country codes:")
    print(available_countries)

    while True:
        country = input("\nEnter country code ('quit' to exit, 'graph' to view the model graph): ").strip().upper()

        if country.lower() == 'quit':
            print("Exiting the program...")
            break

        if country.lower() == 'graph':
            logic.show_plot()
            continue

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
            prediction = logic.predict_gdp(country, year)
            print(f"\nPrediction for  {country} in {year} year:")
            print(f"{prediction:,.2f}")

            real_data = logic.data_file[(logic.data_file['Country Code'] == country)
                                        & (logic.data_file['Year'] == year)]
            if not real_data.empty:
                real_value = real_data['Value'].iloc[0]
                print(f"Real value: {real_value:,.2f} $")
                error_percent = abs(prediction - real_value) / real_value * 100
                print(f"Prediction error: {error_percent:.2f}%")

        except Exception as error:
            print(f"Error: {error}")