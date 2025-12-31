from typing import TypedDict, List

class DebateState(TypedDict):
    topic: str
    clarified_topic: str

    for_opening: str
    against_opening: str

    for_rebuttal: str
    against_rebuttal: str

    final_summary: str
    