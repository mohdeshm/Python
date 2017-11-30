class faculty:
    def __init__(self):
        self.facultyName=""
        self.facultyId=""
        self.facultyCourses=[]

    def setFacultyId(self, facultyId):
        self.facultyId = facultyId

    def setFacultyName(self,facultyName):
        self.facultyName=facultyName

    def setFacultyCourses(self,facultyCourses):
        self.facultyCourses =facultyCourses

    def getFacultyName(self):
        return self.facultyName

    def getFacultyId(self):
        return self.facultyId

    def getFacultyCourses(self):
        return self.facultyCourses