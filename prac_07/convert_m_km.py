from kivy.app import App
from kivy.lang import Builder


class MilesToKilometreApp(App):
    def build(self):
        """Builds the kivy app"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_increment(self, change):
        """Increases/decreases text input number by one."""
        value = float(self.root.ids.input_miles.text) + change
        self.root.ids.input_miles.text = str(value)

MilesToKilometreApp().run()
