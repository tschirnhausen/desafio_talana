from enum import Enum
from typing import List, NamedTuple

class UnknownAttack(Exception):
    ''' The provided combination of keys is not present for the present player '''


class BasicMovement(Enum):
    UP = 'W'
    DOWN = 'S'
    LEFT = 'A'
    RIGHT = 'D'
    PUNCH = 'P'
    KICK = 'K'
    NONE = 'q'

    def get_basic_movement_name(self, is_left: bool = True):
        if self is BasicMovement.UP:
            return 'sube'
        elif self is BasicMovement.DOWN:
            return 'se agacha'
        elif self is BasicMovement.PUNCH:
            return 'da un puñetazo'
        elif self is BasicMovement.KICK:
            return 'da una patada'
        elif self is BasicMovement.LEFT:
            if is_left:
                return 'retrocede'
            return 'avanza'
        elif self is BasicMovement.RIGHT:
            if is_left:
                return 'avanza'
            return 'retrocede'
        else:
            return 'ninguno'
        

class Attack(NamedTuple):
    name: str
    combination: str
    activation_attack: str
    power: int


class Player:
    name: str
    energy_points: int
    attacks: List[Attack]
    is_left: bool = False

    def __init__(self, name: str, energy_points: int, attacks: list, is_left: bool = False):
        self.name = name
        self.energy_points = energy_points
        self.attacks = attacks
        self.is_left = is_left


    def damage(self, damage: int) -> int:
        self.energy_points = self.energy_points - damage
        return self.energy_points


    def get_attack(self, combination: str, activation: str) -> Attack:       
        attack_lst: List[Attack] = [attack for attack in self.attacks if attack.combination == combination and attack.activation_attack == activation]
        if len(attack_lst) != 1:
            return self.attacks[-1]
    
        single_attack: Attack = (lambda x: x)(*attack_lst)

        return single_attack


    def _is_attack(self, combination: str, activation:str) -> bool:
        attack_lst: List[Attack] = [attack for attack in self.attacks if attack.combination == combination and attack.activation_attack == activation]
        if len(attack_lst) != 1:
            return False
        return True


    def _get_message(self, keys: str, is_left: bool) -> str:
        try:
            return BasicMovement(keys).get_basic_movement_name(is_left)
        except Exception as e:
            return ''


    def get_actions(self, combination:str, activation:str, is_left:bool = True) -> dict:

        if combination is None and activation is None:
            return {
                'message': 'no hace nada!',
                'damage': 0
            }

        if self._is_attack(combination, activation):
            attack: Attack = self.get_attack(combination, activation)
            return {
                'message': f'usa un {attack.name}',
                'damage': attack.power
            }
    
        message_1: str = self._get_message(combination, is_left)
        message_2: str = self._get_message(activation, is_left)

        if message_1 == '' and message_2 == '':
            return {
                'message': 'se mueve',
                'damage': 0
            }
        elif message_1 and message_2:
            return {
                'message': f'{message_1} y {message_2}',
                'damage': 1
            }
        elif message_1:
            return {
                'message': f'{message_1}',
                'damage': 0
            }

        return {
            'message': f'se mueve y {message_2}',
            'damage': 1
        }
