from credit.models import Client, Account, Credit
from django.utils import timezone
from random import randint


def acc_numb():
    numbers = []
    for i in range(16):
        numbers.append(randint(0, 10))
    return "".join(map(str, numbers))


client1 = Client(name="Berdiev N.D.", birth_year="1994-07-31", work_place='Codify')
client1.save()
client2 = Client(name="Popov T.V.", birth_year="1983-05-16", work_place='Ksuppro')
client2.save()

account1 = Account(number=acc_numb(), client=client1)
account1.save()
account2 = Account(number=acc_numb(), client=client1)
account2.save()
account3 = Account(number=acc_numb(), client=client2)
account3.save()
account4 = Account(number=acc_numb(), client=client2)
account4.save()


credit1 = Credit(sum=40000, account=account1)
credit1.save()
credit2 = Credit(sum=50000, account=account2)
credit2.save()
credit3 = Credit(sum=40000, account=account3)
credit3.save()
credit4 = Credit(sum=40000, account=account4)
credit4.save()
client2.account_set.create(name="Nasirov N.D.", birth_year="1976-07-31")
