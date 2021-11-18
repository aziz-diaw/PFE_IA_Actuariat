import Actuariat.probabilities_one_insured as poi
import Table.tables as table

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window


class Application(App):
    def liste_proba_on_insured(self,assu_fct):
        assu_fct = DropDown()

        fct1 = Button(text="px", size_hint_y=None, height=44)
        fct1.bind(on_release=lambda fct1: assu_fct.select(fct1.text))
        assu_fct.add_widget(fct1)

        fct2 = Button(text="qx", size_hint_y=None, height=44)
        fct2.bind(on_release=lambda fct2: assu_fct.select(fct2.text))
        assu_fct.add_widget(fct2)

        fct3 = Button(text="v", size_hint_y=None, height=44)
        fct3.bind(on_release=lambda fct3: assu_fct.select(fct3.text))
        assu_fct.add_widget(fct3)

        fct4 = Button(text="dx", size_hint_y=None, height=44)
        fct4.bind(on_release=lambda fct4: assu_fct.select(fct4.text))
        assu_fct.add_widget(fct4)

        fct5 = Button(text="npx", size_hint_y=None, height=44)
        fct5.bind(on_release=lambda fct5: assu_fct.select(fct5.text))
        assu_fct.add_widget(fct5)

        fct6 = Button(text="nqx", size_hint_y=None, height=44)
        fct6.bind(on_release=lambda fct6: assu_fct.select(fct6.text))
        assu_fct.add_widget(fct6)

        fct7 = Button(text="m_qx", size_hint_y=None, height=44)
        fct7.bind(on_release=lambda fct7: assu_fct.select(fct7.text))
        assu_fct.add_widget(fct7)

        return assu_fct

    def liste_commutation_life(self, assu_fct):
        assu_fct = DropDown()

        fct1 = Button(text="Dx", size_hint_y=None, height=44)
        fct1.bind(on_release=lambda fct1: assu_fct.select(fct1.text))
        assu_fct.add_widget(fct1)

        fct2 = Button(text="Nx", size_hint_y=None, height=44)
        fct2.bind(on_release=lambda fct2: assu_fct.select(fct2.text))
        assu_fct.add_widget(fct2)

        fct3 = Button(text="Sx", size_hint_y=None, height=44)
        fct3.bind(on_release=lambda fct3: assu_fct.select(fct3.text))
        assu_fct.add_widget(fct3)

        fct4 = Button(text="nEx", size_hint_y=None, height=44)
        fct4.bind(on_release=lambda fct4: assu_fct.select(fct4.text))
        assu_fct.add_widget(fct4)

        return assu_fct

    def build(self):
        self.window = GridLayout()
        self.window.cols = 3
        self.window.rows = 10
        self.table = table.tables
        Window.clearcolor = (18 / 255, 71 / 255, 159 / 255, 1)

        self.choice = Label(
            text="Choix de la table de mortalité",
            font_size=20,
        )

        self.text_table = Label(
            text="La table choisie est : ",
            font_size=20,
        )
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

        self.mainbutton = Button(text="Cliquer pour choisir la table")
        self.mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        ###
        self.user = Label(
            text="Saisie de l'âge de l'utilisateur ",
            font_size=20,
        )

        self.text_age = Label(
            text="âge : ",
            font_size=20,
        )

        self.age = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
            input_filter="int"
        )

        self.saisie_n = Label(
            text="Saisie du nombre d'année n à ajouter",
            font_size=20,
        )

        self.text_n = Label(
            text=" n : ",
            font_size=20,
        )

        self.n = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
            input_filter="int"
        )

        self.saisie_m = Label(
            text="Saisie du nombre d'année m à ajouter",
            font_size=20,
        )

        self.text_m = Label(
            text=" m : ",
            font_size=20,
        )

        self.m = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
            input_filter="int"
        )

        self.saisie_i = Label(
            text="Saisie du taux   ",
            font_size=20,
        )

        self.text_i = Label(
            text=" i : ",
            font_size=20,
        )

        self.i = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5),
            input_filter="float"
        )

        self.vision = Label(
            text="Voici les 2 visions possibles",
            font_size=20,
        )

        self.text_assureur = Label(
            text="Assureur",
            font_size=20,
        )

        self.text_client = Label(
            text="Client",
            font_size=20,

        )

        self.categorie_text = Label(
            text="Choix de la catégorie",
            font_size=20
        )

        ### liste des catégories Assureurs

        assu= DropDown()
        self.cat1 = Button(text="Probabilities one insured", size_hint_y=None, height=44)
        self.cat1.bind(on_release=lambda cat1: assu.select(self.cat1.text))
        assu.add_widget(self.cat1)

        self.cat2 = Button(text="Commutation case life", size_hint_y=None, height=44)
        self.cat2.bind(on_release=lambda cat2: assu.select(self.cat2.text))
        assu.add_widget(self.cat2)

        self.cat3 = Button(text="Commutation case death", size_hint_y=None, height=44)
        self.cat3.bind(on_release=lambda cat3: assu.select(self.cat3.text))
        assu.add_widget(self.cat3)

        self.cat4 = Button(text="Insurance case death", size_hint_y=None, height=44)
        self.cat4.bind(on_release=lambda cat4: assu.select(self.cat4.text))
        assu.add_widget(self.cat4)

        self.cat5 = Button(text="Life annuities", size_hint_y=None, height=44)
        self.cat5.bind(on_release=lambda cat5: assu.select(self.cat5.text))
        assu.add_widget(self.cat5)

        self.categorie_assureur = Button(text="Cliquer pour choisir la catégorie",
                                      font_size=15)
        self.categorie_assureur.bind(on_release=assu.open)
        assu.bind(on_select=lambda instance, x: setattr(self.categorie_assureur, 'text', x))
        ###

        ### liste des catégories Client

        cli = DropDown()

        self.catA = Button(text="To define", size_hint_y=None, height=44)
        self.catA.bind(on_release=lambda cat1: cli.select(self.catA.text))
        cli.add_widget(self.catA)

        self.catB = Button(text="To define", size_hint_y=None, height=44)
        self.catB.bind(on_release=lambda cat2: cli.select(self.catB.text))
        cli.add_widget(self.catB)

        self.categorie_client = Button(text="Cliquer pour choisir la catégorie",
                                      font_size=15)
        self.categorie_client.bind(on_release=cli.open)
        cli.bind(on_select=lambda instance, x: setattr(self.categorie_client, 'text', x))

        ###

        self.fonction_text = Button(
            text="Mettre à jour fonction/produit",
            bold=True,
            background_color=(0.5, 0.6, 0.3, 1)
        )
        self.fonction_text.bind(on_press = self.add_button)


        ### liste fonctions Client
        cli_fct = DropDown()

        self.fctA = Button(text="To define", size_hint_y=None, height=44)
        self.fctA.bind(on_release=lambda fctA: cli_fct.select(self.fctA.text))
        cli_fct.add_widget(self.fctA)

        self.fctB = Button(text="To define", size_hint_y=None, height=44)
        self.fctB.bind(on_release=lambda fctB: cli_fct.select(self.fctB.text))
        cli_fct.add_widget(self.fctB)

        self.fonction_client = Button(text="Cliquer pour choisir la fonction",
                                        font_size=15)
        self.fonction_client.bind(on_release=cli_fct.open)
        cli_fct.bind(on_select=lambda instance, x: setattr(self.fonction_client, 'text', x))

        ###
        self.resultat_assureur = Button(
                text="Cliquer pour afficher le résultat de la fonction",
                bold=True,
                background_color=(0, 1, 0, 1)
        )
        self.resultat_assureur.bind(on_press=self.callback)

        self.resultat_client = Button(
            text="Supprimer le bouton de la fonction créé",
            bold=True,
            background_color=(1, 1, 0, 1)
        )
        self.resultat_client.bind(on_press=self.remove)

        self.window.add_widget(self.choice)
        self.window.add_widget(self.text_table)
        self.window.add_widget(self.mainbutton)

        self.window.add_widget(self.user)
        self.window.add_widget(self.text_age)
        self.window.add_widget(self.age)

        self.window.add_widget(self.saisie_n)
        self.window.add_widget(self.text_n)
        self.window.add_widget(self.n)

        self.window.add_widget(self.saisie_m)
        self.window.add_widget(self.text_m)
        self.window.add_widget(self.m)

        self.window.add_widget(self.saisie_i)
        self.window.add_widget(self.text_i)
        self.window.add_widget(self.i)

        self.window.add_widget(self.vision)
        self.window.add_widget(self.text_assureur)
        self.window.add_widget(self.text_client)

        self.window.add_widget(self.categorie_text)
        self.window.add_widget(self.categorie_assureur)
        self.window.add_widget(self.categorie_client)

        self.window.add_widget(self.fonction_text)
        self.window.add_widget(self.resultat_assureur)
        self.window.add_widget(self.resultat_client)

        return self.window


    def set_name(self, instance):
        print(self.cat1.text)
        #self.ess.text = "Probabilities one insured"
        self.cat1.text = "Probabilities one insured"
        #self.categorie_assureur.text = self.ess.text



    def buton_creation(self):
        assu_fct = DropDown()

        if self.categorie_assureur.text == "Probabilities one insured":
            assu_fct = self.liste_proba_on_insured(assu_fct)
        if self.categorie_assureur.text == "Commutation case life":
            assu_fct = self.liste_commutation_life(assu_fct)

        fonction_assureur = Button(text="Cliquer pour choisir la fonction", font_size=15)
        fonction_assureur.bind(on_release=assu_fct.open)
        assu_fct.bind(on_select=lambda instance, x: setattr(fonction_assureur, 'text', x))
        return fonction_assureur,assu_fct

    def add_button(self, instance):
        self.fonction_assureur,assu_fct = self.buton_creation()
        assu_fct.bind(on_select=lambda instance, x: setattr(self.fonction_assureur, 'text', x))
        self.window.add_widget(self.fonction_assureur)


    def remove(self,instance):
        self.remove(self.fonction_assureur)


    def choix_table(self):
        if self.mainbutton.text == "TD_88_90":
            return table.tables[0]
        elif self.mainbutton.text == "TV_88_90":
            return table.tables[1]
        elif self.mainbutton.text == "TH_00_02":
            return table.tables[2]
        elif self.mainbutton.text == "TF_00_02":
            return table.tables[3]

    def callback(self, instance):
        if self.text_assureur.text == "Assureur":
            if self.categorie_assureur.text =="Probabilities one insured":
                pass
            elif self.text_assureur.text == "Commutation case life":
                pass
            elif self.text_assureur.text == "Commutation case death":
                pass
            elif self.text_assureur.text == "Insurance case death":
                pass
            elif self.text_assureur.text == "Life annuities":
                pass

        else: # add catégorie Client
            pass


if __name__ == "__main__":
    Application().run()
