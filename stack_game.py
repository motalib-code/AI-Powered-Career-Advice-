import random
import sys

class StackGame:
    """
    A fun stack-based game where blocks are placed on top of each other.
    The goal is to stack blocks without them falling off the platform.
    """
    
    def __init__(self):
        self.stack = []
        self.score = 0
        self.level = 1
        self.game_over = False
        self.block_width = 10
        self.min_block_width = 3
    
    def add_block(self):
        """Add a new block to the stack"""
        if not self.stack:
            # First block
            block = {
                'position': 0,
                'width': self.block_width,
                'level': 1
            }
        else:
            # Calculate overlap with previous block
            prev_block = self.stack[-1]
            offset = random.randint(-2, 2)
            new_position = prev_block['position'] + offset
            
            # Calculate new block width based on overlap
            overlap = self.block_width - abs(offset)
            new_width = max(overlap, self.min_block_width)
            
            block = {
                'position': new_position,
                'width': new_width,
                'level': len(self.stack) + 1
            }
            
            # Check if block is completely off the platform
            if new_width <= 0 or new_position < -self.block_width:
                self.game_over = True
                return False
        
        self.stack.append(block)
        self.score += 10 * self.level
        self.level = len(self.stack) // 5 + 1
        return True
    
    def display_stack(self):
        """Display the current stack"""
        print("\n" + "="*40)
        print(f"Level: {self.level} | Score: {self.score}")
        print("="*40)
        
        if not self.stack:
            print("Stack is empty. Start adding blocks!")
            return
        
        for i, block in enumerate(self.stack[-5:]):  # Show last 5 blocks
            bar = "█" * block['width']
            padding = " " * max(0, block['position'])
            print(f"L{block['level']:2d}: {padding}{bar}")
        
        if len(self.stack) > 5:
            print(f"... ({len(self.stack) - 5} more blocks)")
    
    def undo_last_block(self):
        """Remove the last block from the stack"""
        if len(self.stack) > 1:
            self.stack.pop()
            self.score = max(0, self.score - 10)
            return True
        return False
    
    def get_stats(self):
        """Return game statistics"""
        return {
            'blocks_stacked': len(self.stack),
            'score': self.score,
            'level': self.level,
            'game_over': self.game_over
        }
    
    def reset_game(self):
        """Reset the game"""
        self.stack = []
        self.score = 0
        self.level = 1
        self.game_over = False


def play_game():
    """Main game loop"""
    game = StackGame()
    
    print("\n" + "#"*40)
    print("#" + " "*38 + "#")
    print("#" + "  WELCOME TO STACK GAME!".center(38) + "#")
    print("#" + " "*38 + "#")
    print("#"*40)
    print("\nCommands:")
    print("  'a' - Add a new block")
    print("  'u' - Undo last block")
    print("  's' - Show stats")
    print("  'r' - Reset game")
    print("  'q' - Quit game\n")
    
    while not game.game_over:
        command = input("Enter command: ").lower().strip()
        
        if command == 'a':
            if game.add_block():
                game.display_stack()
            else:
                print("\n❌ GAME OVER! Block fell off the stack!")
                print(f"Final Score: {game.score}")
                print(f"Blocks Stacked: {len(game.stack)}")
                break
        
        elif command == 'u':
            if game.undo_last_block():
                print("✓ Block removed!")
                game.display_stack()
            else:
                print("Cannot undo. At least one block required.")
        
        elif command == 's':
            stats = game.get_stats()
            print("\n" + "-"*40)
            print("GAME STATISTICS")
            print("-"*40)
            for key, value in stats.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            print("-"*40 + "\n")
        
        elif command == 'r':
            game.reset_game()
            print("\n🔄 Game reset!\n")
        
        elif command == 'q':
            print(f"\nThanks for playing! Final Score: {game.score}")
            break
        
        else:
            print("Invalid command. Try 'a', 'u', 's', 'r', or 'q'.")


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
