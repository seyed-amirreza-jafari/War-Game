from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5 import uic
import sys
import random
from PyQt5.QtGui import QPixmap

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		
		uic.loadUi('War_Game.ui', self)

		self.card_one = self.findChild(QLabel, 'Card_1')
		self.card_two = self.findChild(QLabel, 'Card_2')
		self.shuffle_button = self.findChild(QPushButton, 'Shuffle_Button')
		self.deal_button = self.findChild(QPushButton, 'Deal_Button')

		self.setWindowTitle('Dealer Score: 0 | Player Score: 0')

		self.shuffle()

		self.shuffle_button.clicked.connect(self.shuffle)
		self.dealer_score = 0
		self.player_score = 0
		self.deal_button.clicked.connect(self.deal)

		self.show()

	def shuffle(self):
		self.setWindowTitle('Dealer Score: 0 | Player Score: 0')
		self.dealer_score = 0
		self.player_score = 0

		suits = ['Clubs', 'Diamond', 'Hearts', 'Spades']
		values = range(1, 14)

		global deck
		deck = list()

		for suit in suits:
			for value in values:
				deck.append(f'{suit}_{value}')
		
		self.dealer_card = random.choice(deck)
		deck.remove(self.dealer_card)
		pixmap = QPixmap(f'J:/Programming/Python/GUI/Playing Cards/{self.dealer_card}.png')
		self.card_one.setPixmap(pixmap)

		self.player_card = random.choice(deck)
		deck.remove(self.player_card)
		pixmap = QPixmap(f'J:/Programming/Python/GUI/Playing Cards/{self.player_card}.png')
		self.card_two.setPixmap(pixmap)

	def score(self):
		dealer = int(self.dealer_card.split('_')[1])
		player = int(self.player_card.split('_')[1])

		if dealer > player:
			self.dealer_score += 1
		if player > dealer:
			self.player_score += 1

	def deal(self):
		try:
			self.dealer_card = random.choice(deck)
			deck.remove(self.dealer_card)
			pixmap = QPixmap(f'J:/Programming/Python/GUI/Playing Cards/{self.dealer_card}.png')
			self.card_one.setPixmap(pixmap)

			self.player_card = random.choice(deck)
			deck.remove(self.player_card)
			pixmap = QPixmap(f'J:/Programming/Python/GUI/Playing Cards/{self.player_card}.png')
			self.card_two.setPixmap(pixmap)

			self.score()
			self.setWindowTitle(f'Dealer Score: {self.dealer_score} | Player Score: {self.player_score}')

		except:
			self.score()

			if self.dealer_score > self.player_score:
				self.setWindowTitle('Game Over | Dealer Won!')
			elif self.player_score > self.dealer_score:
				self.setWindowTitle('Game Over | Player Won!')
			else:
				self.setWindowTitle('Game Over | Tied!')

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
