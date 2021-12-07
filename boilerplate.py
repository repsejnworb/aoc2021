import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("--part2", action="store_true")
    args = parser.parse_args()

if __name__ == "__main__":
    main()
