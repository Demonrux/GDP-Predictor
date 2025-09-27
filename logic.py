import pandas
import numpy
import matplotlib.pyplot as plt
from category_encoders import TargetEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data_file = (pandas.read_csv('files/gdp_csv.csv')).drop('Country Name', axis=1)

model = None
encoder = None


def train_model():
    global model, encoder

    X = data_file.drop('Value', axis=1)
    y = data_file['Value']
    y_log = numpy.log1p(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y_log, test_size=0.2, random_state=42)

    encoder = TargetEncoder(cols=['Country Code'])
    X_train_encoded = encoder.fit_transform(X_train, y_train)

    model = LinearRegression()
    model.fit(X_train_encoded, y_train)


def predict_gdp(country_code, year):
    input_data = pandas.DataFrame({
        'Country Code': [country_code],
        'Year': [year]
    })

    input_encoded = encoder.transform(input_data)
    prediction_log = model.predict(input_encoded)[0]
    prediction_original = numpy.expm1(prediction_log)

    return prediction_original


def show_plot():

    X = data_file.drop('Value', axis=1)
    y = data_file['Value']
    y_log = numpy.log1p(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y_log, test_size=0.2, random_state=42)

    X_test_encoded = encoder.transform(X_test)
    y_pred_log = model.predict(X_test_encoded)
    y_pred_original = numpy.expm1(y_pred_log)
    y_test_original = numpy.expm1(y_test)

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test_original, y_pred_original, alpha=0.7, c=y_test_original,
                cmap='viridis', edgecolors='black')
    plt.plot([y_test_original.min(), y_test_original.max()],
             [y_test_original.min(), y_test_original.max()])
    plt.xlabel('Real values')
    plt.ylabel('Predicted values')
    plt.title('Real values vs Predicted values')
    plt.colorbar(label='GDP')
    plt.show()


print("Model training...")
train_model()