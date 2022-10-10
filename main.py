from kombat.battle import Battle
from kombat.player import Player, Attack

def main():
    print('Empezando batalla')
    battle_sequence: str = '{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2":{"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}'
    # battle_sequence: str = '{"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]},"player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P","k"]}}'
    # battle_sequence: str = '{"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}}'
    battle: Battle = Battle(battle_sequence=battle_sequence)

    battle.start_battle()

if __name__ ==  '__main__':
    main()