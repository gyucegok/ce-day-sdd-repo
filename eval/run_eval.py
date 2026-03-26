# run_eval.py - Run evaluation questions against the Agent

import os
import re

# We can import the agent once it's created, but for now we define the skeleton
# to read questions and output answers.

def load_evaluation_questions(filepath):
    """
    Reads RAG_EVALUATION_QUESTIONS.md and extracts the questions.
    Assuming questions are numbered or have a specific format.
    """
    if not os.path.exists(filepath):
        print(f"Questions file not found: {filepath}")
        return []

    with open(filepath, 'r') as f:
        content = f.read()

    # Extract questions (assuming format like "Question 1: ...")
    # Let's read the file to see exact format if we can, but let's assume standard pattern.
    # We will use a regex to find questions.
    questions = []
    
    # Generic regex to find numbered questions or bullet points
    pattern = r'(?:Question|Q)\s*\d+[:\.]\s*(.*)'
    matches = re.finditer(pattern, content, re.MULTILINE)
    
    for match in matches:
        questions.append(match.group(1).strip())
        
    return questions

def run_evaluation():
    # Let's check where the file is. Spec says it should be in data/RAG_EVALUATION_QUESTIONS.md for now
    # or moved to eval/. We'll check if it's in eval/ first.
    eval_file = os.path.join("eval", "RAG_EVALUATION_QUESTIONS.md")
    if not os.path.exists(eval_file):
        eval_file = os.path.join("data", "RAG_EVALUATION_QUESTIONS.md")

    questions = load_evaluation_questions(eval_file)
    if not questions:
        print("No questions found or failed to load questions.")
        return

    print(f"Loaded {len(questions)} evaluation questions.")
    
    # Define Agent caller (placeholder for now)
    def call_agent(query):
        # We will import agent_main and call it
        # For now, return mock
        return f"Mock answer for: {query}"

    print("\n--- Starting Evaluation ---\n")
    results = []
    for i, question in enumerate(questions):
        print(f"Processing Question {i+1}: {question}")
        answer = call_agent(question)
        print(f"Answer: {answer}\n")
        results.append({
            "id": i+1,
            "question": question,
            "answer": answer
        })

    # Save results
    output_file = "eval_results.json"
    import json
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    run_evaluation()
