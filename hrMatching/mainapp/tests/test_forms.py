from datetime import date, timedelta
from django.test import TestCase
from ..forms.company import CompanySignUpForm
from ..forms.employee import EmployeeSignUpForm, EmployeeUpdateForm
from ..models import Company, Employee, User, Employee_Cluster
from . import company_data, employee_data, twenty_years_ago


class CompanySignUpFormTest(TestCase):

    def test_form_valid_data(self):
        form = CompanySignUpForm(data=company_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_phone(self):
        invalid_phone_company_data = company_data.copy()
        # Invalid phone number
        invalid_phone_company_data["phone"] = "123-456-789A"
        form = CompanySignUpForm(data=invalid_phone_company_data)
        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors)
        self.assertEqual(
            form.errors["phone"],
            ["Phone number can only contain digits, hyphens, and plus signs."],
        )

    def test_form_save(self):
        form = CompanySignUpForm(data=company_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(User.objects.filter(email="test@example.com").exists())
        self.assertTrue(Company.objects.filter(user=user, name="Test Company").exists())


class EmployeeSignUpFormTest(TestCase):

    def setUp(self):
        self.Form = EmployeeSignUpForm

    def test_form_valid_data(self):
        form = self.Form(data=employee_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_phone(self):
        invalid_phone_employee_data = employee_data.copy()
        invalid_phone_employee_data["phone"] = "123-456-789A"
        form = self.Form(data=invalid_phone_employee_data)
        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors)
        self.assertEqual(
            form.errors["phone"],
            ["Phone number can only contain digits, hyphens, and plus signs."],
        )

    def test_form_invalid_dateOfBirth_in_the_future(self):
        tomorrow = date.today() + timedelta(days=1)
        born_in_future_employee = employee_data.copy()
        born_in_future_employee["dateOfBirth"] = tomorrow
        form = self.Form(data=born_in_future_employee)
        self.assertFalse(form.is_valid())
        self.assertIn("dateOfBirth", form.errors)
        self.assertEqual(
            form.errors["dateOfBirth"], ["Date of birth cannot be in the future."]
        )

    def test_form_invalid_dateOfBirth_younger_than_16(self):
        ten_years_ago = date.today().replace(year=date.today().year - 10)

        younger_than_16_employee = employee_data.copy()
        younger_than_16_employee["dateOfBirth"] = ten_years_ago
        form = self.Form(data=younger_than_16_employee)
        self.assertFalse(form.is_valid())
        self.assertIn("dateOfBirth", form.errors)
        self.assertEqual(
            form.errors["dateOfBirth"],
            ["You must be at least 16 years old to register."],
        )

    def test_form_invalid_dateOfBirth_older_than_80(self):
        ninety_years_ago = date.today().replace(year=date.today().year - 90)
        older_than_80_employee = employee_data.copy()
        older_than_80_employee["dateOfBirth"] = ninety_years_ago
        form = self.Form(data=older_than_80_employee)
        self.assertFalse(form.is_valid())
        self.assertIn("dateOfBirth", form.errors)
        self.assertEqual(form.errors["dateOfBirth"], ["Sorry you must be under 80."])

    def test_form_save(self):
        form = self.Form(data=employee_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(User.objects.filter(email="test@example.com").exists())
        self.assertTrue(Employee.objects.filter(user=user, firstname="Mo").exists())
        employee = Employee.objects.get(user=user, firstname="Mo")
        self.assertTrue(Employee_Cluster.objects.filter(employee=employee).exists())


class EmployeeUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="123123123",
        )
        self.employee = Employee.objects.create(
            user=self.user,
            firstname="John",
            lastname="Doe",
            dateOfBirth=twenty_years_ago,
            gender="MALE",
            city="New York",
            phone="1234567890",
            education="Bachelor",
            experience="5 years",
            awards="",
            hobbies="",
            skills="Python, Django",
            references="",
            other="",
        )

    def test_employee_update_form_valid(self):
        form_data = {
            "firstname": "Mo",
            "lastname": "Doe",
            "dateOfBirth": twenty_years_ago,
            "gender": "MALE",
            "city": "New York",
            "phone": "1234567890",
            "education": "",
            "experience": "",
            "awards": "",
            "hobbies": "",
            "skills": "FRONTEND",
            "references": "",
            "other": "",
        }
        form = EmployeeUpdateForm(data=form_data, instance=self.employee)
        self.assertTrue(form.is_valid())
        employee = form.save()
        self.assertTrue(Employee.objects.filter(firstname="Mo").exists())
        employee = Employee.objects.get(firstname="Mo")
        self.assertTrue(Employee_Cluster.objects.filter(employee=employee).exists())
        employee_cluster = Employee_Cluster.objects.get(employee=employee)
        self.assertEqual(employee_cluster.clusterable_text, "frontend")
