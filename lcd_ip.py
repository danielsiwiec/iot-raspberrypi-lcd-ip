from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime
from RPLCD.i2c import CharLCD

# Initialise the lcd class
lcd = CharLCD('PCF8574', 0x27, auto_linebreaks=False)
lcd.clear()
lcd.backlight_enablled = False


# looking for an active Ethernet or WiFi device
def find_interface():
    find_device = "ip addr show"
    interface_parse = run_cmd(find_device)
    for line in interface_parse.splitlines():
        if "state UP" in line:
            dev_name = line.split(':')[1]
    return dev_name

# find an active IP on the first LIVE network device
def parse_ip():
    find_ip = "ip addr show %s" % interface
    find_ip = "ip addr show %s" % interface
    ip_parse = run_cmd(find_ip)
    for line in ip_parse.splitlines():
        if "inet " in line:
            ip = line.split(' ')[5]
            ip = ip.split('/')[0]
    return ip

# run unix shell command, return as ASCII
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')

# wipe LCD screen before we start

# before we start the main loop - detect active network device and ip address
sleep(2)
interface = find_interface()
ip_address = parse_ip()

while True:

    # date and time
    lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S')

    # current ip address
    lcd_line_2 = "IP " + ip_address

    lcd.home()
    lcd.write_string(f'{lcd_line_1}\r\n{lcd_line_2}')

    sleep(2)
