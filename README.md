# Automated Emails with OpenAI API

This project is an automated emailing script designed to send emails automatically on an AWS Ubuntu server. It utilizes Python, OpenAI API, SMTP, AWS EC2, and cron for scheduling.

## Project Overview

The purpose of this project is to automate the process of sending emails for various purposes, such as notifications, alerts, or scheduled updates. The script generates email content dynamically (optional) and sends emails using SMTP, allowing users to schedule email sending tasks at specific intervals using cron jobs.

## Technologies Used

- Python
- OpenAI API (if applicable)
- SMTP
- AWS (EC2 for hosting the server)
- cron

## Getting Started

To set up and run the emailing script on your own AWS Ubuntu server, follow these steps:

1. Clone the repository to your local machine:  
`https://github.com/PierceBrandies/AutoMail.git`

2. Install the required dependencies:  
`pip install requirements.txt`

3. Configure the script:  
Update the `config.py` file with your email server settings, OpenAI API key (if applicable), and other configuration options. If email message is to be created manually remember to set `USE_API = False`

4. Run the script:  
`python main.py`

## AWS Setup

To host the emailing script on AWS, follow these steps:

1. Launch an EC2 instance with Ubuntu.
2. SSH into the EC2 instance and clone the project repository.
3. Install Python and required dependencies.
4. Configure security group settings to allow SMTP traffic.
5. Set up cron jobs to schedule the script to run at your specified time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.