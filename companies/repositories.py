from .models import Company


class CompanyRepository:
    def get_all(self):
        return Company.objects.all()

    def exists_by_tax_number(self, tax_number: str) -> bool:
        return Company.objects.filter(tax_number=tax_number).exists()

    def create(self, title: str, tax_number: str):
        return Company.objects.create(title=title, tax_number=tax_number)