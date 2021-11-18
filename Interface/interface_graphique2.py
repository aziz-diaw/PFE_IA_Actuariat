import Actuariat.probabilities_one_insured as poi
import Table.tables as table

from tkinter import *
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window


# finitions des fonctions
def petitFormat():
    class Application(App):
        def build(self):
            self.window = GridLayout()
            self.window.cols = 2
            self.window.rows = 8
            self.table = table.tables
            Window.clearcolor = (126 / 255, 147 / 255, 97 / 255, 1)

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

            tab3 = Button(text="TH_00_02", size_hint_y=None, height=44)
            tab3.bind(on_release=lambda tab3: dropdown.select(tab3.text))
            dropdown.add_widget(tab3)

            tab4 = Button(text="TF_00_02", size_hint_y=None, height=44)
            tab4.bind(on_release=lambda tab4: dropdown.select(tab4.text))
            dropdown.add_widget(tab4)

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

            self.saisie_n = Label(
                text="Saisir le nombre d'année n à ajouter : ",
                font_size=20,
            )
            self.window.add_widget(self.saisie_n)

            self.n = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="int"
            )
            self.window.add_widget(self.n)

            self.px = Button(
                text="Probabilité de vivre à l'âge saisi : ",
                bold=True,
                background_color=(1, 0.0, 0.0, 1)
            )
            self.px.bind(on_press=self.callback_px)
            self.window.add_widget(self.px)

            self.print_px = Label(
                text="?",
                font_size=20
            )
            self.window.add_widget(self.print_px)

            return self.window

        def choix_table(self):
            if self.mainbutton.text == "TD_88_90":
                return table.tables[0]
            elif self.mainbutton.text == "TV_88_90":
                return table.tables[1]
            elif self.mainbutton.text == "TH_00_02":
                return table.tables[2]
            elif self.mainbutton.text == "TF_00_02":
                return table.tables[3]

        def callback_px(self, instance):
            self.print_px.text = str(poi.px(int(self.age.text), self.choix_table()))

    Application().run()


def formatNormal():
    from kivy.uix.screenmanager import ScreenManager, Screen

    # class CheckProfil(Screen):
    # pass

    # class Profil_1(Screen):
    # pass

    # class WindowManager(ScreenManager):
    # pass

    class Application(App):
        def build(self):
            self.window = GridLayout()
            self.window.cols = 2
            self.window.rows = 8
            self.table = table.tables
            Window.clearcolor = (126 / 255, 147 / 255, 97 / 255, 1)

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

            tab3 = Button(text="TH_00_02", size_hint_y=None, height=44)
            tab3.bind(on_release=lambda tab3: dropdown.select(tab3.text))
            dropdown.add_widget(tab3)

            tab4 = Button(text="TF_00_02", size_hint_y=None, height=44)
            tab4.bind(on_release=lambda tab4: dropdown.select(tab4.text))
            dropdown.add_widget(tab4)

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

            self.saisie_n = Label(
                text="Saisir le nombre d'année n à ajouter : ",
                font_size=20,
            )
            self.window.add_widget(self.saisie_n)

            self.n = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="int"
            )
            self.window.add_widget(self.n)

            self.qx = Button(
                text="Probabilité de mourir à l'âge saisi : ",
                bold=True,
                background_color=(0.0, 0.0, 1, 1)
            )
            self.qx.bind(on_press=self.callback_qx)
            self.window.add_widget(self.qx)

            self.print_qx = Label(
                text="?",
                font_size=20
            )
            self.window.add_widget(self.print_qx)

            return self.window

        def choix_table(self):
            if self.mainbutton.text == "TD_88_90":
                return table.tables[0]
            elif self.mainbutton.text == "TV_88_90":
                return table.tables[1]
            elif self.mainbutton.text == "TH_00_02":
                return table.tables[2]
            elif self.mainbutton.text == "TF_00_02":
                return table.tables[3]

        def callback_qx(self, instance):
            self.print_qx.text = str(poi.qx(int(self.age.text), self.choix_table()))

    Application().run()


def grandFormat():
    fen_princ.geometry('1200x800')


def fondClair():
    fen_princ.config(bg='ivory')


def fondSombre():
    fen_princ.config(bg='black')


# Création de la fenêtre
fen_princ = Tk()
fen_princ.title("Mon application à moi que j'ai")
fen_princ.geometry("900x600")

# Création du cadre-conteneur pour les menus
zoneMenu = Frame(fen_princ, borderwidth=3, bg='#557788')
zoneMenu.pack(fill=X)

# Création de l'onglet Fichier
menuAssureur = Menubutton(zoneMenu, text='Assureur', width='20', borderwidth=2, bg='gray',
                          activebackground='darkorange', relief=RAISED)
menuAssureur.grid(row=0, column=0)

# Création de l'onglet Affichage
menuAssuré = Menubutton(zoneMenu, text='Assuré', width='20', borderwidth=2, bg='gray', activebackground='darkorange',
                        relief=RAISED)
menuAssuré.grid(row=0, column=3)

# Création d'un menu défilant
menuDeroulant1 = Menu(menuAssureur, tearoff=0)
menuDeroulant1.add_command(label='px', command=petitFormat)
menuDeroulant1.add_command(label="qx", command=formatNormal)
menuDeroulant1.add_command(label="dx", command=grandFormat)
menuDeroulant1.add_command(label="npx", command=fondClair)
menuDeroulant1.add_command(label="nqx", command=fondSombre)

# Attribution du menu déroulant au menu Affichage
menuAssureur.configure(menu=menuDeroulant1)

# Lancement de la surveillance sur la widget
fen_princ.mainloop()
