class Printer:
    def print(self, content: str, color: str):
        if color == "yellow":
            self._print_yellow(content)
        elif color == "red":
            self._print_red(content)
        else:
            print(content)

    def _print_yellow(self, content):
        print(f"\033[93m {content}\033[00m")

    def _print_red(self, content):
        print(f"\033[91m {content}\033[00m")
