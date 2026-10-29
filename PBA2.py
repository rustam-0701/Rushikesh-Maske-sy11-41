import csv

with open("students.csv", "r") as infile:
    reader = csv.DictReader(infile)

    with open("selected.csv", "w", newline="") as outfile:
        fields = ["Name", "Roll_No", "Marks"]
        writer = csv.DictWriter(outfile, fieldnames=fields)

        writer.writeheader()

        for row in reader:
            writer.writerow({
                "Name": row["Name"],
                "Roll_No": row["Roll_No"],
                "Marks": row["Marks"]
            })

print("Selected columns saved successfully!")