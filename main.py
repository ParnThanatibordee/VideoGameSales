from game_sale import GameSale
from game_sale_ui import GameSaleUI

if __name__ == '__main__':
    game_sale = GameSale()
    UI = GameSaleUI(game_sale)
    UI.run()
