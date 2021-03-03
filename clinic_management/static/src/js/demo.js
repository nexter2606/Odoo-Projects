odoo.oepetstore = function(instance, local) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;
    var core = require('web.core');


    local.HomePage = instance.Widget.extend({
        start: function() {
            var products = new local.ProductsWidget(
                this, ["cpu", "mouse", "keyboard", "graphic card", "screen"], "#00FF00");
            products.appendTo(this.$el);
        },
    });

    local.ProductsWidget = instance.Widget.extend({
        template: "ProductsWidget",
        init: function(parent, products, color) {
            this._super(parent);
            this.products = products;
            this.color = color;
        },
    });

    instance.web.client_actions.add(
        'petstore.homepage', 'instance.oepetstore.HomePage');
    core.action_registry.add('petstore.homepage', local.HomePage);

}