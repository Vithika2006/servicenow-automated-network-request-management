# Catalog Item: Network Request

## Item
- Name: Network Request
- Category: Network
- Short description: Network Request Management

## Variables
| Name | Type | Required | Notes |
|---|---|---:|---|
| Requested For | Reference (User) | Yes | sys_user |
| Mobile Number | Single Line Text | Yes | Validate format |
| Type of Connection | Choice | Yes | New / Existing |
| Existing ID | Single Line Text | Conditional | Visible + mandatory for Existing |
| Total Amount | Decimal/Currency | Yes | Non-negative |
| Mode of Payment | Choice | Yes | UPI / CARD |
| Address | Multi-line Text | Yes | Network/customer location |
| Request Type | Choice | Yes | New Connection / Change / Access / Troubleshooting |
| Business Justification | Multi-line Text | Yes | Reason |
| Urgency | Choice | Yes | Low / Medium / High / Critical |
| Device Type | Choice | No | Optional |
| Please Specify | Single Line Text | Conditional | Mandatory when Device Type = Others |

## Reusable variable set: Network Request User Context
- Opened on behalf of — Reference → User
- Email ID — Single Line Text, derived from selected user email
- User Name — Single Line Text, derived from selected user name
- Phone Number — Single Line Text, derived from selected user phone

## Dynamic policies
### Existing connection
Condition: Type of Connection = Existing
- Existing ID visible = true
- Existing ID mandatory = true

Else:
- Existing ID visible = false
- Existing ID mandatory = false

### Other device
Condition: Device Type = Others
- Please Specify visible = true
- Please Specify mandatory = true

Prefer platform-supported auto-population/reference mechanisms before custom scripting.
