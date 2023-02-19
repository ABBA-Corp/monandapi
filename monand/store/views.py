from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from monand.customer.models import UserInfo
from .paginators import CustomPagination
from .serializers import *


class StandardPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page'
    max_page_size = 1000


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['$name_uz', '$name_uz', '$name_uz']
    filterset_fields = ["top", "category_id", "subcategory_id",]


class ProductByCategory(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        products = self.queryset.filter(category_id=id).all()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderByCustomerView(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        orders = self.queryset.filter(customer_id=id).all()
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class DetailsByOrderView(viewsets.ReadOnlyModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        details = self.queryset.filter(order_id=id).all()
        serializer = self.get_serializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderHistory(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        print(kwargs)
        user_id = kwargs['pk']
        history = []
        element = []
        orders = Order.objects.filter(customer_id=user_id)
        for order in orders:
            det = []
            dets = []
            details = OrderDetail.objects.filter(order_id=order.id).all()
            for d in details:
                det = {
                    "id": d.id,
                    "order": d.order.id,
                    "product": d.product.id,
                    "count": d.count
                }
                dets.append(det)
            element = {
                "id": order.id,
                "customer": order.customer.id,
                "date": order.date,
                "summa": order.summa,
                "details": dets,
            }
            history.append(element)
        # serializer = self.get_serializer(history, many=True)
        return Response({"history": history}, status=status.HTTP_200_OK)


class CardView(viewsets.ModelViewSet):
    queryset = CardObject.objects.all()
    serializer_class = CardObjectSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = request.GET['ui']
        product_id = kwargs['pk']
        cards = CardObject.objects.filter(customer_id=user_id, id=product_id).all()
        if len(cards) == 0:
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            for card in cards:
                card.delete()
            return Response({"status": "deleted"})


class CardByCustomer(viewsets.ReadOnlyModelViewSet):
    queryset = CardObject.objects.all()
    serializer_class = CardObjectSerializer

    def list(self, request, *args, **kwargs):
        jwt_object = JWTAuthentication()
        validated_token = jwt_object.get_validated_token(request.headers['token'])
        user = jwt_object.get_user(validated_token)
        user = User.objects.filter(id=user.id).first()
        objects = self.queryset.filter(customer_id=user.id).all()
        data = []
        for object in objects:
            dt = {
                "id": object.id,
                "count": object.count,
                "product": object.product.id,
                "name_uz": object.product.name_uz,
                "name_en": object.product.name_en,
                "name_ru": object.product.name_ru,
                "image": f"https://api-monand.abba.uz/files/{object.product.image}",
                "price": object.product.price
            }
            data.append(dt)
        return Response(data, status=status.HTTP_200_OK)


class LikeView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        data = request.data["likes"]
        if data:
            products = []
            for i in data:
                product = Product.objects.get(id=i)
                products.append(product)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"data": "not null required"})


class LikeByCustomer(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def list(self, request, *args, **kwargs):
        jwt_object = JWTAuthentication()
        validated_token = jwt_object.get_validated_token(request.headers['token'])
        user = jwt_object.get_user(validated_token)
        user = User.objects.filter(id=user.id).first()
        objects = self.queryset.filter(customer_id=user.id).all()
        serializer = self.get_serializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClearCard(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def retrieve(self, request, *args, **kwargs):
        customer_id = kwargs['pk']
        objects = CardObject.objects.filter(customer_id=customer_id).all()
        for object in objects:
            object.delete()
        return Response(status=status.HTTP_200_OK)


class AddOrder(viewsets.ReadOnlyModelViewSet):
    queryset = CardObject.objects.all()
    serializer_class = CardObjectSerializer

    def list(self, request, *args, **kwargs):
        jwt_object = JWTAuthentication()
        validated_token = jwt_object.get_validated_token(request.headers['token'])
        user = jwt_object.get_user(validated_token)
        user = User.objects.filter(id=user.id).first()
        # customer = Customer.objects.get(id=user_id)
        objects = CardObject.objects.filter(customer_id=user.id).all()
        order = Order.objects.create(customer=user, summa=0)
        order.save()
        summa = 0
        for card_object in objects:
            order_detail = OrderDetail.objects.create(order=order, product=card_object.product, count=card_object.count)
            order_detail.save()
            summa += card_object.product.price * card_object.count
        order.summa = summa
        order.save()
        CardObject.clear(customer_id=user.id)
        ord = Order.objects.filter(id=order.id).all()
        serializer = self.get_serializer(ord, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CardsUiView(viewsets.ModelViewSet):
    queryset = CardObject.objects.all()
    serializer_class = CardObjectSerializer

    def list(self, request, *args, **kwargs):
        jwt_object = JWTAuthentication()
        validated_token = jwt_object.get_validated_token(request.headers['token'])
        user = jwt_object.get_user(validated_token)
        user = User.objects.filter(id=user.id).first()
        try:
            userid = UserInfo.objects.filter(user_id=user.id).first()
            card = CardObject.objects.filter(u_id=userid.u_id)
            for cards in card:
                cards.condition = 'True'
                cards.save()
            return Response({'status': 'Success'}, status=status.HTTP_200_OK)
        except:
            pass
        return Response({'status': 'Error'}, status=status.HTTP_400_BAD_REQUEST)


class CardsUiPaymiView(viewsets.ModelViewSet):
    queryset = CardObject.objects.all()
    serializer_class = CardObjectSerializer

    def create(self, request, *args, **kwargs):
        result = ''
        try:
            result = request.data['result']
        except:
            pass
        if not result == '':
            userid = request.data['id']
            card = CardObject.objects.filter(u_id=userid)
            for cards in card:
                cards.condition = True
                cards.save()
            return Response({'status': 'Success'}, status=status.HTTP_200_OK)

        else:
            return Response({'status': 'Error'}, status=status.HTTP_400_BAD_REQUEST)


class CardDeleteView(viewsets.ModelViewSet):
    queryset = CardObject.objects.all()
    serializer_class = CardObjectSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.GET['ui']
        product_id = request.GET['car']
        cards = CardObject.objects.filter(customer_id=user_id, id=product_id).all()
        if len(cards) == 0:
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            for card in cards:
                card.delete()
            return Response({"status": "deleted"})
