import cv2


class ImageMaker:

    def __init__(self, weather, card_sample="python_snippets/external_data/probe.jpg"):
        self.card_sample = card_sample
        self.weather = weather

    def make_card(self):
        if "rainy" == self.weather:
            pass
        elif "clear" == self.weather:
            pass
        elif "cloudy" == self.weather:
            pass
        else:
            pass

    def _rainy_card(self):
        pass

    def _clear_card(self):
        pass

    def _cloudy_card(self):
        pass

    def _snow_card(self):
        pass

