import curses

def print_menu(stdscr, selected_row_idx, menu):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    
    stdscr.refresh()

def menu_selector(stdscr, menu):
    # Turn off cursor blinking
    curses.curs_set(0)
    
    # Color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    # Initial selected row
    current_row = 0
    
    # Print the menu
    print_menu(stdscr, current_row, menu)
    
    while True:
        key = stdscr.getch()
        
        # Navigate up
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        # Navigate down
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        # Enter key to select an option
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return menu[current_row]
        
        print_menu(stdscr, current_row, menu)

def main_menu(menu_options):
    # Wrapper for the curses interface
    selected_option = curses.wrapper(menu_selector, menu_options)
    print(f"You selected: {selected_option}")
    return selected_option

if __name__ == "__main__":
    # You can pass any array to the main_menu function
    options = ["Option 1", "Option 2", "Option 3", "Option 4", "Exit"]
    
    main_menu(options)
