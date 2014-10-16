import collections
from django.conf.urls import patterns, url
from django.contrib import admin
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from yesho.utils import get_model_properties


class YeshoMixin(object):
    """
    A ModelAdmin extension for displaying on-demand detailed information

    Must be mixed with ModelAdmin
    """
    display_properties_button_label = "Display all properties of the model"

    on_demand_display_template = "yesho/on_demand_display.html"
    change_form_template = "yesho/change_form.html"

    excluded_properties = None
    show_only_to_superusers = True

    def get_urls(self):
        """
        Add the on demand display endpoint to the custom URL's
        """
        urls = super(YeshoMixin, self).get_urls()

        extra_urls = patterns('',
            url(r'^(.+)/properties/$',
                self.admin_site.admin_view(self.display_properties),
                name="%s_%s_properties" % (self.model._meta.app_label, self.model._meta.model_name)
        ))
        return extra_urls + urls

    def display_properties(self, request, pk):
        """
        Displays on-demand extra information for admins.
        """
        if not self.user_can_see_properties_of_the_model(request):
            raise Http404

        obj = self.get_object(request, pk)

        if self.excluded_properties is None:
            excluded_properties = []
        else:
            excluded_properties = list(self.excluded_properties)

        property_list = get_model_properties(self.model, excluded_properties)

        property_values = dict()
        for item in property_list:
            property_values[item] = getattr(obj, item)

        return render_to_response(self.on_demand_display_template, {
            "data": collections.OrderedDict(sorted(property_values.items())),
        }, context_instance=RequestContext(request))

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not extra_context:
            extra_context = dict()
        extra_context.update({
            "display_properties_button_label": self.display_properties_button_label,
            "user_can_see_properties_of_the_model": self.user_can_see_properties_of_the_model(request),
        })
        return super(YeshoMixin, self).change_view(request, object_id, form_url, extra_context)

    def user_can_see_properties_of_the_model(self, request):
        if not self.show_only_to_superusers:
            return True

        if request.user.is_superuser:
            return True
        return False


class YeshoAdmin(YeshoMixin, admin.ModelAdmin):
    """
    A simple implementation for ease of use.
    """
    pass