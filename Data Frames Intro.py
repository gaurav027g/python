import pandas as pd
data = {
    'Students': ["Bob", "Tom", "Jack", "Ollie", "Don"],
    'Maths': [89,56,76,64,46],
    'Science': [87,57,37,96,65],
    'Sports': ["Badminton", "Hockey", "Basketball", "Cricket", "Football"]
}

students = pd.DataFrame(data, columns=["Students", "Maths", "Science", "Sports"])
print(students)
