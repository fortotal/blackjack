import random
import numpy as np

class Deck:
	def __init__(self):
		self._deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] * 4

	def shuffle_koloda(self):
		random.shuffle(self._deck)

	def get_card_from_koloda(self):
		card = self._deck.pop()
		return card

class Player:
	def __init__(self, trsh=None):
		self._hand = []
		self._play = True
		if trsh is not None:
			self.trsh = trsh
		else:
			self.trsh = np.random.choice(range(16, 21))

	def get_card(self, deck):
		if self.current_value() >= self.trsh:
			self._finish_game()
		else:
			self._hand.append(deck.get_card_from_koloda())

	def _finish_game(self):
		self._play = False
	
	def get_status(self):
		return self._play

	def current_value(self):
		return sum(self._hand)
