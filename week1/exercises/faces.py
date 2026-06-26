def main():
    prompt=input()
    convert(prompt)

def convert(to):
    print(to.replace(":)", "🙂").replace(":(", "🙁"))

main()

