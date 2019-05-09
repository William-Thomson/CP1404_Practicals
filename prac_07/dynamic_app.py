from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["William", "Lindsay", "Somebody"]

    def build(self):
        self.title = "Dynamic Widget App"
        self.root = Builder.load_file('dynamic_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)
