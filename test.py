from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (360, 800)

def on_press(btn, textinput, label, colors_dict, i):
    textinput.text = ""
    textinput.insert_text(btn)
    label.text = ""
    label.text = colors_dict[i]

class MyApp(App):
    def build(self):
        layout = RelativeLayout()
        colors = ["#ff0000", "#ff8800", "#ffff00",
                  "#00ff00", "#00ffff", "#0000ff", "#ff00ff"]
        colors_dict = ["красный", "оранжевый", "желтый",
                       "зеленый", "голубой", "синий", "фиолетовый"]
        textinput = TextInput(size_hint=(1, .1), pos_hint={
            'center_x': .5, 'center_y': .75})
        layout.add_widget(textinput)
        label = Label(text='Enter your text here:', size_hint=(
            1, .1), pos_hint={'center_x': .5, 'center_y': .9})
        layout.add_widget(label)
        for i in range(7):
            button = Button(text=str(colors[i]), background_color=colors[i], size_hint=(1, .1),
                            pos_hint={'center_x': .5, 'center_y': .65 - i*.1})
            button.bind(on_press=lambda x, btn=colors[i], textinput=textinput, label=label, colors_dict=colors_dict, i=i: on_press(
                btn, textinput, label, colors_dict, i))
            layout.add_widget(button)
        return layout

if __name__ == '__main__':
    MyApp().run()
