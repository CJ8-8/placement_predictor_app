import pandas as pd
import random
import os

os.makedirs("data", exist_ok=True)

data = []
for _ in range(1000):
    cgpa = round(random.uniform(6.0, 10.0), 2)
    internships = random.randint(0, 3)
    projects = random.randint(1, 5)
    comm_skills = random.randint(1, 5)
    cp = random.choice([0, 1])
    dsa = random.randint(1, 5)
    ml = random.choice([0, 1])
    cloud = random.choice([0, 1])
    backlogs = random.choice([0, 1])
    certs = random.randint(0, 5)
    tier = random.choice(["Tier 1", "Tier 2", "Tier 3"])
    resume = random.randint(40, 100)
    
    if cgpa >= 8.2 and ml == 1 and cp == 1 and resume > 80:
        label = "Product"
    elif 6.5 <= cgpa < 8.2 and (internships >= 1 or certs >= 2) and resume > 60:
        label = "Service"
    else:
        label = "None"





    data.append([cgpa, internships, projects, comm_skills, cp, dsa, ml, cloud,
                 backlogs, certs, tier, resume, label])

df = pd.DataFrame(data, columns=[
    "CGPA", "Internships", "Projects", "Communication", "CP", "DSA", "ML", "Cloud",
    "Backlogs", "Certs", "Tier", "ResumeScore", "Placement"
])

df.to_csv("data/synthetic_data.csv", index=False)
