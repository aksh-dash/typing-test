import time
import random

# Predefined sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Typing speed is a good skill to have.",
    "Practice makes perfect when it comes to coding.",
    "A journey of a thousand miles begins with a single step.",
    "Code is like humor. When you have to explain it, it’s bad."
]

def calculate_wpm(start_time, end_time, typed_text):
    time_taken = end_time - start_time
    words = typed_text.split()
    wpm = (len(words) / time_taken) * 60
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct = 0

    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)

def main():
    print("\n===== Typing Speed Tester =====\n")
    input("Press Enter when you're ready to begin...")

    sentence = random.choice(sentences)
    print("\nType the following sentence as fast and accurately as you can:\n")
    print(f"> {sentence}")
    print()

    input("Press Enter to start typing...")
    start_time = time.time()
    typed_input = input("\nYour input: ")
    end_time = time.time()

    # Calculate results
    wpm = calculate_wpm(start_time, end_time, typed_input)
    accuracy = calculate_accuracy(sentence, typed_input)
    time_taken = round(end_time - start_time, 2)

    print("\n===== Results =====")
    print(f"Time taken      : {time_taken} seconds")
    print(f"Words per minute: {wpm}")
    print(f"Accuracy        : {accuracy}%")
    print("=====================\n")

if __name__ == "__main__":
    main()    
    