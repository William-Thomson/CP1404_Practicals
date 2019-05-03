from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKilometreApp(App):
    def build(self):
        """Builds the kivy app"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_increment(self, change):
        """Increases/decreases text input number by one."""
        value = self.is_valid_input() + change
        self.root.ids.input_miles.text = str(value)

    def handle_calculate(self):
        """Converts from miles to km and prints"""
        value = self.is_valid_input() * MILES_TO_KM
        self.root.ids.output_label.text = str(value)

    def is_valid_input(self):
        """Converts input text to float.
        If there is a ValueError, returns 0."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometreApp().run()
