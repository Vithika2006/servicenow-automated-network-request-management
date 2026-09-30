# Architecture

## Logical flow
1. User opens the Network Request catalog item.
2. Catalog variables collect request information.
3. Catalog UI Policies dynamically show and require conditional fields.
4. ServiceNow creates the standard Request/RITM records.
5. Flow Designer triggers from the submitted catalog request.
6. Flow retrieves catalog variables.
7. Flow creates the corresponding u_network_request operational record.
8. Approval routing determines the required approver(s).
9. Rejection stops fulfillment and notifies the requester.
10. Approval creates/updates fulfillment work for the network team.
11. Status and notifications are updated through the lifecycle.
12. Completion closes the operational request and leaves the standard request trail intact.

## Record responsibilities
| Record | Purpose |
|---|---|
| Request (sc_request) | Overall service request container |
| RITM (sc_req_item) | Catalog item transaction |
| Catalog Task (sc_task) | Fulfillment work |
| Approval (sysapproval_approver) | Approval decision and audit trail |
| Network Request (u_network_request) | Network-specific operational data |

Do not use a generic database table as a substitute for these concepts.

## State model
Submitted → Awaiting Approval → Approved → In Progress → Completed

Alternative terminal paths:
- Awaiting Approval → Rejected
- Submitted → Cancelled
- Approved → Cancelled
- In Progress → Cancelled

## Security boundary
Requester access is limited to their own requests. Approval access is based on approval assignment/group membership. Fulfillment access is based on the network fulfillment role/group.
