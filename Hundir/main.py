import logging
from modules.ScanUrl import ScanUrl, argument_parser

if __name__ == "__main__":
    try:
        args = argument_parser()
        scan = ScanUrl(args.url, args.dict, args.thread)
        scan.start()
    except Exception as e:
        logging.error(f"Error: {e}")
