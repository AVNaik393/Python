import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Get Weather",self)
        self.title = QLabel("Apurva The Great!", self)
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.temp = QLabel(self)
        self.Icon = QLabel(self)
        self.Desc = QLabel(self)

        self.UI()

    def UI(self):
        self.setWindowTitle("Apurva's Weather")
        self.resize(400, 550)
        hbox = QHBoxLayout()
        hbox.addWidget(self.textbox1)
        hbox.addWidget(self.textbox2)
        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addLayout(hbox)
        vbox.addWidget(self.button)
        vbox.addWidget(self.temp)
        vbox.addWidget(self.Icon)
        vbox.addWidget(self.Desc)

        self.setLayout(vbox)

        self.title.setAlignment(Qt.AlignCenter)
        self.temp.setAlignment(Qt.AlignCenter)
        self.textbox1.setAlignment(Qt.AlignCenter)
        self.textbox2.setAlignment(Qt.AlignCenter)
        self.Icon.setAlignment(Qt.AlignCenter)
        self.Desc.setAlignment(Qt.AlignCenter)

        self.title.setObjectName("title")
        self.temp.setObjectName("temp")
        self.textbox1.setObjectName("textbox")
        self.textbox2.setObjectName("textbox")
        self.Icon.setObjectName("Icon")
        self.button.setObjectName("button")
        self.Desc.setObjectName("Desc")

        self.setStyleSheet("""
        QWidget {
            background-color: #0F172A;
            color: white;
            font-family: "Segoe UI";
        }

        QLabel#title {
            font-size: 26px;
            font-weight: bold;
            color: #38BDF8;
            padding: 15px;
        }

        QLineEdit#textbox {
            background-color: #1E293B;
            color: white;
            border: 2px solid #334155;
            border-radius: 12px;
            padding: 10px;
            font-size: 22px;
            margin: 5px 20px;
        }

        QLineEdit#textbox:focus {
            border: 2px solid #38BDF8;
        }

        QPushButton#button {
            background-color: #0EA5E9;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px;
            font-size: 20px;
            font-weight: bold;
            margin: 5px 30px;
        }

        QPushButton#button:hover {
            background-color: #38BDF8;
        }

        QPushButton#button:pressed {
            background-color: #0284C7;
        }

        QLabel#temp {
            font-size: 50px;
            font-weight: bold;
            color: white;
            padding: 20px;
        }

        QLabel#Icon {
            font-size: 70px;
            padding: 10px;
        }

        QLabel#Desc {
            font-size: 25px;
            color: #CBD5E1;
            padding: 10px;
            }
        """)

        self.button.clicked.connect(self.getWeather)

    def getWeather(self):
        api = "f6748d122796e08629a781755aece630"
        t1 = self.textbox1.text()
        t2 = self.textbox2.text()

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={t1}&lon={t2}&appid={api}"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            self.showWeather(data)
        else:
            self.error()

    def error(self):
        self.temp.setText("Error!!")
        self.Icon.clear()
        self.Desc.clear()

    def showWeather(self, data):
        temp = data["main"]["temp"] -273.15 
        self.temp.setText(f"{temp : 1f} °C")
        
        datadesc = data["weather"][0]["description"]
        self.Desc.setText(datadesc)

        icon = "*"
        if temp<=0 : icon = "☃️"
        elif 0<=temp<=10: icon = "❄️"
        elif 10<=temp<=20: icon = "🌧️"
        elif 20<=temp<=30: icon = "🌪️"
        else: icon = "☀️"

        self.Icon.setText(icon)

def main(): 
    app = QApplication(sys.argv)
    MyApp = MyWindow()
    MyApp.show()
    sys.exit(app.exec_())

if(__name__ == '__main__'):
    main()

