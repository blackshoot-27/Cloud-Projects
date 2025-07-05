PostgreSQL Migration: EC2 to Amazon RDS using AWS DMS and Same can done using On Prem postgres too
This project demonstrates migrating a PostgreSQL database from an Amazon EC2 instance to Amazon RDS PostgreSQL using AWS Database Migration Service (DMS). The setup ensures secure communication within a VPC and includes validation for data consistency.

+-------------------+         +-------------------------+         +----------------------+
|                   |         |                         |         |                      |
|   EC2 Instance    +--------->  AWS DMS Replication     +--------->    RDS PostgreSQL    |
| (Source DB: Postgres) |      |     Instance             |         |  (Target DB)         |
|                   |         |                         |         |                      |
+-------------------+         +-------------------------+         +----------------------+

              Private Subnet / VPC                              Private or Public Subnet
              Security Group open for                           Security Group open for
              DMS instance                                      DMS instance




🛠 AWS Services Used
EC2 (Elastic Compute Cloud): Hosted the source PostgreSQL database.

RDS (Relational Database Service): Target PostgreSQL database.

AWS DMS (Database Migration Service): Orchestrated schema and data migration.

VPC (Virtual Private Cloud): Isolated networking environment for secure communication.

Security Groups: Controlled access between EC2, DMS, and RDS.

IAM (Identity and Access Management): Managed permissions for DMS.

CloudWatch: Monitored logs and performance metrics.

🖇 Architecture

🚀 Steps to Perform Migration
Prepare Source DB (EC2 PostgreSQL):

Set a password for postgres user.

Edit postgresql.conf to allow connections on all IPs:

ini
Copy
Edit
listen_addresses = '*'
Edit pg_hba.conf to allow connections from DMS replication instance:

css
Copy
Edit
host    all    all    <DMS-Private-IP>/32    md5
Restart PostgreSQL.

Launch RDS PostgreSQL:

Enable "Publicly Accessible" if needed.

Configure Security Groups to allow port 5432.

Create DMS Replication Instance:

Place it in the same VPC as EC2 and RDS.

Assign IAM role with proper permissions.

Configure DMS Endpoints:

Source Endpoint: EC2 PostgreSQL private IP.

Target Endpoint: RDS PostgreSQL endpoint.

Run Migration Task:

Choose "Full Load + CDC" for ongoing replication.

Enable data validation for consistency check.

Monitor using CloudWatch Logs.

🛑 Challenges Faced
🔒 PostgreSQL pg_hba.conf errors:

“no pg_hba.conf entry for host …”

Fixed by adding DMS replication instance IP to pg_hba.conf.

🌐 Connectivity Issues:

Security Groups did not initially allow DMS → EC2/RDS traffic.

Added correct inbound rules for port 5432.

🔑 SSL Requirement:

RDS forced SSL connections (rds.force_ssl=1).

Enabled SSL mode in DMS endpoints to resolve.

✅ Best Practices
Use private IPs and keep DMS within the same VPC for better security and performance.

Validate data post-migration using DMS validation feature.

Always enable CloudWatch logging to troubleshoot migration issues.

Restrict Security Groups to specific IPs rather than 0.0.0.0/0.

📄 Things to Take Care Of
✔ Ensure pg_hba.conf is properly configured for DMS connections.
✔ Check if your RDS requires SSL connections (rds.force_ssl=1).
✔ Avoid using public IPs for source/target unless absolutely necessary.
✔ Allocate sufficient storage in RDS to handle full data load.

📌 Outcome
✅ Successfully migrated PostgreSQL data from EC2 to RDS with validation.
✅ Achieved secure and scalable architecture using AWS managed services.

![RDS](https://github.com/user-attachments/assets/05cc9986-b20a-492d-9faa-6911c377b109)



Replication Instance

![dms instance](https://github.com/user-attachments/assets/d8149285-7c06-4c1f-84f8-02724501205d)


Endpoints Created for DMS:

![enpoints](https://github.com/user-attachments/assets/38e60e02-40b1-4ecc-ab79-6785b4ef0040)


Task Created To Migrate from EC2 to RDS:

![task created](https://github.com/user-attachments/assets/ed326404-7e70-421c-a0e3-45e5a96c24ab)

