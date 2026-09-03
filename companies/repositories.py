from typing import Optional
from .models import Company


class CompanyRepository:
    def get_all(self):
        return Company.objects.all()

    def get_page(self, page: int, size: int):
        offset = (page - 1) * size
        return Company.objects.all()[offset:offset + size]

    def count_all(self) -> int:
        return Company.objects.count()

    def get_by_id(self, company_id: str) -> Optional[Company]:
        return Company.objects.filter(id=company_id).first()

    def exists_by_tax_number(self, tax_number: str) -> bool:
        return Company.objects.filter(tax_number=tax_number).exists()

    def create(self, title: str, tax_number: str) -> Company:
        return Company.objects.create(title=title, tax_number=tax_number)

    def update_status(self, company: Company, status: str) -> Company:
        company.status = status
        company.save()
        return company