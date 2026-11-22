
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Plot
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2. Scatter Plot
plt.figure()
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 3. Box Plot
data = [10, 20, 30, 40, 50, 60, 70]
plt.figure()
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

# 4. Bar Chart
subjects = ['Python', 'Java', 'C++', 'HTML']
marks = [85, 75, 90, 80]

plt.figure()
plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 5. Pie Chart
labels = ['Python', 'Java', 'C++', 'HTML']
sizes = [40, 25, 20, 15]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
