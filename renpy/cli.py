import argparse
import logging
from pathlib import Path

from .core import RenPy


def cli_main():
    RenPy.banner()
    parser = argparse.ArgumentParser(
        prog="RenPy",
        description="RenPy is a Python CLI tool for renaming files efficiently.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("base_name", type=str, help="Base name for the renamed files.")
    parser.add_argument(
        "directory", type=Path, help="Path to the directory containing files to rename."
    )
    parser.add_argument(
        "-r",
        "--order",
        type=str,
        choices=["alphabet", "new", "old"],
        default="old",
        help="Renaming order: \n  'alphabet' - Alphabetically\n  'new' - Newest to oldest\n  'old' - Oldest to newest (default)",
    )
    parser.add_argument(
        "-s",
        "--simulate",
        action="store_true",
        help="Simulate the renaming process without making actual changes.",
    )
    parser.add_argument(
        "--case-sensitive",
        action="store_true",
        help="Sort files alphabetically with case sensitivity.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging.",
    )
    args = parser.parse_args()

    if not args.directory.exists() or not args.directory.is_dir():
        logging.error(f"Error: Directory '{args.directory}' does not exist.")
        exit(1)

    renpy = RenPy(debug=args.debug)
    renpy.renFn(
        args.base_name, args.directory, args.order, args.simulate, args.case_sensitive
    )


if __name__ == "__main__":
    cli_main()
