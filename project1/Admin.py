from StudentScheduler import studentScheduler
class admin:
    def admin(self):
        self.studentScheduler=""

    def showMenu(self):
        self.studentScheduler=studentScheduler()
        while(True):
            x=input("Choose and enter the menu index from below\n1.Add Student\n2.Show All Students by roll number\n"
                    "3.Add Course\n4.Add Faculty\n5.Add Batch\n6.Student Details by Roll Number\n"
                    "7.Batch Details by batch Id\n8.Batch Details by roll number\n9.Exit\n")
            if(x==1):
                while(True):
                    rollNo=input("enter roll no")
                    if(self.studentScheduler.validate(rollNo)):
                        continue
                    else:
                        break
                name=raw_input("enter name")
                noCourses=input("Enter the number of courses you want to attend")
                courses=[]
                for num in range(0,noCourses):
                    course=raw_input("Enter the course name")
                    courses.append(course)
                self.studentScheduler.addStudent(rollNo,name,courses)

            elif(x==2):
                self.studentScheduler.showAllStudents()

            elif(x==3):
                courseName=raw_input("Enter the name of the course")
                self.studentScheduler.addCourse(courseName)

            elif(x==4):
                facultyName = raw_input("Enter the name of the faculty")
                facultyId=input("Enter the Id of the faculty")
                noCourses=input("Enter the number of courses of the faculty")
                print "Enter the names of the courses"
                facultyCourses=[]
                for num in range(0,noCourses):
                    facultyCourse=raw_input()
                    facultyCourses.append(facultyCourse)
                self.studentScheduler.addFaculty(facultyId,facultyName,facultyCourses)

            elif(x==5):
                batchId = input("enter the batch Id")
                batchCourseName = raw_input("enter the batch Course Name")
                batchFacultyName = raw_input("enter the batch Faculty Name")
                self.studentScheduler.showAllStudents()
                numStudents=input("Enter the number of students you want to add from above list")
                batchStudents={}
                for num in range(0,numStudents):
                    rollNo=input("Enter the roll number")
                    batchStudents.update({rollNo:self.studentScheduler.getStudentByRollNo(rollNo)})
                self.studentScheduler.addBatch(batchId,batchCourseName,batchFacultyName,batchStudents)

            elif(x==6):
                rollNo=input("Enter the rollNo")
                self.studentScheduler.getStudentByRollNo(rollNo)

            elif(x==7):
                batchId=input("Enter the batch Id")
                self.studentScheduler.getBatchDetailsByBatchId(batchId)

            elif(x==8):
                rollNo = input("Enter the rollNo")
                self.studentScheduler.getBatchDetailsByRollNo(rollNo)

            elif(x==9):
                break

Admin=admin()
Admin.showMenu()


