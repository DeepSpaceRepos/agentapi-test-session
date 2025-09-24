#!/usr/bin/env python3
import random
import time
import sys

def print_animated(text, delay=0.05):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def rainbow_text(text):
    """Print text with rainbow colors (ANSI escape codes)"""
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    reset = '\033[0m'
    
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(f"{color}{char}{reset}", end='', flush=True)
    print()

def magic_8_ball():
    """Ask the magic 8-ball a question"""
    responses = [
        "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
        "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
        "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
        "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
        "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
        "Very doubtful"
    ]
    
    print_animated("\n🔮 Magic 8-Ball says: ", 0.1)
    time.sleep(1)
    print_animated("🎱 " + random.choice(responses), 0.05)

def number_guessing_game():
    """Play a number guessing game"""
    print_animated("\n🎯 Let's play a guessing game!", 0.05)
    print_animated("I'm thinking of a number between 1 and 100...", 0.05)
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print_animated(f"🎉 Congratulations! You guessed it in {attempts} attempts!", 0.05)
                break
            elif guess < secret_number:
                print_animated("📈 Too low! Try again.", 0.05)
            else:
                print_animated("📉 Too high! Try again.", 0.05)
                
        except ValueError:
            print_animated("❌ Please enter a valid number!", 0.05)

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def show_menu():
    """Display the interactive menu"""
    print("\n" + "="*50)
    rainbow_text("🌟 WELCOME TO THE COOL PYTHON PROGRAM! 🌟")
    print("="*50)
    print("\nChoose an option:")
    print("1. 🎨 Rainbow Hello World")
    print("2. 🔮 Ask the Magic 8-Ball")
    print("3. 🎯 Number Guessing Game")
    print("4. 🔢 Fibonacci Sequence Generator")
    print("5. 🎲 Random Fun Facts")
    print("6. 🚀 ASCII Art Display")
    print("7. ❌ Exit")
    print("\n" + "="*50)

def random_facts():
    """Display random fun facts"""
    facts = [
        "🐧 Penguins can jump as high as 6 feet in the air!",
        "🌙 The Moon is moving away from Earth at about 1.5 inches per year.",
        "🦑 Octopuses have three hearts and blue blood!",
        "🍯 Honey never spoils - archaeologists have found edible honey in ancient Egyptian tombs!",
        "🐝 A group of flamingos is called a 'flamboyance'!",
        "🌊 The Pacific Ocean is larger than all land masses combined!",
        "🦎 Some lizards can regrow their tails up to 8 times!",
        "☁️ A cloud can weigh more than a million pounds!"
    ]
    
    print_animated("\n🎲 Random Fun Fact:", 0.05)
    time.sleep(0.5)
    print_animated(random.choice(facts), 0.03)

def ascii_art():
    """Display cool ASCII art"""
    art_options = [
        """
    ╔══════════════════════════════════╗
    ║        🐍 PYTHON POWER! 🐍        ║
    ║                                  ║
    ║    ╭─────────────────────────╮    ║
    ║    │  print("Hello World!")  │    ║
    ║    ╰─────────────────────────╯    ║
    ║                                  ║
    ║     Code is Poetry! 🎨✨         ║
    ╚══════════════════════════════════╝
        """,
        """
    🌟 ═══════════════════════════════ 🌟
         🚀 WELCOME TO THE FUTURE! 🚀
    🌟 ═══════════════════════════════ 🌟
    
           💻 Coding is Magic! ✨
           🎯 Every bug is a feature!
           🎨 Creativity meets Logic!
        """,
        """
    ╔══════════════════════════════════════╗
    ║  🎮 INTERACTIVE PYTHON ADVENTURE! 🎮  ║
    ║                                      ║
    ║  🎯 Choose your adventure:           ║
    ║  🔮 Magic awaits around every corner ║
    ║  🎨 Colors paint the digital world   ║
    ║  🚀 Code takes you to infinity!      ║
    ╚══════════════════════════════════════╝
        """
    ]
    
    print(random.choice(art_options))

def main():
    while True:
        show_menu()
        
        try:
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                print_animated("\n🎨 Creating rainbow magic...", 0.05)
                time.sleep(0.5)
                rainbow_text("Hello, Beautiful World! 🌈✨")
                
            elif choice == "2":
                question = input("\nAsk the Magic 8-Ball a question: ").strip()
                if question:
                    magic_8_ball()
                else:
                    print_animated("🔮 The Magic 8-Ball needs a question to answer!", 0.05)
                    
            elif choice == "3":
                number_guessing_game()
                
            elif choice == "4":
                try:
                    n = int(input("\nHow many Fibonacci numbers do you want? "))
                    if n > 0:
                        fib_sequence = fibonacci_sequence(n)
                        print_animated(f"\n🔢 First {n} Fibonacci numbers:", 0.05)
                        print_animated(" → ".join(map(str, fib_sequence)), 0.02)
                    else:
                        print_animated("❌ Please enter a positive number!", 0.05)
                except ValueError:
                    print_animated("❌ Please enter a valid number!", 0.05)
                    
            elif choice == "5":
                random_facts()
                
            elif choice == "6":
                ascii_art()
                
            elif choice == "7":
                print_animated("\n👋 Thanks for playing! See you next time! 🚀✨", 0.05)
                break
                
            else:
                print_animated("❌ Invalid choice! Please enter 1-7.", 0.05)
                
        except KeyboardInterrupt:
            print_animated("\n\n👋 Goodbye! Thanks for the fun! 🎉", 0.05)
            break
        except Exception as e:
            print_animated(f"❌ Oops! Something went wrong: {e}", 0.05)
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()