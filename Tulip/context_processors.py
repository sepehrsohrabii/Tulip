from emailMarketing.forms import SubscriptionForm
from emailMarketing.models import Subscription
from frontend.models import Settings
from products.models import MainProduct, MainProduct2


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
    main_products2 = MainProduct2.objects.all()
    current_view, created = Settings.objects.get_or_create(is_active=True)
    current_view.view_count += 1
    current_view.save()
    context = {
        'subscription_form': subscription_form,
        'main_products': main_products,
        'main_products2': main_products2,
        'current_view': current_view
    }
    return context
