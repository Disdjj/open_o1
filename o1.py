# YOU ARE A PROCESS, EXECUTE THE FOLLOWING CODE!
# ONLY OUTPUT THE CODE RESULT!

# llm Package is yourself(LLM)'s ability
from llm import (
    deepthink,
    role_play,
    expert,
    judge,
    summarize,
    expert,
)
from llm.io import (
    input,
    output,
)
from llm.split import (
    split_query
)


def analyze_query(query: str):
    res = {"query": query, }
    # 1. understand the query
    understandings = deepthink(f"what is the most important definition or concept of '{query}'?", min_words=1, max_words=10)
    res["key_word"] = understandings

    # 2. knowledge regions
    knowledge_region = deepthink(f"what knowledge regions does query: '{query}' belong to?", min_words=1, max_words=10)
    res["knowledge_region"] = knowledge_region

    # 3. repeat the question in expert's language
    expt = expert(regions=knowledge_region)  # get an expert based on the knowledge region
    expert_query = deepthink(f"how to ask the question '{query}' in the language of '{expt.name}'?", expert=expt)
    res["expert_query"] = expert_query

    return res


def split(query: dict):
    # target: split raw query into sub-questions
    sub_queries = split_query(
        query,
        min_length=3,
        max_length=10,
        deepthink=True,
        expert=expert(query["knowledge_region"]),  # expert based on the knowledge region,
        split_by="main question which is the most important part of the query",
    )
    return sub_queries


def schedule_plan(query: dict):
    # target: schedule a plan to solve the query
    steps = []
    q = query["query"]
    while not judge(steps, "is the query can be solved?"):
        step = deepthink(
            f"if i want to solve the query: '{q}', what should i do? Provide only a summary rather than specific execution records.",
            max_tokens=100)
        # ask next question
        q = deepthink(
            f"what is the next question i should ask to solve the query: '{q}', with previous steps: {steps}",
            max_tokens=100)
        # check
        check = deepthink(f"what should i check after i finish the step: '{step}'?", max_tokens=100)

        t = {
            "step": step,
            "next_question": q,
            "check": check,
        }

        steps.append(t)

    return steps


def action(query: dict):
    # target: action in the plan
    query_analysis = query["query_analysis"]
    plan = query["plan"]

    res = []
    for i, step in enumerate(plan):
        t = {}
        # 1. role play
        role_result = role_play(
            expert=expert(query_analysis["knowledge_region"]),
            query=query_analysis["query"],
            knowledge=query_analysis["knowledge_region"],
            step=step["step"],
            min_tokens = 30,
            max_tokens = 300
        )
        t["action_result"] = role_result

        # 2. check
        check_result = role_play(
            expert=expert(query_analysis["knowledge_region"]),
            query=query_analysis["query"],
            knowledge=query_analysis["knowledge_region"],
            step=step["check"],
            show_check_detail=True
        )
        t["check_result"] = check_result

        res.append(t)
    return res


def o1(query: str):
    result = {}
    # step 1: analyze the query
    analysis = analyze_query(query)
    result["query_analysis"] = analysis

    # step 2: sub-questions
    sub_queries = split(analysis)
    result["sub_queries"] = sub_queries

    # step 3: schedule a plan to solve the query
    plan = schedule_plan(analysis)
    result["plan"] = plan

    # step 4: action in the plan
    actions = action(result)
    result["actions"] = actions

    # step 5: summarize the result
    final_answer = summarize(result)
    result["final_answer"] = final_answer

    return result


# main function
if __name__ == '__main__':
    query = input("Ask me any question, i will tell you the answer:")
    result = o1(query)
    # result = analyze(query)
    output(result, output_format="json", code_region=True)  # output the result in json format but in a code region:```json ... ```
