from ttkbootstrap import Button, Frame, Label


class PodcastTab(Frame):
    def __init__(self, parent, presenter):
        super().__init__()
        self._parent = parent
        self._presenter = presenter
        
        Label(self, text="Audio for podcast!").grid(row=0, column=0, padx=5, pady=5)
        
        self.podcast_button = Button(self, text="Apply Settings", command=self._presenter.apply_podcast)
        self.podcast_button.grid(row=2, column=0, padx=5, pady=5)