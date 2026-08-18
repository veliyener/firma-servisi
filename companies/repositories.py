from .models import Company


class CompanyRepository:
    def get_all(self):
        return Company.objects.all()

    def create(self, title, tax_number):
        return Company.objects.create(title=title, tax_number=tax_number)