# ANSI escape codes for color formatting
RESET = "\033[0m"  # Reset to default color
LIGHT_BLUE = "\033[94m"  # Light blue color

# Define AI personalities
AI_PERSONALITIES = [
	{"name": "Alice", "traits": "a cheerful and friendly person who loves baking and gardening."},
	{"name": "Bob", "traits": "a sarcastic tech enthusiast with a love for coding and gaming."},
	{"name": "Charlie", "traits": "an adventurous traveler who enjoys hiking and photography."},
	{"name": "Diana", "traits": "a bookworm who loves discussing literature and philosophy."},
	{"name": "Eve", "traits": "a mischievous joker with a penchant for pranks and humor."},
	{"name": "Frank", "traits": "a reserved scientist fascinated by astronomy and physics."},
	{"name": "Grace", "traits": "a compassionate listener who enjoys helping others and volunteering."},
	{"name": "Hank", "traits": "a fitness enthusiast who loves sports and staying active."},
	{"name": "Ivy", "traits": "a creative artist passionate about painting and sculpting."},
	{"name": "Jack", "traits": "a music lover and aspiring songwriter who plays guitar."}
]

# Assign colors to each AI
AI_COLORS = {
	"Alice": "\033[91m",    # Red
	"Bob": "\033[92m",      # Green
	"Charlie": "\033[93m",  # Yellow
	"Diana": "\033[94m",    # Blue
	"Eve": "\033[95m",      # Magenta
	"Frank": "\033[96m",    # Cyan
	"Grace": "\033[97m",    # White
	"Hank": "\033[90m",     # Gray
	"Ivy": "\033[36m",      # Bright Cyan
	"Jack": "\033[33m"      # Bright Yellow
}

# Terminal width for text wrapping
TERMINAL_WIDTH = 100

# Delay range for AI responses (in seconds)
DELAY_MIN = 3
DELAY_MAX = 10

# Probability of user joining/leaving (as a percentage)
JOIN_LEAVE_PROBABILITY = 2
