
odoo.define("clinic_management.sample", function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var AbstractAction = require('web.AbstractAction');
    var Dialog = require('web.Dialog');
    var _t = core._t;
    var QWeb = core.qweb;

    


    var Dashboard = AbstractAction.extend({
        contentTemplate: 'clinic_management.DashboardMain',
        events: {
            'click .patient_id_class': 'onHoverPatient',
        },
        
        
        init: function (parent, action, options) {
            action.name = action.name || 'Dashboard';
            this._super.apply(this, arguments);
            this.context = action.context;
            this.params = Object.assign({}, action.params);
            this.fetchData()
            // this.fetchVisitData()
            this.greeting()

        },

        fetchVisitData: function () {
            return this._rpc({ route: '/visit' }).then(result => {
                var self = this;
                this.visit_data = result;
                var visit_div = this.$('.visit_datas');
                visit_div.empty();
                // div.empty();
                // div.append(QWeb.render('clinic_management.visit_datas', { widget: self }));
                visit_div.append(QWeb.render('clinic_management.record_visit', { widget: self }));
            });
        },

        fetchData: function () {
            return this._rpc({ route: '/patient' }).then(result => {
                var self = this;
                this.data = result;
                console.log(this.data);
                var div = this.$('.clinic_data');
                div.empty();
                this.fetchVisitData();
                div.append(QWeb.render('clinic_management.header', { widget: self }));
                div.append(QWeb.render('clinic_management.content', { widget: self }));
                div.append(QWeb.render('clinic_management.visit_data_sample', { widget: self }));

            });
        },
        greeting: function () {
            var hr = new Date().getHours();
            var self = this;
            var daypart = hr > 19 ? 'night'
                : hr > 15 ? 'evening'
                    : hr > 11 ? 'afternoon'
                        : 'morning';
            console.log(`Good ${daypart},Nisarg`)   
            return `Good ${daypart}, Nisarg`;
        },
        
        // event 1
        onHoverPatient: function (obj) {
            var self = this;
            // var id = obj.target;
            var id = obj.target.getAttribute('p-id');
            var j = parseInt(id);
            console.log(j);

            this.do_action({
                type: 'ir.actions.act_window',
                res_model: 'aspl.patient',
                res_id: j,
                views: [[false, 'form']],
                target: 'current',
            });
        },
    
    });
        
    core.action_registry.add('clinic_dashboard', Dashboard);
    return Dashboard;
});