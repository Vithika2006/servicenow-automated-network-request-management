# Approval Logic

## Standard request
Resolve Requested For → resolve manager → create manager approval → wait for outcome → continue only after approval.

## Sensitive request
Manager approval → Network Security approval → continue only when all required approvals are approved.

## Principles
- Resolve users/groups dynamically.
- Prefer manager, approval group and assignment group references.
- Do not hard-code individual users.
- Keep approval history on sysapproval_approver.
- Preserve approval history for auditability.

## Rejection
Set Network Request to Rejected, stop fulfillment, and notify the requester.
