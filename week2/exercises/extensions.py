file=input("File name: ")
match file.split(".")[-1].lower():
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
