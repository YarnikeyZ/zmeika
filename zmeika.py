from time import sleep as sl
from sys import argv

def create_lines(prb_len, segments, symbols, moving, color_codes):
    def coloring(text, tcolor, bcolor):
        return f"\033[38;5;{tcolor}m\033[48;5;{bcolor}m{text}\033[0;0m"
    
    forward = []
    backward = []

    for n in range(0, moving):
        ##Creating a base line like: "\\  \\  \\", etc.
        prb = "".ljust(prb_len, " ")
        line = ""
        for s in range(0, segments-1):
            line += f"{symbols}{prb}"
        line += symbols

        ##Creating spaces within the end and start of full line
        prbls = ("".ljust(n, " "), "".ljust(moving-n, " "))

        ##Creating full, colored lines from start spaces, base line and end spaces
        forward.append(coloring(f"{prbls[0]}{line}{prbls[1]}", color_codes[0], color_codes[1]))
        backward.append(coloring(f"{prbls[1]}{line}{prbls[0]}", color_codes[0], color_codes[1]))

    return (forward, backward)

def main(prb_len, segments, symbols, moving, wait, color_codes):
    ##Creating lines once to the end
    lines = create_lines(prb_len, segments, symbols, moving, color_codes)
    
    ##Printing them for user in endless loop
    while True:
        for f in lines[0]:
            print(f)
            sl(wait)
        for b in lines[1]:
            print(b)
            sl(wait)

if __name__ == "__main__":
    try:
        try:
            ##Argv handling
            main(
                int(argv[1]),
                int(argv[2]),
                argv[3],
                int(argv[4]),
                float(argv[5]),
                (int(argv[6]),
                int(argv[7]))
            )
        except IndexError:
            ##No argv handling
            main(
                int(input("Number of spaces between chars: ")),
                int(input("Number of char lines: ")),
                input("Symbols of line: "),
                int(input("Moving: ")),
                float(input("Wait time for another line: ")),
                (int(input("Color code for text: ")),
                int(input("Color code for text background: ")))
            )
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit()
