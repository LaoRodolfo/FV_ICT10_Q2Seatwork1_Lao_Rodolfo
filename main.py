
from pyscript import document

# Stores the names of registered ICT Fairview Club members in a list.
club_members = [
    "Rodolfo Lao",
    "Sabine Agacita",
    "Raven Denum",
    "Maria Coronel",
    "Lance Catu",
    "Jhoana Evangelista"
]

# Stores the success and rejection messages using Boolean dictionary keys.
verification_messages = {
    True: "Congratulations {candidate_name}! You are now part of the ICT club.",
    False: "Sorry {candidate_name}, your name is not on the list."
}

# Stores the input field IDs in an immutable tuple.
input_ids = ("first-name", "last-name")

# Stores the labels for the two input fields in another tuple.
input_labels = ("First Name", "Last Name")

# Verifies the candidate's membership when the button is clicked.
def verify_candidate(event):

    # Retrieves the input values from the webpage using tuple unpacking.
    first_name, last_name = (
        document.getElementById(input_ids[0]).value.strip(),
        document.getElementById(input_ids[1]).value.strip()
    )

    # Combines the first and last names into one full name.
    candidate_name = f"{first_name} {last_name}"

    # Removes extra spaces and standardizes the capitalization of the name.
    candidate_name = " ".join(candidate_name.split()).title()

    # Checks whether the candidate's full name exists in the club members list.
    is_member = candidate_name in club_members

    # Selects and formats the appropriate message using the Boolean result.
    result_message = verification_messages[is_member].format(
        candidate_name=candidate_name
    )

    # Creates a copy of the club members list without modifying the original.
    members_copy = club_members.copy()

    # Combines the original list and its copy to demonstrate list concatenation.
    combined_members = club_members + members_copy

    # Adds the current candidate's name to a separate list using append().
    candidate_records = []
    candidate_records.append(candidate_name)

    # Counts how many times the candidate appears in the registered members list.
    membership_count = club_members.count(candidate_name)

    # Gets the total number of registered members using len().
    total_members = len(club_members)

    # Creates an alphabetically sorted copy of the club members list.
    sorted_members = sorted(club_members)

    # Stores the candidate's name and membership result in an immutable tuple.
    candidate_record = (candidate_name, is_member)

    # Unpacks the tuple into separate variables for the candidate and result.
    recorded_name, recorded_status = candidate_record

    # Uses comparison operators to compare the number of members with zero.
    member_count_check = total_members > 0
    candidate_count_check = membership_count >= 1
    name_check = recorded_name == candidate_name
    status_check = recorded_status != False

    # Demonstrates the type() function by identifying the data types used.
    name_type = type(candidate_name)
    members_type = type(club_members)
    record_type = type(candidate_record)

    # Displays the verification message in the webpage's existing result area.
    document.getElementById("result").innerText = result_message
