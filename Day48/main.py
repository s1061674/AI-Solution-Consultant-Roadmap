from dataclasses import dataclass
from enum import Enum

class PlayerStatus(Enum):
    ALIVE = "alive"
    DEAD  = "dead"
    STUNNED = "stunned"

@dataclass
class Player:
    name: str
    status: PlayerStatus

    def is_alive(self) -> bool:
        return self.status == PlayerStatus.ALIVE

    def get_status_message(self) -> str:
        match self.status:

            case PlayerStatus.ALIVE:
                return "玩家存活"
            
            case PlayerStatus.DEAD:
                return "玩家死亡"
            
            case PlayerStatus.STUNNED:
                return "玩家暈眩"
            
p1 = Player("Arthur", PlayerStatus.ALIVE)
p2 = Player("Amy", PlayerStatus.STUNNED)

print(p1.name)
print(p1.is_alive())
print(p1.get_status_message())
print(p2.name)
print(p2.is_alive())
print(p2.get_status_message())