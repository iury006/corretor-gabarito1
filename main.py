from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from PIL import Image

class CorretorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label_titulo = Label(text="📝 Corretor Offline", font_size='22sp', size_hint_y=None, height=60)
        self.layout.add_widget(self.label_titulo)
        
        self.input_freq = TextInput(hint_text="Nº de Frequência", input_filter="int", multiline=False, size_hint_y=None, height=50)
        self.layout.add_widget(self.input_freq)
        
        self.btn_scan = Button(text="📷 Capturar Gabarito", size_hint_y=None, height=60)
        self.layout.add_widget(self.btn_scan)
        
        self.label_status = Label(text="Aguardando leitura...", font_size='16sp')
        self.layout.add_widget(self.label_status)
        
        return self.layout

if __name__ == '__main__':
    CorretorApp().run()
