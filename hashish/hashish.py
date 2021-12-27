from elftools.elf.elffile import ELFFile
from elftools.common.exceptions import ELFError

import argparse
import sys
import hashlib

def main():
    parser = argparse.ArgumentParser(description='Compute hash of an ELF binary\'s section.')
    parser.add_argument('elf_file', type=argparse.FileType('rb'),
                        help='elf binary to hash')
    parser.add_argument('section',
                        help='elf section to hash')
    args = parser.parse_args()

    try:
        elffile = ELFFile(args.elf_file)
        section = elffile.get_section_by_name(args.section)

        if section is None:
            print('{section} is not a valid section in {elf_file}.'.format(section=args.section, elf_file=args.elf_file.name))
            sys.exit(1)
        else:
            hashed = hashlib.sha256(section.data()).hexdigest()
            print(hashed)

    except ELFError:
        print('{elf_file} is not a valid ELF file.'.format(elf_file=args.elf_file.name))
        sys.exit(1)

if __name__ == "__main__":
    main()
