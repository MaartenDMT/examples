from ttkbootstrap import Button, Frame, Label


class DelayTab(Frame):
    def __init__(self, parent, presenter)-> None:
        super().__init__()
        self._parent = parent
        self._presenter = presenter
        
        Label(self, text="Add some Delay !").grid(row=0, column=0, padx=5, pady=5)
        
        self.delay_button = Button(self, text="Apply Delay", command=self._presenter.apply_delay)
        self.delay_button.grid(row=1, column=0, padx=5, pady=5)