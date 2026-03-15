/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class NexusDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({ total: 0, online: 0 });

        onWillStart(async () => {
            const data = await this.orm.searchRead("nexus.endpoint", [], ["status"]);
            this.state.total = data.length;
            this.state.online = data.filter(d => d.status === 'online').length;
        });
    }
}
NexusDashboard.template = "boss_nexus.DashboardTemplate";
registry.category("actions").add("boss_nexus.dashboard", NexusDashboard);