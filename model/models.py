import threading

from model.effects import Effect


class Models:
    def __init__(self) -> None:
        self.effect = Effect()
    
    def create_tabmodels(self, presenter) -> None:
        self._presenter = presenter
        self.delay_model = DelayModel(self._presenter)
        self.distortion_model = DistortionModel(self._presenter)
        self.reverb_model = ReverbModel(self._presenter)
        self.mix_model = MixModel(self._presenter)
        self.podcast_model = PodcastModel(self._presenter)
        
class App:
    def __init__(self, presenter):
        self._presenter = presenter
            

class DelayModel:
    def __init__(self, presenter) -> None:
        self._presenter = presenter
    
    def apply_delay(self) -> None:
        thread = threading.Thread(target=self._presenter.delay)
        thread.setDaemon(True)
        thread.start()

class DistortionModel:
    def __init__(self, presenter) -> None:
        self._presenter = presenter
    
    def apply_distortion(self) -> None:
        thread = threading.Thread(target=self._presenter.distortion)
        thread.setDaemon(True)
        thread.start()

class ReverbModel:
    def __init__(self, presenter) -> None:
        self._presenter = presenter
    
    def apply_reverb(self) -> None:
        thread = threading.Thread(target=self._presenter.reverb)
        thread.setDaemon(True)
        thread.start()

class MixModel:
    def __init__(self, presenter) -> None:
        self._presenter = presenter
    
    def apply_mix(self) -> None:
        thread = threading.Thread(target=self._presenter.mix)
        thread.setDaemon(True)
        thread.start()

class PodcastModel:
    def __init__(self, presenter) -> None:
        self._presenter = presenter
    
    def apply_podcast(self) -> None:
        thread = threading.Thread(target=self._presenter.podcast)
        thread.setDaemon(True)
        thread.start()