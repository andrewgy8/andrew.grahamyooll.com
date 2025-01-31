import argparse

from bakesite.logging import *  # noqa: F401 F403
from bakesite.art import PIE_ASCII
from bakesite.compile import bake
from bakesite.server import serve


def main():
    parser = argparse.ArgumentParser(
        prog="bakesite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=f"{PIE_ASCII}\nSimple static site generator ",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("bake", help="bake your markdown files into a static site")
    subparsers.add_parser(
        "serve", help="locally serve the site at http://localhost:8003"
    )
    args = parser.parse_args()
    if args.command == "bake":
        bake()
    elif args.command == "serve":
        serve()
