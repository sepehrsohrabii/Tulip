from emailMarketing.forms import SubscriptionForm
from emailMarketing.models import Subscription


def global_parameters(request):
    subscription_form = SubscriptionForm(
        request.POST, auto_id=True)
    subscription = []
    if subscription_form.is_valid():
        subscription_save = Subscription()
        subscription_form = SubscriptionForm(
            request.POST, instance=subscription_save, auto_id=True)
        subscription = subscription_form.save(commit=False)
        subscription.save()
    context = {
        'subscription_form': subscription_form,
    }
    return context
