/** @odoo-module **/
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class KpiCard extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({ value: 0 });
        onWillStart(async () => {
            try {
                const res = await this.orm.readGroup("analytics.data.cube", [], ["total_revenue:sum"], []);
                this.state.value = (res && res[0]) ? (res[0].total_revenue || 0) : 0;
            } catch (e) {
                this.state.value = 0;
            }
        });
    }
}
KpiCard.template = "advanced_data_analytics.KpiCard";

// Register here so the <Component T="..."> tag can find it
registry.category("public_components").add("analytics_kpi", KpiCard);