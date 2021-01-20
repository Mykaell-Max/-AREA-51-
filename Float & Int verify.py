# int verify
def lint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERROR! Insert a valid int!')
            continue
        except KeyboardInterrupt:
            print('Value not informed.')
            return 0
        else:
            return n


# float verify
def loat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERROR! Insert a valid float!')
            continue
        except KeyboardInterrupt:
            print('Value not informed.')
            return 0
        else:
            return n
