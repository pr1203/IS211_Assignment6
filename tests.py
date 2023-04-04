import conversions

def test_convertCelsiusToKelvin():
    assert conversions.convertCelsiusToKelvin(-273.15) == 0.0
    assert conversions.convertCelsiusToKelvin(0.0) == 273.15
    assert conversions.convertCelsiusToKelvin(100.0) == 373.15
    assert conversions.convertCelsiusToKelvin(37.0) == 310.15
    assert conversions.convertCelsiusToKelvin(-40.0) == 233.15

def test_convertCelsiusToFahrenheit():
    assert conversions.convertCelsiusToFahrenheit(-273.15) == -459.67
    assert conversions.convertCelsiusToFahrenheit(0.0) == 32.0
    assert conversions.convertCelsiusToFahrenheit(100.0) == 212.0
    assert conversions.convertCelsiusToFahrenheit(37.0) == 98.6
    assert conversions.convertCelsiusToFahrenheit(-40.0) == -40.0

def test_convertFahrenheitToCelsius():
    assert conversions.convertFahrenheitToCelsius(-459.67) == -273.15
    assert conversions.convertFahrenheitToCelsius(32.0) == 0.0
    assert conversions.convertFahrenheitToCelsius(212.0) == 100.0
    assert conversions.convertFahrenheitToCelsius(98.6) == 37.0
    assert conversions.convertFahrenheitToCelsius(-40.0) == -40.0

def test_convertFahrenheitToKelvin():
    assert conversions.convertFahrenheitToKelvin(-459.67) == 0.0
    assert conversions.convertFahrenheitToKelvin(32.0) == 273.15
    assert conversions.convertFahrenheitToKelvin(212.0) == 373.15
    assert conversions.convertFahrenheitToKelvin(98.6) == 310.15
    assert conversions.convertFahrenheitToKelvin(-40.0) == 233.15

def test_convertKelvinToCelsius():
    assert conversions.convertKelvinToCelsius(0.0) == -273.15
    assert conversions.convertKelvinToCelsius(273.15) == 0.0
    assert conversions.convertKelvinToCelsius(373.15) == 100.0
    assert conversions.convertKelvinToCelsius(310.15) == 37.0
    assert conversions.convertKelvinToCelsius(233.15) == -40.0

def test_convertKelvinToFahrenheit():
    assert conversions.convertKelvinToFahrenheit(0.0) == -459.67
    assert conversions.convert

