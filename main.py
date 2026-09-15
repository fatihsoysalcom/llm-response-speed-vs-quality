import time

def generate_response_fast(prompt):
    """Simulates a fast but potentially lower-quality LLM response."""
    print(f"\n[FAST MODEL] Processing prompt: '{prompt[:30]}...'\n")
    time.sleep(0.5)  # Simulate quick processing
    return "This is a quick, possibly less detailed, answer."

def generate_response_quality(prompt):
    """Simulates a slower but higher-quality LLM response."""
    print(f"\n[QUALITY MODEL] Processing prompt: '{prompt[:30]}...'\n")
    time.sleep(2.0)  # Simulate more thorough processing
    return "This is a more comprehensive and thoughtful response, considering multiple aspects of the query."

def main():
    prompt = "What are the main arguments for and against slowing down AI development?"

    print("--- Demonstrating AI Speed vs. Quality Trade-off ---")

    # Simulate a 'fast' AI response
    start_time_fast = time.time()
    response_fast = generate_response_fast(prompt)
    end_time_fast = time.time()
    print(f"Fast Model Response: {response_fast}")
    print(f"Fast Model Time: {end_time_fast - start_time_fast:.2f} seconds")

    # Simulate a 'quality' AI response
    start_time_quality = time.time()
    response_quality = generate_response_quality(prompt)
    end_time_quality = time.time()
    print(f"Quality Model Response: {response_quality}")
    print(f"Quality Model Time: {end_time_quality - start_time_quality:.2f} seconds")

    print("\n--- Conclusion ---")
    print("This simulation illustrates the trade-off between AI response speed and the depth/quality of the response.")
    print("A faster AI might be preferred for quick queries, while a slower, more deliberative AI might be needed for complex tasks or when safety/accuracy is paramount.")

if __name__ == "__main__":
    main()
