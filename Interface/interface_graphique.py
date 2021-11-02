import Actuariat.actuariat_function as af
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Application(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 2
        self.window.rows = 4



        self.user = Label(
            text="Saisir l'âge : ",
            font_size=20,
        )
        self.window.add_widget(self.user)

        self.age = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
            input_filter="int"
        )
        self.window.add_widget(self.age)

        self.qx = Button(
            text="Probabilité de mourir(qx) : ",
            bold=True,
            background_color=(1, 1, 1, 1)
        )
        self.qx.bind(on_press=self.callback_qx)
        self.window.add_widget(self.qx)

        self.print_qx = Label(
            text="?",
            font_size=20
        )
        self.window.add_widget(self.print_qx)

        self.px = Button(
            text="Probabilité de vivre(px) : ",
            bold=True,
            background_color=(1, 1, 1, 1)
        )
        self.px.bind(on_press=self.callback_px)
        self.window.add_widget(self.px)

        self.print_px = Label(
            text="?",
            font_size=20
        )
        self.window.add_widget(self.print_px)

        self.dx = Button(
            text="nombre de personne décédé: ",
            bold=True,
            background_color=(1, 1, 1, 1)
        )
        self.dx.bind(on_press=self.callback_dx)
        self.window.add_widget(self.dx)

        self.print_dx = Label(
            text="?",
            font_size=20
        )
        self.window.add_widget(self.print_dx)



        return self.window

    def callback_qx(self, instance):
        self.print_qx.text = str(af.qx(int(self.age.text), af.TD_88_90))

    def callback_px(self, instance):
            self.print_px.text = str(af.px(int(self.age.text), af.TD_88_90))

    def callback_dx(self, instance):
            self.print_dx.text = str(af.dx(int(self.age.text), af.TD_88_90))


        #resu = af.qx(n,af.TD_88_90)

if __name__ == "__main__":
    Application().run()
0