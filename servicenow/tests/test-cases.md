# Network Request Test Cases

| ID | Scenario | Expected result |
|---|---|---|
| NR-01 | Standard new connection | RITM and Network Request record created; approval requested; fulfillment starts only after approval. |
| NR-02 | Existing connection | Existing ID becomes visible and mandatory. |
| NR-03 | New connection | Existing ID remains hidden and non-mandatory. |
| NR-04 | Rejection | Network Request becomes Rejected; requester is notified; fulfillment does not continue. |
| NR-05 | Approval | Approval status becomes Approved; fulfillment starts and status becomes In Progress. |
| NR-06 | Invalid data | Submission is blocked with clear validation feedback. |
| NR-07 | Requester security | Requester can access their own requests but not another user's sensitive request data. |
| NR-08 | Approver security | Approver can act on approvals assigned to them. |
| NR-09 | Fulfiller security | Fulfiller can update assigned work but cannot change approval decisions. |
| NR-10 | Completion | Request status becomes Completed and completion notification is sent. |

## Runtime validation
These cases must be executed in a ServiceNow PDI. Repository validation alone cannot prove runtime behavior.
