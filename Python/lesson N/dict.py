student_data = {

"id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},

"id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},

"id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"}, # duplicate of id1

"id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},

}
results = {}
seen_Keys=[]

for student_id,details in student_data.items():
    unique_Key = (details["name"], details["class"], details["subject_integration"])

    if unique_Key not in seen_Keys:
        seen_Keys.append(unique_Key)
        results[student_id] = details

for k, v in results.items():
    print(k, ":", v)


