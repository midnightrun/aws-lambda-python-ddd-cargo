from matte import *
from matte.jso import jso
import unittest

class TestMatte(unittest.TestCase):
    def setUp(self):
        self.event = jso({
            "lastEvent": {
                "location": "DEF",
                "voyageId": "XYZ",
                "eventType": "UNLOAD",
                "completionTime": 1526897537633,
            },
            "itinerary": [
                {
                "loadLocation": "ABC",
                "unloadLocation": "DEF",
                "unloadTime": 1526897537633,
                "voyageId": "XYZ"
                },
                {
                "loadLocation": "DEF",
                "loadTime": 1526897537633,
                "voyageId": "STU"
                }    
            ]
        })

    def test_string(self):
        self.assertTrue(isinstance(self.event.lastEvent.location, str))

    def test_integer(self):
        self.assertTrue(isinstance(self.event.lastEvent.completionTime, int))

    def test_len(self):
        self.assertEqual(2, len(self.event.itinerary))

    def test_find(self):
        leg, it = find(lambda leg: leg.voyageId == 'STU', self.event.itinerary)
        self.assertEqual('DEF', leg.loadLocation)
        self.assertIsNone(next(it, None))

    def test_drop(self):
        self.assertEqual({'a': 1}, drop_nulls({'a': 1, 'b': None}))

if __name__ == '__main__':
    unittest.main()



