from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    name = models.CharField(_('name'), max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                             null=True, blank=True, related_name='children')
    menu_name = models.CharField(_('menu name'), max_length=100,
                               help_text=_('Название меню, к которому принаджележит пункт'))
    url = models.CharField(_('url'), max_length=255, blank=True,
                         help_text=_('URL or named URL pattern'))
    named_url = models.CharField(_('named url'), max_length=100, blank=True,
                               help_text=_('Named URL pattern'))
    order = models.PositiveIntegerField(_('order'), default=0)
    is_expanded = models.BooleanField(default=False, editable=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.named_url
        return self.url or '#'

    def toggle_expanded(self):
        self.is_expanded = not self.is_expanded
        self.save()