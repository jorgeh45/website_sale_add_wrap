odoo.define('website_sale.cart', function (require) {
    "use strict";
    var ProductConfiguratorMixin = require('sale.ProductConfiguratorMixin');
    var sAnimations = require('website.content.snippets.animation');

    sAnimations.registry.WebsiteSaleCustomizeCart = sAnimations.Class.extend(ProductConfiguratorMixin, {
        selector: '.oe_website_sale',
        read_events: {
            'change .js_wrap': '_onChangeIsGift',
        },
        init: function () {
            this._super.apply(this, arguments);
        },

        _onChangeIsGift:function (ev){
            let $input = $(ev.currentTarget);          
            let value =  $('input[name="wrap"]:checked').length > 0
            let line_id = parseInt($input.data('line-id'), 10);
            let product_id = parseInt($input.data('product-id'), 10);
            this._changeIsGift(value, line_id, product_id);
        },_changeIsGift: function(value, line_id, product_id){

            this._rpc({
                route: "/shop/cart/update_wrap_json",
                params: {
                    line_id: line_id,
                    product_id: product_id,
                    set_wrap: value
                },
            });
            
        }
        
        });
});