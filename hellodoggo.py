# --- Initial database setup ---
# Use plain data structures in this script for simplicity.
# In a real system you could persist to files or DB.
trigger_responses = {
    "mailman": "bark bark",
    "doorbell": "bark bark",
    "knock knock": "bark bark",
    "throw ball": "chase",
    "treat": "I'm sitting!",
    "good dog": "wag wag",
    "car": "wag wag",
    "walk": "wag wag",
    "sit": "Give me a treat!",
    "speak": "bark bark",
    
}

unknown_triggers = set()  # stores unknown phrases from this session

CASE_INSENSITIVE = True  # Set to True to ignore case in matching


def normalize_input(user_input: str) -> str:
    """Trim and optionally lowercase input for matching."""
    text = user_input.strip()
    if CASE_INSENSITIVE:
        text = text.lower()
    return text


def get_response(normalized: str) -> str | None:
    """Return known response or None if no trigger exists."""
    if normalized in trigger_responses:
        return trigger_responses[normalized]
    return None


def handle_input(raw_input: str) -> None:
    """Process user input and either respond or capture as unknown."""
    normalized = normalize_input(raw_input)
    if normalized == "":
        print("Please say something to play.")
        return

    response = get_response(normalized)
    if response is not None:
        print(response)
        return

    # Unknown trigger flow
    if normalized not in unknown_triggers:
        unknown_triggers.add(normalized)
        print("I don't know that yet, but I learned a new sound!")
    else:
        print("Still learning this one, keep trying!")


def main() -> None:
    print("Play with my dog!")
    print("Type 'quit' or 'exit' to stop.")

    while True:
        user_input = input("You: ")
        normalized = normalize_input(user_input)

        if normalized in {"quit", "exit"}:
            break

        handle_input(user_input)

    print("Unknown triggers collected:", sorted(unknown_triggers))

print(unknown_triggers)  # For debugging: show collected unknown triggers at the end

if __name__ == "__main__":
    main()
