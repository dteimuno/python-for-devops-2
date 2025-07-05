#  DevOps Project: EC2 and Apache Deployment with Python & Fabric
![image](https://github.com/user-attachments/assets/e52073e7-c4d7-4734-aca5-0c90b4436d84)


This project automates the provisioning and deployment of a basic Apache web application using Python-based DevOps tools. It showcases the integration of AWS (via Boto3), SSH-based automation (via Fabric), and infrastructure scripting to streamline web server deployment.

---

##  Project Overview

**Goal:**  
Provision an EC2 instance, upload and install Apache2 using a shell script, and manage infrastructure using Python automation.

---

##  Project Structure

- `run_ec2_instances.py`  
  Automates the creation of an EC2 instance using Boto3 with custom tags, security group, subnet, and monitoring options.
  <img width="1092" alt="Screenshot 2025-07-04 at 10 43 54 PM" src="https://github.com/user-attachments/assets/1f7563bd-03da-409d-9e29-b693e7ed7d6b" />


- `create_s3_bucket.py`  
  Creates a private S3 bucket using Boto3 for optional static file storage or artifact management.
  <img width="1071" alt="Screenshot 2025-07-04 at 11 11 16 PM" src="https://github.com/user-attachments/assets/51e59597-26a2-4c5a-a1ae-c1543d62ec9c" />


- `ssh_into_instance.py`  
  Uses the Fabric library to:
  - SSH into the EC2 instance via PEM key
  - Upload the Apache setup script
  - Make the script executable and run it with `sudo`
  

- `apache.sh`  
  A Bash script executed remotely to:
  - Install Apache2
  - Enable and start the service
  - Display the server’s public IP address
  <img width="1332" alt="image" src="https://github.com/user-attachments/assets/725d12af-79e4-4523-b6d7-f160bc3982ba" />


---

##  Tools & Technologies Used

- **Python 3**
- **Boto3** – AWS automation SDK
- **Fabric** – SSH and remote task automation
- **AWS EC2** – Cloud compute provisioning
- **AWS S3** – Cloud object storage
- **Apache2** – Web server installed via Bash
- **Ubuntu** – EC2 AMI base OS

---

## 🔄 Workflow Summary

1. **Provision EC2 instance** with `run_ec2_instances.py`
2. **Create an S3 bucket** using `create_s3_bucket.py` (optional step)
3. **SSH and deploy Apache** using `ssh_into_instance.py` and `apache.sh`
4.  Apache is now running and serving web content on the EC2 public IP

---

##  Future Enhancements

- Automate web app zip upload to S3 and extraction on EC2
- Add teardown scripts to delete EC2 and S3 resources
- Integrate with CI/CD (e.g., GitHub Actions or Jenkins)
- Add error handling and logging



---

##  Status

✅ Completed — ready for demonstration or extension.

---

