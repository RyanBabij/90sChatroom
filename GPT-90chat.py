import random
import time
import textwrap
import keyboard  # Import keyboard module
import os  # For accessing environment variables
from openai import OpenAI
from config import AI_PERSONALITIES, AI_COLORS, TERMINAL_WIDTH, DELAY_MIN, DELAY_MAX, JOIN_LEAVE_PROBABILITY, RESET

# Load the API keys from environment variables
API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with your API key
client = OpenAI(
	api_key=API_KEY
)

chatlog = ""

# Function to wrap text to fit terminal width
def wrap_text(text, width):
	"""Wrap the text to fit within the terminal width while keeping existing newlines."""
	lines = text.splitlines()
	wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
	return "\n".join(wrapped_lines)

def get_ai_response(ai_name, ai_traits, context):
	global chatlog  # Declare chatlog as global so we can modify it
	
	# Add the AI message to the conversation
	conversation = [
		{"role": "system", "content": f"You are {ai_name}, {ai_traits}. Respond to the chat as yourself."},
		{"role": "user", "content": f"Chatlog so far:\n\n{chatlog}\n\nPost a single response as {ai_name}. Post only your message, don't output your username. Do not make messages overly long unless it's necessary. Spelling, capitalization and grammar should reflect a normal chatroom environment. Don't be too formal. Political incorrectness is allowed. The chatroom is about a group of people playing Majora's Mask"}
	]
	
	# Make the API call for a response
	completion = client.chat.completions.create(
		model="gpt-4o-mini",  # Use the correct model
		store=True,
		messages=conversation
	)

	ai_message = completion.choices[0].message.content  # Access content directly
	
	if ai_message:
		chatlog += f"{ai_name}: {ai_message}\n"
		# Wrap the message to fit terminal width
		wrapped_ai_message = wrap_text(ai_message, TERMINAL_WIDTH)
		ai_color = AI_COLORS.get(ai_name, RESET)  # Get the color or reset if not found
		return f"{ai_color}{ai_name}:{RESET} {wrapped_ai_message}"
	print("ERROR")
	return get_ai_response(ai_name, ai_traits, context)


def manage_users(active_users, idle_users):
	if random.randint(1, 100) <= JOIN_LEAVE_PROBABILITY:  # Probability of user joining/leaving
		if active_users and idle_users:
			# 50% chance to either have someone leave or join
			if random.choice([True, False]):
				# A user leaves the chat
				user_leaving = random.choice(active_users)
				active_users.remove(user_leaving)
				idle_users.append(user_leaving)
				print(f"\n{AI_COLORS[user_leaving['name']]}{user_leaving['name']}{RESET} has left the chat.\n")
			else:
				# A user joins the chat
				user_joining = random.choice(idle_users)
				idle_users.remove(user_joining)
				active_users.append(user_joining)
				print(f"\n{AI_COLORS[user_joining['name']]}{user_joining['name']}{RESET} has joined the chat.\n")
	return active_users, idle_users



def chatroom_simulation():
	global chatlog  # Declare chatlog as global so we can modify it
	
	# Split initial active and idle users
	random.shuffle(AI_PERSONALITIES)
	active_users = AI_PERSONALITIES[:4]
	idle_users = AI_PERSONALITIES[6:]
	
	# Ask for the user's username at the start
	username = input("Enter your username: ")
	
	print(f"Welcome, {username}! Starting the chatroom simulation...\n")
	
	last_message_time = time.time()  # Track when the last message was printed
	delay = random.randint(DELAY_MIN, DELAY_MAX)  # Initial random delay
	last_ai_name = None  # Track the last AI that responded
	
	while True:
		# Check if the space bar is pressed
		if keyboard.is_pressed('space'):
			# Pause the chat and let the user type their own message
			user_message = input(f"{username}: ")
			chatlog += f"{username}: {user_message}\n"
			print("")
			
			# Reset the timer after user input
			last_message_time = time.time()

		# Check if enough time has passed for an AI to respond
		elif time.time() - last_message_time > delay:
			# Select an AI who didn't speak last time
			available_users = [ai for ai in active_users if ai["name"] != last_ai_name]
			if not available_users:
				available_users = active_users  # Fallback if all users are filtered out
			
			ai = random.choice(available_users)
			ai_name = ai["name"]
			ai_traits = ai["traits"]
			
			ai_message = get_ai_response(ai_name, ai_traits, "context")
			print(ai_message + "\n")
			
			# Update the last AI that responded
			last_ai_name = ai_name
			
			# Check if a user joins or leaves
			active_users, idle_users = manage_users(active_users, idle_users)
			
			last_message_time = time.time()  # Track when the last message was printed
			delay = random.randint(DELAY_MIN, DELAY_MAX)  # Generate a new random delay for the next response


# Start the chatroom simulation
chatroom_simulation()
