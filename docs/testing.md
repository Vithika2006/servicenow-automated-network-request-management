# Test Plan

## PDI test matrix
| ID | Scenario | Expected |
|---|---|---|
| NR-01 | Standard request | RITM/network record created; approval requested |
| NR-02 | Existing connection | Existing ID visible and mandatory |
| NR-03 | New connection | Existing ID hidden/not mandatory |
| NR-04 | Device Type = Others | Please Specify visible and mandatory |
| NR-05 | Invalid data | Submission blocked |
| NR-06 | Approval | Fulfillment continues |
| NR-07 | Rejection | Status Rejected; fulfillment stops; requester notified |
| NR-08 | Security | Requester cannot access unrelated requests |
| NR-09 | Fulfiller | Fulfiller can work assigned requests |
| NR-10 | Completion | Completed status and notification |
| NR-11 | Audit | Approval/status history traceable |
| NR-12 | Notification | Correct recipients receive relevant messages |

## Evidence
Use Flow Designer Execution Details, approval records, email logs, audit history and request records. Runtime cases are not considered passed until executed in the PDI.
