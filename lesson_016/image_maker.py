import cv2
import os.path


class ImageMaker:

    def __init__(self, weather, weather_data, card_sample="python_snippets/external_data/probe.jpg",
                 card_weather="python_snippets/external_data/weather_img"):
        self.background = cv2.imread(card_sample)
        self.card_weather = card_weather
        self.weather = weather
        self.colour = None
        self.weather_data = weather_data

    def make_card(self):
        if "rainy" == self.weather:
            self.colour = [200, 60, 0]
            self.card_weather = os.path.join(self.card_weather, "rain.jpg")
        elif "clear" == self.weather:
            self.colour = [0, 217, 254]
            self.card_weather = os.path.join(self.card_weather, "sun.jpg")
        elif "cloudy" == self.weather:
            self.colour = [100, 100, 100]
            self.card_weather = os.path.join(self.card_weather, "cloud.jpg")
        else:
            self.colour = [200, 175, 0]
            self.card_weather = os.path.join(self.card_weather, "snow.jpg")
        self._paint_background()
        self._print_text()
        cv2.imshow("Weather", self.background)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def _print_text(self):
        # TODO Здесь я не хочу использовать цикл, потому что, если структура входящих данных изменится
        # TODO может быть сложно сдвинуть конкретное место так, чтобы не поплыла вся карточка
        # TODO ну и в целом код будет, конечно, короче, но поддерживать его станет труднее
        cv2.putText(self.background, self.weather_data[0], (110, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[1] + " " + self.weather_data[2],
                    (110, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[23], (320, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[24], (320, 40), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[25], (320, 60), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[26], (320, 80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, "утро", (2, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.putText(self.background, "день", (130, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.putText(self.background, "вечер", (258, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.putText(self.background, "ночь", (386, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.rectangle(self.background, (0, 0), (100, 100), (0, 0, 0), 1)
        cv2.rectangle(self.background, (0, 100), (128, 256), (0, 0, 0), 1)
        cv2.rectangle(self.background, (128, 100), (256, 256), (0, 0, 0), 1)
        cv2.rectangle(self.background, (256, 100), (384, 256), (0, 0, 0), 1)
        cv2.rectangle(self.background, (384, 100), (516, 256), (0, 0, 0), 1)
        cv2.putText(self.background, self.weather_data[3], (5, 155), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[4], (5, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[5], (5, 205), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[6], (5, 230), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[7], (5, 255), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[8], (133, 155), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[9], (133, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[10], (133, 205), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[11], (133, 230), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[12], (133, 255), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[13], (261, 155), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[14], (261, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[15], (261, 205), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[16], (261, 230), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[17], (261, 255), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[18], (389, 155), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[19], (389, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[20], (389, 205), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[21], (389, 230), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.background, self.weather_data[22], (389, 255), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    def _paint_background(self):
        rows = self.background.shape[0]
        columns = self.background.shape[1]
        # Counting how often we should change color values
        step = [rows // (255 - self.colour[0]), rows // (255 - self.colour[1]), rows // (255 - self.colour[2])]
        for row in range(rows):
            if row > 0:
                if 0 == row % step[0]:
                    if self.colour[0] < 255:
                        self.colour[0] += 1
                if 0 == row % step[1]:
                    if self.colour[1] < 255:
                        self.colour[1] += 1
                if 0 == row % step[2]:
                    if self.colour[2] < 255:
                        self.colour[2] += 1
            for col in range(columns):
                self.background[row, col] = [*self.colour]
        weather_image = cv2.imread(self.card_weather)
        rows, columns, channels = weather_image.shape
        roi = self.background[0: rows, 0: columns]
        weather_gray = cv2.cvtColor(weather_image, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(weather_gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        background = cv2.bitwise_and(roi, roi, mask=mask_inv)
        weather_art = cv2.bitwise_and(weather_image, weather_image, mask=mask)
        res = cv2.add(background, weather_art)
        self.background[0:rows, 0:columns] = res


if __name__ == "__main__":
    image = ImageMaker("rain", ["Monday", "24", "august", "18...23", "19", "750", "20%", "7m/c",
                                "18...23", "19", "750", "20%", "7m/c",
                                "18...23", "19", "750", "20%", "7m/c",
                                "18...23", "19", "750", "20%", "7m/c", "дождь", "ливень", "переменная облачность",
                                "пасмурно"])
    image.make_card()
