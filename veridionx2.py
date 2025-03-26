import pandas as pd
from rapidfuzz import fuzz

data = {
    "company_name": [
        "SSL Pools",
        "SSL Pools Ltd.",
        "SSL POOLS LTD",
        "Pubblicar System Srl | ALA RENT",
        "Pubblicar System srl",
        "ALA RENT",
        "ING Financial Svces",
        "Ing",
        "ING Financial Services"
    ]
}

df = pd.DataFrame(data)

df["clean_name"] = (
    df["company_name"]
    .str.lower()
    .str.replace(r"[^a-z0-9 ]", "", regex=True)
    .str.strip()
)

groups = []
used = set()

for i in range(len(df)):
    if i in used:
        continue
    name_i = df.loc[i, "clean_name"]
    group = [i]
    for j in range(i + 1, len(df)):
        if j in used:
            continue
        name_j = df.loc[j, "clean_name"]
        score = fuzz.token_sort_ratio(name_i, name_j)
        if score > 85:
            group.append(j)
            used.add(j)
    used.update(group)
    groups.append(group)

group_ids = [None] * len(df)
for gid, group in enumerate(groups):
    for idx in group:
        group_ids[idx] = gid

df["entity_group"] = group_ids

print(df)

df.to_csv("entity_resolution_result.csv", index=False)
