from emailMarketing.forms import SubscriptionForm
from emailMarketing.models import Subscription
from products.models import MainProduct


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
    main_products = MainProduct.objects.all()
    context = {
        'subscription_form': subscription_form,
        'main_products': main_products,
    }
    return context
