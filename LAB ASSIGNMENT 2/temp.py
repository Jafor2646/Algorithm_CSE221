class Student:
    def __init__(self, n, i, d= "CSE"):
        self.name = n
        self.id = i
        self.dept = d
        self.grade = {}
        print("A student is created successfully")
    def addGrades(self, *args):
        sum = 0
        args = list(args)
        for i in args:
            s, g = i.split("-")
            self.grade[s] = float(g)
            sum += float(g)
        avg = sum/len(args)
        print("Grades are added successfully for", self.name)
        print("Current CGPA:", avg)
    def showGradesheet(self):
        print("Grade Sheet for",self.name+",","student ID:", self.id)
        print("Courses completed -> ", end="")
        s = ""
        for k in self.grade.keys():
             s += (k+", ")
        print(s[:-2])
        print("Grade obtained -> ",end="")
        s = ""
        for v in self.grade.values():
            s += (str(v)+", ")
        print(s[:-2])
student1 = Student("Rajin", 123, "CSE")
student2 = Student("Marina", 124)
print("1======================")
student1.addGrades("CSE111-3.7", "CSE230-4.0", "MGT201-3.0")
print("2===================================")
student1.showGradesheet()
print("3==============================")
student2.addGrades("CSE330-4.0", "BUS102-3.0", "ENG101-3.3")
student1.addGrades("CSE220-3.7", "CSE320-4.0", "ENG101-3.7")
print("4==================================")
student2.showGradesheet()
student1.showGradesheet()