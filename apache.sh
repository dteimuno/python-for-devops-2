#install apache2 on ubuntu
#!/bin/bash
# Update package list
sudo apt update
# Install Apache2
sudo apt install -y apache2
# Enable Apache2 to start on boot
sudo systemctl enable apache2
# Start Apache2 service
sudo systemctl start apache2
