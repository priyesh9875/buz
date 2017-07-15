import moment

def parseDate(date):
    """
    Parse date based on different formats
    """
    formats = [
        "D MMM YY, hh:mm a", 
        "YYYY-MM-DDTHH:mm:ss+00:00", 
        "ddd, D MMM YYYY HH:mm:ss +0530", # NDTV
        "ddd, D MMM YYYY HH:mm:ss +0100", # skynews
        "ddd, D MMM YYYY HH:mm:ss -0400",  # reuters
        "D MMM, YYYY", # espn cricket
        "ddd, D MMM YYYY HH:mm:ss GMT", # times of india
        "ddd, D MMM YYYY HH:mm:ss +0200", # lifrea
        "ddd, D MMM YYYY HH:mm:ss +0000", # linux, ubuntu
        "ddd, D MMM YYYY HH:mm:ss -0700", # iTunes
        ]

    for f in formats:
        try:
            parsed_date = tryDateFormat(date, f)
            return parsed_date.format("D MMM YY, hh:mm a")
        except Exception as e:
            pass
    else:
        return "Invalid date"
    
def tryDateFormat(date, format):
    return moment.date(date, format)
