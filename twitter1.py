# Extracts Twitter username from URL using str.removeprefix

url = input("URL: ").strip()

# not just replace at any part but remove prefix
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
