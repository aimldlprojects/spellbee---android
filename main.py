from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout  # Import AnchorLayout

from kivy.core.text import LabelBase
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
import os

# Register a custom font (optional)
font_path = os.path.join(r'C:\Users\eswar\AppData\Local\Microsoft\Windows\Fonts', 'Roboto-Regular.ttf')
LabelBase.register(name='Roboto', fn_regular=font_path)

# Define some styles
def styled_button(text):
    return Button(text=text, size_hint=(None, None), size=(dp(150), dp(50)), font_name='Roboto', background_color=get_color_from_hex("#1e88e5"))

def styled_spinner(text, values):
    spinner = Spinner(text=text, values=values, size_hint=(None, None), size=(dp(150), dp(50)), font_name='Roboto', background_color=get_color_from_hex("#005cb2"))
    return spinner

def styled_label(text):
    return Label(text=text, font_name='Roboto', font_size='20sp', size_hint=(None, None), size=(dp(150), dp(40)), color=get_color_from_hex("#212121"))

class TestOptionsScreen(Screen):
    def __init__(self, **kwargs):
        super(TestOptionsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Adding styled widgets
        layout.add_widget(styled_label('User ID'))
        layout.add_widget(styled_spinner('Select User', ['User1', 'User2', 'User3']))

        layout.add_widget(styled_label('Test Type'))
        layout.add_widget(styled_spinner('Select Test Type', ['Type1', 'Type2', 'Type3']))

        layout.add_widget(styled_label('Word Type'))
        layout.add_widget(styled_spinner('Select Word Type', ['TypeA', 'TypeB', 'TypeC']))

        layout.add_widget(styled_label('Word Length'))
        layout.add_widget(styled_spinner('Select Word Length', ['Length1', 'Length2', 'Length3']))

        # Using AnchorLayout for aligning button text to left and button to right
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        start_test_btn = styled_button('Start Test')
        start_test_btn.bind(on_press=self.start_test)
        anchor_layout.add_widget(start_test_btn)
        layout.add_widget(anchor_layout)

        self.add_widget(layout)

    def start_test(self, instance):
        self.manager.current = 'test_screen'

class TestScreen(Screen):
    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        layout.add_widget(styled_label('This is the test page'))

        back_btn = styled_button('Back to Options')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'test_options_screen'

class SpellBeeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TestOptionsScreen(name='test_options_screen'))
        sm.add_widget(TestScreen(name='test_screen'))
        return sm

if __name__ == '__main__':
    SpellBeeApp().run()
