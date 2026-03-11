/** @odoo-module **/
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class RatioDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({ ratio: 0, status: 'Analyzing...' });

        onWillStart(async () => {
            const data = await this.orm.searchRead("financial.ratio.analysis", [], ["liquidity_ratio"], { limit: 1 });
            if (data && data.length > 0) {
                this.state.ratio = parseFloat(data[0].liquidity_ratio).toFixed(2);
                this.state.status = this.state.ratio >= 1.5 ? "SOLVENT" : "LIQUIDITY RISK";
            } else {
                this.state.ratio = "0.00";
                this.state.status = "NO DATA";
            }
        });
    }
}
RatioDashboard.template = "account_financial_intelligence.RatioDashboard";
registry.category("public_components").add("ratio_dashboard", RatioDashboard);