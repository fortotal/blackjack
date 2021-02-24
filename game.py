from player import Deck, Player



class SimpleGame:
	def __init__(self, *players, deck):
		self._players = players
		self._deck = deck

	def start_game(self):
		self._deck.shuffle_koloda()
		for player in self._players:
			for i in range(2):
				player.get_card(self._deck)

	def game_round(self):
		print('round')
