import random
import os
import time

# Clear screen
os.system("clear" if os.name == "posix" else "cls")

# SAQI Logo
print("""
\033[1;93m★彡[𝐒𝐀𝐐𝐈 - ساقی]彡★
\033[1;96m     🎯 Creator of Chaos | Coder of Shadows 🎯
""")


# Border line function
def linex():
    print('\033[1;37m═\033[1;32m═\033[1;37m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═' * 2)

# Function to generate Israeli number
def generate_israeli_number():
    operator_codes = ['2', '3', '4', '5', '8']
    operator = random.choice(operator_codes)
    number = ''.join(random.choices('0123456789', k=7))
    return f"+9725{operator}{number}"

# Input how many numbers to generate
try:
    linex()
    count = int(input("\033[1;96mHOW MANY NUMBERS TO GENERATE ➤ \033[1;92m"))
except:
    print("\033[1;91mInvalid input. Exiting.")
    exit()

print("\n\033[1;95mGenerating Israeli Numbers...\n")
time.sleep(1)

# Generate and print
for i in range(count):
    color = random.choice(['\033[1;92m', '\033[1;96m', '\033[1;93m', '\033[1;95m'])
    print(f"{color}[{i+1:02}] ➤ {generate_israeli_number()}\033[0m")
    time.sleep(0.1)

linex()
print(f"\033[1;92m✓ Done! {count} numbers generated successfully.\033[0m")
linex()

