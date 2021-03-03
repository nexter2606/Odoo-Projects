
odoo.define("clinic_management.visit", function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var AbstractAction = require('web.AbstractAction');
    var Dialog = require('web.Dialog');
    var _t = core._t;
    var QWeb = core.qweb;

    


    var Visit = AbstractAction.extend({
        contentTemplate: 'clinic_management.visit_data',
        
        init: function (parent, action, options) {
            action.name = action.name || 'Visit';
            this._super.apply(this, arguments);
            this.context = action.context;
            this.params = Object.assign({}, action.params);
            this.fetcVisithData()

        },

        fetcVisithData: function () {
            return this._rpc({ route: '/visit' }).then(result => {
                var self = this;
                this.data = result;
                console.log(this.data)
                console.log(typeof(this.data))
                var div = this.$('.visit');
                div.empty();
                div.append(QWeb.render('clinic_management.visit_data', { widget: self }));
                div.append(QWeb.render('clinic_management.visit_datas', { widget: self }));
            });
        },
        
    });
        
    core.action_registry.add('visit', Visit);
    return Visit;
});