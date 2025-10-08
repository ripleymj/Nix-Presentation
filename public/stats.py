import csv
import math
import random

import requests
from bs4 import BeautifulSoup, Tag


def repo_color(name: str) -> str:
    lower_name = name.lower()
    if lower_name.startswith("ubuntu"):
        return "#e95420"
    if lower_name.startswith("nixpkgs"):
        return "#4f73bd"
    if lower_name.startswith("debian"):
        return "#d80150"
    if lower_name.startswith("alpine"):
        return "#0d597f"
    if lower_name.startswith("fedora"):
        return "#294072"
    if lower_name.startswith("aur"):
        return "#1793d1"

    return f"#{math.floor(random.random() * 0xFFFFFF):06x}"


URL = "https://repology.org/repositories/packages"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0"
}
response = requests.get(URL, headers=HEADERS)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

rows: list[tuple[str, str, str, str]] = []

for tr in soup.select("tbody > tr"):
    # First column: repo name
    name_tag = tr.select_one("th a")
    name = name_tag.get_text(strip=True) if name_tag else ""

    # Second and third columns: prefer span[title], fall back to span text
    td_tags = tr.select("td")
    if len(td_tags) >= 2:

        def extract_value(td: Tag) -> str:
            span = td.select_one("span")
            if span:
                # Prefer title attribute, else text content
                title = span.get("title")
                if title is None:
                    title = span.get_text(strip=True)
                elif type(title) is not str:
                    title = title[0]
                return title
            # Sometimes there's no <span>, just text inside <a> or <td>
            return td.get_text(strip=True)

        packages = extract_value(td_tags[0])
        fresh_packages = extract_value(td_tags[1])
    else:
        packages = fresh_packages = ""

    color = repo_color(name)

    rows.append((name, color, packages, fresh_packages))

# Write to CSV
with open("packages.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "color", "packages", "freshPackages"])
    writer.writerows(rows)

print("✅ Extracted", len(rows), "rows into packages.csv")
