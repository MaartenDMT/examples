from ttkbootstrap import Button, Label, Menu, Notebook, Style, Window

from view.delaytab import DelayTab
from view.distortiontab import DistortionTab
from view.mixtab import MixTab
from view.podcasttab import PodcastTab
from view.reverbtab import ReverbTab


class App(Window):
    def __init__(self):
        super().__init__()
        self.title("Audio Effects")
        self.geometry("600x400")
        style = Style()
        themes = style.theme_names()
        
        self._style.theme_use(themename='superhero')
    
        self.menu = Menu(self)
        self.theme_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Themes", menu=self.theme_menu)
        

        # Add a menu item for each theme
        for theme in themes:
            self.theme_menu.add_command(
                label=theme, command=lambda theme=theme: self.changer(theme))
    
    def create_widgets(self, presenter):
        self._presenter = presenter
        
        Label(self, text="Welcome, to the Audio Effect App!").grid(row=0, column=0, padx=5, pady=5)
        self.select_file_button = Button(self, text="Select File", command=self._presenter.select_file)

        self.notebook = Notebook(self, width='600')
        self.delay_tab= DelayTab(self.notebook, self._presenter)
        self.distortion_tab = DistortionTab(self.notebook, self._presenter)
        self.reverb_tab = ReverbTab(self.notebook, self._presenter)
        self.mix_tab = MixTab(self.notebook, self._presenter)
        self.podcast_tab = PodcastTab(self.notebook, self._presenter)
        
        self.notebook.add(self.delay_tab, text="Delay")
        self.notebook.add(self.distortion_tab, text="Distortion")
        self.notebook.add(self.reverb_tab, text="Reverb")
        self.notebook.add(self.mix_tab, text="Mix")
        self.notebook.add(self.podcast_tab, text="Podcast")
        


        # Tkinter App main page ----------------------------------------------
        self.select_file_button.grid(row=1, column=0, padx=5, pady=5)
        self.notebook.grid(row=2, column=0,padx=5, pady=5)
        


    def changer(self, theme) -> None:
        Style().theme_use(theme)

        

        



