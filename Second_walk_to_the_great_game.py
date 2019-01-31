import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setGeometry(900, 900, 900, 900)
        self.setWindowTitle('Расчет оптовой и розничной цены')

        self.btn = QPushButton('Рассчитать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(500, 800)
        self.btn.clicked.connect(self.math)

        self.label = QLabel(self)
        self.label.setText("Введите переменные")
        self.label.move(40, 30)

        self.name_label = QLabel(self)
        self.name_label.setText("Стартовый капитал")
        self.name_label.move(40, 90)

        self.name_label = QLabel(self)
        self.name_label.setText("Сырье и материалы")
        self.name_label.move(40, 140)

        self.label1 = QLabel(self)
        self.label1.setText("Полуфабрикаты и комплектующие")
        self.label1.move(40, 190)

        self.label1 = QLabel(self)
        self.label1.setText("Топливо и энергия на технологические цели")
        self.label1.move(40, 240)

        self.label1 = QLabel(self)
        self.label1.setText("Основная заработная плата")
        self.label1.move(40, 290)

        self.label1 = QLabel(self)
        self.label1.setText("Дополнительная заработная плата")
        self.label1.move(40, 340)

        self.label1 = QLabel(self)
        self.label1.setText("Отчисления на социальные нужды")
        self.label1.move(40, 390)

        self.label1 = QLabel(self)
        self.label1.setText("Инструменты и приспособления специального назначения")
        self.label1.move(40, 440)

        self.label1 = QLabel(self)
        self.label1.setText("Расходы на эксплуатацию технологического оборудования")
        self.label1.move(40, 490)

        self.label1 = QLabel(self)
        self.label1.setText("Цеховые расходы")
        self.label1.move(40, 540)

        self.label1 = QLabel(self)
        self.label1.setText("Общезаводские производственные расходы")
        self.label1.move(40, 590)

        self.label1 = QLabel(self)
        self.label1.setText("Внепроизводственные расходы")
        self.label1.move(40, 640)

        self.label1 = QLabel(self)
        self.label1.setText("Технологическая себестоимость")
        self.label1.move(40, 690)

        self.label1 = QLabel(self)
        self.label1.setText("Цеховая себестоимость")
        self.label1.move(40, 740)

        self.label1 = QLabel(self)
        self.label1.setText("Производственная себестоимость")
        self.label1.move(40, 790)

        self.label1 = QLabel(self)
        self.label1.setText("Полная себестоимость")
        self.label1.move(40, 840)

        self.label1 = QLabel(self)
        self.label1.setText("% наценки")
        self.label1.move(600, 90)

        self.label1 = QLabel(self)
        self.label1.setText("Торговая надбавка(%)")
        self.label1.move(550, 140)

        self.label1 = QLabel(self)
        self.label1.setText("Обьем выпускаемой продукции")
        self.label1.move(550, 190)

        self.label1 = QLabel(self)
        self.label1.setText("Оптовая цена предприятия")
        self.label1.move(550, 540)

        self.label1 = QLabel(self)
        self.label1.setText("НДС 20%")
        self.label1.move(550, 590)

        self.label1 = QLabel(self)
        self.label1.setText("Розничная цена")
        self.label1.move(550, 640)

        self.label1 = QLabel(self)
        self.label1.setText("Прибыль")
        self.label1.move(550, 690)









        self.name_input1 = QLineEdit(self)
        self.name_input1.move(400, 90)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(400, 140)

        self.name_input3 = QLineEdit(self)
        self.name_input3.move(400, 190)

        self.name_input4 = QLineEdit(self)
        self.name_input4.move(400, 240)

        self.name_input5 = QLineEdit(self)
        self.name_input5.move(400, 290)

        self.name_input6 = QLineEdit(self)
        self.name_input6.move(400, 340)

        self.name_input7 = QLineEdit(self)
        self.name_input7.move(400, 390)

        self.name_input8 = QLineEdit(self)
        self.name_input8.move(400, 440)

        self.name_input9 = QLineEdit(self)
        self.name_input9.move(400, 490)

        self.name_input10 = QLineEdit(self)
        self.name_input10.move(400, 540)

        self.name_input11 = QLineEdit(self)
        self.name_input11.move(400, 590)

        self.name_input12 = QLineEdit(self)
        self.name_input12.move(400, 640)

        self.name_input13 = QLineEdit(self)
        self.name_input13.move(700, 90)

        self.name_input14 = QLineEdit(self)
        self.name_input14.move(700, 140)





        self.LCD_count1 = QLCDNumber(self)
        self.LCD_count1.move(400, 690)

        self.LCD_count2 = QLCDNumber(self)
        self.LCD_count2.move(400, 740)

        self.LCD_count3 = QLCDNumber(self)
        self.LCD_count3.move(400, 790)

        self.LCD_count4 = QLCDNumber(self)
        self.LCD_count4.move(400, 840)

        self.LCD_count5 = QLCDNumber(self)
        self.LCD_count5.move(700, 540)

        self.LCD_count6 = QLCDNumber(self)
        self.LCD_count6.move(700, 590)

        self.LCD_count7 = QLCDNumber(self)
        self.LCD_count7.move(700, 640)

        self.LCD_count8 = QLCDNumber(self)
        self.LCD_count8.move(700, 690)

        self.LCD_count9 = QLCDNumber(self)
        self.LCD_count9.move(750, 190)













        self.count = 0
    def math(self):
        self.count1 = "{}".format(int(self.name_input1.text()))
        self.count2 = "{}".format(int(self.name_input2.text()))
        self.count3 = "{}".format(int(self.name_input3.text()))
        self.count4 = "{}".format(int(self.name_input4.text()))
        self.count5 = "{}".format(int(self.name_input5.text()))
        self.count6 = "{}".format(int(self.name_input6.text()))
        self.count7 = "{}".format(int(self.name_input7.text()))
        self.count8 = "{}".format(int(self.name_input8.text()))
        self.count9 = "{}".format(int(self.name_input9.text()))
        self.count10 = "{}".format(int(self.name_input10.text()))
        self.count11 = "{}".format(int(self.name_input11.text()))
        self.count12 = "{}".format(int(self.name_input12.text()))
        self.count13 = "{}".format(int(self.name_input13.text()))
        self.count14 = "{}".format(int(self.name_input14.text()))

        self.tech = int(self.count2) + int(self.count3) + int(self.count4) + int(self.count5) \
        + int(self.count6) + int(self.count7) + int(self.count8) + int(self.count9)
        self.caeh = self.tech + int(self.count10)

        self.ind = self.caeh + int(self.count11)
        self.full = self.ind + int(self.count12)
        self.opt = float(self.full) * (100 + (float(self.count13)))/100
        self.NDS = self.opt / 100 * 20
        self.rozn = (self.opt + self.NDS) * (100 + (float(self.count14)))/100
        self.a = float(self.count1) / float(self.full)
        self.profit = self.a * (float(self.count13)/100)





        self.LCD_count1.display(self.tech)
        self.LCD_count2.display(self.caeh)
        self.LCD_count3.display(self.ind)
        self.LCD_count4.display(self.full)
        self.LCD_count5.display(self.opt)
        self.LCD_count6.display(self.NDS)
        self.LCD_count7.display(self.rozn)
        self.LCD_count8.display(self.profit)
        self.LCD_count9.display(self.a)















if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
