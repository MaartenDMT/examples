from tkinter import filedialog


class Presenter:
    def __init__(self, model, view) -> None:
        self._model = model
        self._view = view
        self.create_main()
        
    def run(self) -> None:
        self._view.mainloop()
    
    def create_main(self) -> None:
        self._view.create_widgets(self)
        self._model.create_tabmodels(self)

    def get_effects(self):
        return self._model.effect
    
    #main
    
    def select_file(self) -> None:
        effects = self.get_effects()
        effects.file_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("audio files", "*.mp3"), ("all files", "*.*")))
        print(effects.file_path)
    
    
    #Delay_tab 
    def delay(self):
        effect = self.get_effects()
        return effect.delay()
    
    def apply_delay(self) -> None:
        self._model.delay_model.apply_delay()
        
    #Distortion_tab
    def distortion(self):
        effect = self.get_effects()
        return effect.distortion()
    
    def apply_distortion(self) -> None:
        self._model.distortion_model.apply_distortion()
    
    #Reverb_tab
    def reverb(self):
        effect = self.get_effects()
        return effect.reverb()
    
    def apply_reverb(self) -> None:
        self._model.reverb_model.apply_reverb()
        
    #Mix tab
    def mix(self):
        effect = self.get_effects()
        return effect.mix()
    
    def apply_mix(self) -> None:
        self._model.mix_model.apply_mix()
        
    #Podcast tab
    def podcast(self):
        effect = self.get_effects()
        return effect.podcast()
    
    def apply_podcast(self) -> None:
        self._model.podcast_model.apply_podcast()
    