from langchain_core.prompts import PromptTemplate
from llm import llm

def topic_classifier(topic:str) -> str:
    prompt = PromptTemplate.from_template(
        """
clarify the following debate topic into precise and debatable prepositions
avoid ambiguity. and make it suitable for formal debate.
topic: {topic}
"""
    )

    return (prompt | llm).invoke({"topic":topic}).content

def for_opening_agent(topic:str) -> str:
    prompt = PromptTemplate.from_template(""""
You are a professional debater arguing STRICTLY IN FAVOR of the motion below.

Rules:
- Respond in bullet points
- Each bullet should be a single clear argument
- Max 4 bullets
- No long paragraphs

Motion:
{topic}                                          
""")
    return (prompt | llm).invoke({"topic":topic}).content

def against_opening_agent(topic: str) -> str:
    prompt = PromptTemplate.from_template(
        """
You are a professional debater arguing STRICTLY AGAINST the motion below.

Rules:
- Respond in bullet points
- Each bullet should be a single clear argument
- Max 4 bullets
- No long paragraphs

Motion:
{topic}
"""
    )
    return (prompt | llm).invoke({"topic": topic}).content

def for_rebuttal_agent(topic: str, opponent_argument: str) -> str:
    prompt = PromptTemplate.from_template("""
You are rebutting the following opposing argument.

Rules:
- Respond in bullet points
- Each bullet should be a single clear argument
- Max 4 bullets
- No long paragraphs
- Each bullet must directly counter the opponent

Motion:
{topic}

Opponent Argument:
{argument}
"""
    )
    return (prompt | llm).invoke({"topic": topic, 
                                  "argument": opponent_argument
                                  }).content

def against_rebuttal_agent(topic: str, opponent_argument: str) -> str:
    prompt = PromptTemplate.from_template("""
You are rebutting the following opposing argument.

Rules:
- Respond in bullet points
- Each bullet should be a single clear argument
- Max 4 bullets
- No long paragraphs
- Each bullet must directly counter the opponent
                                          

Motion:
{topic}

Opponent Argument:
{argument}

"""
    )
    return (prompt | llm).invoke({"topic": topic, 
                                  "argument": opponent_argument
                                  }).content

def judge_agent(topic:str, for_args:str, against_args:str) -> str:
    prompt = PromptTemplate.from_template("""
You are a neutral debate judge.

Output format:
- Summary of FOR side (bullets)
- Summary of AGAINST side (bullets)
- Key tension between the two

Rules:
- Be neutral
- Use bullet points
- No long paragraphs

Motion:
{topic}

FOR SIDE:
{for_args}

AGAINST SIDE:
{against_args}
""")
    return (prompt | llm).invoke({"topic": topic, 
                                  "for_args": for_args,
                                  "against_args": against_args
                                  }).content