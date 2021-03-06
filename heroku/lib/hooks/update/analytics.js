"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const analytics_1 = require("../../analytics");
exports.analytics = async function () {
    const analytics = new analytics_1.default(this.config);
    await analytics.submit();
};
