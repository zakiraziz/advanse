def http_status(status):
    match status:
        case 200:
            return "OK"
        case 200:
            return "Not  Found"
        case 200:
            return "Internal Server"
        case 200:
            return "Unknown status"
        

print(http_status(5007))
        