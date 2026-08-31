from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer, CompanyStatusUpdateSerializer, CompanyListQuerySerializer
from .messages import Messages, ErrorCodes
from .error_response import error_response
from .services import CompanyService, DuplicateTaxNumberError, CompanyNotFoundError


class CompanyListCreateView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CompanyService()

    def get_serializer(self, *args, **kwargs):
        return CompanySerializer(*args, **kwargs)

    def get(self, request):
        query_serializer = CompanyListQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        page = query_serializer.validated_data['page']
        size = query_serializer.validated_data['size']

        data = self.service.list_companies(page=page, size=size)
        serializer = CompanySerializer(data['results'], many=True)
        return Response({
            'total': data['total'],
            'page': data['page'],
            'size': data['size'],
            'results': serializer.data,
        })

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            company = self.service.create_company(
                title=serializer.validated_data['title'],
                tax_number=serializer.validated_data['tax_number'],
            )
        except DuplicateTaxNumberError as e:
            return error_response(
                ErrorCodes.DUPLICATE_TAX_NUMBER, str(e), status.HTTP_409_CONFLICT, field="tax_number"
            )
        result = CompanySerializer(company)
        return Response(result.data, status=status.HTTP_201_CREATED)


class CompanyDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CompanyService()

    def get_serializer(self, *args, **kwargs):
        return CompanySerializer(*args, **kwargs)

    def get(self, request, id):
        try:
            company = self.service.get_company(id)
        except CompanyNotFoundError as e:
            return error_response(ErrorCodes.COMPANY_NOT_FOUND, str(e), status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def patch(self, request, id):
        serializer = CompanyStatusUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            company = self.service.update_status(id, serializer.validated_data['status'])
        except CompanyNotFoundError as e:
            return error_response(ErrorCodes.COMPANY_NOT_FOUND, str(e), status.HTTP_404_NOT_FOUND)
        result = CompanySerializer(company)
        return Response(result.data)