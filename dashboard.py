# Comprehensive Dashboard System

class Dashboard:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name, value):
        self.metrics[name] = value

    def display(self):
        for name, value in self.metrics.items():
            print(f'{name}: {value}')

if __name__ == '__main__':
    dashboard = Dashboard()
    dashboard.add_metric('CPU Usage', '23%')
    dashboard.add_metric('Memory Usage', '70%')
    dashboard.display()