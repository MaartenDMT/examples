from ttkbootstrap import Button, Frame, Label


class ReverbTab(Frame):
    def __init__(self, parent, presenter) -> None:
        super().__init__()
        self._parent = parent
        self._presenter = presenter
        
        Label(self, text="Add some Reverb !").grid(row=0, column=0, padx=5, pady=5)
        
        self.reverb_button = Button(self, text="Apply Reverb", command=self._presenter.apply_reverb)
        self.reverb_button.grid(row=3, column=0, padx=5, pady=5)