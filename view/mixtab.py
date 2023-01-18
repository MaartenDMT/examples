from ttkbootstrap import Button, Frame, Label


class MixTab(Frame):
    def __init__(self, parent, presenter):
        super().__init__()
        self._parent = parent
        self._presenter = presenter
        
        Label(self, text="Mix of effects !").grid(row=0, column=0, padx=5, pady=5)
        
        self.mix_button = Button(self, text="Apply Mix", command=self._presenter.apply_mix)
        self.mix_button.grid(row=2, column=0, padx=5, pady=5)