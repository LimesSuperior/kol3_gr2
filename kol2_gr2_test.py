import unittest
from kol2_gr2 import Student, SchoolClass, ClassDiary


class StudentTest(unittest.TestCase):

	def setUp(self):
		self.student_instance = Student("Jan", "Nowak")

	def test_init_name(self):
		self.assertEqual(self.student_instance.name, "Jan")

	def test_init_surname(self):
		self.assertEqual(self.student_instance.surname, "Nowak")

	def test_init_args_type(self):
		assertRaises(Exception, Student(1,5))
		

class SchoolClassTest(unittest.TestCase):
	
	def setUp(self):
		self.student_instance = Student("Adam", "Kawa")
		self.schoolclass_instance = SchoolClass("A", [student_instance])

	def test_init_name(self):
		assertEqual(self.schoolclass_instance.name, "A")

	def test_init_students(self):
		assertEqual(self.schoolclass_instance.students, [self.student_instance])

	def test_init_classname_type(self):
		assertRaises(Exception, SchoolClass(5, None))

	
class ClassDiaryTest(unittest.TestCase):

	def setUp(self):
		pass

