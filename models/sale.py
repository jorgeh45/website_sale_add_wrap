from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    wrap = fields.Boolean(
        string=_('Gift wrap'),
    )


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _update_wrap(self, product_id, line_id, set_wrap, **kwargs):
        self.ensure_one()
        product_context = dict(self.env.context)
        product_context.setdefault('lang', self.sudo().partner_id.lang)
        SaleOrderLineSudo = self.env['sale.order.line'].sudo(
        ).with_context(product_context)
        order_line = None

        if line_id is not False:
            order_line = self._cart_find_product_line(
                product_id, line_id, **kwargs)[:1]
            if order_line:
                order_line.write({'wrap': set_wrap})
