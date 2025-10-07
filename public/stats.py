import csv

from bs4 import BeautifulSoup, Tag

# Load your HTML (replace this with reading from a file or requests.get().text)
with open("packages_table.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

rows: list[tuple[str, str, str]] = []

for tr in soup.select("tbody > tr"):
    # 1️⃣ First column: repo name
    name_tag = tr.select_one("th a")
    name = name_tag.get_text(strip=True) if name_tag else ""

    # 2️⃣ Second and third columns: prefer span[title], fall back to span text
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

    rows.append((name, packages, fresh_packages))

# Write to CSV
with open("packages.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Packages", "Fresh Packages"])
    writer.writerows(rows)

print("✅ Extracted", len(rows), "rows into packages.csv")
