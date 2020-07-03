from django.shortcuts import render, redirect
from products import models, forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages


class ProtectedTemplateView(UserPassesTestMixin, TemplateView):
    def test_func(self):
        return self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


def index(request):
    return render(request, 'products/homepage.html')

def some_crap(request):
    return render(request, 'products/logo_click.html')

class ProductCreate(CreateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('all_products')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('all_products')


class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'products/product_by_id.html'


class ProductsListView(ListView):
    model = models.Product
    queryset = models.Product.objects.all()
    ordering = '-name'


    def post(self, request, *args, **kwargs):
        user = self.request.user
        product_id = request.POST.get('product_id')
        product = models.Product.objects.get(id=product_id)
        quantity = int(request.POST.get('quantity'))
        cost = round(quantity * product.price, 2)
        if product.quantity < quantity:
            messages.error(request, 'In stock not enough goods')
        elif user.wallet < cost:
            messages.error(request, 'You have not enough money!')
        else:
            user.wallet = round(user.wallet - cost, 2)
            product.quantity -= quantity
            purchase = models.Purchase(user=user, product=product, quantity=quantity, cost=cost)
            user.save()
            product.save()
            purchase.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PurchaseListView(ListView):
    model = models.Purchase
    queryset = models.Purchase.objects.filter(is_deleted=False)
    ordering = '-created_at'

    def post(self, request, *args, **kwargs):
        # user = self.request.user
        purchase_id = request.POST.get('purchase_id')
        purchase = models.Purchase.objects.get(id=purchase_id)
        if purchase.status == 1:
            purchase.status = purchase.IN_PROCESSING
            cancel = models.Return(purchase=purchase)
            cancel.save()
            purchase.save()
        elif purchase.status == 5:
            messages.error(request, 'Time is up! Cancellation is not possible!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ReturnListView(ListView):
    model = models.Return
    queryset = models.Return.objects.filter(is_deleted=False)
    ordering = '-created_at'

    def post(self, request, *args, **kwargs):
        cancel_id = request.POST.get('return_id')
        cancel = models.Return.objects.get(id=cancel_id)
        action = request.POST.get('action')
        if action == 'Approve':
            cancel.status = cancel.APPROVED
            cancel.purchase.user.wallet += cancel.purchase.cost
            cancel.purchase.product.quantity += cancel.purchase.quantity
            cancel.purchase.status = cancel.purchase.APPROVED
            cancel.purchase.is_deleted = True
            cancel.purchase.user.save()
            cancel.purchase.product.save()
            cancel.purchase.save()
        elif action == 'Decline':
            cancel.purchase.status = cancel.purchase.DECLINED
            cancel.purchase.save()
            cancel.status = cancel.DECLINED
        cancel.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))







# def cancel_return(request, purchase_id):
#     model = models.Return.objects.get(purchase_id=purchase_id)
#     model.cancelled = True
#     model.save()
#     return render(request, 'products/return_is_cancelled.html')
#
#
# def approve_return(request, purchase_id):
#     model = models.Return.objects.get(purchase_id=purchase_id)
#     model.approved = True
#     model.save()
#     return render(request, 'products/return_is_approved.html')

