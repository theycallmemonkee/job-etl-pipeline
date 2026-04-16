def transform_data(data):
    cleaned = []
    seen = set()

    for job in data[1:]:  # skip metadata

        # extract
        title = job.get("position", "Unknown")
        company = job.get("company", "Unknown")
        location = job.get("location", "Unknown")

        # filtering
        if not title:
            continue

        # cleaning
        title = title.strip().title()
        company = company.strip().title()
        location = location.strip().title()

        # derived
        is_remote = "remote" in location.lower()

        # validation
        if len(title) < 3:
            continue

        # deduplication
        key = (title, company)
        if key in seen:
            continue
        seen.add(key)

        salary = None

        cleaned.append({
            "title": title,
            "company": company,
            "location": location,
            "salary": salary,
            "is_remote": is_remote
        })

    return cleaned