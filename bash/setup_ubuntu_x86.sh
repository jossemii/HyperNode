#!/bin/bash

# Update package lists
apt-get -y update > /dev/null

# Install Python 3.11 and pip
apt-get -y install python3.11 python3.11-venv python3-pip > /dev/null

# Create and activate a Python virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install Python dependencies from requirements.txt
pip3 install -r requirements.txt > /dev/null

# Install required system packages for Docker
apt-get -y install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release > /dev/null

# Add Docker GPG key and repository
if [ ! -f /usr/share/keyrings/docker-archive-keyring.gpg ]; then
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg > /dev/null
fi
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package lists again
apt-get -y update > /dev/null

# Install Docker
apt-get -y install docker-ce docker-ce-cli containerd.io > /dev/null

# Install QEMU and binfmt-support for multi-architecture support
apt-get -y install qemu binfmt-support qemu-user-static > /dev/null
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes > /dev/null

# Install Rust (Cargo)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y > /dev/null

# Source the Rust environment
source $HOME/.cargo/env

# Execute initialization script
sh ./bash/init_x86.sh > /dev/null

# Run migrations for Python application
python3 nodo.py migrate > /dev/null
