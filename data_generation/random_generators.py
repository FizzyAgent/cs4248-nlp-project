import random


def get_random_time():
    digit = random.randint(1, 12)
    am_pm = random.choice(["am", "pm"])
    return f"{digit} {am_pm}"


def get_random_room():
    room = random.choice([
        "meeting room",
        "conference room",
        "seminar room",
    ])
    digit = random.randint(1, 10)
    return f"{room} {digit}"

def get_random_meeting_platform():
    return random.choice([
        "Zoom",
        "Google Meet",
        "Skype",
        "Microsoft Teams",
        "Slack",
    ])

def get_random_first_name(is_male: Optional[bool] = None):
    gender = None if is_male is None else "male" if is_male else "female"
    return names.get_first_name(gender=gender)

def get_random_document():
    return random.choice([
        "legal contract",
        "contract",
        "financial report",
        "business report",
        "report",
        "file",
        "Word document",
        "Excel spreadsheet"
        "PDF document",
        "schedule",
        "invoice",
        "quotation",
        "proposal",
        "diagram",
        "draft",
    ])

def get_random_office_role():
    return random.choice([
        "secretary",
        "HR manager",
        "team leader",
        "supervisor",
        "department head",
        "group director",
        "chairman",
        "director",
        "deputy CEO",
        "CEO",
        "client"
    ])


def get_random_non_office_venue():
    return random.choice([
        "restaurant", 
        "store", 
        "cafe", 
        "theatre", 
        "hotel",
        "camp"
    ])

def get_random_task():
    return random.choice([
        "project",
        "report",
        "pitch",
        "spreadsheet",
        "presentation",
        "negotiation"
    ])
