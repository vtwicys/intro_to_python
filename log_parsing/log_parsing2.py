def parse_logs(filename):
    with open(filename, "r") as logs:
        for line in logs:
            line_split = line.split()
            date = line_split[0]
            time = line_split[1]
            message = line_split[2]
            user = line_split[-1]

            # We want only FATAL Errors
            if message == "FATAL":
                print(f"{user} => Error {message} on {date} at {time}")


parse_logs("logs.txt")