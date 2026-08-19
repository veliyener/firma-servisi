from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer
from .services import CompanyService, DuplicateTaxNumberError


class CompanyListCreateView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CompanyService()

    def get_serializer(self, *args, **kwargs):
        return CompanySerializer(*args, **kwargs)

    def get(self, request):
        companies = self.service.list_companies()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            company = self.service.create_company(
                title=serializer.validated_data['title'],
                tax_number=serializer.validated_data['tax_number'],
            )
        except DuplicateTaxNumberError as e:
            return Response({'tax_number': [str(e)]}, status=status.HTTP_409_CONFLICT)
        result = CompanySerializer(company)
        return Response(result.data, status=status.HTTP_201_CREATED)