from kivy.app import App
from kivy.lang import Builder


class MilesToKilometreApp(App):
    def build(self):
        """Builds the kivy app"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root


MilesToKilometreApp().run()
