from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import sys
import requests


class MenuWindow(QMainWindow):
    def __init__(self, file):
        super(MenuWindow, self).__init__()
        self.pixmap = QPixmap(file.name)
        self.mapLabel = QLabel(self)
        self.initUi()

    def initUi(self):
        self.setGeometry(420, 120, 450, 450)
        self.mapLabel.resize(450, 450)
        self.mapLabel.move(0, 0)
        self.mapLabel.setPixmap(self.pixmap)


ll = '37.620070,55.753630'
spn = '0.01,0.01'
l = 'map'

map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&size=450,450&spn={spn}&l={l}"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
    file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenuWindow(file)
    ex.show()
    sys.exit(app.exec())
