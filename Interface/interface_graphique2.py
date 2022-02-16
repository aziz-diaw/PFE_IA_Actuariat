
import Actuariat.probabilities_one_insured as poi
import Table.tables as table
import Actuariat.commutation_case_death as ccd
import Actuariat.commutation_case_life as ccl
import Actuariat.insurance_case_death as icd
import Actuariat.life_annuities as lan
import Actuariat.product as prod
import Actuariat.StressTest as st
import FileATDD.check_file_atdd as cfa
import Actuariat.Reserves as res
import Bilan.balance_sheet as bs



import tkinter
from tkinter import *
from tkinter import messagebox
import math

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window

def fct1():
    class Application(App):
        def liste_proba_on_insured(self, assu_fct):
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

            fct8 = Button(text="m_n_qx", size_hint_y=None, height=44)
            fct8.bind(on_release=lambda fct8: assu_fct.select(fct8.text))
            assu_fct.add_widget(fct8)

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

            return assu_fct

        def liste_commutation_death(self, assu_fct):
            assu_fct = DropDown()

            fct1 = Button(text="Cx", size_hint_y=None, height=44)
            fct1.bind(on_release=lambda fct1: assu_fct.select(fct1.text))
            assu_fct.add_widget(fct1)

            fct2 = Button(text="Mx", size_hint_y=None, height=44)
            fct2.bind(on_release=lambda fct2: assu_fct.select(fct2.text))
            assu_fct.add_widget(fct2)

            fct3 = Button(text="Rx", size_hint_y=None, height=44)
            fct3.bind(on_release=lambda fct3: assu_fct.select(fct3.text))
            assu_fct.add_widget(fct3)

            return assu_fct

        def liste_life_annuities(self, assu_fct):
            assu_fct = DropDown()

            fct1 = Button(text="ax", size_hint_y=None, height=44)
            fct1.bind(on_release=lambda fct1: assu_fct.select(fct1.text))
            assu_fct.add_widget(fct1)

            fct2 = Button(text="a_xn", size_hint_y=None, height=44)
            fct2.bind(on_release=lambda fct2: assu_fct.select(fct2.text))
            assu_fct.add_widget(fct2)

            fct3 = Button(text="m_ax", size_hint_y=None, height=44)
            fct3.bind(on_release=lambda fct3: assu_fct.select(fct3.text))
            assu_fct.add_widget(fct3)

            fct4 = Button(text="_ax_", size_hint_y=None, height=44)
            fct4.bind(on_release=lambda fct4: assu_fct.select(fct4.text))
            assu_fct.add_widget(fct4)

            fct5 = Button(text="_m_ax_", size_hint_y=None, height=44)
            fct5.bind(on_release=lambda fct5: assu_fct.select(fct5.text))
            assu_fct.add_widget(fct5)

            fct6 = Button(text="_m_a_xn_", size_hint_y=None, height=44)
            fct6.bind(on_release=lambda fct6: assu_fct.select(fct6.text))
            assu_fct.add_widget(fct6)

            fct7 = Button(text="ax_k", size_hint_y=None, height=44)
            fct7.bind(on_release=lambda fct7: assu_fct.select(fct7.text))
            assu_fct.add_widget(fct7)

            fct8 = Button(text="a_xn_k", size_hint_y=None, height=44)
            fct8.bind(on_release=lambda fct8: assu_fct.select(fct8.text))
            assu_fct.add_widget(fct8)

            fct9 = Button(text="m_ax_k", size_hint_y=None, height=44)
            fct9.bind(on_release=lambda fct9: assu_fct.select(fct9.text))
            assu_fct.add_widget(fct9)

            fct10 = Button(text="m_a_xn_k", size_hint_y=None, height=44)
            fct10.bind(on_release=lambda fct10: assu_fct.select(fct10.text))
            assu_fct.add_widget(fct10)

            fct11 = Button(text="_ax__k", size_hint_y=None, height=44)
            fct11.bind(on_release=lambda fct11: assu_fct.select(fct11.text))
            assu_fct.add_widget(fct11)

            fct12 = Button(text="_a_xn__k", size_hint_y=None, height=44)
            fct12.bind(on_release=lambda fct12: assu_fct.select(fct12.text))
            assu_fct.add_widget(fct12)

            fct13 = Button(text="_m_ax__k", size_hint_y=None, height=44)
            fct13.bind(on_release=lambda fct13: assu_fct.select(fct13.text))
            assu_fct.add_widget(fct13)

            fct14 = Button(text="_m_a_xn__k", size_hint_y=None, height=44)
            fct14.bind(on_release=lambda fct14: assu_fct.select(fct14.text))
            assu_fct.add_widget(fct14)

            fct15 = Button(text="m_a_xn", size_hint_y=None, height=44)
            fct15.bind(on_release=lambda fct15: assu_fct.select(fct15.text))
            assu_fct.add_widget(fct15)

            fct16 = Button(text="_a_xn_", size_hint_y=None, height=44)
            fct16.bind(on_release=lambda fct14: assu_fct.select(fct16.text))
            assu_fct.add_widget(fct16)

            return assu_fct

        def liste_insurance_case_death(self, assu_fct):
            assu_fct = DropDown()

            fct3 = Button(text="m_n_Ax", size_hint_y=None, height=44)
            fct3.bind(on_release=lambda fct3: assu_fct.select(fct3.text))
            assu_fct.add_widget(fct3)

            fct4 = Button(text="m_Ax", size_hint_y=None, height=44)
            fct4.bind(on_release=lambda fct4: assu_fct.select(fct4.text))
            assu_fct.add_widget(fct4)

            fct5 = Button(text="n_IA_x", size_hint_y=None, height=44)
            fct5.bind(on_release=lambda fct5: assu_fct.select(fct5.text))
            assu_fct.add_widget(fct5)

            fct6 = Button(text="n_DA_x", size_hint_y=None, height=44)
            fct6.bind(on_release=lambda fct6: assu_fct.select(fct6.text))
            assu_fct.add_widget(fct6)

            return assu_fct

        def list_product(self, assu_fct):
            assu_fct = DropDown()

            fct1 = Button(text="nEx", size_hint_y=None, height=44)
            fct1.bind(on_release=lambda fct1: assu_fct.select(fct1.text))
            assu_fct.add_widget(fct1)

            fct2 = Button(text="Ax", size_hint_y=None, height=44)
            fct2.bind(on_release=lambda fct2: assu_fct.select(fct2.text))
            assu_fct.add_widget(fct2)

            fct3 = Button(text="nAx", size_hint_y=None, height=44)
            fct3.bind(on_release=lambda fct3: assu_fct.select(fct3.text))
            assu_fct.add_widget(fct3)

            fct4 = Button(text="Ax_n", size_hint_y=None, height=44)
            fct4.bind(on_release=lambda fct4: assu_fct.select(fct4.text))
            assu_fct.add_widget(fct4)

            fct5 = Button(text="Cx_n", size_hint_y=None, height=44)
            fct5.bind(on_release=lambda fct5: assu_fct.select(fct5.text))
            assu_fct.add_widget(fct5)

            return assu_fct

        def list_stress_product(self,assu_fct):
            assu_fct = DropDown()

            fct1 = Button(text="nAx_stress", size_hint_y=None, height=44)
            fct1.bind(on_release=lambda fct1: assu_fct.select(fct1.text))
            assu_fct.add_widget(fct1)

            return assu_fct

        def list_reserve(self,assu_fct):
            assu_fct = DropDown()

            fct1 = Button(text="nAx_reserve", size_hint_y=None, height=44)
            fct1.bind(on_release=lambda fct1: assu_fct.select(fct1.text))
            assu_fct.add_widget(fct1)

            return assu_fct



        def build(self):
            self.window = GridLayout()
            self.window.cols = 3
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
                text="Saisie de l'âge de l'utilisateur (en année)  ",
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
                text="Saisie du nombre d'année n à ajouter (en année) ",
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
                text="Saisie du nombre d'année m à ajouter (en année)",
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
                text="Saisie du taux (entre 0 et 1)",
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

            self.saisie_k = Label(
                text="Saisie du nombre de paiements par année (entre 0 et 12)",
                font_size=20,
            )

            self.text_k = Label(
                text=" k : ",
                font_size=20,
            )

            self.k = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="int"
            )
            self.saisie_cbenef = Label(
                text="Saisie du montant du bénéfice (en €) ",
                font_size=20
            )

            self.text_cbenef = Label(
                text=" C : ",
                font_size=20,
            )

            self.c_benef = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="float"
            )

            self.saisie_clife = Label(
                text = "Saisie du montant du bénéfice en cas de vie après les n années (en €)",
                font_size=20
            )

            self.text_clife = Label(
                text=" C1 : ",
                font_size=20,
            )

            self.c_life = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="float"
            )

            self.saisie_cdeath = Label(
                text="Saisie du montant du bénéfice en cas de mort après les n années (en €)",
                font_size=20
            )

            self.text_cdeath = Label(
                text=" C2 : ",
                font_size=20,
            )

            self.c_death = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="float"
            )

            self.saisie_stress_rate = Label(
                text="Saisie du stress rate (entre 0 et 1)",
                font_size=20
            )

            self.text_stress_rate = Label(
                text=" stress rate : ",
                font_size=20,
            )

            self.stress_rate = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="float"
            )

            self.saisie_t = Label(
                text="Saisie de l'année pour voir les réserves",
                font_size=20
            )

            self.text_t = Label(
                text=" t: ",
                font_size=20,
            )

            self.t = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="int"
            )



            ### liste des catégories Assureurs

            assu = DropDown()
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

            self.cat6 = Button(text="Insurance products", size_hint_y=None, height=44)
            self.cat6.bind(on_release=lambda cat6: assu.select(self.cat6.text))
            assu.add_widget(self.cat6)

            self.cat7 = Button(text="Stress product", size_hint_y=None, height=44)
            self.cat7.bind(on_release=lambda cat6: assu.select(self.cat7.text))
            assu.add_widget(self.cat7)

            self.cat7 = Button(text="Reserves", size_hint_y=None, height=44)
            self.cat7.bind(on_release=lambda cat6: assu.select(self.cat7.text))
            assu.add_widget(self.cat7)


            self.categorie_assureur = Button(text="Choix du type de produit",
                                             font_size=15)
            self.categorie_assureur.bind(on_release=assu.open)
            assu.bind(on_select=lambda instance, x: setattr(self.categorie_assureur, 'text', x))
            ###

            self.fonction_text = Button(
                text="choix du produit d'assurance",
                bold=True,
                background_color=(0.5, 0.6, 0.3, 1)
            )
            self.fonction_text.bind(on_press=self.add_button)

            self.resultat_assureur = Button(
                text="Cliquer pour afficher le résultat de la formule",
                bold=True,
                background_color=(0, 1, 0, 1)
            )
            self.resultat_assureur.bind(on_press=self.callback)

            self.resultat_client = Button(
                text="Supprimer le bouton de la fonction créée",
                bold=True,
                background_color=(1, 1, 0, 1)
            )
            self.resultat_client.bind(on_press=self.remove)

            self.balance_sheet= Button(
                text="Cliquer pour imprimer le Bilan pour Temporaire Décès",
                bold=True,
                background_color=(0.4, 0.2, 0, 1)
            )
            self.balance_sheet.bind(on_press=self.bilan)

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

            self.window.add_widget(self.saisie_k)
            self.window.add_widget(self.text_k)
            self.window.add_widget(self.k)

            self.window.add_widget(self.saisie_cbenef)
            self.window.add_widget(self.text_cbenef)
            self.window.add_widget(self.c_benef)

            self.window.add_widget(self.saisie_clife)
            self.window.add_widget(self.text_clife)
            self.window.add_widget(self.c_life)

            self.window.add_widget(self.saisie_cdeath)
            self.window.add_widget(self.text_cdeath)
            self.window.add_widget(self.c_death)

            self.window.add_widget(self.saisie_stress_rate)
            self.window.add_widget(self.text_stress_rate)
            self.window.add_widget(self.stress_rate)

            self.window.add_widget(self.saisie_t)
            self.window.add_widget(self.text_t)
            self.window.add_widget(self.t)

            self.window.add_widget(self.categorie_assureur)

            self.window.add_widget(self.fonction_text)
            self.window.add_widget(self.resultat_assureur)
            self.window.add_widget(self.resultat_client)

            self.window.add_widget(self.balance_sheet)
            return self.window

        def bilan(self,instance):
            bs.balance_sheet(int(self.age.text),int(self.n.text),int(self.m.text),float(self.i.text),self.choix_table(),int(self.t.text))

        def buton_creation(self):
            assu_fct = DropDown()

            if self.categorie_assureur.text == "Probabilities one insured":
                assu_fct = self.liste_proba_on_insured(assu_fct)
            if self.categorie_assureur.text == "Commutation case life":
                assu_fct = self.liste_commutation_life(assu_fct)
            if self.categorie_assureur.text == "Commutation case death":
                assu_fct = self.liste_commutation_death(assu_fct)
            if self.categorie_assureur.text == "Life annuities":
                assu_fct = self.liste_life_annuities(assu_fct)
            if self.categorie_assureur.text == "Insurance case death":
                assu_fct = self.liste_insurance_case_death(assu_fct)
            if self.categorie_assureur.text == "Insurance products" :
                assu_fct = self.list_product(assu_fct)
            if self.categorie_assureur.text == "Stress product" :
                assu_fct = self.list_stress_product(assu_fct)
            if self.categorie_assureur.text == "Reserves" :
                assu_fct = self.list_reserve(assu_fct)

            fonction_assureur = Button(text="Cliquer pour choisir la fonction", font_size=15)
            fonction_assureur.bind(on_release=assu_fct.open)
            assu_fct.bind(on_select=lambda instance, x: setattr(fonction_assureur, 'text', x))
            return fonction_assureur, assu_fct

        def add_button(self, instance):
            self.fonction_assureur, assu_fct = self.buton_creation()
            assu_fct.bind(on_select=lambda instance, x: setattr(self.fonction_assureur, 'text', x))
            self.window.add_widget(self.fonction_assureur)

        def remove(self, instance):
            self.window.remove_widget(self.fonction_assureur)

        def choix_table(self):
            if self.mainbutton.text == "TD_88_90":
                return table.tables[0]
            elif self.mainbutton.text == "TV_88_90":
                return table.tables[1]
            elif self.mainbutton.text == "TH_00_02":
                return table.tables[2]
            elif self.mainbutton.text == "TF_00_02":
                return table.tables[3]

        def float_round_up(self,x):
            return math.ceil(x*1000)/1000

        def callback(self, instance):  # add le check des params ds cette fonction
                if self.categorie_assureur.text == "Probabilities one insured":
                    if self.fonction_assureur.text == "px":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(poi.px(int(self.age.text), self.choix_table()))
                    if self.fonction_assureur.text == "qx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(poi.qx(int(self.age.text), self.choix_table()))
                    if self.fonction_assureur.text == "v":
                        if (float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(poi.v(float(self.i.text)))
                    if self.fonction_assureur.text == "dx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(poi.dx(int(self.age.text), self.choix_table())) + "morts"
                    if self.fonction_assureur.text == "npx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                int(self.age.text) + int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                poi.npx(int(self.age.text), int(self.n.text), self.choix_table()))
                    if self.fonction_assureur.text == "nqx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) < 0) | (
                                int(self.age.text) + int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                poi.nqx(int(self.age.text), int(self.n.text), self.choix_table()))
                    if self.fonction_assureur.text == "m_qx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + 1 > len(self.choix_table()) - 1) | (int(self.m.text) < 0) | (
                                int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + int(self.age.text) + 1 > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                poi.m_qx(int(self.age.text), int(self.m.text), self.choix_table()))
                    if self.fonction_assureur.text == "m_n_qx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + int(self.age.text) + int(self.n.text) > len(
                                self.choix_table()) - 1) | (int(self.n.text) < 0) | (
                                int(self.n.text) > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                poi.m_n_qx(int(self.age.text), int(self.n.text), int(self.m.text), self.choix_table()))
                elif self.categorie_assureur.text == "Commutation case death":
                    if self.fonction_assureur.text == "Cx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                ccd.Cx(int(self.age.text), float(self.i.text), self.choix_table()))
                    if self.fonction_assureur.text == "Mx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                ccd.Mx(int(self.age.text), float(self.i.text), self.choix_table()))
                    if self.fonction_assureur.text == "Rx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                ccd.Rx(int(self.age.text), float(self.i.text), self.choix_table()))
                elif self.categorie_assureur.text == "Commutation case life":
                    if self.fonction_assureur.text == "Dx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                ccl.Dx(int(self.age.text), float(self.i.text), self.choix_table()))
                    if self.fonction_assureur.text == "Nx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                ccl.Nx(int(self.age.text), self.choix_table(), float(self.i.text)))
                    if self.fonction_assureur.text == "Sx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                ccl.Sx(int(self.age.text), self.choix_table(), float(self.i.text)))
                elif self.categorie_assureur.text == "Insurance case death":
                    if self.fonction_assureur.text == "m_n_Ax":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) + int(self.age.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) + int(self.age.text) + int(self.m.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                icd.m_n_Ax(int(self.age.text), int(self.n.text), int(self.m.text), float(self.i.text),
                                           self.choix_table()))
                    if self.fonction_assureur.text == "m_Ax":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + int(self.age.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                icd.m_Ax(int(self.age.text), int(self.m.text), float(self.i.text), self.choix_table()))
                    if self.fonction_assureur.text == "n_IA_x":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) + int(self.age.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                icd.n_IA_x(int(self.age.text), int(self.n.text), float(self.i.text),
                                           self.choix_table()))  # check this formule => does a negative value is possible ?
                    if self.fonction_assureur.text == "n_DA_x":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + int(self.age.text) + 1 > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                icd.n_DA_x(int(self.age.text), int(self.n.text), float(self.i.text),
                                           self.choix_table()))
                elif self.categorie_assureur.text == "Life annuities":
                    if self.fonction_assureur.text == "ax":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.age.text) + 1 > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan.ax(int(self.age.text), self.choix_table(), float(self.i.text)))
                    if self.fonction_assureur.text == "a_xn":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) + int(self.age.text) + 1 > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan.a_xn(int(self.age.text), int(self.n.text), float(self.i.text), self.choix_table()))
                    if self.fonction_assureur.text == "m_ax":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + int(self.age.text) + 1 > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan.m_ax(int(self.age.text), int(self.m.text), float(self.i.text), self.choix_table()))
                    if self.fonction_assureur.text == "_ax_":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan._ax_(int(self.age.text), self.choix_table(), float(self.i.text)))
                    if self.fonction_assureur.text == "_m_ax_":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + int(self.age.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan._m_ax_(int(self.age.text), int(self.m.text), float(self.i.text),
                                           self.choix_table()))
                    if self.fonction_assureur.text == "_m_a_xn_":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) + int(self.age.text) + int(self.n.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan._m_a_xn_(int(self.age.text), int(self.n.text), int(self.m.text), float(self.i.text),
                                             self.choix_table()))
                    if self.fonction_assureur.text == "ax_k":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.k.text) < 1) | (int(self.k.text) > 12
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan.ax_k(int(self.age.text), self.choix_table(), float(self.i.text), int(self.k.text)))
                    if self.fonction_assureur.text == "a_xn_k":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.k.text) < 1) | (int(self.k.text) > 12) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan.a_xn_k(int(self.age.text), int(self.n.text), float(self.i.text), self.choix_table(),
                                           int(self.k.text)))
                    if self.fonction_assureur.text == "m_ax_k":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.k.text) < 1) | (int(self.k.text) > 12) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan.m_ax_k(int(self.age.text), int(self.m.text), float(self.i.text), self.choix_table(),
                                           int(self.k.text)))
                    if self.fonction_assureur.text == "m_a_xn_k":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.k.text) < 1) | (int(self.k.text) > 12) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.age.text) + int(self.m.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan.m_a_xn_k(int(self.age.text), int(self.n.text), int(self.m.text), float(self.i.text),
                                             self.choix_table(), int(self.k.text)))
                    if self.fonction_assureur.text == "_ax__k":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.k.text) < 1) | (int(self.k.text) > 12
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan._ax__k(int(self.age.text), self.choix_table(), float(self.i.text),
                                           int(self.k.text)))
                    if self.fonction_assureur.text == "_a_xn__k":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.k.text) < 1) | (int(self.k.text) > 12) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan._a_xn__k(int(self.age.text), int(self.n.text), float(self.i.text),
                                             self.choix_table(), int(self.k.text)))
                    if self.fonction_assureur.text == "_m_ax__k":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.k.text) < 1) | (int(self.k.text) > 12) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan._m_ax__k(int(self.age.text), int(self.m.text), float(self.i.text),
                                             self.choix_table(), int(self.k.text)))
                    if self.fonction_assureur.text == "_m_a_xn__k":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.k.text) < 1) | (int(self.k.text) > 12) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.age.text) + int(self.m.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan._m_a_xn__k(int(self.age.text), int(self.n.text), int(self.m.text),
                                               float(self.i.text), self.choix_table(), int(self.k.text)))
                    if self.fonction_assureur.text == "m_a_xn":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.m.text) < 0) | (int(self.m.text) > len(self.choix_table()) - 1) | (
                                int(self.age.text) + int(self.m.text) + int(self.n.text) + 1 > len(
                            self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan.m_a_xn(int(self.age.text), int(self.n.text), int(self.m.text), float(self.i.text),
                                           self.choix_table()))
                    if self.fonction_assureur.text == "_a_xn_":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.age.text) + int(self.n.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                lan._a_xn_(int(self.age.text), int(self.n.text), float(self.i.text),
                                           self.choix_table()))
                elif self.categorie_assureur.text == "Insurance products":
                    if self.fonction_assureur.text == "nEx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (int(self.n.text) < 0) | (
                                int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.age.text) + int(self.n.text) > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.nEx(int(self.age.text), int(self.n.text), float(self.i.text), self.choix_table())))
                    if self.fonction_assureur.text == "Ax":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.Ax(int(self.age.text), float(self.i.text), self.choix_table())))
                    if self.fonction_assureur.text == "nAx":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) + int(self.age.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.nAx(int(self.age.text), int(self.n.text), float(self.i.text),
                                         self.choix_table())))
                    if self.fonction_assureur.text == "Ax_n":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) + int(self.age.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.Ax_n(int(self.c_benef.text),int(self.age.text), int(self.n.text), float(self.i.text),
                                         self.choix_table())))
                    if self.fonction_assureur.text == "Cx_n":
                        if (int(self.age.text) < 0) | (float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0)  :
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else:
                            self.resultat_assureur.text = str(
                               self.float_round_up(prod.Cx_n(int(self.c_life.text),int(self.c_death.text),int(self.age.text), int(self.n.text), float(self.i.text))))
                elif self.categorie_assureur.text == "Stress product":
                    if self.fonction_assureur.text == "nAx_stress":
                        if (int(self.age.text) < 0) | (float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0)   :
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else :
                            self.resultat_assureur.text =str(self.float_round_up(st.nAx_stress(int(self.age.text),float(self.i.text),int(self.n.text),float(self.stress_rate.text),self.choix_table())))
                elif self.categorie_assureur.text == "Reserves":
                    if self.fonction_assureur.text == "nAx_reserve":
                        if (int(self.age.text) < 0) | (float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0)   :
                            self.resultat_assureur.text = "Erreur dans les paramètres saisis"
                        else :
                            self.resultat_assureur.text =str(self.float_round_up(res.nAx_reserve(int(self.age.text),int(self.n.text),int(self.m.text),float(self.i.text),self.choix_table(),int(self.t.text))))



    x = 50
    n = 5
    m = 5
    tab = table.tables[0]
    i = 0.2

    if poi.check_function_poi(x, n, m, tab) == lan.check_function_lan(x, n, m, i, tab) == True:
        if cfa.check_atdd()[0] == True and cfa.check_atdd()[1] == True :
            if __name__ == "__main__":
                Application().run()
def fct2():
    class Application(App):


        def list_product(self, assu_fct):
            assu_fct = DropDown()

            fct1 = Button(text="Pure Endowment", size_hint_y=None, height=44)
            fct1.bind(on_release=lambda fct1: assu_fct.select(fct1.text))
            assu_fct.add_widget(fct1)

            fct2 = Button(text="Whole Life", size_hint_y=None, height=44)
            fct2.bind(on_release=lambda fct2: assu_fct.select(fct2.text))
            assu_fct.add_widget(fct2)

            fct3 = Button(text="Term Insurance", size_hint_y=None, height=44)
            fct3.bind(on_release=lambda fct3: assu_fct.select(fct3.text))
            assu_fct.add_widget(fct3)

            fct4 = Button(text="Endowment", size_hint_y=None, height=44)
            fct4.bind(on_release=lambda fct4: assu_fct.select(fct4.text))
            assu_fct.add_widget(fct4)

            fct5 = Button(text="Combined Endowment", size_hint_y=None, height=44)
            fct5.bind(on_release=lambda fct5: assu_fct.select(fct5.text))
            assu_fct.add_widget(fct5)

            return assu_fct

        def build(self):
            self.window = GridLayout()
            self.window.cols = 3
            self.table = table.tables
            Window.clearcolor = (18 / 255, 71 / 255, 159 / 255, 1)

            self.choice = Label(
                text="The choose the mortality table",
                font_size=20,
            )

            self.text_table = Label(
                text="The table is : ",
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

            self.mainbutton = Button(text="Click to choose the table : ")
            self.mainbutton.bind(on_release=dropdown.open)
            dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

            ###
            self.user = Label(
                text="Entering the user's age (in year)",
                font_size=20,
            )

            self.text_age = Label(
                text="age : ",
                font_size=20,
            )

            self.age = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="int"
            )

            self.saisie_n = Label(
                text="Entering the number of year to add (in year)",
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
                text="Entering the number of deferred year to add (in year)",
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
                text="Entering the rate ( between 0 and 1 ) : ",
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

            self.saisie_k = Label(
                text="Entering the number of payment by year ( between 1 and 12 ) : ",
                font_size=20,
            )

            self.text_k = Label(
                text=" k : ",
                font_size=20,
            )

            self.k = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="int"
            )
            self.saisie_cbenef = Label(
                text="Entering the beneficary amount (in €)",
                font_size=20
            )

            self.text_cbenef = Label(
                text=" C : ",
                font_size=20,
            )

            self.c_benef = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="float"
            )
            self.saisie_clife = Label(
                text="Entering the life beneficary amount after the n years (in €)",
                font_size=20
            )

            self.text_clife = Label(
                text=" C1 : ",
                font_size=20,
            )

            self.c_life = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="float"
            )

            self.saisie_cdeath = Label(
                text="Entering the death beneficary amount after the n years (in €)",
                font_size=20
            )

            self.text_cdeath = Label(
                text=" C2 : ",
                font_size=20,
            )

            self.c_death = TextInput(
                multiline=False,
                padding_y=(20, 20),
                size_hint=(0.5, 0.5),
                input_filter="float"
            )

            ### liste des catégories Assureurs

            assu = DropDown()

            self.cat6 = Button(text="Insurance products", size_hint_y=None, height=44)
            self.cat6.bind(on_release=lambda cat6: assu.select(self.cat6.text))
            assu.add_widget(self.cat6)

            self.categorie_assureur = Button(text="Products",
                                             font_size=15)
            self.categorie_assureur.bind(on_release=assu.open)
            assu.bind(on_select=lambda instance, x: setattr(self.categorie_assureur, 'text', x))
            ###

            self.fonction_text = Button(
                text="Choose the kind of insurance :",
                bold=True,
                background_color=(0.5, 0.6, 0.3, 1)
            )
            self.fonction_text.bind(on_press=self.add_button)

            self.resultat_assureur = Button(
                text="Click to show the premium",
                bold=True,
                background_color=(18 / 255, 71 / 255, 159 / 255, 1)

            )

            self.resultat_assureur.bind(on_press=self.callback)

            self.resultat_client = Button(
                text="Delete the button created",
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

            self.window.add_widget(self.saisie_k)
            self.window.add_widget(self.text_k)
            self.window.add_widget(self.k)

            self.window.add_widget(self.saisie_cbenef)
            self.window.add_widget(self.text_cbenef)
            self.window.add_widget(self.c_benef)

            self.window.add_widget(self.saisie_clife)
            self.window.add_widget(self.text_clife)
            self.window.add_widget(self.c_life)

            self.window.add_widget(self.saisie_cdeath)
            self.window.add_widget(self.text_cdeath)
            self.window.add_widget(self.c_death)

            self.window.add_widget(self.categorie_assureur)

            self.window.add_widget(self.fonction_text)
            self.window.add_widget(self.resultat_assureur)
            self.window.add_widget(self.resultat_client)
            return self.window

        def buton_creation(self):
            assu_fct = DropDown()

            if self.categorie_assureur.text == "Insurance products" :
                assu_fct = self.list_product(assu_fct)

            fonction_assureur = Button(text="Click to choose the function", font_size=15)
            fonction_assureur.bind(on_release=assu_fct.open)
            assu_fct.bind(on_select=lambda instance, x: setattr(fonction_assureur, 'text', x))
            return fonction_assureur, assu_fct

        def add_button(self, instance):
            self.fonction_assureur, assu_fct = self.buton_creation()
            assu_fct.bind(on_select=lambda instance, x: setattr(self.fonction_assureur, 'text', x))
            self.window.add_widget(self.fonction_assureur)

        def remove(self, instance):
            self.window.remove_widget(self.fonction_assureur)

        def choix_table(self):
            if self.mainbutton.text == "TD_88_90":
                return table.tables[0]
            elif self.mainbutton.text == "TV_88_90":
                return table.tables[1]
            elif self.mainbutton.text == "TH_00_02":
                return table.tables[2]
            elif self.mainbutton.text == "TF_00_02":
                return table.tables[3]

        def float_round_up(self,x):
            return math.ceil(x*1000)/1000

        def callback(self, instance):
                if self.categorie_assureur.text == "Insurance products":
                    if self.fonction_assureur.text == "Pure Endowment":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (int(self.n.text) < 0) | (
                                int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.age.text) + int(self.n.text) > len(self.choix_table()) - 1):
                            self.resultat_assureur.text = "parameter input error"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.nEx(int(self.age.text), int(self.n.text), float(self.i.text), self.choix_table())))+"€ pour un montant de 1€"
                    if self.fonction_assureur.text == "Whole Life":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1):
                            self.resultat_assureur.text = "parameter input error"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.Ax(int(self.age.text), float(self.i.text), self.choix_table())))+"€ pour un montant de 1€"
                    if self.fonction_assureur.text == "Term Insurance":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) + int(self.age.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "parameter input error"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.nAx(int(self.age.text), int(self.n.text), float(self.i.text),
                                         self.choix_table())))+"€ pour un montant de 1€"
                    if self.fonction_assureur.text == "Endowment":
                        if (int(self.age.text) < 0) | (int(self.age.text) > len(self.choix_table()) - 1) | (
                                float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) | (int(self.n.text) > len(self.choix_table()) - 1) | (
                                int(self.n.text) + int(self.age.text) > len(self.choix_table()) - 1
                        ):
                            self.resultat_assureur.text = "parameter input error"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.Ax_n(int(self.c_benef.text),int(self.age.text), int(self.n.text), float(self.i.text),
                                         self.choix_table())))+"€ for a beneficary of " + self.c_benef.text +"€"
                    if self.fonction_assureur.text == "Combined Endowment":
                        if (int(self.age.text) < 0) |  (float(self.i.text) < 0) | (float(self.i.text) > 1) | (
                                int(self.n.text) < 0) :
                            self.resultat_assureur.text = "parameter input error"
                        else:
                            self.resultat_assureur.text = str(
                                self.float_round_up(prod.Cx_n(int(self.c_life.text),int(self.c_death.text),int(self.age.text), int(self.n.text), float(self.i.text))))+"€ for a beneficary of "+self.c_life.text+" for life and " + self.c_death.text+" for the death"

    x = 50
    n = 5
    m = 5
    tab = table.tables[0]
    i = 0.2

    if poi.check_function_poi(x, n, m, tab) == lan.check_function_lan(x, n, m, i, tab) == True:
        if cfa.check_atdd()[0] == True and cfa.check_atdd()[1] == True:
            if __name__ == "__main__":
                Application().run()


def fct3():
    pass

# Création de la fenêtre
fen_princ = Tk()
fen_princ.title("Mon application à moi que j'ai")
fen_princ.geometry("900x600")
bg = PhotoImage(file = "pns.png")

# Show image using label
label1 = tkinter.Label(fen_princ, image = bg)
label1.place(x = 50, y = 50)

# Création du cadre-conteneur pour les menus
zoneMenu = Frame(fen_princ, borderwidth=3, bg='#557788')
zoneMenu.pack(fill=X)

# Création de l'onglet Assureur
menuAssurance = Menubutton(zoneMenu, text='Assurance', width='20', borderwidth=2, bg='gray',
                          activebackground='darkorange', relief=RAISED)
menuAssurance.grid(row=0, column=0)

# Création de l'onglet Assuré
menuInfo = Menubutton(zoneMenu, text='Aide', width='20', borderwidth=2, bg='gray', activebackground='darkorange',
                        relief=RAISED)
menuInfo.grid(row=0, column=3)

# Création d'un menu défilant pour l'assurance
menuDeroulant1 = Menu(menuAssurance, tearoff=0)
menuDeroulant1.add_command(label="Cliquer ici si vous etes un assureur", command=fct1)
menuDeroulant1.add_command(label="Cliquer ici si vous etes un assuré", command=fct2)

menuAssurance.configure(menu=menuDeroulant1)


# Création d'un menu défilant pour les infos
menuDeroulant2 = Menu(menuInfo, tearoff=0)
menuDeroulant2.add_command(label="Infos Assurance Vie", command=fct3)
menuDeroulant2.add_command(label="Infos d'Assurance décés", command=fct3)
menuDeroulant2.add_command(label="Infos d'Assurance vie et décés", command=fct3)
menuInfo.configure(menu=menuDeroulant2)


fen_princ.mainloop()
