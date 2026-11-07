
__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.06, 0.15, 0.12, 1)

class SalatiApp(App):

    def build(self):
            root = BoxLayout(
                        orientation="vertical",
                                    padding=18,
                                                spacing=12
                                                        )

                                                                title = Label(
                                                                            text="🕌 صلاتي | SALATI",
                                                                                        font_size="28sp",
                                                                                                    size_hint_y=None,
                                                                                                                height=65
                                                                                                                        )
                                                                                                                                root.add_widget(title)

                                                                                                                                        subtitle = Label(
                                                                                                                                                    text="رفيقك اليومي للصلاة والذكر",
                                                                                                                                                                font_size="16sp",
                                                                                                                                                                            size_hint_y=None,
                                                                                                                                                                                        height=40
                                                                                                                                                                                                )
                                                                                                                                                                                                        root.add_widget(subtitle)

                                                                                                                                                                                                                buttons = [
                                                                                                                                                                                                                            "🕋 مواقيت الصلاة",
                                                                                                                                                                                                                                        "🔊 صوت الأذان",
                                                                                                                                                                                                                                                    "🧭 اتجاه القبلة",
                                                                                                                                                                                                                                                                "📿 الأذكار والسبحة",
                                                                                                                                                                                                                                                                            "⚙️ الإعدادات"
                                                                                                                                                                                                                                                                                    ]

                                                                                                                                                                                                                                                                                            for name in buttons:
                                                                                                                                                                                                                                                                                                        btn = Button(
                                                                                                                                                                                                                                                                                                                        text=name,
                                                                                                                                                                                                                                                                                                                                        font_size="20sp",
                                                                                                                                                                                                                                                                                                                                                        size_hint_y=None,
                                                                                                                                                                                                                                                                                                                                                                        height=65,
                                                                                                                                                                                                                                                                                                                                                                                        background_normal="",
                                                                                                                                                                                                                                                                                                                                                                                                        background_color=(0.15, 0.32, 0.25, 1)
                                                                                                                                                                                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                                                                                                                                                                                                                                root.add_widget(btn)

                                                                                                                                                                                                                                                                                                                                                                                                                                        footer = Label(
                                                                                                                                                                                                                                                                                                                                                                                                                                                    text="نسأل الله أن يجعلنا من المحافظين على الصلاة",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                font_size="13sp",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            size_hint_y=None,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        height=50
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        root.add_widget(footer)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                return root

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    SalatiApp().run()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    