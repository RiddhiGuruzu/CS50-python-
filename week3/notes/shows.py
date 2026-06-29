SHOWS = [" avatar: the last airbender ", "ben 10", " arthur", "kim possible "]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print(', '.join(cleaned_shows))

main()
