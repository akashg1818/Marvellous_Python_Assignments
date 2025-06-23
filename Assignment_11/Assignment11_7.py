def Display(col):
    if col == 0:
        return
    print("*", end="  ")
    Display(col - 1)

def pattern(row,max_row):
    if row > max_row:
        return
    Display(row)
    print()  # Move to next line
    pattern(row + 1, max_row)

def main():

    pattern(1,4)

if __name__ == "__main__":
    main()