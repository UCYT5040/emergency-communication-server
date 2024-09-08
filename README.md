# Emergency Communication Server

A server that allows user to communicate with each other in events of emergency.

Users can request help and include their room number and a brief description of the emergency.

Officials can send announcements to all users.

## Installation

Ensure you have Python 3 installed.

1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Run the server using `python app.py`

Input the server’s IP address and port number, prefixed with `http://`, in the App Inventor project (do not include a trailing slash).

## Usage

The included MIT App Inventor project can be used to interact with the server.

Or, you can use the following endpoints:
- `/help-request`: POST a JSON object with `room` (`str`) and `message` (`str`) to request help
- `/announcement`: POST a JSON object with `message` (`str`) to send an announcement
- `/messages`: GET to retrieve all messages
