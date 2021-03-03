
odoo.define("clinic_management.appointment", function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var AbstractAction = require('web.AbstractAction');
    var Dialog = require('web.Dialog');
    var _t = core._t;
    var QWeb = core.qweb;

    var Appointment = AbstractAction.extend({
        contentTemplate: 'clinic_management.MainAppointment',
        events: {
            'click .patient_id': 'AppointmentIDChange',
            'click .patient_name': 'AppointmentNameChange',
        },
        
        init: function (parent, action, options) {
            action.name = action.name || 'Appointment';
            this._super.apply(this, arguments);
            this.context = action.context;
            this.params = Object.assign({}, action.params);
            this.fetchData()
            this.AppointmentGreeting()

        },

        fetchData: function () {
            return this._rpc({ route: '/appointment' }).then(result => {
                var self = this;
                this.app_data = result;
                var div = this.$('.appointment_data');
                // console.log(this.app_data);
                div.empty();
                div.append(QWeb.render('clinic_management.appointment_header', { widget: self }));
                div.append(QWeb.render('clinic_management.appointment_content', { widget: self }));
            });
        },

        AppointmentIDChange: function (obj) {
            var self = this;
            var id = obj.target.getAttribute('patient-id');
            // console.log(id);
            // console.log(typeof(id));
            var x = parseInt(id);
            // console.log(x);
            // console.log(typeof(x));
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: 'aspl.appointment',
                res_id: x,
                views: [[false, 'form']],
                target: 'current',
            });
        },

        AppointmentNameChange: function (obj) {
            var self = this;
            var id = obj.target.getAttribute('patient-record-id');
            console.log(id);
            var y = parseInt(id);
            console.log(y);
            console.log(typeof(y));
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: 'aspl.patient',
                res_id: y,
                views: [[false, 'form']],
                target: 'current',
            });
        },

        AppointmentGreeting: function () {
            var hr = new Date().getHours();
            var self = this;
            var daypart = hr > 19 ? 'night'
                : hr > 15 ? 'evening'
                    : hr > 11 ? 'afternoon'
                        : 'morning';
            return `Good ${daypart}, Nisarg`;
        },

    });

    core.action_registry.add('main_appointment', Appointment);
    return Appointment;
});



// AppointmentNameChange: function (obj) {
//     var self = this;
//     var id = obj.target.getAttribute('patient-record-id');
//     console.log(id);
//     var y = parseInt(id);
//     console.log(y);
//     console.log(typeof(y));
//     this.do_action({
//         type: 'ir.actions.act_window',
//         res_model: 'aspl.patient',
//         res_id: y,
//         views: [[false, 'form']],
//         target: 'current',
//     });
// },