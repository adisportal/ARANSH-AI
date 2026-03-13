from kivy.app import App
from kivy.uix.label import Label
from plyer import tts, stt
import time

class AranshApp(App):
    def build(self):
        return Label(text="Aransh AI: Ready for boAt Earbuds")

    def on_start(self):
        # This triggers when you long-press the earpod
        self.wake_up_aransh()

    def wake_up_aransh(self):
        try:
            tts.speak("Aransh here. How can I help?")
            # Small delay for Bluetooth switch
            time.sleep(1)
            stt.listen()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    AranshApp().run()
