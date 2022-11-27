from time import sleep as sl
from sys import argv

def main(prb_len: int, segments: int, symbols: str, moving: int, wait: float, color_codes):
    ##Creating lines once to the end
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
        forward.append(f"\033[38;5;{color_codes[0]}m\033[48;5;{color_codes[1]}m{prbls[0]}{line}{prbls[1]}\033[0;0m")
        backward.append(f"\033[38;5;{color_codes[0]}m\033[48;5;{color_codes[1]}m{prbls[1]}{line}{prbls[0]}\033[0;0m")
    
    while True:
        for f in forward:
            print(f)
            sl(wait)
        for b in backward:
            print(b)
            sl(wait)

if __name__ == "__main__":
    try:
        try:
            main(
                int(argv[1]),   # prb_len
                int(argv[2]),   # segments
                argv[3],        # symbols
                int(argv[4]),   # moving
                float(argv[5]), # wait
                (int(argv[6]),  # color_code text
                int(argv[7]))   # color_code text background
            )
        except IndexError:
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
