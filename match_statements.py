def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teacup"
        case ():
            return "Something is  wrong with the internet"
        case 401 | 403 | 404:
            return "Not allowed"
