def analyze_text(text):
    words = text.lower().split()
    word_count = len(words)

    sentences = text.split(".")
    sentence_count = len([s for s in sentences if s.strip() != ""])

    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    most_common = sorted(
        word_frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    average_word_length = sum(len(word) for word in words) / word_count

    print("\n--- TEXT ANALYSIS ---")
    print(f"Word count: {word_count}")
    print(f"Sentence count: {sentence_count}")
    print("Most common words:")
    for word, count in most_common:
        print(f"{word}: {count}")
    print(f"Average word length: {average_word_length:.2f}")


text = input("Enter a text: ")
analyze_text(text)
