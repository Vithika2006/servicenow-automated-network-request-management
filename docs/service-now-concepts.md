# ServiceNow Record Relationships

- **Request (REQ):** the overall service request created from a catalog submission.
- **Requested Item (RITM):** the catalog item instance under the Request; it contains the submitted catalog variables.
- **Catalog Task (SCTASK):** fulfillment work generated for a requested item.
- **Approval:** standard approval records, commonly represented through `sysapproval_approver`.
- **Network Request (`u_network_request`):** application-specific record created by Flow Designer to track network business state and fulfillment information.

The custom Network Request record should retain a reference to the originating RITM so the business record can be traced back to the submitted catalog request.

Use Flow Designer rather than legacy Workflow Editor for new automation unless a documented platform constraint requires otherwise.
