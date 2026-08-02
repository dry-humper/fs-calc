import streamlit as st
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import json

cInfo = [
    {"name": "Sabrina", "birthdate": "1996-06-20", "region": "Texas"},
    {"name": "Adam", "birthdate": "1994-11-04", "region": "Texas"},
    {"name": "Herman", "birthdate": "1972-06-30", "region": "Texas"},
    {"name": "Abel", "birthdate": "1973-03-31", "region": "Texas"},
    {"name": "Celeste", "birthdate": "2005-04-04", "region": "Texas"},
    {"name": "Marlin", "birthdate": "1972-03-08", "region": "Texas"},
    {"name": "Camilo", "birthdate": "1994-11-19", "region": "Texas"},
    {"name": "Kamila", "birthdate": "1995-06-18", "region": "Texas"},
    {"name": "Marley", "birthdate": "1994-12-03", "region": "Texas"},
    {"name": "Paxton", "birthdate": "1995-04-05", "region": "Texas"},
    {"name": "Amber", "birthdate": "1995-02-06", "region": "Texas"},
    {"name": "Jazmine", "birthdate": "1993-09-03", "region": "Texas"},
    {"name": "Zaid", "birthdate": "1994-12-07", "region": "Texas"},
    {"name": "Dusty", "birthdate": "1995-01-18", "region": "Texas"},
    {"name": "Natalie", "birthdate": "1995-07-03", "region": "Texas"},
    {"name": "Kevin", "birthdate": "1995-07-21", "region": "Texas"},
    {"name": "Sam", "birthdate": "1996-11-18", "region": "Texas"},
    {"name": "Peter", "birthdate": "1993-12-16", "region": "Texas"},
    {"name": "Cameron", "birthdate": "1995-05-12", "region": "Texas"},
    {"name": "Noah", "birthdate": "1995-02-20", "region": "Texas"},
    {"name": "Lisa", "birthdate": "1977-07-11", "region": "Texas"},
    {"name": "Julie", "birthdate": "2006-10-28", "region": "Texas"},
    {"name": "Rafaela", "birthdate": "1977-04-19", "region": "Texas"},
    {"name": "Harunobu", "birthdate": "1974-07-01", "region": "California"},
    {"name": "Ethan", "birthdate": "1994-11-04", "region": "California"},
    {"name": "Nathaniel", "birthdate": "1989-01-26", "region": "California"},
    {"name": "Vernon", "birthdate": "1986-05-21", "region": "California"},
    {"name": "Drew", "birthdate": "1988-08-22", "region": "California"},
    {"name": "Beatus", "birthdate": "1988-07-24", "region": "California"},
    {"name": "Arthur", "birthdate": "1989-10-17", "region": "California"},
    {"name": "Makani", "birthdate": "1985-12-13", "region": "California"},
    {"name": "Manuel", "birthdate": "1967-09-05", "region": "California"},
    {"name": "Nilo", "birthdate": "1978-09-12", "region": "California"},
    {"name": "Evalyn", "birthdate": "2005-06-29", "region": "California"},
    {"name": "Alice", "birthdate": "1994-12-01", "region": "California"},
    {"name": "Wakuni", "birthdate": "1994-08-27", "region": "California"},
    {"name": "Nora", "birthdate": "1994-10-02", "region": "California"},
    {"name": "Izalea", "birthdate": "1995-03-07", "region": "California"},
    {"name": "Devin", "birthdate": "1995-02-28", "region": "California"},
    {"name": "Korey", "birthdate": "1993-12-10", "region": "California"},
    {"name": "Antonio", "birthdate": "1990-08-31", "region": "California"},
    {"name": "Wendell", "birthdate": "1968-02-14", "region": "Indigo Society"},
    {"name": "Madison", "birthdate": "1993-03-08", "region": "Indigo Society"},
    {"name": "Kingston", "birthdate": "2002-05-06", "region": "Indigo Society"},
    {"name": "Mariah", "birthdate": "1980-08-13", "region": "Indigo Society"},
    {"name": "Jackson", "birthdate": "2002-01-13", "region": "Indigo Society"},
    {"name": "Everest", "birthdate": "1994-02-13", "region": "Indigo Society"},
    {"name": "Roy", "birthdate": "1971-06-17", "region": "Indigo Society"},
    {"name": "Krystol", "birthdate": "1969-01-03", "region": "Indigo Society"}
]


def calc_age(bir_str, tar_str):
    # Convert both string dates into date objects
    try:
        bir_date = date.fromisoformat(bir_str)
        tar_date = date.fromisoformat(tar_str)
    except ValueError:
        return "Invalid Birthdate"

    # Calculate basic year difference
    age = tar_date.year - bir_date.year

    # Adjust age if birthday hasn't passed
    if (tar_date.month, tar_date.day) >= (bir_date.month, bir_date.day):
        return age
    else:
        age = age - 1
        return age


def compare_age(char_a, char_b):
    # Parse dates
    date_a = date.fromisoformat(char_a["birthdate"])
    date_b = date.fromisoformat(char_b["birthdate"])

    # Determine who is older by comparing birthdays
    if date_a < date_b:
        older_char = char_a["name"]
        younger_char = char_b["name"]
        diff = relativedelta(date_b, date_a)
    elif date_b < date_a:
        older_char = char_b["name"]
        younger_char = char_a["name"]
        diff = relativedelta(date_a, date_b)
    else:
        return f"{char_a['name']} and {char_b['name']} were born on the same day."

    # Format the result string
    return f"{older_char} is {diff.years} years, {diff.months} months, and {diff.days} days older than {younger_char}."


def load_canon_dates():
    try:
        with open("canon_dates.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        # Fallback dictionary if the file doesn't exist yet
        return {
            "Texas": "2026-01-01",
            "California": "2026-01-01",
            "Indigo Society": "2026-01-01",
            "Other": "2026-01-01"
        }


def update_canon_date(region_name, new_date_str):
    # Load current dictionary
    dates_dict = load_canon_dates()

    # Update the specific region's date
    dates_dict[region_name] = new_date_str

    # Save back to the file
    with open("canon_dates.json", "w") as file:
        json.dump(dates_dict, file, indent=4)


def get_chars_by_region(region_name):
    chars = []
    if region_name == "All":
        return cInfo

    for x in cInfo:
        if x["region"] == region_name:
            chars.append(x)

    return chars


def get_chars_by_name(search_name):
    chars = []
    for x in cInfo:
        if search_name.lower() in x["name"].lower():
            chars.append(x)

    return chars


# Setup and Title
st.set_page_config(page_title="Fallen Star Age Tracker and Calculator", page_icon="⭐️", layout="centered")
st.title("Fallen Star Age Tracker and Calculator")

# Sidebar Mode Selector
st.sidebar.title("Modes")
mode = st.sidebar.radio(
    "Choose Mode:",
    ["Canonical", "Hypothetical"]
)

canon_dates = load_canon_dates()

# Canonical Updates Mode
if mode == "Canonical":
    st.header("Canonical Date Update & Ages")
    st.caption("Here you can updated the last date we did for each chat and check ages.")

    # Display current saved dates
    st.subheader("Current Canonical Dates")
    cols = st.columns(2)
    regions = ["Texas", "California", "Indigo Society", "Other"]

    for idx, reg in enumerate(regions):
        current_val = canon_dates.get(reg, "Not set")
        cols[idx % 2].metric(label=reg, value=current_val)

    st.divider()

    # Select Region to View Canonical Ages & Update Date
    st.subheader("Region Canonical Ages & Update")
    selected_reg = st.selectbox("Selected Region:", regions)

    current_reg_date_str = canon_dates.get(selected_reg, date.today().isoformat())
    current_reg_date = date.fromisoformat(current_reg_date_str)

    # Auto Age Checker for Canon Date
    st.write(f"### Character Ages in {selected_reg} as of {current_reg_date_str}:")
    reg_chars = get_chars_by_region(selected_reg)

    if reg_chars:
        for char in reg_chars:
            age = calc_age(char["birthdate"], current_reg_date_str)
            st.write(f"**{char['name']}**: {age} years old *(Born: {char['birthdate']}*")
    else:
        st.info(f"No characters assigned to {selected_reg} yet.")

    # Form to update a date
    st.write("Update Canonical Date for " + selected_reg)
    new_canon_date = st.date_input(
        value=current_reg_date,
        min_value=date(1800, 1, 1),
        max_value=date(2100, 12, 31)
    )

    if st.button("Save"):
        update_canon_date(selected_reg, new_canon_date.isoformat())
        st.success(f"Successfully updated canonical date for {selected_reg} to {new_canon_date}.")
        st.rerun()


elif mode == "Hypothetical":
    st.header("Hypothetical Date & Age Checker")
    st.caption("Here you can check stuff without updating anything.")

    # Create sub-tabs for different search types
    tab_search, tab_region, tab_compare = st.tabs([
        "Search Character",
        "Filter by Region",
        "Compare Ages"
    ])

    # Tab A -- Search by Name
    with (tab_search):
        st.subheader("Find a Character's Age on a Certain Date")
        search_query = st.text_input("Enter character's name:")
        target_date = st.date_input(
            "Select date:",
            value=date.today(),
            min_value=date(1800, 1, 1),
            max_value=date(2100, 12, 31)
        )



        if search_query:
            results = get_chars_by_name(search_query)
            if results:
                for char in results:
                    age = calc_age(char["birthdate"], target_date.isoformat())
                    st.success(f"{char['name']} is {age} years old on {target_date.isoformat()}.")
            else:
                st.warning("No characters found.")

    # Tab B -- Filter by Region
    with tab_region:
        st.subheader("Region Character List")
        selected_region = st.selectbox(
            "Choose Region:",
            ["All", "Texas", "California", "Indigo Society", "Other"]
        )

        default_date = canon_dates.get(selected_region, date.today().isoformat())
        target_date_reg = st.date_input(
            "Select date:",
            value=date.today(),
            min_value=date(1800, 1, 1),
            max_value=date(2100, 12, 31)
        )

        region_chars = get_chars_by_region(selected_region)

        st.write(f"Showing {len(region_chars)} character(s) in {selected_region}:")
        for char in region_chars:
            age = calc_age(char["birthdate"], target_date_reg.isoformat())
            st.write(f"**{char['name']}**: {age} years old *(Born: {char['birthdate']})*")

    # Tab C -- Compare Ages
    with tab_compare:
        st.subheader("Compare Age Differences")

        char_names = [c["name"] for c in cInfo]
        char_a_name = st.selectbox("Select Character A:", char_names, index=0)
        char_b_name = st.selectbox("Select Character B:", char_names, index=min(1, len(char_names)-1))

        if char_a_name != char_b_name:
            char_a = get_chars_by_name(char_a_name)[0]
            char_b = get_chars_by_name(char_b_name)[0]

            comparison_result = compare_age(char_a, char_b)
            st.info(f"**{comparison_result}**")
        else:
            st.warning("No characters found.")
