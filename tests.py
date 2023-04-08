import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvintoFahrenheit
from conversions import convertKelvintoCelsius
from conversions_refactored import convert
from conversions_refactored import ConversionNotPossible


class ConversionsCheck(unittest.TestCase):

    # Tests that fail
    def test_convertCelsiusToKelvin_0(self):
        value = convertCelsiusToKelvin(10)
        expected = 35
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToKelvin_00(self):
        value = convertCelsiusToKelvin(20)
        expected =79
        self.assertAlmostEqual(value, expected, delta=0.01)

    # C to K
    def test_convertCelsiusToKelvin(self):
        test_cases = [(0, 273.15), (100, 373.15), (200, 473.15), (300, 573.15), (400, 673.15)]
        for temp, expected in test_cases:
            value = convertCelsiusToKelvin(temp)
            self.assertAlmostEqual(value, expected, delta=0.01)

    # C to F
    def test_convertCelsiusToFahrenheit(self):
        test_cases = [(0, 32), (200, 392), (300, 572), (400, 752), (500, 932)]
        for celsius, fahrenheit in test_cases:
            with self.subTest(celsius=celsius, fahrenheit=fahrenheit):
                value = convertCelsiusToFahrenheit(celsius)
                self.assertAlmostEqual(value, fahrenheit, delta=0.01)

    # F to C
    def test_convertFahrenheitToCelsius(self):
        test_cases = [(0, -17.78), (200., 93.33), (300., 148.88), (400., 204.44), (500., 260)]
        for value, expected in test_cases:
            self.assertAlmostEqual(convertFahrenheitToCelsius(value), expected, delta=0.01)

    # F to K
    def test_convertFahrenheitToKelvin(self):
        test_cases = [(0, 255.37), (200, 366.48), (300, 422.03), (400, 477.59), (500, 533.15)]
        for value, expected in test_cases:
            self.assertAlmostEqual(convertFahrenheitToKelvin(value), expected, delta=0.01)

    # K to F
    def test_convertKelvintoFahrenheit(self):
        test_cases = [(0, -459.67), (200, -99.67), (300, 80.33), (400, 260.33), (500, 440.33)]
        for value, expected in test_cases:
            result = convertKelvintoFahrenheit(value)
            self.assertAlmostEqual(result, expected, delta=0.01)

    # K to C
    def test_convertKelvintoCelsius(self):
        test_cases = [(0, -273.15), (200, -73.15), (300, 26.85), (400, 126.85), (500, 226.85)]
        for value, expected in test_cases:
            self.assertAlmostEqual(convertKelvintoCelsius(value), expected, delta=0.01)

    # C to K
    def test_convert_CelsiusToKelvin(self):
        test_cases = [(0, 273.15), (200, 473.15), (300, 573.15), (400, 673.15), (500, 773.15)]
        for value, expected in test_cases:
            result = convert("Celsius", "Kelvin", value)
            self.assertAlmostEqual(result, expected, delta=0.01)

    # Yrd to M
    def test_convert_YardsToMeters(self):
        tests = [(50, 45.72), (100, 91.44), (250, 228.6), (500, 457.2), (1000, 914.4)]
        for value, expected in tests:
            result = convert("Yards", "Meters", value)
            self.assertAlmostEqual(result, expected, delta=0.01)

    # Yrd to Mi
    def test_convert_YardsToMiles(self):
        test_cases = [(50, 0.0284091), (100, 0.0568182), (250, 0.142045), (500, 0.284091), (1000, 0.568182)]
        for value, expected in test_cases:
            result = convert("Yards", "Miles", value)
            self.assertAlmostEqual(result, expected, delta=0.01)

    # M to Yrd
    def test_convert_MetersToYards(self):
        test_cases = [(50, 54.68065), (100, 109.361), (250, 273.40325), (500, 546.807), (1000, 1093.61)]
        for input_val, expected_val in test_cases:
            output_val = convert("Meters", "Yards", input_val)
            self.assertAlmostEqual(output_val, expected_val, delta=0.01)

    # M to Mi
    def test_convert_MetersToMiles(self):
        test_cases = [(50, 0.0310686), (100, 0.0621371), (250, 0.155342), (500, 0.310686), (1000, 0.621371)]
        for input_val, expected_val in test_cases:
            output_val = convert("Meters", "Miles", input_val)
            self.assertAlmostEqual(output_val, expected_val, delta=0.01)

    # Mi to Yrd
    def test_convert_MilesToYards(self):
        test_cases = [(50, 88000), (100, 176000), (250, 440000), (500, 880000), (1000, 1760000)]
        for input_val, expected_val in test_cases:
            output_val = convert("Miles", "Yards", input_val)
            self.assertAlmostEqual(output_val, expected_val, delta=0.01)

    # Mi to M
    def test_convert_MilesToMeters(self):
        test_cases = [(1, 1609.34), (50, 80467.2), (250, 402336), (500, 804672), (1000, 1609344)]
        for distance, expected in test_cases:
            value = convert("Miles", "Meters", distance)
            self.assertAlmostEqual(value, expected, delta=0.01)

    # incompatible

    def test_conversion_not_possible(self):
        with self.assertRaises(ConversionNotPossible):
            convert('FAHRENHEIT', 'METERS', 10)


if __name__ == '__main__':
    unittest.main()
