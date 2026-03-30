class AlertHandler:
    def __init__(self):
        self.subscriptions = []

    def subscribe(self, subscriber):
        self.subscriptions.append(subscriber)

    def alert(self, message):
        for subscriber in self.subscriptions:
            subscriber.notify(message)

    def log_alert(self, message):
        with open('alert_log.txt', 'a') as log_file:
            log_file.write(f'{message}\n')

    def report_alerts(self):
        with open('alert_log.txt', 'r') as log_file:
            return log_file.readlines()