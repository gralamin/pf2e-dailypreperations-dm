import unittest
import unittest
import weather


# These tests are coverage to ensure all code paths are run
class TestWeather(unittest.TestCase):
    def testRandomPrecipitation(self):
        def mockRoller(min, max):
            return 20

        weather.random_precipitation(weather.Season.SUMMER, roller=mockRoller)

    def testRandomPrecipitationWinter(self):
        def mockRoller(min, max):
            return 1

        weather.random_precipitation(weather.Season.WINTER, roller=mockRoller)

    def testRandomTemp(self):
        def mockRoller(min, max):
            return 20

        weather.random_temp(weather.Season.SUMMER, True, roller=mockRoller)

    def testRandomTempWinter(self):
        def mockRoller(min, max):
            return 20

        weather.random_temp(weather.Season.WINTER, False, roller=mockRoller)

    def testRandomTempSpring(self):
        def mockRoller(min, max):
            return 20

        weather.random_temp(weather.Season.SPRING, False, roller=mockRoller)

    def testRandomWeather(self):
        def mockRoller(min, max):
            return 20

        weather.random_weather(weather.Season.SPRING, False, 5, roller=mockRoller)


if __name__ == "__main__":
    unittest.main()
