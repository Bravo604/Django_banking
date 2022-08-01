from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО Клиента')
    citizenship = models.CharField(max_length=20, verbose_name='Гражданство', default='Кыргызстан')
    birth_year = models.DateField()
    work_place = models.CharField(max_length=30, blank=True)
    update_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'

    def __str__(self):
        return f'{self.name} - {self.citizenship} - {self.birth_year} - {self.work_place} - {self.update_date}'


class Account(models.Model):
    number = models.CharField(max_length=16, verbose_name='Номер счета', primary_key=True)
    account_type = models.IntegerField(verbose_name='Тип счета', default=1)
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        db_table = 'accounts'

    def __str__(self):
        return f'{self.number} - {self.account_type} - {self.client}'


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сума')
    date = models.DateField(auto_now_add=True)
    account = models.ForeignKey(Account, verbose_name='счет', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'
        db_table = 'loans'

    def __str__(self):
        return f'{self.sum} - {self.date} - {self.account}'
