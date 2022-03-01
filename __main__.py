import os
import argparse
from terminalsize import get_terminal_size
print('Loading dictionary...')
from bijective_map import uk_us, undo

UK = 'uk'
US = 'us'

def parseArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='"Translate" text from American to British English and back')
    parser.add_argument(
        '--to', type = str, 
        choices=[UK, US], required=True,
        help='select target language',
    )
    parser.add_argument(
        'input_filename', type=str, 
    )
    parser.add_argument(
        'output_filename', type=str, 
        nargs='?', default=None, 
    )
    args = parser.parse_args()
    if args.output_filename is None:
        base, ext = os.path.splitext(args.input_filename)
        args.output_filename = (
            base + '_' + args.to + ext
        )
    return args

def main():
    args = parseArgs()
    if os.path.isfile(args.output_filename):
        print(f'Ok to overwrite "{args.output_filename}"? y/n')
        if input('>').lower() != 'y':
            print('User aborted.')
            return
    print('Note: wide characters (e.g. Chinese) breaks character alignment.')
    print('Rules of undo:')
    for uk, us in undo:
        source, target = selectDirection(uk, us, args.to, reverse=True)
        print(' '*3, source, '\t->  ', target)
    print()
    print(    '|------------ × ------------|')
    if args.to == UK:
        print('| Beginning  Britishisation |')
    else:
        print('| Beginning Americanization |')
    print(    '|------------ × ------------|')
    print()
    with open(args.input_filename, 'r', encoding='utf-8') as inF:
        for line_no, line in enumerate(inF):
            undone = tryUndo(line)
            if undone != line:
                print(f'Error: undo rule can operate on original string. Line {line_no}: ')
                print(line)
                raise ValueError
    with open(args.input_filename, 'r', encoding='utf-8') as inF:
        with open(
            args.output_filename, 'w', newline='\n', 
            encoding='utf-8', 
        ) as outF:
            for line_no, line in enumerate(inF):
                for uk, us in uk_us:
                    for source, target in iterCapitalize(*selectDirection(
                        uk, us, args.to, 
                    )):
                        line = processLine(
                            line_no, line, source, target, 
                        )
                outF.write(line)
    print('Done.')

def selectDirection(uk, us, to, reverse = False):
    if (to == UK) ^ reverse:
        return us, uk
    else:
        return uk, us

def iterCapitalize(source, target):
    return (
        (source, target), 
        (source.capitalize(), target.capitalize()), 
    )

def tryUndo(line):
    for source, target in undo:
        for s, t in iterCapitalize(source, target):
            line = line.replace(s, t)
    return line

INDENT = 4
def processLine(line_no, line, source, target):
    try:
        start = line.index(source)
    except ValueError:
        return line
    replaced = line.replace(source, target, 1)
    undone = tryUndo(replaced)
    if undone != line:
        width = get_terminal_size()[0] - 1 - INDENT
        print('-' * width)
        print('line', line_no, ':')
        assert replaced == undone
        mid = width // 2
        offset = max(0, start - mid)
        sub_line = line[offset : offset + width]
        print(' ' * INDENT, sub_line.rstrip(), sep='')
        display_padding = ' ' * (INDENT + start - offset)
        print(display_padding, '^' * len(source), sep='')
        print(display_padding, target, sep='')
        print('Replace? y/n >', end='', flush=True)
        if input().lower() == 'y':
            return undone[:start + 1] + processLine(
                line_no, undone[start + 1:], source, target, 
            )
        else:
            print('User decided not to replace.')
    return line[:start + 1] + processLine(
        line_no, line[start + 1:], source, target, 
    )

main()
