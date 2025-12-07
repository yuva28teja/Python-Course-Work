

def count_messages(messages):
    return len(messages)

def unique_users(messages):
    users = {msg.split(":")[0].strip() for msg in messages}
    return users

def total_words(messages):
    return sum(len(msg.split(":")[1].split()) for msg in messages)

def average_words_per_message(messages):
    total = total_words(messages)
    return total / len(messages)

def longest_message(messages):
    return max(messages, key=lambda x: len(x))

def most_active_user(messages):
    count = {}
    for msg in messages:
        user = msg.split(":")[0]
        count[user] = count.get(user, 0) + 1
    user = max(count, key=count.get)
    return user, count[user]

def message_count_of_user(messages, user):
    return sum(1 for msg in messages if msg.startswith(user + ":"))

def most_frequent_word_by_user(messages, user):
    words = []
    for msg in messages:
        if msg.startswith(user + ":"):
            part = msg.split(":", 1)[1].lower()
            words.extend(part.split())

    if not words:
        return None
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return max(freq, key=freq.get)

def first_and_last_message(messages, user):
    user_msgs = [msg for msg in messages if msg.startswith(user + ":")]
    if not user_msgs:
        return None, None
    return user_msgs[0], user_msgs[-1]

def check_user_present(messages, user):
    users = unique_users(messages)
    return user in users

def commonly_repeated_words(messages):
    word_count = {}
    for msg in messages:
        content = msg.split(":", 1)[1].lower()
        for w in content.split():
            word_count[w] = word_count.get(w, 0) + 1
    return {w for w, c in word_count.items() if c > 1}

def user_with_longest_avg_message(messages):
    user_lengths = {}
    user_counts = {}

    for msg in messages:
        user, text = msg.split(":", 1)
        word_count = len(text.split())

        user_lengths[user] = user_lengths.get(user, 0) + word_count
        user_counts[user] = user_counts.get(user, 0) + 1

    avg_lengths = {u: user_lengths[u] / user_counts[u] for u in user_lengths}
    user = max(avg_lengths, key=avg_lengths.get)
    return user, avg_lengths[user]

def messages_mentioning_user(messages, user):
    return sum(1 for msg in messages if user.lower() in msg.lower())

def remove_duplicate_messages(messages):
    unique_msgs = list(dict.fromkeys(messages))
    return unique_msgs

def sort_messages(messages):
    return sorted(messages)

def extract_questions(messages):
    return [msg for msg in messages if "?" in msg]

def reply_ratio(messages, user1, user2):
    
    replies = 0
    for i in range(len(messages) - 1):
        if messages[i].startswith(user1 + ":") and messages[i+1].startswith(user2 + ":"):
            replies += 1
    return replies

def check_deleted_messages(messages):
    return sum(1 for msg in messages if "This message was deleted" in msg)



# --------------------------------------------

messages = []
n = int(input("Enter the number of messages: "))

print("Enter messages in the format -> Name: message")
for _ in range(n):
    messages.append(input())

while True:
    print("\nChoose an option:")
    print("""
1. Count total number of messages
2. Identify unique users
3. Count total words
4. Average words per message
5. Longest message
6. Most active user
7. Message count of a user
8. Most frequent word by a user
9. First and last message of a user
10. Check if a user is present
11. Common repeated words
12. (Skipped intentionally)
13. User with longest average message
14. Count messages mentioning a user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions
18. Reply ratio between two users
19. Check deleted messages
0. Exit
""")

    option = int(input("Enter option: "))

    if option == 0:
        print("Exiting...")
        break

    elif option == 1:
        print("Total messages:", count_messages(messages))

    elif option == 2:
        print("Unique users:", unique_users(messages))

    elif option == 3:
        print("Total words:", total_words(messages))

    elif option == 4:
        print("Average words per message:", round(average_words_per_message(messages), 2))

    elif option == 5:
        print("Longest message:", longest_message(messages))

    elif option == 6:
        user, count = most_active_user(messages)
        print(f"Most active user: {user} ({count} messages)")

    elif option == 7:
        user = input("Enter user: ")
        print(f"Messages sent by {user}:", message_count_of_user(messages, user))

    elif option == 8:
        user = input("Enter user: ")
        print("Most frequent word:", most_frequent_word_by_user(messages, user))

    elif option == 9:
        user = input("Enter user: ")
        first, last = first_and_last_message(messages, user)
        if first:
            print("First:", first)
            print("Last:", last)
        else:
            print("User not found.")

    elif option == 10:
        user = input("Enter user: ")
        if check_user_present(messages, user):
            print(f"User '{user}' is present")
        else:
            print(f"User '{user}' not found in the chat.")

    elif option == 11:
        print("Common repeated words:", commonly_repeated_words(messages))

    elif option == 13:
        user, avg = user_with_longest_avg_message(messages)
        print(f"User with longest avg message: {user} ({round(avg,2)} words)")

    elif option == 14:
        user = input("Enter user to search: ")
        print(f"Messages mentioning '{user}':", messages_mentioning_user(messages, user))

    elif option == 15:
        unique_msgs = remove_duplicate_messages(messages)
        print("Unique messages count:", len(unique_msgs))
        for m in unique_msgs:
            print(m)

    elif option == 16:
        for msg in sort_messages(messages):
            print(msg)

    elif option == 17:
        for q in extract_questions(messages):
            print(q)

    elif option == 18:
        user1 = input("Enter first user: ")
        user2 = input("Enter second user: ")
        print(f"Reply ratio from {user2} to {user1}:", reply_ratio(messages, user1, user2), "replies")

    elif option == 19:
        print("Deleted messages found:", check_deleted_messages(messages))

    else:
        print("Invalid option. Try again.")
