import pymavlink
from pymavlink import mavutil, mavtestgen

def wait_heartbeat(m):
    '''wait for a heartbeat so we know the target system IDs'''
    print("Waiting for APM heartbeat")
    msg = m.recv_match(type='HEARTBEAT', blocking=True)
    print("Heartbeat from APM (system %u component %u)" % (m.target_system, m.target_component))

def main():
    # Start a connection listening on the serial port
    the_connection = mavutil.mavlink_connection("/dev/ttyAMA0", "baud=57600")

    # Wait for the first heartbeat

    wait_heartbeat(the_connection)

    # Once connected, use 'the_connection' to get and send messages

    # Send heartbeat from a MAVLink application.
    the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                      mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)


main()