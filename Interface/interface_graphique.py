import Actuariat.actuariat_function as af
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown


class Application(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 2
        self.window.rows = 5
        self.table = af.tables

        self.choice = Label(
            text="Choix de la table de mortalité",
            font_size=20,
        )
        self.window.add_widget(self.choice)

        ### liste des tables
        dropdown = DropDown()
        tab1 = Button(text="TD_88_90", size_hint_y=None, height=44)
        tab1.bind(on_release=lambda tab1: dropdown.select(tab1.text))
        dropdown.add_widget(tab1)

        tab2 = Button(text="TV_88_90", size_hint_y=None, height=44)
        tab2.bind(on_release=lambda tab2: dropdown.select(tab2.text))
        dropdown.add_widget(tab2)

        self.mainbutton = Button(text="Tables")
        self.mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        self.window.add_widget(self.mainbutton)
        ###

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

    def choix_table(self):
        if self.mainbutton.text == "TD_88_90":
            return af.tables[0]
        elif self.mainbutton.text == "TV_88_90":
            return af.tables[1]

    def callback_qx(self, instance):
        self.print_qx.text = str(af.qx(int(self.age.text), self.choix_table()))
        print(af.qx(10, af.tables[0]))

    def callback_px(self, instance):
        self.print_px.text = str(af.px(int(self.age.text), self.choix_table()))

    def callback_dx(self, instance):
        self.print_dx.text = str(af.dx(int(self.age.text), self.choix_table()))


if __name__ == "__main__":
    Application().run()
