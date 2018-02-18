from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from productos.models import Producto, LogBuy
import stripe
from django.conf import settings


class HomeView(TemplateView):
    template_name = 'products/home.html'

    def get_context_data(self, **kwargs):
        products = Producto.objects.all()
        return {'products': products}


class ProductBuyView(DetailView):
    model = Producto
    template_name = 'products/buy.html'

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST['stripeToken']
        product = self.get_object()
        error_message = None
        try:
            charge = stripe.Charge.create(
                amount=product.precio,
                currency='usd',
                description='cobro por []'.format(product.nombre),
                statement_descriptor="cobro a mi marketDigital",
                source=token
            )
        except stripe.error.CardError as e:
            body = e.json_body
            err = body['error']
            error_message = err['message']
        except stripe.error.StripeError as e:
            error_message = "No puede proceder tu compra, intentelo luego"

        if error_message:
            return render(request, "products/failed.html", {'error_message': error_message, 'producto': product})

        buyer = None
        if request.user.is_authenticated:
            buyer = request.user
        LogBuy.objects.create(product=product, user=buyer)

        return render(request, "products/success.html", {'debug_info': charge, 'producto': product})
