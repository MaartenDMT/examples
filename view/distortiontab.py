from ttkbootstrap import Button, Frame, Label


class DistortionTab(Frame):
    def __init__(self, parent, presenter):
        super().__init__()
        self._parent = parent
        self._presenter = presenter
        
        Label(self, text="Add some Distortion !").grid(row=0, column=0, padx=5, pady=5)
        
        self.distortion_button = Button(self, text="Apply Distortion", command=self._presenter.apply_distortion)
        self.distortion_button.grid(row=2, column=0, padx=5, pady=5)