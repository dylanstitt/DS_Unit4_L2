# Dylan Stitt
# Unit 4 Lab 2
# Simple Reverse

from Stack import ArrayStack

def main():
    original = "Sphinx of black quartz, judge my vow"
    new = ""

    stack = ArrayStack()
    for i in original:
        stack.push(i)

    for i in range(len(stack)):
        new += stack.pop()

    print(f'Original: {original}')
    print(f'New: {new}')


if __name__ == '__main__':
    main()
