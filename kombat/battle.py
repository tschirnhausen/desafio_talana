from kombat.player import Player, Attack
from typing import List, NamedTuple, Optional
import json

class InvalidBattleSequence(Exception):
    ''' An error ocurred while parsing the sequence of the battle '''


class IncompleteBattleSequence(Exception):
    ''' Missing information while checking the movements of the battle '''


class Battle:
    player_1: Player
    player_2: Player
    battle_sequence: dict

    DEFAULT_PLAYER: str = 'player1'

    def __init__(self, battle_sequence: str):
        try:
            dict_sequence = json.loads(battle_sequence)
            self.battle_sequence = dict_sequence
        except Exception as e:
            raise InvalidBattleSequence('Invalid JSON: Please check the battle sequence')

        player_1 = Player(
            name='Tony',
            energy_points=6,
            is_left=True,
            attacks=[
                Attack(
                    name='Taladoken',
                    combination='DSD',
                    activation_attack='P',
                    power=3
                ),
                Attack(
                    name='Remuyuken',
                    combination='SD',
                    activation_attack='K',
                    power=2
                ),
                Attack(
                    name='Puño',
                    combination='P',
                    activation_attack=None,
                    power=1
                ),
                Attack(
                    name='Patada',
                    combination='K',
                    activation_attack=None,
                    power=1
                )
            ]
        )

        player_2 = Player(
            name='Arnaldor',
            energy_points=6,
            attacks=[
                Attack(
                    name='Remuyuken',
                    combination='SA',
                    activation_attack='K',
                    power=3
                ),
                Attack(
                    name='Taladoken',
                    combination='ASA',
                    activation_attack='P',
                    power=2
                ),
                Attack(
                    name='Puño',
                    combination='P',
                    activation_attack=None,
                    power=1
                ),
                Attack(
                    name='Patada',
                    combination='K',
                    activation_attack=None,
                    power=1
                )
            ]
        )

        self.player_1 = player_1
        self.player_2 = player_2


    def _get_min_dict(self, dict_data: dict) -> tuple:
        return min(dict_data.items(), key=lambda x: x[1])

    
    def _get_single_stroke(self) -> Attack:
        pass

    def _get_max_length(self) -> int:
        player_1_data: dict = self.battle_sequence.get('player1', None)
        player_2_data: dict = self.battle_sequence.get('player2', None)

        player_1_movements: list = len(player_1_data.get('movimientos'))
        player_2_movements: list = len(player_2_data.get('movimientos'))

        return max(player_1_movements, player_2_movements)


    def _check_first_player(self):
        player_1_data: dict = self.battle_sequence.get('player1', None)
        player_2_data: dict = self.battle_sequence.get('player2', None)

        if player_1_data is None or player_2_data is None:
            raise IncompleteBattleSequence('Error while reading the battle: Missing information for at least one player')

        player_1_movements: list = len(player_1_data.get('movimientos'))
        player_2_movements: list = len(player_2_data.get('movimientos'))

        player_1_strokes: list = len(player_1_data.get('golpes'))
        player_2_strokes: list = len(player_2_data.get('golpes'))

        players_data: dict = {
            'total_actions': {
                'player1': player_1_movements + player_1_strokes,
                'player2': player_2_movements + player_2_strokes
            },
            'total_movements': {
                'player1': player_1_movements,
                'player2': player_2_movements
            },
            'total_strokes': {
                'player1': player_1_strokes,
                'player2': player_2_strokes
            }
        }

        # First round of checking: Total actions
        if players_data.get('total_actions').get('player1') != players_data.get('total_actions').get('player2'):
            return self._get_min_dict(players_data.get('total_actions'))
        # Only movements if total re equal
        elif players_data.get('total_movements').get('player1') != players_data.get('total_movements').get('player2'):
            return self._get_min_dict(players_data.get('total_movements'))
        # Only strokes if movements are equal
        elif players_data.get('total_strokes').get('player1') != players_data.get('total_strokes').get('player2'):
            return self._get_min_dict(players_data.get('total_strokes'))
        # Default case
        else:
            return (self.DEFAULT_PLAYER, None)

    
    def _get_winner_message(self, loser: Player) -> str:
        winner: Player = None

        if loser == self.player_1:
            winner = self.player_2
        elif loser == self.player_2:
            winner = self.player_1

        return f'¡La batalla termina! El ganador es {winner.name} y aún le quedan {winner.energy_points} puntos de vida'


    def _update_battle_at_next(self, player: Player, damage: int):
        current_energy: int = player.damage(damage=damage)
        if current_energy < 1:
            print(self._get_winner_message(player))
            return True
        return False


    def _get_key_action(self, player: str, action_type: str, current_round: int) -> Optional[str]:
        if current_round > (len(self.battle_sequence.get(player).get(action_type)) - 1):
            ''' Case when player didn't press any key '''
            return None
        return self.battle_sequence.get(player).get(action_type)[current_round]


    def start_battle(self) -> str:
        first_player, player_movements_qty = self._check_first_player() # ('playerN', 2)
        second_player: str = 'player2' if first_player == 'player1' else 'player1'

        first_player_obj: Player = self.player_1 if first_player == self.DEFAULT_PLAYER else self.player_2
        second_player_obj: Player = self.player_2 if first_player == self.DEFAULT_PLAYER else self.player_1

        IS_BATTLE_FINISHED: bool = False
        current_round: int = 0

        while not IS_BATTLE_FINISHED:
            first_player_mov: str = self._get_key_action(player=first_player, action_type='movimientos', current_round=current_round)
            first_player_stroke: str = self._get_key_action(player=first_player, action_type='golpes', current_round=current_round)

            second_player_mov: str = self._get_key_action(player=second_player, action_type='movimientos', current_round=current_round)
            second_player_stroke: str = self._get_key_action(player=second_player, action_type='golpes', current_round=current_round)

            first_player_actions = first_player_obj.get_actions(
                    combination=first_player_mov,
                    activation=first_player_stroke,
                    is_left=first_player_obj.is_left
                )

            print(first_player_obj.name, first_player_actions.get('message'))

            # Realizar daño del primer jugador al segundo
            if self._update_battle_at_next(second_player_obj, first_player_actions.get('damage')):
                IS_BATTLE_FINISHED = True
                break

            second_player_actions = second_player_obj.get_actions(
                combination=second_player_mov,
                activation=second_player_stroke,
                is_left=second_player_obj.is_left
            )

            print(second_player_obj.name, second_player_actions.get('message'))

            # Realizar daño del segundo jugador al primero
            if self._update_battle_at_next(first_player_obj, second_player_actions.get('damage')):
                IS_BATTLE_FINISHED = True
                break

            current_round += 1 # update

            if current_round == self._get_max_length():
                IS_BATTLE_FINISHED = True
