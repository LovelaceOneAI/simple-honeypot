# Simple Honeypot

A basic honeypot server that listens on a fake SSH port and logs all unauthorized login attempts.

## How It Works

- Listens for incoming TCP connections on port 2222 (pretending to be SSH).
- Logs the IP address of any connection attempt.
- Sends a fake "Unauthorized" response to the attacker.

## Usage

```bash
python honeypot.py
