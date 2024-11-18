from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesToKm(App):
    output_label = StringProperty()
    def build(self):
        self.title = "Miles to Km converter"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_calculate(self):
        miles = self.get_valid_miles()
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.miles.text)
            return value
        except ValueError:
            return 0

    def change_counter(self, change):
        result = self.get_valid_miles() + change
        self.root.ids.miles.text = str(result)

ConvertMilesToKm().run()