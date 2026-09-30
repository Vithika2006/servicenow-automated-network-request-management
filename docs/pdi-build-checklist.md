# ServiceNow PDI Build Checklist

Build in this order:

1. Create/verify application scope for Network Request Management.
2. Create custom table `u_network_request`.
3. Configure Network Request number with `NET` prefix.
4. Add reference, choice, numeric, address, status, approval, assignment and RITM fields.
5. Create the **Network Request** catalog item in the Network category.
6. Add catalog variables from `servicenow/catalog/variables.json`.
7. Attach the reusable user-details variable set.
8. Configure the Existing Connection UI Policy.
9. Add the minimal requester auto-population Catalog Client Script.
10. Create the `Network Request` Flow Designer flow.
11. Map RITM/catalog variables to the custom record.
12. Route manager approval using the requested user's manager; add Network Security approval for sensitive request types.
13. Create/update fulfillment tasks for the network fulfillment group.
14. Configure the six notification events/templates.
15. Configure roles and ACLs using the security matrix.
16. Create reports listed in `servicenow/reporting.json`.
17. Execute every test in `servicenow/tests/test-cases.md`.
18. Review Flow Execution Details, System Logs, Email Logs, approval records and audit history.

> Do not invent sys_ids. Capture real sys_ids only after the PDI records are created.
