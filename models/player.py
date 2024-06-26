from datetime import datetime
from typing import NamedTuple

from .units import UnitType
from .alliance import Alliance

class Player(NamedTuple):
    id: int
    registered_at: datetime
    gold: int
    ruby: int
    units: dict[UnitType, int]
    npc_level: int
    last_npc_win: datetime | None
    queue_slots: int
    alliance: Alliance
    silver: int
    observer: bool
    peace: int
    letter_bird: int
    food_stored: int
    prestige: int

    @staticmethod
    def from_data(data, alliance_data):
        if data is None:
            return None
        
        return Player(
            id=data["id"],
            registered_at=datetime.fromisoformat(data["registered_at"]),
            gold=data["gold"],
            ruby=data["ruby"],
            units={
                UnitType.INFANTRY: data["units"]["infantry"],
                UnitType.CAVALRY: data["units"]["cavalry"],
                UnitType.ARTILLERY: data["units"]["artillery"],
                UnitType.ASSASSINS: data["units"]["assassins"],
                UnitType.BOWMEN: data["units"]["bowmen"],
                UnitType.BIG_BOWMEN: data["units"]["big_bowmen"],
                UnitType.HEAVY_MEN: data["units"]["heavy_men"],
                UnitType.KINGS_GUARDS: data["units"]["kings_guards"]
            },
            npc_level=data["npc_level"],
            last_npc_win=datetime.fromisoformat(data["last_npc_win"]),
            votes=data["votes"],
            alliance=alliance_data,
            queue_slots=data["queue_slots"],
            silver=data["silver"],
            observer=data["observer"],
            peace=data["peace"],
            letter_bird=data["letter_bird"],
            food_stored=data["food_stored"],
            prestige=data["prestige"]
        )

class EventPlayer(NamedTuple):
    user_id: int
    event_points: int
    skins: list
    currently_wearing: int

    @staticmethod
    def from_database(row):
        if row is None:
            return None
        return EventPlayer(
            user_id=row[0],
            event_points=row[1],
            skins=row[2],
            currently_wearing=row[3]
        )