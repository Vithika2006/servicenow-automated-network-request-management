# Automated Network Request Management in ServiceNow

An enterprise-style ServiceNow solution for capturing, approving, fulfilling, tracking, and reporting network service requests.

## Solution lifecycle
End User → Service Catalog → Network Request → RITM → Flow Designer → Network Request Record → Approval → Fulfillment → Notifications → Closure

## Repository structure
- docs/architecture.md
- docs/catalog-item.md
- docs/flow-designer.md
- docs/approvals.md
- docs/security.md
- docs/testing.md
- docs/deployment.md
- docs/troubleshooting.md
- docs/demo.md
- docs/future-enhancements.md
- servicenow/catalog/network-request.yaml
- servicenow/data-model/network-request.yaml
- servicenow/flow/network-request.yaml
- servicenow/security/security.yaml
- servicenow/catalog/client-scripts/populate-requester.js

## Important implementation note
This repository is the source-controlled design/configuration package. ServiceNow platform records such as catalog items, flows, ACLs, notifications and roles must be created/imported in a ServiceNow instance (PDI) and runtime-tested there. The repository does not claim PDI execution that cannot be verified from GitHub.

## Core statuses
Submitted, Awaiting Approval, Approved, Rejected, In Progress, Completed, Cancelled

## Design principles
- Prefer standard ServiceNow Request/RITM/approval capabilities.
- Keep the custom u_network_request record focused on network-specific operational data.
- Prefer Flow Designer and Catalog configuration over unnecessary Business Rules.
- Avoid hard-coded user/sys_id values.
- Use reference and choice fields where appropriate.
- Enforce least privilege.
