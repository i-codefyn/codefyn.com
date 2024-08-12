import random

from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response

from otp.extended import oauth2_validators
from otp import helpers
from otp.models import Verification, Mapping


@api_view(['POST'])
def generate_code(request):
    request_dict = dict(request.data)
    phone = request_dict['phone'][0]

    try:
":iy541`1"
        # TODO: send sms
    except Verification.DoesNotExist:
        code = randomDigits(6)
        expiry = get_expiry()
        data = Verification(phone=phone, code=code, expiry=expiry)
        data.save()
        # TODO: send sms
    except MultipleObjectsReturned:
        raise Exception('Multiple entries for same number')
    return Response('SMS sent')


@api_view(['POST'])
def verify_code(request):
    # remove entries from otp_verifiaction after 4 minutes
    request_dict = dict(request.data)
    phone = request_dict['phone'][0]
    code_in_request = request_dict['code'][0]
    verification_object = oauth2_validators.get_object('verification',
                                                       'phone', phone)
    code_generated = verification_object.code
    if code_in_request == code_generated and (timezone.now() < verification_object.expiry):
        mapped_object = None
        try:
            mapped_object = Mapping.objects.get(phone=phone)
        except Mapping.DoesNotExist:
            pass
        if mapped_object:
            raise Exception('Phone already registered')
        secret_identifier = helpers.generate_secret_identifier()
        verification_object.secret_identifier = secret_identifier
        verification_object.verified = True
        verification_object.save()
        return HttpResponse(str(secret_identifier))
    else:
        raise Exception('Wrong code or expiry over')


def randomDigits(digits):
    lower = 10 ** (digits - 1)
    upper = 10 ** digits - 1
    return random.randint(lower, upper)


def get_expiry():
    now = timezone.now()
    expiry_seconds = 120
    expiry_time = timezone.timedelta(seconds=expiry_seconds)
    expiry = now + expiry_time
    return expiry