from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
import pandas as pd
import datetime


credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

workspace_id = ""

time_range = datetime.timedelta(days=1)

query = """
AppRequests
| where TimeGenerated > ago(1d)
| project TimeGenerated, Name, Url, Success, ResultCode, DurationMs
"""

response = client.query_workspace(
    workspace_id=workspace_id,
    query=query,
    timespan=time_range,
)

if response.tables:
    table = response.tables[0]
    df = pd.DataFrame(table.rows, columns=table.columns)
    df.to_csv("failed_requests_report.csv", index=False)
    print("Report saved as failed_requests_report.csv")
else:
    print("No data found.")
