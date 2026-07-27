# Extracts Twitter username from URL using str.replace

url = input("URL: ").strip()

# replacing the beginning of url with nothing ""
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
