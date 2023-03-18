from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLCDNumber
from PyQt5.QtCore import QRect, QSize, QTime, QTimer
from PyQt5.QtGui import QFont
from random import sample, choice
from moudle_new import Minimax


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()

        self.game_rules(['X', 'O'])

        self.p = [1, 2, 3,
                  4, 5, 6,
                  7, 8, 9]

        self.setWindowTitle('tic tac toe')
        self.setGeometry(800, 300, 0, 0)
        self.setFixedSize(QSize(442, 441))
        self.minimax = Minimax(self.bot, self.opponet)

        self.setupUi()
        self.time_lcd()
        self.which_first()

    def game_rules(self, player):
        player = sample(player, 2)
        self.bot = player[0]
        self.opponet = player[1]
        self.winner = False
        self.is_finish = False
        self.select_font = QFont()
        self.select_font.setPointSize(35)

    def setupUi(self):

        font = QFont()
        font.setPointSize(1)

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(10, 80, 141, 71))
        self.pushButton.setFont(font)

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setGeometry(QRect(150, 80, 141, 71))
        self.pushButton_2.setFont(font)

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setGeometry(QRect(290, 80, 141, 71))
        self.pushButton_3.setFont(font)

        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setGeometry(QRect(10, 160, 141, 71))
        self.pushButton_4.setFont(font)

        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setGeometry(QRect(150, 160, 141, 71))
        self.pushButton_5.setFont(font)

        self.pushButton_6 = QPushButton(self)
        self.pushButton_6.setGeometry(QRect(290, 160, 141, 71))
        self.pushButton_6.setFont(font)

        self.pushButton_7 = QPushButton(self)
        self.pushButton_7.setGeometry(QRect(10, 240, 141, 71))
        self.pushButton_7.setFont(font)

        self.pushButton_8 = QPushButton(self)
        self.pushButton_8.setGeometry(QRect(150, 240, 141, 71))
        self.pushButton_8.setFont(font)

        self.pushButton_9 = QPushButton(self)
        self.pushButton_9.setGeometry(QRect(290, 240, 141, 71))
        self.pushButton_9.setFont(font)

        self.label = QLabel(self)
        self.label.setGeometry(QRect(50, 10, 351, 71))
        font = QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(24)
        # font.setBold(False)
        # font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(47, 330, 161, 51))
        font2 = QFont()
        font2.setFamily(("URW Gothic"))
        font2.setPointSize(23)
        font2.setWeight(50)
        self.label_2.setFont(font2)

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(52, 380, 161, 51))
        self.label_3.setFont(font2)

        # //#-- to do
        self.pushButton.clicked.connect(self.player_execute)
        self.pushButton_2.clicked.connect(self.player_execute)
        self.pushButton_3.clicked.connect(self.player_execute)
        self.pushButton_4.clicked.connect(self.player_execute)
        self.pushButton_5.clicked.connect(self.player_execute)
        self.pushButton_6.clicked.connect(self.player_execute)
        self.pushButton_7.clicked.connect(self.player_execute)
        self.pushButton_8.clicked.connect(self.player_execute)
        self.pushButton_9.clicked.connect(self.player_execute)

    def which_first(self):

        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        self.pushButton_9.setDisabled(True)

        self.label.setText("First move ?")

        self.pushButton_bot = QPushButton(self)
        self.pushButton_bot.setGeometry(QRect(260, 25, 61, 41))
        font3 = QFont()
        font3.setFamily(("Z003 [urw]"))
        font3.setPointSize(21)
        font3.setWeight(50)
        self.pushButton_bot.setFont(font3)
        self.pushButton_bot.setStyleSheet("background-color:red")

        self.pushButton_you = QPushButton(self)
        self.pushButton_you.setGeometry(QRect(330, 25, 61, 41))
        self.pushButton_you.setFont(font3)
        self.pushButton_you.setStyleSheet("background-color:blue")

        self.pushButton_bot.setText("Bot")
        self.pushButton_you.setText("You")

        self.pushButton_bot.clicked.connect(self.set_text)
        self.pushButton_you.clicked.connect(self.set_text)

    def set_text(self):

        turn = self.sender()

        self.pushButton_bot.deleteLater()
        self.pushButton_you.deleteLater()

        self.pushButton.setText("1")
        self.pushButton_2.setText("2")
        self.pushButton_3.setText("3")
        self.pushButton_4.setText("4")
        self.pushButton_5.setText("5")
        self.pushButton_6.setText("6")
        self.pushButton_7.setText("7")
        self.pushButton_8.setText("8")
        self.pushButton_9.setText("9")
        self.label.setText("Please start the game ")
        self.label_2.setText(f"You => {self.opponet}")
        self.label_3.setText(f"Bot => {self.bot}")

        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)

        if turn.text() == "Bot":
            self.bot_execution()

    def player_execute(self):
        sender = self.sender()

        self.p[int(sender.text())-1] = self.opponet
        sender.setFont(self.select_font)
        sender.setText(self.opponet)

        sender.setStyleSheet("color:blue")

        sender.setDisabled(True)

        self.lead_round(self.bot)

    def bot_execution(self):
        game_match = self.minimax.generate_2d(self.p)
        button_number = self.minimax.findBestMove(game_match)
        # button_number = 1
        # print(button_number)

        if button_number == 0:
            self.pushButton.setFont(self.select_font)
            self.pushButton.setText(self.bot)
            self.pushButton.setStyleSheet("color:red")
            self.pushButton.setDisabled(True)
            self.p[0] = self.bot

        elif button_number == 1:
            self.pushButton_2.setFont(self.select_font)
            self.pushButton_2.setText(self.bot)
            self.pushButton_2.setStyleSheet("color:red")
            self.pushButton_2.setDisabled(True)
            self.p[1] = self.bot

        elif button_number == 2:
            self.pushButton_3.setFont(self.select_font)
            self.pushButton_3.setText(self.bot)
            self.pushButton_3.setStyleSheet("color:red")
            self.pushButton_3.setDisabled(True)
            self.p[2] = self.bot

        elif button_number == 3:
            self.pushButton_4.setFont(self.select_font)
            self.pushButton_4.setText(self.bot)
            self.pushButton_4.setStyleSheet("color:red")
            self.pushButton_4.setDisabled(True)
            self.p[3] = self.bot

        elif button_number == 4:
            self.pushButton_5.setFont(self.select_font)
            self.pushButton_5.setText(self.bot)
            self.pushButton_5.setStyleSheet("color:red")
            self.pushButton_5.setDisabled(True)
            self.p[4] = self.bot

        elif button_number == 5:
            self.pushButton_6.setFont(self.select_font)
            self.pushButton_6.setText(self.bot)
            self.pushButton_6.setStyleSheet("color:red")
            self.pushButton_6.setDisabled(True)
            self.p[5] = self.bot

        elif button_number == 6:
            self.pushButton_7.setFont(self.select_font)
            self.pushButton_7.setText(self.bot)
            self.pushButton_7.setStyleSheet("color:red")
            self.pushButton_7.setDisabled(True)
            self.p[6] = self.bot

        elif button_number == 7:
            self.pushButton_8.setFont(self.select_font)
            self.pushButton_8.setText(self.bot)
            self.pushButton_8.setStyleSheet("color:red")
            self.pushButton_8.setDisabled(True)
            self.p[7] = self.bot

        elif button_number == 8:
            self.pushButton_9.setFont(self.select_font)
            self.pushButton_9.setText(self.bot)
            self.pushButton_9.setStyleSheet("color:red")
            self.pushButton_9.setDisabled(True)
            self.p[8] = self.bot
        # print(self.p)
        self.lead_round(self.opponet)

    def lead_round(self, whose_turn):
        self.label.setText(choice(
            ["Dont give up", "You can do it", "Tecnial move", "Great", "You are the best"])+" !!")
        self.check_winner()

        is_left = self.minimax.generate_2d(self.p)

        if (self.minimax.isMovesLeft(is_left) == False):
            if (not self.is_finish):
                self.finalization(False)

        if whose_turn == self.bot:
            self.bot_execution()

    def check_winner(self):
        yellow = "background-color:yellow"
        if self.p[0] == self.p[1] == self.p[2]:
            self.pushButton.setStyleSheet(yellow)
            self.pushButton_2.setStyleSheet(yellow)
            self.pushButton_3.setStyleSheet(yellow)
            self.winner = self.p[0]

        elif self.p[3] == self.p[4] == self.p[5]:
            self.pushButton_4.setStyleSheet(yellow)
            self.pushButton_5.setStyleSheet(yellow)
            self.pushButton_6.setStyleSheet(yellow)
            self.winner = self.p[3]

        elif self.p[6] == self.p[7] == self.p[8]:
            self.pushButton_7.setStyleSheet(yellow)
            self.pushButton_8.setStyleSheet(yellow)
            self.pushButton_9.setStyleSheet(yellow)
            self.winner = self.p[6]

        elif self.p[0] == self.p[3] == self.p[6]:
            self.pushButton.setStyleSheet(yellow)
            self.pushButton_4.setStyleSheet(yellow)
            self.pushButton_7.setStyleSheet(yellow)
            self.winner = self.p[0]

        elif self.p[1] == self.p[4] == self.p[7]:
            self.pushButton_2.setStyleSheet(yellow)
            self.pushButton_5.setStyleSheet(yellow)
            self.pushButton_8.setStyleSheet(yellow)
            self.winner = self.p[1]

        elif self.p[2] == self.p[5] == self.p[8]:
            self.pushButton_3.setStyleSheet(yellow)
            self.pushButton_6.setStyleSheet(yellow)
            self.pushButton_9.setStyleSheet(yellow)
            self.winner = self.p[2]

        elif self.p[0] == self.p[4] == self.p[8]:
            self.pushButton.setStyleSheet(yellow)
            self.pushButton_5.setStyleSheet(yellow)
            self.pushButton_9.setStyleSheet(yellow)
            self.winner = self.p[0]

        elif self.p[2] == self.p[4] == self.p[6]:
            self.pushButton_3.setStyleSheet(yellow)
            self.pushButton_5.setStyleSheet(yellow)
            self.pushButton_7.setStyleSheet(yellow)
            self.winner = self.p[2]

        if (self.winner != False):
            self.is_finish = True
            self.finalization(True)

    def finalization(self, games_end):

        if (games_end):
            if self.winner == self.bot:
                self.label.setText(" sorry  Bot  won !!!")
            else:
                self.label.setText(" congatulations You won :)")

            self.pushButton.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.pushButton_5.setDisabled(True)
            self.pushButton_6.setDisabled(True)
            self.pushButton_7.setDisabled(True)
            self.pushButton_8.setDisabled(True)
            self.pushButton_9.setDisabled(True)
            self.timer.stop()
            self.lcdNumber.setStyleSheet("color:red; background-color:white")

        else:
            self.label.setText(" game has no winner")
            self.timer.stop()

    def time_lcd(self):
        self.lcdNumber = QLCDNumber(self)

        self.lcdNumber.setGeometry(QRect(300, 330, 121, 91))
        # self.lcdNumber.resize(200,200)

        self.currentTime = QTime(0, 0)
        self.lcdNumber.display(self.currentTime.toString('mm:ss'))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLcdNumberContent)
        self.timer.start(1000)

    def updateLcdNumberContent(self):

        self.currentTime = self.currentTime.addSecs(1)
        self.lcdNumber.display(self.currentTime.toString('mm:ss'))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    Ui = Ui_Form()
    Ui.show()

    sys.exit(app.exec())
