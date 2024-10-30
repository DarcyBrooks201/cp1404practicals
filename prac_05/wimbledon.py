"""
CP1404 prac 5
Wimbledon.py and wimbledon.csv
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    print(records)
    champions_wins = find_number_of_wins(records)
    champions_countries = record_champions_countries(records)
    print_results(champions_countries, champions_wins)


def print_results(champions_countries, champions_wins):
    """Print how many times each champ won, and what country they are from"""
    # Print champs and how many times they won
    for champions, wins in champions_wins.items():
        print(f"{champions} {wins}")
    # Print sorted champs countries
    print(f"These {len(champions_countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(champions_countries)))


def record_champions_countries(records):
    """Record each new country of a champion"""
    champions_countries = set()
    for record in records:
        champions_country = record[1]
        champions_countries.add(champions_country)
    return champions_countries


def find_number_of_wins(records):
    """Find champs and how many times they won"""
    champions_wins = {}
    for record in records:
        if record[2] in champions_wins:
            champions_wins[record[2]] += 1
        else:
            champions_wins[record[2]] = 1
    return champions_wins


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
