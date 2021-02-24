import player as pl


def test_player_logic():
	deck = pl.Deck()
	deck.shuffle_koloda()
	simple_player = pl.Player(16)
	while simple_player.get_status():
		simple_player.get_card(deck)
	assert simple_player.current_value() < 16

