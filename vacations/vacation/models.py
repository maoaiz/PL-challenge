from django.db import models


class Vacation(models.Model):

    user = models.ForeignKey('account.User', related_name="employee", on_delete=models.CASCADE)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    is_approved = models.BooleanField(default=False)
    approved_date = models.DateTimeField(null=True, blank=True)
    approver = models.ForeignKey(
        'account.User', related_name="manager", on_delete=models.CASCADE, null=True, blank=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " -- " + self.user.username
