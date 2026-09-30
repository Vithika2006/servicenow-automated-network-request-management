# Security

## Roles
- network_requester
- network_approver
- network_fulfiller
- network_admin

Reuse equivalent existing application roles if the target instance already provides them.

## Access model
| Actor | Read | Write | Scope |
|---|---|---|---|
| Requester | Yes | Limited | Own requests |
| Approver | Yes | Approval decision | Requests requiring their approval |
| Fulfiller | Yes | Yes | Assigned/network work |
| Admin | Yes | Yes | Application administration |

## ACL guidance
- Table read/write ACLs require appropriate roles.
- Requester record access should verify ownership where appropriate.
- Sensitive fields require additional protection.
- Do not use unrestricted allow-all ACLs for testing convenience.
- Validate with impersonation in a PDI.

Do not store passwords, tokens, card data or other secrets in this solution.
