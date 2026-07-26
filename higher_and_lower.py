# Display art
from art import logo, data, vs
import random
print(logo)
score = 0
account_b = random.choice(data)

def format_data(account):
    """Format the account data into a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a{account_descr}, from {account_country}")

def check_answer(user_guess, a_follower, b_follower):
    """Take the user's guess and the follwer counts and return if they got it right."""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"
game_should_continue = True
# Generate a random account from the game data
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Format the account data into printable format

    # Ask user for a guess
    guess = input("Who has more followers ? Type A or B:").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # Check if user is correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Get follower count of each account
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong.Final score: {score}.")
        game_should_continue = False
# Use if statement to check if user is correct

# Give user feedback on their guess

# Score keeping

# Make the game repeatable.