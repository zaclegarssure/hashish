from elftools.elf.elffile import ELFFile
from elftools.common.exceptions import ELFError

import argparse
import sys
import hashlib

def hash_section(elf_file, section):
    try:
        elffile = ELFFile(elf_file)
        elf_section = elffile.get_section_by_name(section)

        if elf_section is None:
            raise Exception('{section} is not a valid section in {elf_file}.'.format(section=section, elf_file=elf_file.name))
        else:
            return hashlib.sha256(elf_section.data()).hexdigest()

    except ELFError:
        raise Exception('{elf_file} is not a valid ELF file.'.format(elf_file=elf_file.name))

def main():
    parser = argparse.ArgumentParser(description='Compute hash of an ELF binary\'s section.')
    parser.add_argument('elf_file', type=argparse.FileType('rb'),
                        help='elf binary to hash')
    parser.add_argument('section',
                        help='elf section to hash')
    args = parser.parse_args()

    try:
        hashed = hash_section(args.elf_file, args.section)
        print(hashed)
    except Exception as exc:
        print('{}: {}'.format(type(exc).__name__, exc))
        sys.exit(1)


if __name__ == "__main__":
    main()
