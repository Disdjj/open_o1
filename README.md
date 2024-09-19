# open_o1

An open-source implementation of OpenAI o1, base on prompt, inspired by [Code-Prompt](https://github.com/Disdjj/prompt_in_code)

## usage

o1.py can be a prompt of any LLM, use it and ask anyting

## principle

context-learning not only in chat, but also in output

## exampls

> base on LLM: deepseek-chat, top_p = 1, temperature=0.7
> deepseek-chat is best LLM !!!

### Two Sum

> Input: how to solve `Two Sum` problem?

```json
{
  "query_analysis": {
    "query": "how to solve `Two Sum` problem?",
    "key_word": "Two Sum problem",
    "knowledge_region": "algorithms, data structures",
    "expert_query": "How to efficiently solve the Two Sum problem using data structures and algorithms?"
  },
  "sub_queries": [
    "What is the Two Sum problem?",
    "What are the common approaches to solve the Two Sum problem?",
    "How to implement the Two Sum solution using a hash table?"
  ],
  "plan": [
    {
      "step": "Understand the definition and requirements of the Two Sum problem.",
      "next_question": "What are the common approaches to solve the Two Sum problem?",
      "check": "Verify that the problem definition is clear and understood."
    },
    {
      "step": "Explore common approaches such as brute force, two-pass hash table, and one-pass hash table.",
      "next_question": "How to implement the Two Sum solution using a hash table?",
      "check": "Ensure that the common approaches are understood and can be implemented."
    },
    {
      "step": "Implement the Two Sum solution using a hash table for optimal time complexity.",
      "next_question": "None",
      "check": "Verify that the implementation correctly solves the Two Sum problem."
    }
  ],
  "actions": [
    {
      "action_result": "The Two Sum problem involves finding two numbers in an array that add up to a given target. For example, given an array [2, 7, 11, 15] and a target of 9, the solution should return [0, 1] because 2 + 7 = 9.",
      "check_result": "The problem definition is clear and understood."
    },
    {
      "action_result": "Common approaches to solve the Two Sum problem include: 1) Brute force: Check all possible pairs in the array. 2) Two-pass hash table: Store the array in a hash table and check for the complement in a second pass. 3) One-pass hash table: Store elements in a hash table while checking for the complement.",
      "check_result": "The common approaches are understood and can be implemented."
    },
    {
      "action_result": "To implement the Two Sum solution using a hash table, iterate through the array and for each element, check if the complement (target - element) exists in the hash table. If it does, return the indices. If not, add the element to the hash table.",
      "check_result": "The implementation correctly solves the Two Sum problem."
    }
  ],
  "final_answer": "To solve the Two Sum problem, first understand its definition: find two numbers in an array that add up to a given target. Common approaches include brute force, two-pass hash table, and one-pass hash table. The optimal solution is to use a one-pass hash table, where you store elements and check for their complements in a single pass, ensuring O(n) time complexity."
}
```
