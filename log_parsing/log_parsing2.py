def parse_logs(filename):
    """
    Parses a log file to identify and print FATAL error messages.

    Args:
        filename (str): The path to the log file to be parsed.

    Returns:
        None
    
    Side effect: 
        Prints out FATAL logs with the user, the error message, date, and time of occurrence.

    """
    with open(filename, "r") as logs:
        for line in logs:
            line_split = line.split()
            date = line_split[0]
            time = line_split[1]
            message = line_split[2]
            user = line_split[-1]

            # Print a message for only FATAL Errors
            if message == "FATAL":
                print(f"{user} => Error {message} on {date} at {time}")


parse_logs("logs.txt")