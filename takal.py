"""ALGORITHM FOR DEVELOPING THE GAME"""


"""1. Initialize game parameters (player balance, bet amount)

2. Display possible betting options (HH, HT, TH, TT)

3. Accept player's bet choice and amount

4. Validate bet amount (must be positive and ≤ player balance)

5. Simulate two independent coin tosses using random number generation

6. Determine the outcome combination

7. Compare outcome with player's bet

8. Adjust player balance based on result

9. Display results and new balance

10. Ask if player wants to play again"""


import random

def coin_toss_game():
    # Initialize player balance
    balance = 100  # Starting balance
    
    while True:
        print(f"\nCurrent balance: ${balance}")
        if balance <= 0:
            print("You're out of money! Game over.")
            break
            
        # Display betting options
        print("\nBet on:")
        print("1. HH (Both Heads)")
        print("2. HT (Heads then Tails)")
        print("3. TH (Tails then Heads)")
        print("4. TT (Both Tails)")
        
        # Get player's bet choice
        while True:
            try:
                choice = int(input("Enter your bet choice (1-4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Get bet amount
        while True:
            try:
                bet = float(input(f"Enter bet amount (max ${balance}): "))
                if 0 < bet <= balance:
                    break
                else:
                    print(f"Bet must be between $0 and ${balance}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Simulate coin tosses
        coin1 = random.choice(['H', 'T'])
        coin2 = random.choice(['H', 'T'])
        outcome = coin1 + coin2
        
        # Determine result
        choices = {1: 'HH', 2: 'HT', 3: 'TH', 4: 'TT'}
        player_choice = choices[choice]
        
        print(f"\nCoin toss result: {coin1} and {coin2} -> {outcome}")
        print(f"You bet on: {player_choice}")
        
        # Calculate winnings
        if outcome == player_choice:
            winnings = bet * 3
            balance += winnings
            print(f"Congratulations! You won ${winnings}!")
        else:
            balance -= bet
            print(f"Sorry, you lost ${bet}. Better luck next time!")
        
        # Ask to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Game over. Final balance: ${balance}")
            break

# Start the game
coin_toss_game()