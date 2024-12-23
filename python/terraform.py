 #this is a template to be used for terraform scripts to automate container deployments
 #in k8s

from python_terraform import Terraform
import os
import subprocess

from traits.traits_listener import is_not_none

 # Set up the Terraform instance
tf = Terraform(working_dir='./terraform')  # path to your Terraform configuration folder

def initialize_terraform():
    """Initialize Terraform working directory."""
    print("Initializing Terraform...")
    init_code, stdout, stderr = tf.init()
    if init_code != 0:
        print(f"Error during initialization: {stderr}")
    else:
        print(f"Terraform initialized successfully:\n{stdout}")

def plan_terraform():
    """Generate and show an execution plan."""
    print("Generating Terraform plan...")
    plan_code, stdout, stderr = tf.plan(no_color=is_not_none())
    if plan_code != 0:
        print(f"Error during plan: {stderr}")
    else:
        print(f"Terraform plan generated successfully:\n{stdout}")

def apply_terraform():
    """Apply the Terraform configuration to deploy the resources."""
    print("Applying Terraform configuration...")
    apply_code, stdout, stderr = tf.apply(skip_plan=True)  # skip the interactive plan confirmation
    if apply_code != 0:
        print(f"Error during apply: {stderr}")
    else:
        print(f"Terraform applied successfully:\n{stdout}")

def main():
    # Make sure Terraform files are available
    if not os.path.exists('./terraform/main.tf'):
        print("Terraform configuration files not found!")
        return

    # Initialize, Plan, and Apply Terraform configuration
    try:
        initialize_terraform()
        plan_terraform()
        apply_terraform()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
