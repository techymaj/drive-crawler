from colorama import just_fix_windows_console

# Expanded ANSI escape sequences for colors and effects
# Standard foreground colors
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'

# Bright foreground colors (bold variants)
BRIGHT_BLACK = '\u001b[30;1m'
BRIGHT_RED = '\u001b[31;1m'
BRIGHT_GREEN = '\u001b[32;1m'
BRIGHT_YELLOW = '\u001b[33;1m'
BRIGHT_BLUE = '\u001b[34;1m'
BRIGHT_MAGENTA = '\u001b[35;1m'
BRIGHT_CYAN = '\u001b[36;1m'
BRIGHT_WHITE = '\u001b[37;1m'

# Background colors
BG_BLACK = '\u001b[40m'
BG_RED = '\u001b[41m'
BG_GREEN = '\u001b[42m'
BG_YELLOW = '\u001b[43m'
BG_BLUE = '\u001b[44m'
BG_MAGENTA = '\u001b[45m'
BG_CYAN = '\u001b[46m'
BG_WHITE = '\u001b[47m'

# Bright background colors
BG_BRIGHT_BLACK = '\u001b[40;1m'
BG_BRIGHT_RED = '\u001b[41;1m'
BG_BRIGHT_GREEN = '\u001b[42;1m'
BG_BRIGHT_YELLOW = '\u001b[43;1m'
BG_BRIGHT_BLUE = '\u001b[44;1m'
BG_BRIGHT_MAGENTA = '\u001b[45;1m'
BG_BRIGHT_CYAN = '\u001b[46;1m'
BG_BRIGHT_WHITE = '\u001b[47;1m'

# Text effects
RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'
DIM = '\u001b[2m'
ITALIC = '\u001b[3m'
BLINK = '\u001b[5m'
HIDDEN = '\u001b[8m'

# Example usage
# if __name__ == "__main__":
#     print(f"{BOLD}{RED}This is bold red text{RESET}")
#     print(f"{BG_BLUE}{BLACK}This is black text on a blue background{RESET}")
#     print(f"{BRIGHT_YELLOW}{UNDERLINE}Bright yellow underlined text{RESET}")



just_fix_windows_console()

def print_ic(text, *effects: "A list of styles", reset: str = RESET) -> None:
    """
    Prints a given text in the color specified by `effect`.

    :param effects: A list of the various styles to apply. e.g
        `BLUE, BOLD, UNDERLINE`
    :param text: The text to apply the color to.
    :param reset: Resets the effect to the terminal default.
    """
    combined_effects = ''.join(effects)
    print(f"{combined_effects}", f"{text}", f"{reset}")
