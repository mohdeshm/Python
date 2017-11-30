from Student import student
from Course import course
from Faculty import faculty
from Batch import batch
class studentScheduler:
    def __init__(self):
         self.Student=""
         self.Students={}
         self.Course=""
         self.Courses = []
         self.Faculty = ""
         self.Faculties = []
         self.Batch =""
         self.Batches ={}

    def validate(self,rollNo):
        if rollNo in self.Students.keys():
            print "Student already exists with the same roll number"
            return True
        else:
            return False

    def getStudentByRollNo(self,rollNo):
        self.Student=self.Students[rollNo]
        print self.Student.rollNo
        print self.Student.name
        print self.Student.courseNames
        return self.Student

    def addStudent(self,rollNo,name,courseNames):
        self.Student=student()
        self.Student.setRollNo(rollNo)
        self.Student.setName(name)
        self.Student.setCourseNames(courseNames)
        self.Students.update({rollNo:self.Student})


    def addCourse(self,courseName):
        self.Course = course()
        self.Course.setCourseName(courseName)
        self.Courses.append(self.Course)

    def addFaculty(self,facultyId,facultyName,facultyCourses):
        self.Faculty = faculty()
        self.Faculty.setFacultyName(facultyName)
        self.Faculty.setFacultyId(facultyId)
        self.Faculty.setFacultyCourses(facultyCourses)
        self.Faculties.append(self.Faculty)

    def addBatch(self,batchId,batchCourseName,batchFacultyName,batchStudents):
        self.Batch=batch()
        self.Batch.setBatchId(batchId)
        self.Batch.setBatchCourseName(batchCourseName)
        self.Batch.setBatchFacultyName(batchFacultyName)
        self.Batch.setBatchStudents(batchStudents)
        self.Batches.update({batchId:self.Batch})

    def showAllStudents(self):
        sortedStudentRollNos=sorted(self.Students, key=self.Students.get, reverse=True)
        for rolNo in sortedStudentRollNos:
             self.Student=self.Students[rolNo]
             print self.Student.rollNo
             print self.Student.name
             print self.Student.courseNames

    def getBatchDetailsByBatchId(self,batchId):
        self.Batch = self.Batches[batchId]
        print self.Batch.batchId
        print self.Batch.batchCourseName
        print self.Batch.batchFacultyName
        print self.Batch.batchStudents
        return self.Batch

    def getBatchDetailsByRollNo(self,rollNo):
        for batchId in self.Batches.keys():
                if rollNo in self.Batches[batchId].batchStudents.keys():
                    print self.Batch.batchId
                    print self.Batch.batchCourseName
                    print self.Batch.batchFacultyName
                    print self.Batch.batchStudents
                    break

