# Flow Designer

## Flow: Network Request
Trigger: Service Catalog submission for the Network Request item.

### Actions
1. Get Catalog Variables from the submitted RITM.
2. Create a u_network_request record and map typed values.
3. Set request status to Submitted, then Awaiting Approval.
4. Ask for Approval using dynamic manager/group routing.
5. If rejected: set Rejected, stop fulfillment, notify requester.
6. If approved: set Approved, create/update fulfillment work, assign the network fulfillment group.
7. Set In Progress when fulfillment begins.
8. Set Completed when fulfillment finishes and notify requester.

## Approval routing
- Standard: Requested For user's manager.
- Sensitive: manager followed by configured Network Security approval group.
- Department-specific: configured approval group where required.

Never hard-code a personal sys_id.

## State transitions
Submitted → Awaiting Approval / Cancelled
Awaiting Approval → Approved / Rejected / Cancelled
Approved → In Progress / Cancelled
In Progress → Completed / Cancelled
