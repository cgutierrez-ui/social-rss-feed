import argparse
import os
import sys
from urllib.parse import quote

from dotenv import load_dotenv

load_dotenv()

RSS_BRIDGE_BASE_URL = os.getenv("RSS_BRIDGE_BASE_URL", "")

def build_instagram_feed_url(username: str, base_url: str | None = None ) -> str:
	base = (base_url or RSS_BRIDGE_BASE_URL).rstrip("/")
	if not base:
		raise ValueError(
			"No base URL configured -- set RSS-Bridge base URL in .env, or pass --base-url"
		)

	username = username.strip().lstrip("@")
	return (
		f"{base}/?action=display&bridge=Instagram&context=Username"
		f"&u={quote(username)}&format=Atom"
	)

def validate_feed(feed_url: str) -> tuple[bool, str]:
	import feedparser

	try:
		parsed = feedparser.parse(feed_url)
	except Exception as e:
		return False, f"couldn't fetch: {e}"

	if parsed.bozo and not parsed.entries:
		return False, "not a valid feed (check the username and base URL)"
	if not parsed.entries:
		return True, "valid feed, but there are no posts to share"
	return True, f"valid feed, {len(parsed.entries)} available"

def main():
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("usernames", nargs="+", help="One or more Instagram usernames")
	parser.add_argument(
		"--base-url",
		default = None,
		help = "RSS-Bridge base URL (overrides RSS base URL in .env)"
	)

	parser.add_argument(
		"--validate",
		action = "store_true",
		help = "Fetch each feed and confirm it parses before printing it"
	)
	
	args = parser.parse_args()

	exit_code = 0

	for username in args.usernames:
		try:
			url = build_instagram_feed_url(username, args.base_url)
		except ValueError as e:
			print(f"@{username}: {e}", file = sys.stderr)
			exit_code = 1
			continue

		if args.validate:
			ok, message = validate_feed(url)
			status = "OK" if ok else "FAILED"
			print(f"[{status}] @{username}: {message}")
			if not ok:
				exit_code = 1
		print(url)
		print()
	sys.exit(exit_code)

if __name__ == "__main__":
	main()