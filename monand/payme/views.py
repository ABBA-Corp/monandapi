import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from monand.store.models import Order
from paymeuz.serializers import SubscribeSerializer
from paymeuz.config import *
from paymeuz.methods import *
from paymeuz.models import Transaction

from .models import Payment
from .serializer import PaymentSerializer

AUTHORIZATION1 = {'X-Auth': AUTHORIZATION['X-Auth'].split(':')[0]}


class CardCreateApiView(APIView):

    def post(self, request):
        serializer = SubscribeSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        result = self.card_create(serializer.validated_data)

        return Response(result)

    def card_create(self, validated_data):
        data = dict(
            id=validated_data['id'],
            method=CARD_CREATE,
            params=dict(
                card=dict(
                    number=validated_data['params']['card']['number'],
                    expire=validated_data['params']['card']['expire'],
                    save=validated_data['params']['save']
                )
            )
        )
        print(AUTHORIZATION)
        response = requests.post(URL, json=data, headers=AUTHORIZATION1)
        result = response.json()
        print(result)
        if 'error' in result:
            return result

        token = result['result']['card']['token']
        result = self.card_get_verify_code(token)

        return result

    def card_get_verify_code(self, token):
        data = dict(
            method=CARD_GET_VERIFY_CODE,
            params=dict(
                token=token
            )
        )
        response = requests.post(URL, json=data, headers=AUTHORIZATION1)
        result = response.json()
        if 'error' in result:
            return result

        result.update(token=token)
        return result


class CardVerifyApiView(APIView):

    def post(self, request):
        serializer = SubscribeSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        result = self.card_verify(serializer.validated_data)

        return Response(result)

    def card_verify(self, validated_data):
        data = dict(
            id=validated_data['id'],
            method=CARD_VERIFY,
            params=dict(
                token=validated_data['params']['token'],
                code=validated_data['params']['code'],
            )
        )
        response = requests.post(URL, json=data, headers=AUTHORIZATION1)
        result = response.json()

        return result


class PaymentApiView(APIView):

    def post(self, request, format=None):
        serializer = SubscribeSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['params']['token']
        result = self.receipts_create(token, serializer.validated_data)
        print('Params')
        return Response(result)

    def receipts_create(self, token, validated_data):
        order_id=validated_data['params']['account']['order_id']
        key_2 = validated_data['params']['account'][KEY_2] if KEY_2 else None
        data = dict(
            id=validated_data['id'],
            method=RECEIPTS_CREATE,
            params=dict(
                amount=10000,
                account=dict(
                    order_id=validated_data['params']['account']['order_id']
                )
            )
        )
        response = requests.post(URL, json=data, headers=AUTHORIZATION)
        result = response.json()
        if 'error' in result:
            return result

        trans_id = result['result']['receipt']['_id']
        trans = Transaction()
        trans.create_transaction(
            trans_id=trans_id,
            request_id=result['id'],
            amount=result['result']['receipt']['amount'],
            account=result['result']['receipt']['account'],
            status=trans.PROCESS,
        )
        result = self.receipts_pay(trans_id, token, order_id)
        return result

    def receipts_pay(self, trans_id, token, order_id):
        data = dict(
            method=RECEIPTS_PAY,
            params=dict(
                id=trans_id,
                token=token,
            )
        )
        response = requests.post(URL, json=data, headers=AUTHORIZATION)
        result = response.json()
        trans = Transaction()

        if 'error' in result:
            trans.update_transaction(
                trans_id=trans_id,
                status=trans.FAILED,
            )
            return result

        trans.update_transaction(
            trans_id=result['result']['receipt']['_id'],
            status=trans.PAID,
        )

        if not 'error' in result:
            dit = {"message":'ok'}
            order = Order.objects.get(id=order_id)
            order.status = "confirmed"
            print(order.id)
            order.save()
            data = json.dumps(dit)
            return result
        return result