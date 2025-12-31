from state import DebateState
from agents import (
    topic_classifier,
    for_opening_agent,
    against_opening_agent,
    for_rebuttal_agent,
    against_rebuttal_agent,
    judge_agent,
)


def run_debate(topic: str) -> DebateState:
    state: DebateState = {
        "topic": topic,
        "clarified_topic": "",
        "for_opening": "",
        "against_opening": "",
        "for_rebuttal": "",
        "against_rebuttal": "",
        "final_summary": "",
    }

    # Step 1: Clarify topic
    state["clarified_topic"] = topic_classifier(topic)

    # Step 2: Opening arguments
    state["for_opening"] = for_opening_agent(state["clarified_topic"])
    state["against_opening"] = against_opening_agent(state["clarified_topic"])

    # Step 3: Rebuttals
    state["for_rebuttal"] = for_rebuttal_agent(
        state["clarified_topic"],
        state["against_opening"]
    )

    state["against_rebuttal"] = against_rebuttal_agent(
        state["clarified_topic"],
        state["for_opening"]
    )

    # Step 4: Judge summary
    combined_for = state["for_opening"] + "\n\n" + state["for_rebuttal"]
    combined_against = state["against_opening"] + "\n\n" + state["against_rebuttal"]

    state["final_summary"] = judge_agent(
        state["clarified_topic"],
        combined_for,
        combined_against
    )

    return state
