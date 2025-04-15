# Objective
Ensure minimal downtime and data loss in the event of outages, disasters, or system failures for an enterprise application hosted in **Microsoft Azure**.

---

## Key Metrics

| Metric                              | Definition                                                            |
|--------                             |------------                                                           |
| **RTO (Recovery Time Objective)**   | The maximum acceptable time to restore a service after a disruption.  |
| **RPO (Recovery Point Objective)**  | The maximum acceptable data loss measured in time.                    |

---

##  DR & Backup Strategy Components

### 1.  Automated Backups

- **Azure SQL Database**
  - Automated daily backups retained for up to **35 days** (configurable).
  - Long-term retention policies available for **monthly/yearly** backups.

- **Azure Blob Storage**
  - Enable **Soft Delete** to protect against accidental deletions.
  - Enable **Blob Versioning** to maintain historical versions.
  - Use **Azure Backup vaults** for scheduled backups.

- **Virtual Machines (VMs)**
  - Use **Azure Backup** to schedule **daily/weekly full and incremental** backups.

---

### 2.  Geo-Redundancy

- Replicate **databases** and **storage** to a **secondary region**.
- Helps protect against region-wide failures and supports disaster recovery operations.

---

### 3.  High Availability (HA)

- Use **Availability Zones** for mission-critical VMs.
- Use **Availability Sets** to distribute VMs across fault and update domains.
- Deploy **Application Gateway** with:
  - **Autoscaling**
  - **Web Application Firewall (WAF)** enabled.

---

### 4.  Failover Strategy

- Use **Azure Traffic Manager** or **Azure Front Door** to:
  - Automatically route traffic to a **backup region** during outages.
- Enable **Geo-Replication** for Azure SQL Databases.
- Use **Auto-Failover Groups** for seamless and automated database failover.

---

##  RTO & RPO Matrix

| Component                  | RTO           | RPO           |
|--------------------------  |---------------|---------------|
| Web App (App Service / VM) | < 30 minutes  | < 15 minutes  |
| SQL Database               | < 15 minutes  | < 5 minutes   |
| Blob Storage               | < 60 minutes  | < 15 minutes  |
| DNS + Traffic Manager      | < 10 minutes  | N/A           |
