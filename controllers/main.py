# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):

    @http.route(['/shop/cart/update_wrap_json'], type='json',
                auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_wrap_json(self, product_id, line_id=None, set_wrap=None):
        """This route is called when changing the wrap of a product"""
        order = request.website.sale_get_order(force_create=1)
        if order.state != 'draft':
            request.website.sale_reset()
            return {}

        if set_wrap:
            order._update_wrap(product_id=product_id,
                               line_id=line_id, set_wrap=set_wrap)
        return {}
