# basic structure for any project with kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App): # class name on the tooleft of the window
    def build(self):
        self.window= GridLayout() # variable
        self.window.cols = 1  # number of column on the window
        self.window.size_hint = (0.6,0.7) # en % de l'écran, la taille des cases
        self.window.pos_hint = {"center_x": 0.5, "center_y ": 0.5}



        #add widgets to window

        #image widget
        #self.window.add_widget(Image(source="")) # add image with the url (if the image is in the same folder, just put the image name )

        #label widget
        self.greeting= Label( # greeting is a variable
            text="what's your name",
            font_size = 18, # taille texte
            color = '#00FFCE' # couleur texte
            )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user= TextInput(
            multiline=False,# write only on 1 line
            padding_y =(20,20),
            size_hint =(1,0.5)
            )
        self.window.add_widget(self.user)

        #button widget
        self.button = Button(
            text="Greet",
            size_hint=(1 , 0.5),
            bold=True,
            background_color='#00FFCE'
            )
        self.button.bind(on_press= self.callback) # permet au bouton d'exécuter la fonction marqué ds on_press
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance): # action for a button
        self.greeting.text="Hello " + self.user.text + " !"  # récupère les infos du texte saisie ds user et remplace le text de greeting par ce que a saisie le user



if __name__ == "__main__":
    SayHello().run()


