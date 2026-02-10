import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import google.generativeai as genai

# अपनी API Key यहाँ पेस्ट करें
API_KEY = "AIzaSyAwt5Y4K4tZl-iCaLhl96h-3fTCS8X6Ark"
genai.configure(api_key=API_KEY)

class LeoChatApp(App):
    def build(self):
        self.title = "Leo AI"
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.scroll = ScrollView()
        self.chat_history = Label(
            text="[Leo]: नमस्ते! मैं तैयार हूँ। पूछिये क्या पूछना है?\n",
            size_hint_y=None,
            halign='left',
            valign='top',
            markup=True
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll)

        self.input_layout = BoxLayout(size_hint_y=None, height=50, spacing=5)
        self.user_input = TextInput(multiline=False, hint_text="यहाँ लिखें...")
        self.send_button = Button(text="Send", size_hint_x=None, width=80)
        self.send_button.bind(on_press=self.get_ai_response)
        
        self.input_layout.add_widget(self.user_input)
        self.input_layout.add_widget(self.send_button)
        self.layout.add_widget(self.input_layout)

        return self.layout

    def get_ai_response(self, instance):
        query = self.user_input.text
        if not query.strip(): return
        self.chat_history.text += f"\n[You]: {query}\n"
        self.user_input.text = ""

        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(query)
            self.chat_history.text += f"\n[Leo]: {response.text}\n"
        except Exception as e:
            self.chat_history.text += f"\n[Error]: कनेक्शन में दिक्कत है।\n"

if __name__ == "__main__":
    LeoChatApp().run()
